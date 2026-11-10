# United States (Illinois): law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Illinois, United States, which global-law reads at `united-states/illinois/acts/`.

The law of Illinois as a git history: one file per provision, with `git blame` and `git log` working line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-*/` | Constitution of the State of Illinois (1970): the preamble, one folder per article, and the transition schedule | 1 | 139 provisions, text as read on 2026-01-01 |
| `ilcs-<chapter>-<act>[-article-NNNN]/` | Illinois Compiled Statutes: 1382 of the 2859 acts in force that the 72 chapter act lists name (one folder per act, or per article of a large act) | 1-2 | 36455 sections; each act dated by the day of the capture read (2024-12-22 to 2026-10-22) |

English. Only statute and Constitution text and the compilation's own "(Source: ...)" lines are taken.

## Dates

The General Assembly's pages carry the current text only. Each act is therefore one version, "oldest version available". The first build's articles of the Criminal Code of 2012 are dated 2024-12-22, the file date of the /ftp/ILCS/ files; acts read from the 2025 site are dated by the day of the Internet Archive capture read (the newest since 1 January 2025). The Constitution is dated 2026-01-01, the day of the capture read; it was adopted on 1970-12-15 and the text is as amended to that capture. Later builds will add later versions on top.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; the results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@ilga.gov.invalid`). In this first build no dated history is available, so every commit is credited to the publisher as "oldest version available". The committer is always Lexifina.

## Limits

1382 of the 2859 acts in force listed by the General Assembly are included. An act is included only when its page (or, for a large act, its full text or every article page) has a capture holding section text. Acts marked repealed or renumbered are not read. Left out so far: large act: no capture of its full text or of every article page (88); no section text on the page (366); no capture (987); large act: a page without section text (37). The Public Acts and administrative rules are not included. There is no history before the dates above.
