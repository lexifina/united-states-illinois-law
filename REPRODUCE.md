# How this repository was made (United States (Illinois))

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Illinois Constitution and Illinois Compiled Statutes (ilga.gov), read from Internet Archive captures | <https://www.ilga.gov/> | 2026-10-30 | Statute text carries no copyright (Georgia v. Public.Resource.Org, 2020). The ILCS FTP readme calls the web copy non-authoritative ("The only official copy of the law is the printed copy"); no reuse restriction was found. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution-art-01` | Constitution of the State of Illinois, ARTICLE I BILL OF RIGHTS | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-02` | Constitution of the State of Illinois, ARTICLE II THE POWERS OF THE STATE | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-03` | Constitution of the State of Illinois, ARTICLE III SUFFRAGE AND ELECTIONS | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-04` | Constitution of the State of Illinois, ARTICLE IV THE LEGISLATURE | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-05` | Constitution of the State of Illinois, ARTICLE V THE EXECUTIVE | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-06` | Constitution of the State of Illinois, ARTICLE VI THE JUDICIARY | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-07` | Constitution of the State of Illinois, ARTICLE VII LOCAL GOVERNMENT | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-08` | Constitution of the State of Illinois, ARTICLE VIII FINANCE | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-09` | Constitution of the State of Illinois, ARTICLE IX REVENUE | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-10` | Constitution of the State of Illinois, ARTICLE X EDUCATION | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-11` | Constitution of the State of Illinois, ARTICLE XI ENVIRONMENT | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-12` | Constitution of the State of Illinois, ARTICLE XII MILITIA | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-13` | Constitution of the State of Illinois, ARTICLE XIII GENERAL PROVISIONS | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-art-14` | Constitution of the State of Illinois, ARTICLE XIV CONSTITUTIONAL REVISION | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-preamble` | Constitution of the State of Illinois, Preamble | 1 | 2026-01-01 to 2026-01-01 |
| `constitution-transition-schedule` | Constitution of the State of Illinois, Transition Schedule | 1 | 2026-01-01 to 2026-01-01 |
| `ilcs-720-5-article-0001` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 1 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0010` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 10 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0003` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 3 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0004` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 4 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0005` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 5 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0006` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 6 | 1 | 2024-12-22 to 2024-12-22 |
| `ilcs-720-5-article-0009` | Illinois Compiled Statutes, Criminal Code of 2012 (720 ILCS 5), Article 9 | 1 | 2024-12-22 to 2024-12-22 |

The build made 23 commits:

| Commits | Kind |
| ---: | --- |
| 23 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 23 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No dated history is published: each act is the oldest version available, dated by the source's own currency statement. https://www.ilga.gov/ftp/ILCS/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `79474259289b9aeedfa4ba73ac85113290475872995266ba526d1a349950f8ed` (247369 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- ILCS acts are dated 2024-12-22, the file date every file in the /ftp/ILCS/ directory listing shows; each section page was taken from the Internet Archive capture nearest after 2025-01-01 (all February 2025).
- The Constitution acts are dated 2026-01-01, the day the Internet Archive capture read was nearest; the Constitution was adopted 1970-12-15 and the text is as amended to that capture.
- One act per article of the Constitution and per article of each ILCS act; one unit per section. The "(Source: P.A. ...)" line kept as a section's last line is the compilation's own source note, not an annotation.
- Only section files of the ILCS tree are read; article headings, tables of contents and notes files are not copied.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
