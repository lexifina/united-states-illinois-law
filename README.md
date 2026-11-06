# United States (Illinois): law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Illinois, United States, which global-law reads at `united-states/illinois/acts/`.

The law of Illinois as a git history: one file per provision, with `git blame` and `git log` working line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-*/` | Constitution of the State of Illinois (1970): the preamble, one folder per article, and the transition schedule | 1 | 139 provisions, text as read on 2026-01-01 |
| `ilcs-<chapter>-<act>[-article-NNNN]/` | Illinois Compiled Statutes: 1968 of the 2859 acts in force that the 72 chapter act lists name (one folder per act, or per article of a large act) | 1-2 | 50633 sections; each act dated by the day of the capture read (2024-12-22 to 2026-10-31) |

English. Only statute and Constitution text and the compilation's own "(Source: ...)" lines are taken.

## Dates

The General Assembly's pages carry the current text only. Each act is therefore one version, "oldest version available". The first build's articles of the Criminal Code of 2012 are dated 2024-12-22, the file date of the /ftp/ILCS/ files; acts read from the 2025 site are dated by the day of the Internet Archive capture read (the newest since 1 January 2025). The Constitution is dated 2026-01-01, the day of the capture read; it was adopted on 1970-12-15 and the text is as amended to that capture. Later builds will add later versions on top.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; the results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@ilga.gov.invalid`). In this first build no dated history is available, so every commit is credited to the publisher as "oldest version available". The committer is always Lexifina.

## Limits

1968 of the 2859 acts in force listed by the General Assembly are included. An act is included only when its page (or, for a large act, its full text or every article page) has a capture holding section text. Acts marked repealed or renumbered are not read. Left out so far: large act: no capture of its full text or of every article page (98); no section text on the page (527); no capture (217); large act: a page without section text (49). The Public Acts and administrative rules are not included. There is no history before the dates above.

## Archive additions

This partial rebuild uses Internet Archive captures of Illinois General Assembly pages. The existing coverage record above is retained; two additional listed acts are included below. Remaining gaps include uncaptured or incomplete text, undatable text, and source pages with alternative versions.

