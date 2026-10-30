"""Writes repo/README.md, LICENSE, jurisdiction.json from corpus.json."""
import json
import os

from state_lib import write_docs

HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(os.path.join(HERE, 'corpus.json'), encoding='utf-8'))
rows = []
cons = [a for a in c['acts'] if a['slug'].startswith('constitution-')]
rows.append(('constitution-*/', 'Constitution of the State of Illinois (1970): the preamble, one folder per article, and the transition schedule', 1,
              f"{sum(len(a['versions'][0]['units']) for a in cons)} provisions, text as read on 2026-01-01"))
ilcs = [a for a in c['acts'] if a['slug'].startswith('ilcs-')]
for a in ilcs:
    rows.append((a['slug'] + '/', a['title'], 1, f"{len(a['versions'][0]['units'])} sections, text as of 2024-12-22"))
write_docs(HERE, {
    'name': 'United States (Illinois)', 'state': 'Illinois', 'code': 'US-IL', 'slug': 'illinois',
    'domain': 'ilga.gov', 'acts_table': rows,
    'source': 'The Illinois Constitution pages of the Legislative Reference Bureau and the Illinois Compiled Statutes files of the [Illinois General Assembly](https://www.ilga.gov/), read from Internet Archive captures because ilga.gov refuses connections from the build machine. English. Only statute and Constitution text and the compilation\'s own "(Source: ...)" lines are taken.',
    'dates': 'The General Assembly\'s files carry the current text only. Each article is therefore one version, "oldest version available". The ILCS articles are dated 2024-12-22, the file date every file in the /ftp/ILCS/ directory listing shows (the pages were read from Internet Archive captures of February 2025). The Constitution is dated 2026-01-01, the day of the Internet Archive capture read; it was adopted on 1970-12-15 and the text is as amended to that capture. Later builds will add later versions on top.',
    'limits': 'A first build: the Constitution and the first articles of the Criminal Code of 2012 (720 ILCS 5). The rest of the Criminal Code, the other chapters of the ILCS and the Public Acts are not included. There is no history before the dates above.',
    'license': """Source: Illinois General Assembly and Legislative Reference Bureau, https://www.ilga.gov/ (read from Internet Archive captures; retrieved 2026-10-30).

Statute text is not copyrightable: under the government edicts doctrine, as the Supreme Court applied it in Georgia v.
Public.Resource.Org, Inc., 590 U.S. 255 (2020), no one holds copyright in the laws that legislators make in their official
capacity. The ILCS FTP readme describes the web copy as not authoritative ("The only official copy of the law is the printed
copy"); no restriction on reuse of the text was found. No annotations are used.""",
    'publisher': 'Illinois General Assembly, ilga.gov', 'build': 'built', 'date': '2026-10-30',
})
