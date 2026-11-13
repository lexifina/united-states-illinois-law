"""Append one source-dated current Illinois act from the publisher's ILCS listing."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parents[1]
JOB = HERE.parent / 'gpt-workers/jobs/q-2050'
REPO = JOB / 'published'
EVIDENCE = JOB / 'source-evidence'
CHECKED = '2026-11-13'
BASE_URL = 'https://ftp.ilga.gov/ILCS/'
FUTURE_REL = 'Ch 0075/Act 0040/007500400K4.5.html'

sys.argv = [sys.argv[0], str(JOB)]
sys.path.insert(0, str(HERE / 'tools'))
import parse_mirror_q1573 as P
P.owned(JOB)
sys.path.insert(0, str(HERE.parent / 'gitlaw_common'))
import append as A
import build as B
import check as K
import private
import build_mirror_q1622 as M

M.EVIDENCE = EVIDENCE
M.CHECKED = CHECKED

def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def source_date(row):
    citations = []
    for rel in row['files']:
        text, images = P.source_text((EVIDENCE / rel).read_bytes())
        require(not images, 'normative image in retained source: ' + rel)
        for note in re.findall(r'\(Source:.*?\)', P.norm(text)):
            acts = list(re.finditer(r'(?<![\d-])(\d{2,3})-(\d{1,4})(?![\d-])', note))
            for i, match in enumerate(acts):
                fragment = note[match.start():acts[i + 1].start() if i + 1 < len(acts) else len(note)]
                dates = []
                for month, day, year in re.findall(r'\beff\.\s*(\d{1,2})-(\d{1,2})-(\d{2,4})\b', fragment):
                    year = int(year)
                    year += (2000 if year < 50 else 1900) if year < 100 else 0
                    dates.append(P.date(year, int(month), int(day)).isoformat())
                for day in dates:
                    require(day <= CHECKED, 'future effective date in retained source: ' + rel)
                citations.append({'public_act': [int(match[1]), int(match[2])], 'dates': dates,
                                  'quote': fragment, 'source_url': P.source_url(rel)})
    require(citations, 'no cited Public Act')
    dated = [c for c in citations if c['dates']]
    require(dated, 'no explicit current Public Act effective date')
    latest_date = max(day for c in dated for day in c['dates'])
    latest_pa = max(tuple(c['public_act']) for c in citations)
    latest_pa_rows = [c for c in citations if tuple(c['public_act']) == latest_pa]
    latest_pa_dates = [day for c in latest_pa_rows for day in c['dates']]
    require(latest_pa_dates and max(latest_pa_dates) == latest_date,
            'latest cited Public Act does not carry the latest current effective date')
    witness = next(c for c in latest_pa_rows if latest_date in c['dates'])
    return {'date': latest_date, 'latest_public_act': '-'.join(map(str, latest_pa)),
            'quote': witness['quote'], 'source_url': witness['source_url'], 'citations': citations}

def verify_listing(row):
    root = (EVIDENCE / 'index.html').read_bytes()
    chapter = (EVIDENCE / 'Ch 0075/index.html').read_bytes()
    act_index = (EVIDENCE / 'Ch 0075/Act 0040/index.html').read_bytes()
    require('Ch 0075/' in P.links(root), 'official root listing lacks chapter 75')
    require('Ch 0075/Act 0040/' in P.links(chapter), 'official chapter listing lacks act 40')
    listed = [p for p in P.links(act_index) if p.startswith(row['directory'] + '/') and p.endswith('.html')]
    require(len(listed) == len(set(listed)), 'duplicate document in official act listing')
    require(set(listed) == set(row['files']), 'official act listing and saved publisher index differ')
    proof = json.loads((EVIDENCE / 'fetch-proof.json').read_text(encoding='utf-8'))
    for item in proof:
        raw = (EVIDENCE / item['evidence_file']).read_bytes()
        require(len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'],
                'fetched source proof hash mismatch: ' + item['url'])
    return {'root_sha256': hashlib.sha256(root).hexdigest(),
            'chapter_sha256': hashlib.sha256(chapter).hexdigest(),
            'act_index_sha256': hashlib.sha256(act_index).hexdigest(),
            'listed_documents': listed, 'fetched_responses': len(proof)}

def parse_act(row, listing):
    all_files = list(row['files'])
    require(FUTURE_REL in all_files, 'expected future-only section absent from publisher listing')
    future_raw = (EVIDENCE / FUTURE_REL).read_bytes()
    future_text, future_images = P.source_text(future_raw)
    require(not future_images, 'normative image in future-only section')
    future_note = re.search(r'\(Source:.*?\)', P.norm(future_text))
    require(future_note and 'P.A. 104-808, eff. 1-1-27' in future_note.group(0),
            'future-only section lacks exact delayed effective date')
    row = {**row, 'files': [rel for rel in all_files if rel != FUTURE_REL]}
    first, detail = M.parse_variant(row)
    second, detail2 = M.parse_variant(row)
    require(first is not None and first == second and detail == detail2,
            'two source parses differ or selected no act')
    date = source_date(row)
    version = first['versions'][0]
    require(version['from'] == date['date'], 'parser date and Public Act date witness differ')
    version['source_images'] = 0
    version['note'] = (f"Publisher compilation updated 2026-10-30 through Public Act 104-854. "
                       f"In-force basis: latest currently cited Public Act {date['latest_public_act']} "
                       f"has explicit effective date {date['date']}; the separately labelled future-only "
                       f"section is excluded until Public Act 104-808 takes effect on 2027-01-01.")
    proofs = []
    for i, rel in enumerate(row['files'], 1):
        raw = (EVIDENCE / rel).read_bytes()
        text, images = P.source_text(raw)
        key = P.document_key(rel, i)
        require(not images, 'normative image in retained source: ' + rel)
        require(P.norm(version['units'][key]['text']) == P.norm(text),
                'parser words differ from fetched publisher document: ' + rel)
        proofs.append({'file': first['slug'] + '/' + key + '.md', 'source_url': P.source_url(rel),
                       'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                       'source_images': 0, 'referenced': 0, 'omitted': 0, 'words_equal': True})
    excluded = {'file': FUTURE_REL, 'source_url': P.source_url(FUTURE_REL),
                'sha256': hashlib.sha256(future_raw).hexdigest(), 'effective_date': '2027-01-01',
                'public_act': '104-808', 'reason': 'publisher section text states delayed effective date'}
    return first, date, proofs, excluded

def make_corpus(act):
    part = M.part_for([act])
    corpus = M.corpus_for(part)
    errors = B.validate(corpus)
    require(not errors, 'shared corpus schema validation failed: ' + repr(errors))
    return corpus

def append_act(act, date, proofs, excluded, listing):
    base = P.git(REPO, 'rev-parse', 'HEAD').decode().strip()
    require(base == 'f9ddf20882efbc429f7b9fa167f5756d957282c8', 'published clone base changed')
    require(not P.git(REPO, 'status', '--porcelain').strip(), 'published clone worktree is not clean')
    corpus = make_corpus(act)
    parent_fields = P.git(REPO, 'log', '-1', '--format=%ct %ci', base).decode().split()
    parent_ct, tz = int(parent_fields[0]), parent_fields[-1]
    writer = A.Appender(REPO, base, parent_ct, tz)
    clock = B.Clock(corpus['country']['tz'])
    committer = ('Lexifina', 'united-states-illinois-law@lexifina.com')
    plan = B.plan(corpus)
    require(len(plan) == 1 and plan[0]['kind'] == 'start', 'expected one new current-text act commit')
    step = plan[0]
    author, message, trailers = B.start_message(corpus, step)
    version = step['version']
    additions = ['Source: ' + version['source_url'], 'Compilation-updated: 2026-10-30',
                 'In-force-basis: ' + version['note'].split('In-force basis: ', 1)[1]]
    keys = {t.split(':', 1)[0] for t in trailers}
    trailers += [t for t in additions if t.split(':', 1)[0] not in keys]
    B.check_trailers(trailers)
    act_head = writer.commit(author, clock.stamp(step['day']), committer,
                             '\n'.join(message).rstrip() + '\n\n' + '\n'.join(trailers) + '\n',
                             B.act_files(step['act'], version['units'], None))
    tag = act['slug'] + '/' + version['from']
    require(not P.git(REPO, 'tag', '--list', tag).strip(), 'tag already exists: ' + tag)
    writer.tag(tag, act_head)

    versions = json.loads(P.git(REPO, 'show', base + ':data/versions.json'))
    require(not any(old['slug'] == act['slug'] for old in versions['acts']), 'act already represented')
    versions['acts'].append({k: act[k] for k in ('slug', 'short', 'title', 'url')} | {'versions': [
        {k: version[k] for k in ('from', 'source_url', 'sha256', 'source_images')} | {'units': len(version['units'])}]})
    readme = P.git(REPO, 'show', base + ':README.md').decode('utf-8')
    readme += ('\n## Further current ILCS text, 13 November 2026\n\n'
               'One additional indexed act from the [Illinois General Assembly static ILCS compilation]'
               '(https://ftp.ilga.gov/ILCS/) is included at its latest currently cited source effective date. '
               'The compilation states that it is updated through Public Act 104-854 on 30 October 2026 and '
               'that the printed Secretary of State copy is the official text. Future-effective statutory text '
               'is excluded until its stated effective date. The source inventory and exclusions are in '
               '`data/ilcs-depth-q2050.json`.\n\n'
               '| Act | Source date | Sections |\n| --- | --- | ---: |\n'
               f'| [{act["title"]} ({act["short"]})]({act["url"]}) | {version["from"]} | '
               f'{sum(1 for unit in version["units"].values() if unit["kind"] == "section")} |\n')
    jurisdiction = json.loads(P.git(REPO, 'show', base + ':jurisdiction.json'))
    jurisdiction['ilcs_depth_q2050'] = {'acts': 1, 'checked_on': CHECKED,
        'source': BASE_URL, 'authoritative': False,
        'date_basis': 'latest currently cited Public Act explicit effective date; future-only section held'}
    oldcsv = P.git(REPO, 'show', base + ':data/commits.csv').decode('utf-8')
    reader = csv.DictReader(io.StringIO(oldcsv)); outbuf = io.StringIO(newline='')
    out = csv.DictWriter(outbuf, fieldnames=reader.fieldnames, lineterminator='\n')
    out.writeheader(); out.writerows(reader)
    out.writerow({'day': version['from'], 'kind': 'start', 'law': '', 'acts': act['slug'],
                  'files': len(version['units']), 'branch': 'main'})
    provenance = {'checked_on': CHECKED, 'source': BASE_URL, 'authoritative': False,
                  'listing': listing, 'act': act['slug'], 'title': act['title'],
                  'in_force': date, 'included_documents': proofs, 'excluded_documents': [excluded],
                  'source_images': 0, 'referenced_images': 0, 'omitted_images': 0}
    docs = {'README.md': readme, 'jurisdiction.json': json.dumps(jurisdiction, indent=2) + '\n',
            'data/versions.json': json.dumps(versions, ensure_ascii=False, indent=1) + '\n',
            'data/commits.csv': outbuf.getvalue(),
            'data/ilcs-depth-q2050.json': json.dumps(provenance, ensure_ascii=False, indent=2) + '\n'}
    tool_copy = (HERE / 'tools/depth_q2050.py').read_text(encoding='utf-8')
    docs['tools/depth_q2050.py'] = tool_copy
    writer.commit(committer, f'{parent_ct + 2} {tz}', committer,
                  'Documentation: one further current ILCS act\n\nKind: documentation\n', docs)
    writer.finish()
    head = P.git(REPO, 'rev-parse', 'HEAD').decode().strip()
    return base, act_head.decode().strip() if isinstance(act_head, bytes) else act_head, head, corpus, proofs

def final_proof(act, proofs, source_files):
    output = []
    for i, rel in enumerate(source_files, 1):
        source, images = P.source_text((EVIDENCE / rel).read_bytes())
        key = P.document_key(rel, i)
        path = act['slug'] + '/' + key + '.md'
        actual = P.git(REPO, 'show', 'HEAD:' + path).decode('utf-8')
        require(not images and P.norm(actual) == P.norm(source), 'final Git law text differs from source: ' + path)
        output.append({'file': path, 'source_url': P.source_url(rel), 'words_equal': True,
                       'source_images': 0, 'referenced': 0, 'omitted': 0})
    return output

def main():
    row = next(r for r in json.loads((JOB.parent / 'q-2034/source-evidence/missing-survey.json').read_text(encoding='utf-8'))['missing']
               if r['slug'] == 'ilcs-75-40')
    listing = verify_listing(row)
    act, date, proofs, excluded = parse_act(row, listing)
    source_files = [r for r in row['files'] if r != FUTURE_REL]
    corpus = make_corpus(act)
    staging = JOB / 'staging/corpus.json'
    write(staging, corpus)
    require(len(proofs) == 7, 'incomplete source proof')
    base, act_head, head, corpus, proofs = append_act(act, date, proofs, excluded, listing)
    check = K.check(REPO, staging)
    write(JOB / 'append-check.json', check)
    require(not any(check.get(k, 0) for k in ('mismatches', 'trailer_errors', 'missing_in_force', 'merges',
                                                'backwards', 'future_dated', 'tip_errors', 'image_errors')), str(check))
    final = final_proof(act, proofs, source_files)
    audit = private.audit_push(REPO, head, base)
    write(JOB / 'audit-push.json', audit)
    require(not audit, 'audit_push findings: ' + repr(audit))
    write(JOB / 'source-proof.json', {'listing': listing, 'in_force': date, 'included': proofs,
                                      'excluded_future': excluded, 'final_git_words': final,
                                      'source_images': 0, 'referenced': 0, 'omitted': 0})
    write(JOB / 'append-result.json', {'base': base, 'act_head': act_head, 'head': head,
                                       'act': act['slug'], 'date': date['date'],
                                       'files': len(final), 'units': len(act['versions'][0]['units'])})
    print(json.dumps({'base': base, 'act_head': act_head, 'head': head, 'date': date['date'],
                      'source_files': len(final), 'units': len(act['versions'][0]['units']),
                      'check': check, 'audit': audit}, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