| Act | Sections | Source effective date | Capture |
| --- | ---: | --- | --- |
| Secretary of State Buildings in Cook County Act (15 ILCS 330) | 4 | 2007-01-01 | [20251207055418](https://web.archive.org/web/20251207055418id_/https://ilga.gov/Legislation/ILCS/Articles?ActID=203&ChapterID=4&Print=True) |
| Comptroller's Records Act (15 ILCS 415) | 7 | 2012-08-10 | [20251009230622](https://web.archive.org/web/20251009230622id_/https://ilga.gov/Legislation/ILCS/Articles?ActID=207&ChapterID=4&Print=True) |

These added current-text versions are dated by the latest explicit effective date in the compilation's own amendment notes. Capture timestamps identify the source snapshots. No earlier wording is reconstructed.

## ILCS static compilation additions

The [Illinois General Assembly static ILCS compilation](https://ftp.ilga.gov/ILCS/) is dated 30 October 2026, through Public Act 104-854. Its publisher states: “The only official copy of the law is the printed copy maintained by the Secretary of State’s office.” The provisions “have NOT been edited for publication, and are NOT in any sense the 'official' text”. The publisher says this copy should not be cited as official or authoritative.

Of the locally available compilation, 49 complete indexed acts have identifiers already represented in published records. Their static source text includes every section, act title and article heading in the publisher’s source index, in its Section Sequence. These static copies were validated separately; this update does not assert that the existing published versions equal those copies. Five other complete acts contain future-effective text and are held. No additional law version is included in this documentation update. The remaining static compilation is incomplete in the material available for this record.

Current-text preparation uses the latest explicit effective date in the source amendment notes. Where there is no explicit section effective date, they use the publisher’s compilation update date, 30 October 2026. Individual section source URLs and byte digests are recorded in `data/ilcs-static-additions.json` when additions are available. Source pages containing future-effective text or normative images are held. No earlier wording is reconstructed. Existing records above retain their historical date labels.

## Static ILCS compilation additions, 30 October 2026

27 additional complete indexed acts from the [Illinois General Assembly compilation](https://ftp.ilga.gov/ILCS/) are included. The compilation incorporates Public Acts through 104-854. The publisher states that these provisions have NOT been edited for publication and are NOT the official text; this copy should not be cited as official or authoritative. The only official copy is the printed copy maintained by the Secretary of State’s office.

Each addition retains all sections, act-title documents and article headings in the publisher’s Section Sequence. Dates use the latest explicit amendment effective date in the source, otherwise the compilation’s own update date, 2026-10-30. This date fallback does not claim a commencement date the source does not identify. Future-effective text and normative images are held. Existing records retain their historical dates and text; their inclusion above does not establish equality with this static compilation. Public Acts, administrative rules and earlier wording are not added.

| Act | Sections | Source date |
| --- | ---: | --- |
| [State Services Assurance Act for FY2008 (5 ILCS 382)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200382/) | 6 | 2025-08-15 |
| [State Employment Records Act (5 ILCS 410)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200410/) | 8 | 2025-07-01 |
| [Pekin and Greenville Federal Correctional Institutions Cession Law (5 ILCS 517)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200517/) | 20 | 2026-10-30 |
| [Chanute Air Force Base Retrocession Law (5 ILCS 537)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200537/) | 20 | 2026-10-30 |
| [Ft. Dearborn United States Army Reserve Center Retrocession Law (5 ILCS 539)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200539/) | 3 | 1999-07-30 |
| [Glenview Naval Air Station Retrocession Law (5 ILCS 543)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200543/) | 6 | 1995-06-30 |
| [Joliet Outdoor Training Area Military Reservation Retrocession Law (5 ILCS 573)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200573/) | 39 | 2026-10-30 |
| [State Fair Grounds Title Law of the Civil Administrative Code of Illinois (5 ILCS 620)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200620/) | 2 | 2000-01-01 |
| [Successor Agency Act (5 ILCS 705)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200705/) | 5 | 1995-08-04 |
| [Gun Trafficking Information Act (5 ILCS 830)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200830/) | 4 | 2026-01-01 |
| [Uniform Faithful Presidential Electors Act (10 ILCS 22)](https://ftp.ilga.gov/ILCS/Ch%200010/Act%200022/) | 18 | 2025-08-15 |
| [Illinois Congressional Redistricting Act of 2021 (10 ILCS 78)](https://ftp.ilga.gov/ILCS/Ch%200010/Act%200078/) | 7 | 2021-11-23 |
| [Chicago Board of Education District Act (10 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200010/Act%200115/) | 6 | 2024-03-18 |
| [Governor Transition Act (15 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200010/) | 2 | 2026-10-30 |
| [Executive Reorganization Implementation Act (15 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200015/) | 16 | 2021-08-20 |
| [Executive Order 1 (2012 (15 ILCS 16)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200016/) | 25 | 2025-08-15 |
| [Executive Order 3 (2017 (15 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200017/) | 31 | 2021-08-20 |
| [Governors Conference Act (15 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200025/) | 2 | 2026-10-30 |
| [Gubernatorial Boards and Commissions Act (15 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200050/) | 10 | 2018-01-01 |
| [Pollution Abatement Enforcement Act (15 ILCS 215)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200215/) | 3 | 2026-10-30 |
| [Illinois State Library Foundation Act (15 ILCS 321)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200321/) | 6 | 2004-01-01 |
| [Lost State Archives Act (15 ILCS 325)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200325/) | 2 | 2026-10-30 |
| [State Comptroller Act (15 ILCS 405)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200405/) | 70 | 2026-07-01 |
| [Comptroller Merit Employment Code (15 ILCS 410)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200410/) | 57 | 2025-11-21 |
| [Treasurer as Custodian of Funds Act (15 ILCS 515)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200515/) | 6 | 1996-02-07 |
| [Securities Safekeeping Act (15 ILCS 525)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200525/) | 2 | 2026-10-30 |
| [Disabled Militarymen Money Act (15 ILCS 540)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200540/) | 3 | 2026-10-30 |
