"""Parse the cached Illinois Constitution and ILCS pages (Internet Archive captures of ilga.gov) into corpus.json. No network."""
import hashlib
import html
import os
import re
import sys
import urllib.parse
from pathlib import Path

from state_lib import Act, key, norm, sha, text_of, write_corpus

HERE = os.path.dirname(os.path.abspath(__file__))
C = Path(HERE) / '.cache'
BASE = 'https://www.ilga.gov'
CONST_TS = '20260101'       # the capture nearest this day was read for every Constitution page
CONST_DATE = '2026-01-01'
TREE_TS = '20250101'
TREE_DATE = '2024-12-22'    # the file date every ILCS file shows in the ilga.gov /ftp/ILCS/ directory listing
RETRIEVED = '2026-10-30'
ARTS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV']
ACTS = [('Ch%200720/Act%200005', '720', '5', 'Criminal Code of 2012'),
        ('Ch%200805/Act%200005', '805', '5', 'Business Corporation Act of 1983')]


def cap(url, ts):
    p = C / hashlib.sha256(f'https://web.archive.org/web/{ts}id_/{url}'.encode()).hexdigest()
    return p.read_bytes() if p.exists() else None


def plain(b):
    return html.unescape(re.sub(r'<[^>]+>', '', b.decode('latin-1'))).replace('\r', '')


def constitution():
    out = []
    for i, rn in enumerate(ARTS, 1):
        u = f'{BASE}/commission/lrb/con{i}.htm'
        b = cap(u, CONST_TS)
        if b is None:
            raise SystemExit('missing ' + u)
        t = plain(b)
        k = t.find('SECTION 1.')
        head = t[:k]
        title = norm(head.split('Constitution of the State of Illinois', 1)[-1])
        body = t[k:]
        if 'to preceding Article' in body:
            body = body[:body.rfind('to preceding Article')]
        a = Act(f'constitution-art-{i:02d}', f'Ill. Const. art. {rn}', f'Constitution of the State of Illinois, {title}', u, CONST_DATE,
                sha256=sha(b))
        for p in re.split(r'(?m)^(?=SECTION \d+[A-Za-z]?\. )', body):
            m = re.match(r'SECTION (\d+[A-Za-z]?)\.', p)
            if not m:
                continue
            first, _, rest = p.strip('\n').partition('\n')
            txt = ['# ' + norm(first)]
            cur = []
            for l in rest.split('\n'):
                if l.startswith('(Source'):
                    if cur:
                        txt.append(norm(' '.join(cur)))
                        cur = []
                    txt.append(norm(l))
                elif not l.strip():
                    if cur:
                        txt.append(norm(' '.join(cur)))
                        cur = []
                else:
                    if re.match(r'^\s{4}\S', l) and cur:
                        txt.append(norm(' '.join(cur)))
                        cur = []
                    cur.append(l.strip())
            if cur:
                txt.append(norm(' '.join(cur)))
            a.add(key('sec', m.group(1)), 'Section ' + m.group(1), 'section', text_of(txt))
        out.append(a)
    for slug, name, fn in (('constitution-preamble', 'Preamble', 'conp'), ('constitution-transition-schedule', 'Transition Schedule', 'contrans')):
        u = f'{BASE}/commission/lrb/{fn}.htm'
        b = cap(u, CONST_TS)
        if b is None:
            raise SystemExit('missing ' + u)
        t = plain(b)
        t = t.split('Constitution of the State of Illinois', 1)[-1]
        t = t.split('to main Constitution page')[0]
        t = re.sub(r'to preceding Article|to next Article', '', t)
        paras = [norm(x.replace('\n', ' ')) for x in re.split(r'\n\s*\n', t)]
        paras = [p for p in paras if p]
        a = Act(slug, 'Ill. Const. ' + name.lower(), f'Constitution of the State of Illinois, {name}', u, CONST_DATE, sha256=sha(b))
        if paras and paras[0].upper() == name.upper():
            paras = paras[1:]
        a.add('text', name, 'section', text_of(['# ' + name] + paras))
        out.append(a)
    return out


