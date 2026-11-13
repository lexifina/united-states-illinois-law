"""Append a second source-dated current ILCS act from the publisher's static listing."""
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
EVIDENCE = JOB / 'source-evidence/next-620-35'
CHECKED = '2026-11-13'
FUTURE_REL = 'Ch 0620/Act 0035/062000350K16.html'

sys.path.insert(0, str(HERE / 'tools'))
import parse_mirror_q1573 as P
P.owned(JOB)
sys.path.insert(0, str(HERE.parent / 'gitlaw_common'))
import append as A
import build as B
import check as K
import private
sys.argv = [sys.argv[0], str(JOB)]
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

def main():
    row = next(r for r in json.loads((JOB.parent / 'q-2034/source-evidence/missing-survey.json').read_text(encoding='utf-8'))['missing']
               if r['slug'] == 'ilcs-620-35')
    root = (JOB / 'source-evidence/index.html').read_bytes()
    chapter = (EVIDENCE / 'Ch 0620/index.html').read_bytes()
    act_index = (EVIDENCE / 'Ch 0620/Act 0035/index.html').read_bytes()
    require('Ch 0620/' in P.links(root), 'publisher root listing lacks chapter 620')
    require('Ch 0620/Act 0035/' in P.links(chapter), 'publisher chapter listing lacks act 35')
    listed = [p for p in P.links(act_index) if p.startswith(row['directory'] + '/') and p.endswith('.html')]
    require(len(listed) == len(set(listed)) and set(listed) == set(row['files']),
            'publisher act listing and source inventory differ')
    fetched = json.loads((EVIDENCE / 'fetch-proof.json').read_text(encoding='utf-8'))
    by_url = {item['url']: item for item in fetched}
    for item in fetched:
        raw = (EVIDENCE / item['evidence_file']).read_bytes()
        require(len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'],
                'saved publisher response hash mismatch: ' + item['url'])
    require(FUTURE_REL in row['files'], 'expected future-effective section missing from publisher listing')
    future_raw = (EVIDENCE / FUTURE_REL).read_bytes()
    future_text, future_images = P.source_text(future_raw)
    future_note = re.search(r'\(Source:.*?\)', P.norm(future_text))
    require(not future_images and future_note and 'P.A. 104-751, eff. 1-1-27' in future_note.group(0),
            'future-only section does not have the expected dated publisher note')
    row = {**row, 'files': [rel for rel in row['files'] if rel != FUTURE_REL]}
    D = __import__('depth_q2050')
    D.EVIDENCE = EVIDENCE
    D.M.EVIDENCE = EVIDENCE
    date = D.source_date(row)
    first, detail = M.parse_variant(row)
    second, detail2 = M.parse_variant(row)
    require(first is not None and first == second and detail == detail2, 'two parses differ or yield no current text')
    version = first['versions'][0]
    require(version['from'] == date['date'], 'parsed in-force day differs from source date audit')
    version['source_images'] = 0
    version['note'] = (f"Publisher compilation updated 2026-10-30 through Public Act 104-854. "
                       f"In-force basis: latest currently cited Public Act {date['latest_public_act']} "
                       f"has explicit effective date {date['date']}; the standalone future-effective section "
                       f"is excluded until Public Act 104-751 takes effect on 2027-01-01.")
    proofs = []
    for i, rel in enumerate(row['files'], 1):
        raw = (EVIDENCE / rel).read_bytes()
        text, images = P.source_text(raw)
        key = P.document_key(rel, i)
        require(not images and P.norm(version['units'][key]['text']) == P.norm(text),
                'parsed text differs from fetched publisher document: ' + rel)
        item = by_url[P.source_url(rel)]
        proofs.append({'file': first['slug'] + '/' + key + '.md', 'source_url': item['url'],
                       'bytes': item['bytes'], 'sha256': item['sha256'], 'words_equal': True,
                       'source_images': 0, 'referenced': 0, 'omitted': 0})
    listing = {'root_sha256': hashlib.sha256(root).hexdigest(),
               'chapter_sha256': hashlib.sha256(chapter).hexdigest(),
               'act_index_sha256': hashlib.sha256(act_index).hexdigest(),
               'listed_documents': listed, 'fetched_responses': len(fetched) +
               len(json.loads((JOB / 'source-evidence/fetch-proof.json').read_text(encoding='utf-8')))}
    excluded_item = by_url[P.source_url(FUTURE_REL)]
    excluded = {'file': FUTURE_REL, 'source_url': excluded_item['url'], 'sha256': excluded_item['sha256'],
                'effective_date': '2027-01-01', 'public_act': '104-751',
                'reason': 'publisher section text states delayed effective date'}
    corpus = M.corpus_for(M.part_for([first]))
    errors = B.validate(corpus)
    require(not errors, 'shared corpus schema validation failed: ' + repr(errors))
    staging = JOB / 'staging/second-corpus.json'
    write(staging, corpus)
    base = P.git(REPO, 'rev-parse', 'HEAD').decode().strip()
    require(base == '7ae994048e0b8ea81cd07a3e7ff82f9aa2d1eff2', 'scratch head changed before second batch')
    require(not P.git(REPO, 'status', '--porcelain').strip(), 'scratch checkout is not clean before second batch')
    parent_fields = P.git(REPO, 'log', '-1', '--format=%ct %ci', base).decode().split()
    parent_ct, tz = int(parent_fields[0]), parent_fields[-1]
    writer = A.Appender(REPO, base, parent_ct, tz)
    clock = B.Clock(corpus['country']['tz'])
    committer = ('Lexifina', 'united-states-illinois-law@lexifina.com')
    plan = B.plan(corpus)
    require(len(plan) == 1 and plan[0]['kind'] == 'start', 'expected one current-text act commit')
    step = plan[0]
    author, message, trailers = B.start_message(corpus, step)
    additions = ['Source: ' + version['source_url'], 'Compilation-updated: 2026-10-30',
                 'In-force-basis: ' + version['note'].split('In-force basis: ', 1)[1]]
    trailer_keys = {t.split(':', 1)[0] for t in trailers}
    trailers += [t for t in additions if t.split(':', 1)[0] not in trailer_keys]
    B.check_trailers(trailers)
    act_commit = writer.commit(author, clock.stamp(step['day']), committer,
                               '\n'.join(message).rstrip() + '\n\n' + '\n'.join(trailers) + '\n',
                               B.act_files(step['act'], version['units'], None))
    tag = first['slug'] + '/' + version['from']
    require(not P.git(REPO, 'tag', '--list', tag).strip(), 'tag already exists: ' + tag)
    writer.tag(tag, act_commit)

    versions = json.loads(P.git(REPO, 'show', base + ':data/versions.json'))
    require(not any(item['slug'] == first['slug'] for item in versions['acts']), 'act already represented')
    versions['acts'].append({k: first[k] for k in ('slug', 'short', 'title', 'url')} | {'versions': [
        {k: version[k] for k in ('from', 'source_url', 'sha256', 'source_images')} | {'units': len(version['units'])}]})
    readme = P.git(REPO, 'show', base + ':README.md').decode('utf-8')
    readme += ('\n## Further current ILCS text, 13 November 2026\n\n'
               'One additional indexed act from the [Illinois General Assembly static ILCS compilation]'
               '(https://ftp.ilga.gov/ILCS/) is included at its latest currently cited source effective date. '
               'The compilation states that it is updated through Public Act 104-854 on 30 October 2026 and '
               'that the printed Secretary of State copy is the official text. Future-effective statutory text '
               'is excluded until its stated effective date. The source inventory and exclusions are in '
               '`data/ilcs-depth-q2050-second.json`.\n\n'
               '| Act | Source date | Sections |\n| --- | --- | ---: |\n'
               f'| [{first["title"]} ({first["short"]})]({first["url"]}) | {version["from"]} | '
               f'{sum(1 for unit in version["units"].values() if unit["kind"] == "section")} |\n')
    jurisdiction = json.loads(P.git(REPO, 'show', base + ':jurisdiction.json'))
    jurisdiction.setdefault('ilcs_depth_q2050', {})['acts'] = 2
    jurisdiction['ilcs_depth_q2050'].update({'checked_on': CHECKED, 'source': 'https://ftp.ilga.gov/ILCS/',
        'authoritative': False, 'date_basis': 'latest currently cited Public Act explicit effective date; future-only sections held'})
    oldcsv = P.git(REPO, 'show', base + ':data/commits.csv').decode('utf-8')
    reader = csv.DictReader(io.StringIO(oldcsv)); output = io.StringIO(newline='')
    writer_csv = csv.DictWriter(output, fieldnames=reader.fieldnames, lineterminator='\n')
    writer_csv.writeheader(); writer_csv.writerows(reader)
    writer_csv.writerow({'day': version['from'], 'kind': 'start', 'law': '', 'acts': first['slug'],
                         'files': len(version['units']), 'branch': 'main'})
    provenance = {'checked_on': CHECKED, 'source': 'https://ftp.ilga.gov/ILCS/', 'authoritative': False,
                  'listing': listing, 'act': first['slug'], 'title': first['title'], 'in_force': date,
                  'included_documents': proofs, 'excluded_documents': [excluded],
                  'source_images': 0, 'referenced_images': 0, 'omitted_images': 0}
    docs = {'README.md': readme, 'jurisdiction.json': json.dumps(jurisdiction, indent=2) + '\n',
            'data/versions.json': json.dumps(versions, ensure_ascii=False, indent=1) + '\n',
            'data/commits.csv': output.getvalue(),
            'data/ilcs-depth-q2050-second.json': json.dumps(provenance, ensure_ascii=False, indent=2) + '\n',
            'tools/depth_q2050.py': (HERE / 'tools/depth_q2050.py').read_text(encoding='utf-8'),
            'tools/depth_q2050_second.py': Path(__file__).read_text(encoding='utf-8')}
    writer.commit(committer, f'{parent_ct + 2} {tz}', committer,
                  'Documentation: one more current ILCS act\n\nKind: documentation\n', docs)
    writer.finish()
    head = P.git(REPO, 'rev-parse', 'HEAD').decode().strip()
    check = K.check(REPO, staging)
    write(JOB / 'append-check-second.json', check)
    bad = ('mismatches', 'trailer_errors', 'missing_in_force', 'merges', 'backwards', 'future_dated', 'tip_errors', 'image_errors')
    require(not any(check.get(key, 0) for key in bad), 'shared check failed: ' + repr(check))
    final = []
    for i, rel in enumerate(row['files'], 1):
        text, images = P.source_text((EVIDENCE / rel).read_bytes())
        path = first['slug'] + '/' + P.document_key(rel, i) + '.md'
        actual = P.git(REPO, 'show', 'HEAD:' + path).decode('utf-8')
        require(not images and P.norm(actual) == P.norm(text), 'final Git law text mismatch: ' + path)
        final.append({'file': path, 'source_url': P.source_url(rel), 'words_equal': True,
                      'source_images': 0, 'referenced': 0, 'omitted': 0})
    audit = private.audit_push(REPO, head, 'f9ddf20882efbc429f7b9fa167f5756d957282c8')
    write(JOB / 'audit-push-final.json', audit)
    write(JOB / 'source-proof-second.json', {'listing': listing, 'in_force': date, 'included': proofs,
        'excluded_future': excluded, 'final_git_words': final, 'source_images': 0, 'referenced': 0, 'omitted': 0})
    write(JOB / 'append-result-second.json', {'base': base, 'head': head, 'act_head': act_commit,
        'date': version['from'], 'act': first['slug'], 'source_documents': len(final),
        'check': check, 'audit': audit})
    print(json.dumps({'base': base, 'head': head, 'act': first['slug'], 'date': version['from'],
        'source_documents': len(final), 'check': check, 'audit': audit}, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
