# United States (Illinois): law history in git

The law of Illinois as a git history: one file per provision, with `git blame` and `git log` working line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-*/` | Constitution of the State of Illinois (1970): the preamble, one folder per article, and the transition schedule | 1 | 139 provisions, text as read on 2026-01-01 |
| `ilcs-720-5-article-0001/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 1 | 1 | 7 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0010/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 10 | 1 | 14 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0003/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 3 | 1 | 8 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0004/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 4 | 1 | 9 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0005/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 5 | 1 | 5 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0006/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 6 | 1 | 4 sections, text as of 2024-12-22 |
| `ilcs-720-5-article-0009/` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 9 | 1 | 11 sections, text as of 2024-12-22 |

English. Only statute and Constitution text and the compilation's own "(Source: ...)" lines are taken.

## Dates

The General Assembly's files carry the current text only. Each article is therefore one version, "oldest version available". The ILCS articles are dated 2024-12-22, the file date every file in the /ftp/ILCS/ directory listing shows (the pages were read from Internet Archive captures of February 2025). The Constitution is dated 2026-01-01, the day of the Internet Archive capture read; it was adopted on 1970-12-15 and the text is as amended to that capture. Later builds will add later versions on top.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; the results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@ilga.gov.invalid`). In this first build no dated history is available, so every commit is credited to the publisher as "oldest version available". The committer is always Lexifina.

## Limits

A first build: the Constitution and the first articles of the Criminal Code of 2012 (720 ILCS 5). The rest of the Criminal Code, the other chapters of the ILCS and the Public Acts are not included. There is no history before the dates above.