def ilcs():
    out = []
    for path, ch, act, name in ACTS:
        idx = cap(f'{BASE}/ftp/ILCS/{path}/', '20251116')
        if idx is None:
            continue
        files = [urllib.parse.unquote(f) for f in re.findall(r'HREF="([^"]*)"', idx.decode('utf8', 'replace'))]
        files = [f for f in files if re.search(r'/\d{9}K\d[^/]*\.html$', f)]
        arts, raw = {}, {}
        incomplete = set()
        for f in files:
            b = cap('https://ilga.gov' + f.replace(' ', '%20'), TREE_TS)
            if b is None:
                incomplete.add(re.search(r'K(\d+[A-Za-z]*)-', f).group(1) if re.search(r'K(\d+[A-Za-z]*)-', f) else f)
                continue
            t = re.sub(r'<br\s*/?>', '\n@@', b.decode('latin-1'), flags=re.I)
            t = html.unescape(re.sub(r'<[^>]+>', '', t)).replace('\r', '')
            paras = [norm(x.replace('\n', ' ')) for x in t.split('@@')]
            paras = [p for p in paras if p]
            if not paras:
                continue
            m = re.search(r'\((\d+) ILCS (\d+)/([0-9A-Za-z.\-]+)\)', paras[0])
            if not m:
                raise SystemExit(f'no citation: {f}: {paras[0][:80]}')
            sec = m.group(3)
            hi = next((i for i, p in enumerate(paras) if p.startswith('Sec.')), None)
            if hi is not None:
                paras = ['# ' + paras.pop(hi)] + paras
            else:
                paras[0] = '# ' + paras[0]
            artno = sec.split('-')[0]
            art = arts.setdefault(artno, Act(key(f'ilcs-{ch}-{act}-article', artno), f'{ch} ILCS {act} art. {artno}',
                                             f'Illinois Compiled Statutes, {name} ({ch} ILCS {act}), Article {artno}',
                                             f'{BASE}/ftp/ILCS/{path}/', TREE_DATE))
            raw[artno] = raw.get(artno, b'') + b
            art.add(key('sec', sec), f'{ch} ILCS {act}/{sec}', 'section', text_of(paras))
        for k, a in arts.items():
            if k in incomplete:
                continue   # an article is published only when every one of its section files was read
            a.sha256 = sha(raw[k])
            out.append(a)
    return out


def main():
    acts = constitution() + ilcs()
    country = {'code': 'US-IL', 'name': 'United States (Illinois)', 'slug': 'united-states-illinois', 'lang': 'en',
               'tz': 'America/Chicago', 'future_branch': 'future',
               'publisher': {'name': 'Illinois General Assembly (ilga.gov)', 'email': 'ilcs@ilga-gov.invalid'},
               'default_in_force_rule': {'text': 'No dated history is published: each act is the oldest version available, dated by the source\'s own currency statement.',
                                         'source': BASE + '/ftp/ILCS/'},
               'licence_note': 'Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). Source: Illinois General Assembly, ilga.gov.'}
    sources = [{'name': 'Illinois Constitution and Illinois Compiled Statutes (ilga.gov), read from Internet Archive captures',
                'url': BASE + '/', 'retrieved': RETRIEVED,
                'licence': 'Statute text carries no copyright (Georgia v. Public.Resource.Org, 2020). The ILCS FTP readme calls the web copy non-authoritative ("The only official copy of the law is the printed copy"); no reuse restriction was found.',
                'notes': 'Constitution of 1970; 720 ILCS 5 (Criminal Code of 2012); 805 ILCS 5 (Business Corporation Act of 1983).'}]
    decisions = [
        'ilga.gov refuses connections from this machine, so every page was read from an Internet Archive capture; no request was made to ilga.gov itself and its robots.txt could not be read.',
        f'ILCS acts are dated {TREE_DATE}, the file date every file in the /ftp/ILCS/ directory listing shows; each section page was taken from the Internet Archive capture nearest after 2025-01-01 (all February 2025).',
        f'The Constitution acts are dated {CONST_DATE}, the day the Internet Archive capture read was nearest; the Constitution was adopted 1970-12-15 and the text is as amended to that capture.',
        'One act per article of the Constitution and per article of each ILCS act; one unit per section. The "(Source: P.A. ...)" line kept as a section\'s last line is the compilation\'s own source note, not an annotation.',
        'Only section files of the ILCS tree are read; article headings, tables of contents and notes files are not copied.']
    write_corpus(HERE, country, sources, acts, decisions)


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    main()
