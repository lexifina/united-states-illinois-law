# United States (Illinois): law history in git

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Illinois law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

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

752 additional complete indexed acts from the [Illinois General Assembly compilation](https://ftp.ilga.gov/ILCS/) are included. The compilation incorporates Public Acts through 104-854. The publisher states that these provisions have NOT been edited for publication and are NOT the official text; this copy should not be cited as official or authoritative. The only official copy is the printed copy maintained by the Secretary of State’s office.

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
| [Open Operating Standards Act (20 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200045/) | 10 | 2020-01-01 |
| [Uniform Racial Classification Act (20 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200050/) | 3 | 2024-01-01 |
| [State Agency Student Worker Opportunity Act (20 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200055/) | 3 | 2018-01-01 |
| [Native American Employment Plan Act (20 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200060/) | 6 | 2020-01-01 |
| [Department of Agriculture Law of the Civil Administrative Code of Illinois (20 ILCS 205)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200205/) | 52 | 2023-07-28 |
| [State Fair Act (20 ILCS 210)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200210/) | 19 | 2026-06-16 |
| [Rural Rehabilitation Corporation Act (20 ILCS 220)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200220/) | 8 | 2007-08-21 |
| [Department of Human Services (Alcoholism and Substance Abuse (20 ILCS 310)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200310/) | 2 | 2005-09-11 |
| [Department of Central Management Services Law of the Civil Administrative Code of Illinois (20 ILCS 405)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200405/) | 69 | 2026-08-21 |
| [Forms Notice Act (20 ILCS 435)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200435/) | 7 | 1998-07-01 |
| [Office of Consumer Services Information Act (20 ILCS 440)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200440/) | 3 | 2026-10-30 |
| [State Off Street Parking in Rockford Act (20 ILCS 445)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200445/) | 2 | 2026-10-30 |
| [Data Security on State Computers Act (20 ILCS 450)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200450/) | 9 | 2018-01-01 |
| [Foster Parent Law (20 ILCS 520)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200520/) | 8 | 2025-08-15 |
| [Statewide Foster Care Advisory Council Law (20 ILCS 525)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200525/) | 11 | 2023-08-08 |
| [Brownfields Redevelopment and Intermodal Promotion Act (20 ILCS 607)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200607/) | 14 | 2021-08-20 |
| [Electric Vehicle Act (20 ILCS 627)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200627/) | 11 | 2026-08-21 |
| [Renewable Energy, Energy Efficiency, and Coal Resources Development Law of 1997 (20 ILCS 687)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200687/) | 14 | 2025-06-16 |
| [Small Business Advisory Act (20 ILCS 692)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200692/) | 4 | 2006-05-19 |
| [State and Regional Development Strategy Act (20 ILCS 695)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200695/) | 5 | 2005-01-15 |
| [Technology Advancement and Development Act (20 ILCS 700)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200700/) | 25 | 2025-11-21 |
| [Energy Transition Act (20 ILCS 730)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200730/) | 40 | 2026-06-26 |
| [Energy Community Reinvestment Act (20 ILCS 735)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200735/) | 34 | 2025-02-20 |
| [Job Training Assistance and Support Services Pilot Program Act (20 ILCS 740)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200740/) | 6 | 2023-01-01 |
| [Forest Land Exchange Act (20 ILCS 825)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200825/) | 2 | 1996-02-07 |
| [Interagency Wetland Policy Act of 1989 (20 ILCS 830)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200830/) | 15 | 2018-08-03 |
| [Illinois and Michigan Canal State Park Act (20 ILCS 850)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200850/) | 5 | 1996-02-07 |
| [Department of Natural Resources World Shooting and Recreational Complex Act (20 ILCS 861)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200861/) | 12 | 2026-08-21 |
| [Recreational Trails of Illinois Act (20 ILCS 862)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200862/) | 24 | 2022-01-01 |
| [Prairie Wind Trail Property Transfer Act (20 ILCS 863)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200863/) | 8 | 2018-08-03 |
| [Kaskaskia River Watershed Operation and Maintenance Act (20 ILCS 865)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200865/) | 2 | 1996-02-07 |
| [Firearms Training Act (20 ILCS 875)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200875/) | 4 | 1996-02-07 |
| [Natural Resources Restoration Trust Fund Act (20 ILCS 882)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200882/) | 5 | 2014-08-19 |
| [Lake Michigan Wind Energy Act (20 ILCS 896)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200896/) | 12 | 2025-11-21 |
| [Public Employment Office Act (20 ILCS 1015)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201015/) | 18 | 2020-01-01 |
| [Clean Coal FutureGen for Illinois Act of 2011 (20 ILCS 1108)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201108/) | 23 | 2011-10-26 |
| [Illinois Coal and Energy Development Bond Act (20 ILCS 1110)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201110/) | 19 | 2022-06-10 |
| [Energy Conservation Act (20 ILCS 1115)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201115/) | 5 | 2021-08-20 |
| [Hazardous Waste Technology Exchange Service Act (20 ILCS 1130)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201130/) | 6 | 2013-08-14 |
| [Financial Institutions Act (20 ILCS 1205)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201205/) | 22 | 2026-08-21 |
| [Domestic Violence Shelters Act (20 ILCS 1310)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201310/) | 7 | 2026-06-16 |
| [Assistive Technology Evaluation and Training Centers Act (20 ILCS 1320)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201320/) | 6 | 1998-01-01 |
| [2-1-1 Service Act (20 ILCS 1335)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201335/) | 16 | 2026-08-21 |
| [Department of Insurance Law of the Civil Administrative Code of Illinois (20 ILCS 1405)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201405/) | 13 | 2025-08-15 |
| [Burn Victims Relief Act (20 ILCS 1410)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201410/) | 9 | 2019-07-01 |
| [Department of Labor Law of the Civil Administrative Code of Illinois (20 ILCS 1505)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201505/) | 22 | 2026-01-01 |
| [Department of Human Services (Mental Health and Developmental Disabilities (20 ILCS 1710)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201710/) | 11 | 2026-06-16 |
| [Illinois Code of Military Justice (20 ILCS 1807)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201807/) | 199 | 2025-08-01 |
| [Military Property Act (20 ILCS 1810)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201810/) | 3 | 2026-10-30 |
| [Illinois State Guard Act (20 ILCS 1815)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201815/) | 12 | 2018-08-22 |
| [Illinois National Guardsman's Compensation Act (20 ILCS 1825)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201825/) | 5 | 2006-06-08 |
| [Department of Natural Resources (Mines and Minerals (20 ILCS 1905)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201905/) | 19 | 2021-08-20 |
| [Coal Products Commission Transfer Act (20 ILCS 1910)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201910/) | 2 | 1996-02-07 |
| [Surface Coal Mining Fee Act (20 ILCS 1915)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201915/) | 3 | 1999-07-29 |
| [Abandoned Mined Lands and Water Reclamation Act (20 ILCS 1920)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201920/) | 27 | 2019-01-01 |
| [Illinois Health Finance Reform Act (20 ILCS 2215)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202215/) | 15 | 2021-04-27 |
| [Health Care Affordability Act (20 ILCS 2230)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202230/) | 14 | 2020-07-07 |
| [Health Access Network Act (20 ILCS 2320)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202320/) | 8 | 2007-10-11 |
| [Disabilities Services Act of 2003 (20 ILCS 2407)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202407/) | 10 | 2025-11-21 |
| [Civil Administrative Code of Illinois (20 ILCS 2415)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202415/) | 1 | 1994-07-01 |
| [Certified Audit Program Law of the Civil Administrative Code of Illinois (20 ILCS 2510)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202510/) | 8 | 2001-08-21 |
| [Narcotic Control Division Abolition Act (20 ILCS 2620)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202620/) | 10 | 2024-07-01 |
| [Volunteer Firefighting Rescue Unit Use Act (20 ILCS 2625)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202625/) | 5 | 2026-01-01 |
| [Peace Officer Fire Investigation Act (20 ILCS 2910)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202910/) | 2 | 2023-07-01 |
| [Capital Spending Accountability Law (20 ILCS 3020)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203020/) | 3 | 2021-08-06 |
| [Capital Development Board Act (20 ILCS 3105)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203105/) | 87 | 2026-01-01 |
| [Asbestos Abatement Authority Act (20 ILCS 3120)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203120/) | 6 | 2004-08-12 |
| [Green Buildings Act (20 ILCS 3130)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203130/) | 5 | 2018-08-03 |
| [Mechanical Insulation Energy and Safety Assessment Act (20 ILCS 3135)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203135/) | 57 | 2024-01-01 |
| [Division of Banking Act (20 ILCS 3205)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203205/) | 24 | 2024-03-22 |
| [Historic Preservation Act (20 ILCS 3405)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203405/) | 33 | 2025-08-15 |
| [Reimagining Hotel Florence Act (20 ILCS 3407)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203407/) | 13 | 2025-01-01 |
| [Archaeological and Paleontological Resources Protection Act (20 ILCS 3435)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203435/) | 17 | 2024-07-01 |
| [Human Remains Protection Act (20 ILCS 3440)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203440/) | 23 | 2024-07-01 |
| [Abraham Lincoln Presidential Library and Museum Act (20 ILCS 3475)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203475/) | 24 | 2025-06-16 |
| [Asbestos Abatement Finance Act (20 ILCS 3510)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203510/) | 11 | 2026-07-01 |
| [Illinois Environmental Facilities Financing Act (20 ILCS 3515)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203515/) | 18 | 2018-12-10 |
| [Capital Punishment Reform Study Committee Act (20 ILCS 3929)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203929/) | 11 | 2008-08-22 |
| [Illinois Business Regulatory Review Act (20 ILCS 3966)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203966/) | 13 | 2006-05-19 |
| [Illinois Workforce Innovation Board Act (20 ILCS 3975)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203975/) | 12 | 2025-08-15 |
| [Laboratory Review Board Act (20 ILCS 3980)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203980/) | 4 | 2021-08-20 |
| [Illinois Latino Family Commission Act (20 ILCS 3983)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203983/) | 9 | 2022-01-01 |
| [Law Enforcement and Fire Fighting Medal of Honor Act (20 ILCS 3985)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203985/) | 8 | 2024-01-01 |
| [Illinois Manufacturing Technology Alliance Act (20 ILCS 3990)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203990/) | 15 | 2006-05-19 |
| [Minority Males Act (20 ILCS 4000)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204000/) | 6 | 2026-10-30 |
| [Illinois Vehicle Hijacking and Motor Vehicle Theft Prevention and Insurance Verification Act (20 ILCS 4005)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204005/) | 14 | 2025-06-16 |
| [Illinois Council on Developmental Disabilities Law (20 ILCS 4010)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204010/) | 8 | 2022-04-19 |
| [Sex Offender Management Board Act (20 ILCS 4026)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204026/) | 11 | 2026-08-21 |
| [World's Fair Commission (1976 (20 ILCS 4030)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204030/) | 7 | 2026-10-30 |
| [Commission on Discrimination and Hate Crimes Act (20 ILCS 4070)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204070/) | 8 | 2007-08-24 |
| [Commission on Children and Youth Act (20 ILCS 4075)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204075/) | 9 | 2008-08-05 |
| [High-Speed Railway Commission Act (20 ILCS 4102)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204102/) | 6 | 2026-07-24 |
| [Advisory Commission on Reducing the Disproportionate Representation of African-American Children in Foster Care Act (20 ILCS 4104)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204104/) | 6 | 2024-01-01 |
| [Illinois America 250 Commission Act (20 ILCS 4114)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204114/) | 11 | 2022-05-27 |
| [Rivers of Illinois Coordinating Council Act (20 ILCS 4117)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204117/) | 9 | 2023-01-01 |
| [Water Plan Task Force Act (20 ILCS 4132)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204132/) | 3 | 2025-08-15 |
| [Farmland Transition Commission Act (20 ILCS 4135)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204135/) | 2 | 2026-01-01 |
| [Commission on Youth Sports Act (20 ILCS 4136)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204136/) | 7 | 2025-08-15 |
| [Health Care Workforce Task Force Act (20 ILCS 4137)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204137/) | 9 | 2026-01-01 |
| [Climate Displacement Task Force Act (20 ILCS 4138)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204138/) | 7 | 2026-07-24 |
| [Illinois Holocaust and Genocide Commission Act (20 ILCS 5010)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%205010/) | 13 | 2026-06-16 |
| [Racial and Ethnic Impact Research Task Force Act (20 ILCS 5025)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%205025/) | 6 | 2021-08-20 |
| [Illinois Route 66 Centennial Commission Act (20 ILCS 5125)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%205125/) | 11 | 2019-07-12 |
| [Illinois Council on Women and Girls Act (20 ILCS 5130)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%205130/) | 9 | 2026-08-07 |
| [General Assembly Organization Act (25 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200005/) | 17 | 2018-12-10 |
| [General Assembly Operations Act (25 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200010/) | 10 | 2026-07-01 |
| [Special Session Act (25 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200015/) | 4 | 2026-10-30 |
| [House Voting Device Act (25 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200020/) | 4 | 2026-10-30 |
| [Pre-Filing of Bills Act (25 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200025/) | 6 | 1994-09-16 |
| [Bill Synopsis Act (25 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200030/) | 2 | 2026-10-30 |
| [Bill Introduction and Duplication Act (25 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200035/) | 3 | 1994-09-16 |
| [Governor's Bill Action Report Act (25 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200040/) | 3 | 2026-10-30 |
| [State Debt Impact Note Act (25 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200065/) | 9 | 2005-01-15 |
| [Correctional Budget and Impact Note Act (25 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200070/) | 9 | 2001-06-28 |
| [Housing Affordability Impact Note Act (25 ILCS 82)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200082/) | 8 | 2017-08-18 |
| [Racial Impact Note Act (25 ILCS 83)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200083/) | 7 | 2021-12-17 |
| [General Assembly Appointments Act (25 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200090/) | 2 | 2026-10-30 |
| [General Assembly Appointing Authority Act (25 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200095/) | 3 | 2026-10-30 |
| [Debate Transcript Act (25 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200100/) | 3 | 2026-10-30 |
| [Legislative Materials Act (25 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200105/) | 2 | 2023-01-09 |
| [Reports to the Commission on Government Forecasting and Accountability Act (25 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200110/) | 2 | 2018-12-10 |
| [General Assembly Compensation Act (25 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200115/) | 13 | 2023-01-09 |
| [Compensation Review Act (25 ILCS 120)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200120/) | 19 | 2018-06-04 |
| [Legislative Commission Reorganization Act of 1984 (25 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200130/) | 45 | 2025-08-15 |
| [Legislative Reference Bureau Act (25 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200135/) | 12 | 2025-08-15 |
| [Statute Computerization Act (25 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200140/) | 4 | 2026-10-30 |
| [Legislative Information System Act (25 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200145/) | 17 | 2018-12-10 |
| [General Assembly Staff Assistants Act (25 ILCS 160)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200160/) | 3 | 2003-11-19 |
| [National Conference of State Legislatures Act (25 ILCS 165)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200165/) | 2 | 2026-10-30 |
| [Council of State Governments Act (25 ILCS 166)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200166/) | 54 | 2024-01-01 |
| [Legislative Accessibility Act (25 ILCS 175)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200175/) | 4 | 2025-01-01 |
| [Public Funds Statement Publication Act (30 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200015/) | 10 | 2012-01-01 |
| [Public Funds Accounting Act (30 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200020/) | 10 | 2002-06-24 |
| [State Revenue Sharing Act (30 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200115/) | 12 | 2026-06-16 |
| [Fair and Exposition Transfer of Funds Act (30 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200135/) | 2 | 2026-10-30 |
| [Illinois Non-Game Wildlife Protection Act (30 ILCS 155)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200155/) | 4 | 2013-01-01 |
| [Tobacco Product Manufacturers' Escrow Act (30 ILCS 168)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200168/) | 6 | 2025-06-16 |
| [Railsplitter Tobacco Settlement Authority Act (30 ILCS 171)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200171/) | 16 | 2023-06-07 |
| [Transportation Funding Protection Act (30 ILCS 178)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200178/) | 3 | 2019-06-28 |
| [Uncollected State Claims Act (30 ILCS 205)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200205/) | 4 | 2011-08-19 |
| [Illinois State Collection Act of 1986 (30 ILCS 210)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200210/) | 12 | 2019-06-28 |
| [Gifts to State for Charitable Use Act (30 ILCS 215)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200215/) | 2 | 2026-10-30 |
| [Fees and Salaries Act (30 ILCS 220)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200220/) | 3 | 1996-01-01 |
| [Public Funds Deposit Act (30 ILCS 225)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200225/) | 3 | 2021-08-06 |
| [Public Funds Investment Act (30 ILCS 235)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200235/) | 14 | 2026-01-01 |
| [Accountability for the Investment of Public Funds Act (30 ILCS 237)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200237/) | 4 | 2025-08-15 |
| [Public Funds in Failed Banks Act (30 ILCS 240)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200240/) | 2 | 2026-10-30 |
| [Tennessee Valley Authority Payment Act (30 ILCS 250)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200250/) | 2 | 2011-06-28 |
| [Technology Development Act (30 ILCS 265)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200265/) | 8 | 2023-01-01 |
| [Bond Authorization Act (30 ILCS 305)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200305/) | 7 | 2004-01-01 |
| [Illinois Bond Replacement Act (30 ILCS 315)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200315/) | 9 | 2026-10-30 |
| [General Obligation Bond Act (30 ILCS 330)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200330/) | 30 | 2026-06-16 |
| [General Obligation Bond Investment Act (30 ILCS 335)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200335/) | 3 | 2026-10-30 |
| [Short Term Borrowing Act (30 ILCS 340)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200340/) | 5 | 2020-05-29 |
| [Coronavirus Urgent Remediation Emergency Borrowing Act (30 ILCS 343)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200343/) | 8 | 2020-05-29 |
| [Bond Issue Notification Act (30 ILCS 352)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200352/) | 13 | 2018-06-01 |
| [Public Works Finance Act (30 ILCS 370)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200370/) | 2 | 2026-10-30 |
| [Local Government Debt Offering Act (30 ILCS 375)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200375/) | 9 | 2021-08-06 |
| [Build Illinois Bond Act (30 ILCS 425)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200425/) | 20 | 2026-06-16 |
| [Human Services Provider Bond Reserve Payment Act (30 ILCS 435)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200435/) | 7 | 2007-08-21 |
| [Illinois Unemployment Insurance Trust Fund Financing Act (30 ILCS 440)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200440/) | 18 | 2011-11-18 |
| [Climate Bank Loan Financing Act (30 ILCS 445)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200445/) | 11 | 2025-06-16 |
| [Procurement of Domestic Products Act (30 ILCS 517)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200517/) | 10 | 2023-01-01 |
| [Transportation Sustainability Procurement Program Act (30 ILCS 530)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200530/) | 5 | 2024-01-01 |
| [Design-Build Procurement Act (30 ILCS 537)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200537/) | 16 | 2026-06-26 |
| [Public Contract Fraud Act (30 ILCS 545)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200545/) | 5 | 2025-01-01 |
| [Illinois Mined Coal Act (30 ILCS 555)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200555/) | 5 | 1996-02-07 |
| [Public Construction Contract Act (30 ILCS 557)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200557/) | 7 | 1999-11-30 |
| [Public-Private Partnership for Civic and Transit Infrastructure Project Act (30 ILCS 558)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200558/) | 42 | 2021-08-20 |
| [Illinois Works Jobs Program Act (30 ILCS 559)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200559/) | 46 | 2026-06-16 |
| [Steel Products Procurement Act (30 ILCS 565)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200565/) | 7 | 2026-10-30 |
| [State Entities Single-Use Plastic Reporting Act (30 ILCS 567)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200567/) | 5 | 2023-08-04 |
| [Drug Free Workplace Act (30 ILCS 580)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200580/) | 11 | 2026-10-30 |
| [International Anti-Boycott Certification Act (30 ILCS 582)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200582/) | 6 | 1999-07-29 |
| [Data Processing Confidentiality Act (30 ILCS 585)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200585/) | 3 | 2026-10-30 |
| [State Property Control Act (30 ILCS 605)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200605/) | 37 | 2026-01-01 |
| [State Facilities Closure Act (30 ILCS 608)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200608/) | 6 | 2025-08-15 |
| [Grant Information Collection Act (30 ILCS 707)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200707/) | 3 | 2018-07-20 |
| [Rural Economic Development Act (30 ILCS 710)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200710/) | 14 | 2026-08-21 |
| [Intergovernmental Drug Laws Enforcement Act (30 ILCS 715)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200715/) | 12 | 2026-07-31 |
| [Industrial Development Assistance Law (30 ILCS 720)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200720/) | 8 | 2023-07-28 |
| [Illinois Coal Technology Development Assistance Act (30 ILCS 730)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200730/) | 6 | 2026-06-16 |
| [Urban and Community Forestry Assistance Act (30 ILCS 735)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200735/) | 7 | 2026-01-01 |
| [Urban Weatherization Initiative Act (30 ILCS 738)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200738/) | 11 | 2026-08-07 |
| [Downstate Public Transportation Act (30 ILCS 740)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200740/) | 70 | 2026-07-10 |
| [Intermodal Facilities Promotion Act (30 ILCS 743)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200743/) | 10 | 2009-08-21 |
| [Public Radio and Television Grant Act (30 ILCS 745)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200745/) | 10 | 1999-06-09 |
| [Invest in Illinois Act (30 ILCS 751)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200751/) | 31 | 2023-02-03 |
| [Community Youth Employment Act (30 ILCS 757)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200757/) | 5 | 2010-07-23 |
| [Business Economic Support Act (30 ILCS 760)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200760/) | 4 | 2026-10-30 |
| [Park and Recreational Facility Construction Act of 2009 (30 ILCS 764)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200764/) | 11 | 2021-08-20 |
| [Illinois Equal Justice Act (30 ILCS 765)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200765/) | 11 | 2026-06-16 |
| [Community Health Center Construction Act (30 ILCS 766)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200766/) | 7 | 2009-07-13 |
| [Public Library Construction Act (30 ILCS 767)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200767/) | 14 | 2020-06-10 |
| [Private Colleges and Universities Capital Distribution Formula Act (30 ILCS 769)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200769/) | 6 | 2025-06-16 |
| [Employee Wellness Program Grant Act (30 ILCS 770)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200770/) | 11 | 1996-12-31 |
| [Equity in Long-term Care Quality Act (30 ILCS 772)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200772/) | 9 | 2025-11-21 |
| [Eliminate the Digital Divide Law (30 ILCS 780)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200780/) | 13 | 2026-08-21 |
| [Inclusion of Women and Minorities in Clinical Research Act (30 ILCS 785)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200785/) | 7 | 2022-01-01 |
| [State Mandates Act (30 ILCS 805)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200805/) | 60 | 2026-08-21 |
| [Economic Development for a Growing Economy Tax Credit Act (35 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200010/) | 30 | 2026-08-21 |
| [Live Theater Production Tax Credit Act (35 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200017/) | 13 | 2026-06-16 |
| [Tax Shelter Voluntary Compliance Law (35 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200020/) | 6 | 2004-07-30 |
| [Small Business Job Creation Tax Credit Act (35 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200025/) | 13 | 2018-08-14 |
| [Historic Preservation Tax Credit Pilot Program Act (35 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200030/) | 8 | 2018-08-03 |
| [State Tax Preparer Oversight Act (35 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200035/) | 6 | 2017-01-01 |
| [Manufacturing Illinois Chips for Real Opportunity (MICRO (35 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200045/) | 31 | 2026-08-21 |
| [Recovery and Mental Health Tax Credit Act (35 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200050/) | 8 | 2022-06-10 |
| [Advancing Innovative Manufacturing for Illinois Tax Credit Act (35 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200065/) | 16 | 2026-01-01 |
| [Service Use Tax Act (35 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200110/) | 53 | 2026-08-21 |
| [Cigarette Machine Operators' Occupation Tax Act (35 ILCS 128)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200128/) | 39 | 2026-06-16 |
| [Cigarette Use Tax Act (35 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200135/) | 55 | 2026-06-16 |
| [Home Rule Cigarette Tax Restriction Act (35 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200140/) | 2 | 2026-10-30 |
| [Tobacco Products Tax Act of 1995 (35 ILCS 143)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200143/) | 51 | 2026-08-21 |
| [Use and Occupation Tax Refund Act (35 ILCS 150)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200150/) | 2 | 2026-06-01 |
| [Watercraft Use Tax Law (35 ILCS 158)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200158/) | 13 | 2004-07-30 |
| [Simplified Sales and Use Tax Administration Act (35 ILCS 171)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200171/) | 14 | 2026-06-01 |
| [Gas Use Tax Law (35 ILCS 173)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200173/) | 13 | 2024-06-26 |
| [Leveling the Playing Field for Illinois Retail Act (35 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200185/) | 46 | 2025-06-16 |
| [Targeted Advertising Services Tax Act (35 ILCS 190)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200190/) | 55 | 2026-07-01 |
| [Digital Asset Tax Act (35 ILCS 195)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200195/) | 51 | 2026-07-01 |
| [Illinois Hydraulic Fracturing Tax Act (35 ILCS 450)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200450/) | 17 | 2019-01-04 |
| [Mobile Home Local Services Tax Act (35 ILCS 515)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200515/) | 24 | 2025-08-15 |
| [Mobile Home Local Services Tax Enforcement Act (35 ILCS 516)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200516/) | 94 | 2026-08-21 |
| [Illinois Central Railroad Tax Act (35 ILCS 605)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200605/) | 3 | 2026-10-30 |
| [Water Company Invested Capital Tax Act (35 ILCS 625)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200625/) | 16 | 2021-06-25 |
| [Simplified Municipal Telecommunications Tax Act (35 ILCS 636)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200636/) | 28 | 2024-06-26 |
| [Mobile Telecommunications Sourcing Conformity Act (35 ILCS 638)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200638/) | 23 | 2002-08-01 |
| [Tax Collection Suit Act (35 ILCS 705)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200705/) | 4 | 2026-10-30 |
| [Local Tax Collection Act (35 ILCS 720)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200720/) | 2 | 2017-08-18 |
| [Federal Excise Tax Refund Act (35 ILCS 730)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200730/) | 2 | 2026-10-30 |
| [Tax Delinquency Amnesty Act (35 ILCS 745)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200745/) | 5 | 2025-06-16 |
| [American Hostage Tax Liability Postponement Act (35 ILCS 746)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200746/) | 14 | 2026-01-01 |
| [State Tax Lien Registration Act (35 ILCS 750)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200750/) | 34 | 2020-01-01 |
| [Glenview Naval Air Station Tax Exemption Act (35 ILCS 805)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200805/) | 2 | 2026-10-30 |
| [Great Lakes Naval Station Tax Exemption Act (35 ILCS 810)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200810/) | 2 | 2026-10-30 |
| [Illinois Independent Tax Tribunal Act of 2012 (35 ILCS 1010)](https://ftp.ilga.gov/ILCS/Ch%200035/Act%201010/) | 49 | 2026-06-16 |
| [New Harmony Bridge Authority Act (45 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200185/) | 13 | 2018-08-19 |
| [Local Government Revenue Recapture Act (50 ILCS 355)](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200355/) | 22 | 2021-12-17 |
| [Local Government Electronic Reverse Auction Act (50 ILCS 531)](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200531/) | 5 | 2010-07-01 |
| [Police and Community Relations Improvement Act (50 ILCS 727)](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200727/) | 26 | 2023-07-01 |
| [Fees and Salaries Act (55 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200045/) | 10 | 1996-01-01 |
| [Revised Cities and Villages Act of 1941 (65 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200020/) | 53 | 2026-08-21 |
| [Mayoral Election Validation Act (65 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200025/) | 2 | 2026-10-30 |
| [Village Incorporation Validation Act (65 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200035/) | 2 | 2026-10-30 |
| [Town Incorporation Validation Act (65 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200040/) | 3 | 2026-10-30 |
| [Municipal Tax Validation (1989 (65 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200045/) | 2 | 2026-10-30 |
| [Municipal Validation Law of 2002 (65 ILCS 46)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200046/) | 4 | 2003-01-13 |
| [Municipal Federal Grant Tax and Bond Act (65 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200055/) | 26 | 1999-07-29 |
| [Neighborhood Security Patrol Act (65 ILCS 97)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200097/) | 13 | 2026-10-30 |
| [Sports Stadium Act (65 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200100/) | 5 | 2007-01-01 |
| [Shore Lands for Park Use Act (65 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200105/) | 2 | 2026-10-30 |
| [River Edge Redevelopment Zone Act (65 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200115/) | 21 | 2026-08-21 |
| [Civic Center Code (70 ILCS 200)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200200/) | 658 | 2026-06-16 |
| [Southern Illinois Economic Development Authority Act (70 ILCS 519)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200519/) | 18 | 2025-08-15 |
| [Chicago Submerged Lands (1931 (70 ILCS 1555)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%201555/) | 2 | 2026-10-30 |
| [Massac-Metropolis Port District Act (70 ILCS 1831)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%201831/) | 39 | 2009-12-16 |
| [Rock Island Regional Port District Act (70 ILCS 1842)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%201842/) | 29 | 2024-01-01 |
| [Railroad Terminal Authority Act (70 ILCS 1905)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%201905/) | 31 | 2007-01-01 |
| [Dixon Railroad Relocation Authority Law (70 ILCS 1925)](https://ftp.ilga.gov/ILCS/Ch%200070/Act%201925/) | 24 | 2007-08-21 |
| [License to Read Act (75 ILCS 12)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200012/) | 11 | 2023-06-30 |
| [Chicago Public Library Act (75 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200020/) | 3 | 2026-10-30 |
| [Maywood Public Library District Tax Levy Validation (2002 (75 ILCS 23)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200023/) | 4 | 2003-01-13 |
| [Township Library Bond Validation (1963 (75 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200025/) | 2 | 2026-10-30 |
| [Township Library Bond Validation (1969 (75 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200030/) | 2 | 2026-10-30 |
| [Village Library Conversion Act (75 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200045/) | 2 | 2026-10-30 |
| [Library Incorporation Act (75 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200060/) | 6 | 2010-01-01 |
| [Library Records Confidentiality Act (75 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200075/Act%200070/) | 2 | 2008-01-01 |
| [School Construction Law (105 ILCS 230)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200230/) | 30 | 2026-07-01 |
| [School District Intergovernmental Cooperation Renewable Energy Act (105 ILCS 240)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200240/) | 17 | 2010-06-25 |
| [Vocational Academies Act (105 ILCS 433)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200433/) | 5 | 2019-07-01 |
| [School Tax Rate Validation (1968 (105 ILCS 520)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200520/) | 2 | 2026-10-30 |
| [School Tax Rate Validation (1969 (105 ILCS 525)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200525/) | 2 | 2026-10-30 |
| [Educational Credit for Military Experience Act (110 ILCS 32)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200032/) | 4 | 2018-01-01 |
| [Grow Your Own Teacher Education Act (110 ILCS 48)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200048/) | 12 | 2019-07-26 |
| [Medical School Matriculant Criminal History Records Check Act (110 ILCS 57)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200057/) | 9 | 2026-01-01 |
| [Nonresident College Trustees Act (110 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200060/) | 2 | 2000-07-09 |
| [State University Certificates of Participation Act (110 ILCS 73)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200073/) | 11 | 2009-06-22 |
| [University Airport Access Road Act (110 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200080/) | 2 | 2026-10-30 |
| [University Faculty Research and Consulting Act (110 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200100/) | 4 | 1996-01-01 |
| [Public University Direct Admission Program Act (110 ILCS 117)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200117/) | 8 | 2025-06-30 |
| [Illinois Articulation Initiative Act (110 ILCS 152)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200152/) | 7 | 2024-08-09 |
| [Bridge Program for Underrepresented Students Act (110 ILCS 170)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200170/) | 7 | 2018-08-24 |
| [Transitions in Education Act (110 ILCS 180)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200180/) | 4 | 2025-11-21 |
| [Health Services Education Grants Act (110 ILCS 215)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200215/) | 7 | 2009-07-23 |
| [Equity in Higher Education Act (110 ILCS 235)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200235/) | 3 | 2021-03-08 |
| [University of Illinois Act (110 ILCS 305)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200305/) | 68 | 2026-08-07 |
| [University of Illinois at Chicago Land Transfer Act (110 ILCS 325)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200325/) | 6 | 2007-01-01 |
| [University of Illinois at Springfield Law (110 ILCS 327)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200327/) | 5 | 1995-07-01 |
| [Specialized Care for Children Act (110 ILCS 345)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200345/) | 4 | 2015-07-27 |
| [University of Illinois Works Projects Act (110 ILCS 410)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200410/) | 5 | 2026-10-30 |
| [University of Illinois Revenue Bond Act (110 ILCS 420)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200420/) | 9 | 2026-10-30 |
| [State Colleges and Universities Revenue Bond Act of 1967 (110 ILCS 615)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200615/) | 15 | 2007-01-01 |
| [Chicago State University Law (110 ILCS 660)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200660/) | 59 | 2026-08-07 |
| [Eastern Illinois University Law (110 ILCS 665)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200665/) | 60 | 2026-08-07 |
| [Eastern Illinois University Revenue Bond Law (110 ILCS 666)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200666/) | 15 | 2007-01-01 |
| [Governors State University Revenue Bond Law (110 ILCS 671)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200671/) | 15 | 2007-01-01 |
| [Northeastern Illinois University Revenue Bond Law (110 ILCS 681)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200681/) | 15 | 2007-01-01 |
| [Northern Illinois University Law (110 ILCS 685)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200685/) | 61 | 2026-08-07 |
| [Northern Illinois University Revenue Bond Law (110 ILCS 686)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200686/) | 15 | 2007-01-01 |
| [Western Illinois University Law (110 ILCS 690)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200690/) | 60 | 2026-08-07 |
| [Western Illinois University Revenue Bond Law (110 ILCS 691)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200691/) | 15 | 2007-01-01 |
| [Dental Student Grant Act (110 ILCS 925)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200925/) | 16 | 2022-05-27 |
| [Military School Scholarship Act (110 ILCS 955)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200955/) | 3 | 2026-08-21 |
| [Nurse Educator Assistance Act (110 ILCS 967)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200967/) | 20 | 2022-06-10 |
| [Private Medical Scholarship Agreement Act (110 ILCS 980)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200980/) | 4 | 2022-05-17 |
| [Savings and Loan Share and Account Act (205 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200205/Act%200115/) | 4 | 2026-10-30 |
| [Corporate Fiduciary Act (205 ILCS 620)](https://ftp.ilga.gov/ILCS/Ch%200205/Act%200620/) | 99 | 2025-08-18 |
| [Residential Mortgage License Act of 1987 (205 ILCS 635)](https://ftp.ilga.gov/ILCS/Ch%200205/Act%200635/) | 83 | 2025-01-01 |
| [Foreign Banking Office Act (205 ILCS 645)](https://ftp.ilga.gov/ILCS/Ch%200205/Act%200645/) | 30 | 2010-07-28 |
| [Adverse Claims to Deposit Accounts Act (205 ILCS 700)](https://ftp.ilga.gov/ILCS/Ch%200205/Act%200700/) | 9 | 2018-01-01 |
| [Illinois Clinical Laboratory and Blood Bank Act (210 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200025/) | 47 | 2025-11-21 |
| [Accountable Care Organization Clinical Laboratory Testing Advisory Board Act (210 ILCS 26)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200026/) | 8 | 2015-01-01 |
| [Illinois Certified Community Behavioral Health Clinics Act (210 ILCS 34)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200034/) | 6 | 2021-07-06 |
| [Supportive Residences Licensing Act (210 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200065/) | 15 | 2015-07-27 |
| [Emergency Medical Treatment Act (210 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200070/) | 3 | 2015-01-01 |
| [Hospital Infant Feeding Act (210 ILCS 81)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200081/) | 6 | 2013-01-01 |
| [Language Assistance Services Act (210 ILCS 87)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200087/) | 8 | 2021-04-27 |
| [X-Ray Retention Act (210 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200090/) | 2 | 2026-10-30 |
| [Swimming Pool Safety Act (210 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200130/) | 4 | 2026-10-30 |
| [Safe Pharmaceutical Disposal Act (210 ILCS 150)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200150/) | 8 | 2021-08-20 |
| [Birth Center Licensing Act (210 ILCS 170)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200170/) | 16 | 2024-07-01 |
| [Small Employer Health Insurance Rating Act (215 ILCS 93)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200093/) | 10 | 2023-08-04 |
| [Dental Service Plan Act (215 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200110/) | 54 | 2026-01-01 |
| [Illinois Health Benefits Exchange Law (215 ILCS 122)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200122/) | 15 | 2026-06-16 |
| [Illinois Long-Term Care Partnership Program Act (215 ILCS 132)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200132/) | 7 | 2007-08-16 |
| [Religious and Charitable Risk Pooling Trust Act (215 ILCS 150)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200150/) | 30 | 2001-07-20 |
| [Prior Authorization Reform Act (215 ILCS 200)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200200/) | 23 | 2026-01-01 |
| [Health Insurance Coverage Premium Misalignment Study Act (215 ILCS 210)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200210/) | 4 | 2023-01-01 |
| [Funeral Directors and Embalmers Licensing Code (225 ILCS 41)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200041/) | 67 | 2025-01-01 |
| [Kidney Disease Treatment Delegation Act (225 ILCS 66)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200066/) | 7 | 2026-07-31 |
| [Uniform Emergency Volunteer Health Practitioners Act (225 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200140/) | 12 | 2026-01-01 |
| [Illinois Explosives Act (225 ILCS 210)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200210/) | 39 | 2026-01-01 |
| [Fire Equipment Distributor and Employee Regulation Act of 2011 (225 ILCS 217)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200217/) | 31 | 2022-04-29 |
| [Auction License Act (225 ILCS 407)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200407/) | 68 | 2026-08-21 |
| [Slaughter Livestock Buyers Act (225 ILCS 655)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200655/) | 27 | 2018-01-01 |
| [Coal Mining Act (225 ILCS 705)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200705/) | 474 | 2025-01-01 |
| [Fluorspar Mines Act (225 ILCS 710)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200710/) | 122 | 2021-08-20 |
| [Surface Coal Mining Land Conservation and Reclamation Act (225 ILCS 720)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200720/) | 93 | 2019-07-12 |
| [Timber Buyers Licensing Act (225 ILCS 735)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200735/) | 15 | 2024-07-01 |
| [Sports Wagering Act (230 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200230/Act%200045/) | 74 | 2026-08-21 |
| [State Fair Gaming Act (230 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200230/Act%200050/) | 44 | 2020-06-30 |
| [Grain Code (240 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200240/Act%200040/) | 51 | 2022-06-10 |
| [Water and Sewer Financial Assistance Act (305 ILCS 21)](https://ftp.ilga.gov/ILCS/Ch%200305/Act%200021/) | 10 | 2021-08-06 |
| [Pediatric Palliative Care Act (305 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200305/Act%200060/) | 15 | 2022-01-01 |
| [Rebuild Illinois Mental Health Workforce Act (305 ILCS 66)](https://ftp.ilga.gov/ILCS/Ch%200305/Act%200066/) | 8 | 2026-07-01 |
| [Medicaid Technical Assistance Act (305 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200305/Act%200075/) | 9 | 2026-07-01 |
| [House Relocation Act (310 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200310/Act%200035/) | 6 | 2007-01-01 |
| [Displaced Person Relocation Act (310 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200310/Act%200040/) | 8 | 2026-10-30 |
| [Illinois Mortgage Insurance Fund Act (310 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200310/Act%200045/) | 12 | 2026-10-30 |
| [Community Land Trust Home Ownership Act (310 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200310/Act%200130/) | 13 | 2025-08-15 |
| [Blighted Vacant Areas Development Act of 1949 (315 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200315/Act%200010/) | 8 | 2018-07-20 |
| [Neighborhood Redevelopment Corporation Law (315 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200315/Act%200020/) | 57 | 2021-08-20 |
| [Urban Community Conservation Act (315 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200315/Act%200025/) | 14 | 2025-08-15 |
| [Urban Renewal Consolidation Act of 1961 (315 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200315/Act%200030/) | 39 | 2021-08-20 |
| [Senior Citizens Real Estate Tax Deferral Act (320 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200320/Act%200030/) | 8 | 2026-08-21 |
| [Illinois Caregiver Assistance and Resource Portal Act (320 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200320/Act%200070/) | 19 | 2026-08-21 |
| [Bias-Free Child Removal Pilot Program Act (325 ILCS 7)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200007/) | 8 | 2026-06-26 |
| [Children's Privacy Protection and Parental Empowerment Act (325 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200017/) | 6 | 2015-01-01 |
| [Language Equality Acquisition for Deaf, Hard of Hearing, or DeafBlind Children Act (325 ILCS 43)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200043/) | 11 | 2026-07-30 |
| [Minor Identification and Protection Act (325 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200045/) | 3 | 2026-10-30 |
| [Missing Children Records Act (325 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200050/) | 6 | 2026-07-01 |
| [Missing Children Registration Law (325 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200055/) | 8 | 2021-08-20 |
| [Equitable Early Childhood Education and Care Act (325 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200075/) | 3 | 2021-03-08 |
| [Early Childhood Workforce Act (325 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200080/) | 3 | 2021-03-08 |
| [Smart Start Illinois Act (325 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200085/) | 57 | 2026-07-01 |
| [Veterans' Employment Act (330 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200025/) | 7 | 2006-01-01 |
| [Prisoner of War Bonus Act (330 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200035/) | 7 | 2025-08-15 |
| [Veteran Service Organizations State Charter Act (330 ILCS 46)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200046/) | 11 | 2024-01-01 |
| [Veterans' Employment Representative Act (330 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200050/) | 3 | 2013-07-23 |
| [Veterans Preference Act (330 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200055/) | 5 | 2025-01-01 |
| [Veterans Preference in Private Employment Act (330 ILCS 56)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200056/) | 6 | 2016-01-01 |
| [Service Member's Tenure Act (330 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200060/) | 11 | 2019-01-01 |
| [Service Member Employment and Reemployment Rights Act (330 ILCS 61)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200061/) | 32 | 2025-08-15 |
| [Service Member Residential Property Act (330 ILCS 62)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200062/) | 8 | 2018-07-20 |
| [Illinois Service Member Civil Relief Act (330 ILCS 63)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200063/) | 34 | 2019-01-01 |
| [Records for Veterans Administration Act (330 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200070/) | 3 | 2025-08-15 |
| [Military Compensation Records Act (330 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200075/) | 2 | 2026-10-30 |
| [Service Compensation Records Transfer Act (330 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200080/) | 2 | 2026-10-30 |
| [Service Recognition Board Termination Act (330 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200085/) | 3 | 2026-10-30 |
| [Military Service Button Act (330 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200090/) | 2 | 2026-10-30 |
| [Under Age Veterans Benefits Act (330 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200095/) | 2 | 2026-10-30 |
| [Deceased, Disabled, and MIA/POW Veterans' Dependents Educational Opportunity Grant Act (330 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200105/) | 3 | 2026-08-21 |
| [Veterans Burial Places Act (330 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200110/) | 6 | 2026-08-21 |
| [Disposition of Veterans' Cremated Remains Act (330 ILCS 112)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200112/) | 5 | 2011-08-12 |
| [National Guard Veterans Exposure to Hazardous Materials Act (330 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200130/) | 6 | 2025-08-15 |
| [Military and Veterans Courts Act (330 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200135/) | 5 | 2009-07-27 |
| [Veterans' and Military Discount Program Act (330 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200140/) | 6 | 2025-08-15 |
| [Uniform Act for the Extradition of Persons of Unsound Mind (405 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200010/) | 6 | 1999-07-29 |
| [Mental Treatment for Incarcerated Persons Act (405 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200015/) | 3 | 1997-07-01 |
| [Specialized Living Centers Act (405 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200025/) | 28 | 2023-01-01 |
| [Community Support Systems Act (405 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200035/) | 6 | 2009-08-25 |
| [Protection and Advocacy for Persons with Developmental Disabilities Act (405 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200040/) | 2 | 2019-01-01 |
| [Protection and Advocacy for Mentally Ill Persons Act (405 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200045/) | 5 | 2015-07-29 |
| [Infant/Early Childhood Mental Health Consultations Act (405 ILCS 47)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200047/) | 3 | 2026-07-01 |
| [Mental Health Patient Travel Act (405 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200055/) | 2 | 1997-07-01 |
| [Mental Health Hispanic Interpreter Act (405 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200075/) | 2 | 2000-01-01 |
| [Developmental Disability and Mental Health Safety Act (405 ILCS 82)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200082/) | 14 | 2015-07-27 |
| [Home Environment Living Program Act (405 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200085/) | 9 | 2015-07-27 |
| [Psychiatry Practice Incentive Act (405 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200100/) | 9 | 2018-12-10 |
| [Illinois Mental Health First Aid Training Act (405 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200105/) | 9 | 2019-01-01 |
| [Out-of-State Person Subject to Involuntary Admission on an Inpatient Basis Mental Health Treatment Act (405 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200110/) | 11 | 2025-08-01 |
| [Maternal Mental Health Conditions Education, Early Diagnosis, and Treatment Act (405 ILCS 120)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200120/) | 6 | 2025-01-01 |
| [Interstate Contracts for Mental Health Disorder Treatment Act (405 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200130/) | 12 | 2022-01-01 |
| [First Responder Mental Health Grant Program Act (405 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200135/) | 5 | 2025-08-15 |
| [Psychiatric Residential Treatment Facilities (PRTF (405 ILCS 142)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200142/) | 12 | 2026-06-16 |
| [Outdoor Rx Program Act (405 ILCS 155)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200155/) | 10 | 2024-01-01 |
| [Interagency Children's Behavioral Health Services Act (405 ILCS 165)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200165/) | 11 | 2026-01-01 |
| [Community Health Worker Certification and Reimbursement Act (410 ILCS 67)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200067/) | 9 | 2021-11-30 |
| [Obesity Prevention Initiative Act (410 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200115/) | 4 | 2009-08-07 |
| [Feminine Hygiene Products for the Homeless Act (410 ILCS 175)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200175/) | 2 | 2022-01-01 |
| [Latex Glove Ban Act (410 ILCS 180)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200180/) | 4 | 2023-01-01 |
| [Sickle Cell Prevention, Care, and Treatment Program Act (410 ILCS 460)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200460/) | 9 | 2021-04-27 |
| [Tracking Infectious Cases Knowledgeably Act (410 ILCS 465)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200465/) | 5 | 2025-08-01 |
| [Illinois Health Statistics Act (410 ILCS 520)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200520/) | 11 | 2025-08-15 |
| [Right to Try Act (410 ILCS 649)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200649/) | 8 | 2016-01-01 |
| [Patient Access to Pharmacy Protection Act (410 ILCS 660)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200660/) | 12 | 2026-08-07 |
| [340B Transparency, Reporting, and Accountability Act (410 ILCS 665)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200665/) | 9 | 2026-08-07 |
| [Illinois Hemp Act (410 ILCS 707)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200707/) | 37 | 2026-11-12 |
| [Drug Take-Back Act (410 ILCS 720)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200720/) | 20 | 2023-06-30 |
| [Local Solid Waste Disposal Act (415 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200010/) | 8 | 1999-07-29 |
| [Solid Waste Hauling and Recycling Program Act (415 ILCS 12)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200012/) | 9 | 2014-08-26 |
| [Water Pollutant Discharge Act (415 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200025/) | 7 | 2026-10-30 |
| [Public Water Supply Regulation Act (415 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200040/) | 6 | 2016-07-08 |
| [Public Water Supply Operations Act (415 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200045/) | 33 | 2026-01-01 |
| [Safe Public Drinking Water Act (415 ILCS 47)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200047/) | 5 | 2026-01-01 |
| [PFAS Wastewater Citizen Protection Act (415 ILCS 52)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200052/) | 9 | 2026-08-21 |
| [Pesticide Application on Rights-of-Way Notification Act (415 ILCS 61)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200061/) | 5 | 2025-08-15 |
| [Environmental Toxicology Act (415 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200075/) | 8 | 2019-07-12 |
| [Degradable Plastic Act (415 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200080/) | 5 | 2018-07-20 |
| [Toxic Pollution Prevention Act (415 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200085/) | 7 | 2022-06-10 |
| [Regulation of Phosphorus in Detergents Act (415 ILCS 92)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200092/) | 3 | 2007-08-13 |
| [Junkyard Act (415 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200095/) | 11 | 2007-01-01 |
| [Litter Control Act (415 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200105/) | 13 | 2016-07-28 |
| [MTBE Elimination Act (415 ILCS 122)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200122/) | 6 | 2002-06-24 |
| [Environmental Impact Fee Law (415 ILCS 125)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200125/) | 23 | 2024-06-07 |
| [Environmental Justice Act (415 ILCS 155)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200155/) | 5 | 2026-08-07 |
| [Justice40 Oversight Committee Act (415 ILCS 157)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200157/) | 6 | 2023-07-28 |
| [Illinois Underground Natural Gas Storage Safety Act (415 ILCS 160)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200160/) | 18 | 2024-01-01 |
| [Safety and Aid for the Environment in Carbon Capture and Sequestration Act (415 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200185/) | 14 | 2026-01-01 |
| [Large Event Facilities Act (415 ILCS 190)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200190/) | 4 | 2025-01-01 |
| [Small Single-Use Plastic Act (415 ILCS 195)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200195/) | 4 | 2025-01-01 |
| [Fire Escape Act (425 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200425/Act%200015/) | 8 | 2026-10-30 |
| [Fire Extinguisher Service Act (425 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200425/Act%200017/) | 2 | 2026-10-30 |
| [Fire Investigation Act (425 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200425/Act%200025/) | 18 | 2026-06-26 |
| [Furniture Fire Safety Act (425 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200425/Act%200045/) | 9 | 2023-06-30 |
| [Hotel Floor Plan Posting Act (425 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200425/Act%200050/) | 7 | 1999-07-29 |
| [Firearm Dealer License Certification Act (430 ILCS 68)](https://ftp.ilga.gov/ILCS/Ch%200430/Act%200068/) | 27 | 2026-07-01 |
| [Road Worker Safety Act (430 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200430/Act%200105/) | 9 | 2026-10-30 |
| [Illinois Conservation Enhancement Act (505 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200505/Act%200035/) | 13 | 2016-07-28 |
| [Industrial Hemp Act (505 ILCS 89)](https://ftp.ilga.gov/ILCS/Ch%200505/Act%200089/) | 13 | 2026-06-12 |
| [Herptiles-Herps Act (510 ILCS 68)](https://ftp.ilga.gov/ILCS/Ch%200510/Act%200068/) | 87 | 2026-08-21 |
| [Illinois Natural Areas Stewardship Act (525 ILCS 31)](https://ftp.ilga.gov/ILCS/Ch%200525/Act%200031/) | 9 | 2017-08-25 |
| [Dirksen Memorial Highway Act (605 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200015/) | 2 | 2026-10-30 |
| [Jolliet - Marquette Trail Act (605 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200025/) | 3 | 1996-01-01 |
| [Milwaukee Avenue Polish Heritage Corridor Act (605 ILCS 27)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200027/) | 2 | 2023-01-01 |
| [Bridge Construction Act (605 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200105/) | 2 | 2026-10-30 |
| [Bridge Pier Protection Act (605 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200110/) | 2 | 2026-10-30 |
| [Toll Bridge Act (605 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200115/) | 16 | 2020-06-26 |
| [Illinois Adopt-A-Highway Act (605 ILCS 120)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200120/) | 12 | 2007-01-01 |
| [Roadside Memorial Act (605 ILCS 125)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200125/) | 9 | 2026-06-16 |
| [Heroes Way Designation Program Act (605 ILCS 127)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200127/) | 4 | 2017-01-01 |
| [Illinois Dig Once Act (605 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200145/) | 6 | 2026-08-21 |
| [Railroad Lessees Act (610 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200045/) | 3 | 2026-10-30 |
| [Railroad Depot Act (610 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200055/) | 4 | 2026-10-30 |
| [Railroad Director Residence Act (610 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200075/) | 3 | 2026-10-30 |
| [Railroad Police Act (610 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200080/) | 5 | 2026-08-21 |
| [Railroad Mooring Act (610 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200100/) | 4 | 2026-10-30 |
| [Railroad Employees Medical Treatment Act (610 ILCS 107)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200107/) | 3 | 2006-01-01 |
| [Elevated Railroad Approval Act (610 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200610/Act%200130/) | 3 | 2026-10-30 |
| [Illinois Waterway Act (615 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200010/) | 24 | 2007-01-01 |
| [Flood Control Act of 1945 (615 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200015/) | 11 | 2021-01-01 |
| [Navigable Waters Obstruction Act (615 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200020/) | 6 | 1999-07-29 |
| [Illinois and Michigan Canal Management Act (615 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200030/) | 21 | 2007-01-01 |
| [Illinois and Michigan Canal Protection Act (615 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200035/) | 7 | 1996-02-07 |
| [Illinois and Michigan Canal Land Use Act (615 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200040/) | 3 | 1996-02-07 |
| [Illinois and Michigan Canal Development Act (615 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200045/) | 15 | 2023-01-01 |
| [Lake Michigan Shore Line Act (615 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200055/) | 7 | 1996-02-07 |
| [Lake Calumet Harbor Act (615 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200065/) | 6 | 1996-02-07 |
| [Kaskaskia River Watershed and Basin Act (615 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200075/) | 2 | 2001-08-02 |
| [Big Kinkaid Creek Reservoir Act (615 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200080/) | 2 | 1996-02-07 |
| [Blue Waters Ditch Flood Control Act (615 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200085/) | 5 | 1996-02-07 |
| [Fox Waterway Agency Act (615 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200090/) | 26 | 2025-01-01 |
| [Vermilion River Middle Fork Act (615 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200095/) | 6 | 1996-02-07 |
| [McHenry County Dam Act (615 ILCS 100)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200100/) | 5 | 1996-02-07 |
| [Hennepin Canal Parkway State Park Act (615 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200105/) | 6 | 1997-07-01 |
| [Kankakee River Dam Transfer Act (615 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200615/Act%200110/) | 4 | 2013-08-09 |
| [Military Emergency Aircraft Restriction Act (620 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200010/) | 9 | 2021-08-20 |
| [Aircraft Landing and Taking Off Restriction Act (620 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200015/) | 9 | 1999-07-29 |
| [Joint Airports Act (620 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200020/) | 8 | 2026-10-30 |
| [Airport Zoning Act (620 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200025/) | 37 | 2007-01-01 |
| [Zoning to Eliminate Airport Hazards Act (620 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200030/) | 13 | 2026-10-30 |
| [General County Airport and Landing Field Act (620 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200040/) | 18 | 2007-01-01 |
| [County Airport Law of 1943 (620 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200045/) | 23 | 2014-07-16 |
| [County Airports Act (620 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200050/) | 76 | 2025-08-15 |
| [County Air Corridor Protection Act (620 ILCS 52)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200052/) | 6 | 2007-01-01 |
| [East St. Louis Airport Act (620 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200055/) | 3 | 2007-01-01 |
| [O'Hare Modernization Act (620 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200065/) | 20 | 2012-07-13 |
| [Aircraft Crash Parts Act (620 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200070/) | 2 | 2026-10-30 |
| [Public-Private Agreements for the South Suburban Airport Act (620 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200620/Act%200075/) | 36 | 2024-08-09 |
| [Chauffeur Protection Act (625 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200625/Act%200020/) | 3 | 2026-10-30 |
| [Snowmobile Registration and Safety Act (625 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200625/Act%200040/) | 63 | 2026-01-01 |
| [Taxi Safety Act of 2007 (625 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200625/Act%200055/) | 4 | 2013-01-01 |
| [O'Hare Driver Safety Act (625 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200625/Act%200080/) | 8 | 2026-01-01 |
| [Innovations for Transportation Infrastructure Act (630 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200630/Act%200010/) | 31 | 2025-08-15 |
| [Supreme Court Act (705 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200005/) | 13 | 2021-07-09 |
| [Supreme Court Terms Act (705 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200010/) | 2 | 2026-10-30 |
| [Supreme Court Building Act (705 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200015/) | 3 | 2001-08-15 |
| [Supreme Court Historic Preservation Act (705 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200017/) | 9 | 2007-12-31 |
| [Judicial Districts Act of 2021 (705 ILCS 23)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200023/) | 12 | 2021-12-17 |
| [Judicial Circuits Districting Act of 2022 (705 ILCS 24)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200024/) | 17 | 2023-02-10 |
| [Circuit Courts Act (705 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200035/) | 49 | 2026-08-07 |
| [Judicial Vacancies Act (705 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200040/) | 5 | 2023-02-10 |
| [Qualifications of Judges Act (705 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200060/) | 2 | 2026-10-30 |
| [Foreign Language Court Interpreter Act (705 ILCS 78)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200078/) | 4 | 2001-06-28 |
| [Judicial Privacy Act (705 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200090/) | 15 | 2026-01-01 |
| [Access to Justice Act (705 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200095/) | 13 | 2025-08-15 |
| [Building and Loan Receivership Fee Act (705 ILCS 230)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200230/) | 2 | 2026-10-30 |
| [Jury Secrecy Act (705 ILCS 315)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200315/) | 3 | 2000-01-01 |
| [Juror Protection Act (705 ILCS 320)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200320/) | 5 | 2013-01-25 |
| [Dependency Determinations for Unaccompanied Children Act (705 ILCS 420)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200420/) | 10 | 2026-06-01 |
| [Medical Fees of State Inmate Escapees Act (705 ILCS 510)](https://ftp.ilga.gov/ILCS/Ch%200705/Act%200510/) | 2 | 1997-07-01 |
| [International Commercial Arbitration Act (710 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200710/Act%200030/) | 36 | 1998-07-24 |
| [Methamphetamine Precursor Control Act (720 ILCS 648)](https://ftp.ilga.gov/ILCS/Ch%200720/Act%200648/) | 25 | 2025-08-15 |
| [Methamphetamine Precursor Tracking Act (720 ILCS 649)](https://ftp.ilga.gov/ILCS/Ch%200720/Act%200649/) | 12 | 2025-08-15 |
| [Sale of Immoral Publications to Children Act (720 ILCS 670)](https://ftp.ilga.gov/ILCS/Ch%200720/Act%200670/) | 4 | 2026-10-30 |
| [State Appellate Defender Act (725 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200105/) | 14 | 2024-01-01 |
| [Arrest and Conviction of Out of State Murderers Act (725 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200110/) | 2 | 2026-10-30 |
| [Citizen Privacy Protection Act (725 ILCS 137)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200137/) | 5 | 2017-01-01 |
| [Criminal Proceeding Interpreter Act (725 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200140/) | 5 | 2009-01-01 |
| [Criminal Victims' Asset Discovery Act (725 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200145/) | 5 | 2026-10-30 |
| [Firearm Seizure Act (725 ILCS 165)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200165/) | 6 | 2009-08-11 |
| [Violent Crime Witness Protection Act (725 ILCS 173)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200173/) | 8 | 2024-06-05 |
| [Pretrial Success Act (725 ILCS 187)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200187/) | 22 | 2025-08-15 |
| [Privacy of Adult Victims of Criminal Sexual Offenses Act (725 ILCS 191)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200191/) | 4 | 2022-05-13 |
| [Quasi-criminal and Misdemeanor Pretrial Release Act (725 ILCS 195)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200195/) | 6 | 2023-01-01 |
| [Uniform Act to Secure the Attendance of Witnesses from Within or Without a State in Criminal Proceedings (725 ILCS 220)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200220/) | 6 | 2023-01-13 |
| [Uniform Criminal Extradition Act (725 ILCS 225)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200225/) | 32 | 2023-01-13 |
| [Uniform Rendition of Accused Persons Act (725 ILCS 230)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200230/) | 6 | 2026-10-30 |
| [Witness Protection Act (725 ILCS 245)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200245/) | 4 | 2016-07-28 |
| [Secure Residential Youth Care Facility Licensing Act (730 ILCS 175)](https://ftp.ilga.gov/ILCS/Ch%200730/Act%200175/) | 34 | 2015-07-29 |
| [Equitable Access to Education, Employment, and Training for Incarcerated Individuals with Disabilities Act (730 ILCS 230)](https://ftp.ilga.gov/ILCS/Ch%200730/Act%200230/) | 9 | 2026-08-07 |
| [Choice of Law and Forum Act (735 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200735/Act%200105/) | 6 | 1998-01-01 |
| [Alienation of Affections Abolition Act (740 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200740/Act%200005/) | 9 | 2016-01-01 |
| [Assistance Animal Damages Act (740 ILCS 13)](https://ftp.ilga.gov/ILCS/Ch%200740/Act%200013/) | 3 | 2000-01-01 |
| [Illinois Civil Rights Act of 2006 (740 ILCS 24)](https://ftp.ilga.gov/ILCS/Ch%200740/Act%200024/) | 4 | 2008-01-01 |
| [Police Search Cost Recovery Act (740 ILCS 125)](https://ftp.ilga.gov/ILCS/Ch%200740/Act%200125/) | 2 | 2013-01-25 |
| [County Engineer and Highway Superintendent Liability Act (745 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200015/) | 8 | 2026-10-30 |
| [Alcoholism and Drug Addiction Intervenor and Reporter Immunity Law (745 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200035/) | 4 | 2019-01-01 |
| [Communicable Disease Report Act (745 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200045/) | 2 | 2024-01-01 |
| [Good Samaritan Medical Equipment Donor Act (745 ILCS 51)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200051/) | 2 | 2012-01-01 |
| [Long-term Care Peer Review and Quality Assessment and Assurance Protection Act (745 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200055/) | 4 | 2026-10-30 |
| [Menstrual Products Donor Immunity Act (745 ILCS 57)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200057/) | 4 | 2024-07-19 |
| [Real Estate Investment Trust Act (745 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200060/) | 3 | 2017-08-18 |
| [State of Illinois Recreational Use of Leased Land Act (745 ILCS 67)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200067/) | 6 | 2007-09-11 |
| [Sports Volunteer Immunity Act (745 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200080/) | 2 | 2015-07-27 |
| [Trustees' Emergency Act (760 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200010/) | 7 | 2026-10-30 |
| [Disclaimer Under Nontestamentary Instrument Act (760 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200025/) | 2 | 2026-10-30 |
| [Instruments Regarding Adopted Children Act (760 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200030/) | 2 | 1998-01-01 |
| [Uniform Prudent Management of Institutional Funds Act (760 ILCS 51)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200051/) | 13 | 2009-06-30 |
| [Charitable Trust Tax Law Conformance Act (760 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200060/) | 3 | 2026-10-30 |
| [Fiduciary Transfer of Securities Act (760 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200070/) | 10 | 2026-10-30 |
| [Securities in Fiduciary Accounts Act (760 ILCS 75)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200075/) | 5 | 2026-10-30 |
| [Trustee Surety Release Act (760 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200085/) | 2 | 2026-10-30 |
| [Cemetery Perpetual Trust Authorization Act (760 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200760/Act%200095/) | 2 | 2010-03-01 |
| [Seals and Real Estate Contracts Act (765 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200010/) | 9 | 2026-10-30 |
| [Land Patent Act (765 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200015/) | 2 | 2026-10-30 |
| [Residential Real Property Disclosure Act (765 ILCS 77)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200077/) | 22 | 2026-06-16 |
| [Conveyance and Encumbrance of Manufactured Homes as Real Property and Severance Act (765 ILCS 170)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200170/) | 36 | 2015-07-28 |
| [Land Trustee as Creditor Act (765 ILCS 415)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200415/) | 5 | 2026-10-30 |
| [Mining Act of 1874 (765 ILCS 505)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200505/) | 14 | 2007-01-01 |
| [Cemetery Company Land Not Used for Burial Act (765 ILCS 810)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%200810/) | 2 | 2026-10-30 |
| [Registered Container Trade Mark Act (765 ILCS 1050)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%201050/) | 10 | 1998-01-01 |
| [Illinois Trade Secrets Act (765 ILCS 1065)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%201065/) | 9 | 2021-08-20 |
| [Park District and Public Utility Liability Act (765 ILCS 1080)](https://ftp.ilga.gov/ILCS/Ch%200765/Act%201080/) | 4 | 2022-06-10 |
| [Attorneys Lien Act (770 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200005/) | 2 | 2003-07-01 |
| [Innkeepers Lien Act (770 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200040/) | 5 | 2012-01-01 |
| [Labor and Storage Lien Act (770 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200045/) | 10 | 2017-11-23 |
| [Labor and Storage Lien (Small Amount (770 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200050/) | 8 | 2017-11-23 |
| [Liens Against Railroads Act (770 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200055/) | 9 | 1999-07-29 |
| [Oil and Gas Lien Act of 1989 (770 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200070/) | 21 | 2000-01-01 |
| [Preference of Claims for Wages Act (770 ILCS 85)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200085/) | 4 | 2026-10-30 |
| [Sale of Unclaimed Property Act (770 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200090/) | 4 | 2018-01-01 |
| [Self-Service Storage Facility Act (770 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200095/) | 9 | 2026-01-01 |
| [Timeshare Lien and Security Interest Act (770 ILCS 103)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200103/) | 5 | 2019-01-01 |
| [Tool and Die Lien Act (770 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200770/Act%200105/) | 9 | 2006-01-01 |
| [Public Works Employment Discrimination Act (775 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200010/) | 9 | 2015-07-27 |
| [Illinois Blacklist Trade Law (775 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200015/) | 6 | 2026-10-30 |
| [Discriminatory Club Act (775 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200025/) | 5 | 2015-01-01 |
| [White Cane Law (775 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200030/) | 6 | 2015-07-27 |
| [Reproductive Health Act (775 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200055/) | 34 | 2023-01-13 |
| [Civil Rights Remedies Restoration Act (775 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200060/) | 7 | 2024-01-01 |
| [Franchise Tax and License Fee Amnesty Act of 2007 (805 ILCS 8)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200008/) | 6 | 2025-11-21 |
| [Dissolution of Corporations Act (805 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200020/) | 9 | 2026-10-30 |
| [Corporation Canal Construction Act (805 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200025/) | 5 | 2007-01-01 |
| [Gas Company Property Act (805 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200030/) | 14 | 2007-01-01 |
| [Benefit Corporation Act (805 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200040/) | 13 | 2022-01-01 |
| [Religious Corporation Act (805 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200110/) | 27 | 2020-01-01 |
| [Religious Corporation Validation Act (805 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200115/) | 2 | 2026-10-30 |
| [Merger of Not For Profit Corporations Act (805 ILCS 120)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200120/) | 14 | 2007-01-01 |
| [German School Educational Corporation Act (805 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200130/) | 2 | 2026-10-30 |
| [Fraternal Corporation Property and Borrowing Powers Act (805 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200145/) | 2 | 2026-10-30 |
| [Illinois Clean Energy Jobs and Justice Fund Act (805 ILCS 155)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200155/) | 34 | 2021-09-15 |
| [Uniform Partnership Act (1997 (805 ILCS 206)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200206/) | 81 | 2020-01-01 |
| [Uniform Limited Partnership Act (2001 (805 ILCS 215)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200215/) | 128 | 2026-08-21 |
| [Professional Association Act (805 ILCS 305)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200305/) | 12 | 2013-10-01 |
| [Agricultural Co-Operative Act (805 ILCS 315)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200315/) | 41 | 2003-07-14 |
| [Limited Worker Cooperative Association Act (805 ILCS 317)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200317/) | 29 | 2021-08-20 |
| [Entity Omnibus Act (805 ILCS 415)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200415/) | 42 | 2021-08-13 |
| [Buy-Now-Pay-Later Loan Consumer Protection Act (815 ILCS 124)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200124/) | 44 | 2026-06-25 |
| [Tax Refund Anticipation Loan Reform Act (815 ILCS 177)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200177/) | 9 | 2013-01-01 |
| [Illinois Business Brokers Act of 1995 (815 ILCS 307)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200307/) | 33 | 2017-08-18 |
| [Car-Sharing Program Act (815 ILCS 312)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200312/) | 14 | 2022-01-01 |
| [Modular Housing Buyer Protection Act (815 ILCS 362)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200362/) | 4 | 2010-01-01 |
| [Personal Information Protection Act (815 ILCS 530)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200530/) | 12 | 2020-01-01 |
| [Taxpreparer Disclosure of Information Act (815 ILCS 535)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200535/) | 4 | 2026-10-30 |
| [Illinois Fertility Fraud Act (815 ILCS 540)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200540/) | 11 | 2024-01-01 |
| [Motor Vehicle Dealer Protection Act (815 ILCS 545)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200545/) | 5 | 2025-01-01 |
| [Digital Voice and Likeness Protection Act (815 ILCS 550)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200550/) | 5 | 2026-01-01 |
| [Complex Rehabilitation Technology Act (815 ILCS 555)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200555/) | 18 | 2026-01-01 |
| [Automatic Contract Renewal Act (815 ILCS 601)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200601/) | 5 | 2025-01-01 |
| [Business Opportunity Sales Law of 1995 (815 ILCS 602)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200602/) | 40 | 2017-08-18 |
| [Contractor Prompt Payment Act (815 ILCS 603)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200603/) | 6 | 2019-08-20 |
| [Consumer Contract Reciprocal Attorney's Fees Act (815 ILCS 604)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200604/) | 5 | 2024-01-01 |
| [Credit Services Organizations Act (815 ILCS 605)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200605/) | 16 | 1999-07-29 |
| [Dance Studio Act (815 ILCS 610)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200610/) | 12 | 2026-08-21 |
| [Dating Referral Services Act (815 ILCS 615)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200615/) | 13 | 2022-01-01 |
| [Educational Planning Services Consumer Protection Act (815 ILCS 616)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200616/) | 12 | 2024-01-01 |
| [Euro Conversion Act (815 ILCS 617)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200617/) | 8 | 1997-07-30 |
| [Illinois Fair Invention Development Standards Act (815 ILCS 620)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200620/) | 28 | 2026-10-30 |
| [In-Office Membership Care Act (815 ILCS 628)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200628/) | 12 | 2019-08-02 |
| [Job Referral and Job Listing Services Consumer Protection Act (815 ILCS 630)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200630/) | 12 | 2026-08-21 |
| [Military Personnel Cellular Phone Contract Termination Act (815 ILCS 633)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200633/) | 14 | 2013-01-01 |
| [Illinois Membership Campground Act (815 ILCS 635)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200635/) | 5 | 2026-10-30 |
| [Motor Vehicle Leasing Act (815 ILCS 636)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200636/) | 46 | 2013-01-01 |
| [Music Licensing Fees Act (815 ILCS 637)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200637/) | 10 | 2013-01-25 |
| [Personal Injury Representation Agreement Act (815 ILCS 640)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200640/) | 2 | 2026-10-30 |
| [Physical Fitness Services Act (815 ILCS 645)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200645/) | 15 | 2026-08-21 |
| [Private Seal Abolishment Act (815 ILCS 650)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200650/) | 2 | 2026-10-30 |
| [Rental-Purchase Agreement Act (815 ILCS 655)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200655/) | 6 | 1994-09-09 |
| [Building and Construction Contract Act (815 ILCS 665)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200665/) | 6 | 2002-07-16 |
| [Illinois Residential Building Code Act (815 ILCS 670)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200670/) | 6 | 2024-01-01 |
| [Restaurant Reservation Anti-Piracy Act (815 ILCS 672)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200672/) | 4 | 2026-01-01 |
| [Snow Removal Service Liability Limitation Act (815 ILCS 675)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200675/) | 5 | 2016-08-25 |
| [Franchise Disclosure Act of 1987 (815 ILCS 705)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200705/) | 44 | 2009-10-01 |
| [Motor Vehicle Franchise Act (815 ILCS 710)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200710/) | 35 | 2024-08-09 |
| [Illinois Equipment Fair Dealership Law (815 ILCS 715)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200715/) | 14 | 2011-08-12 |
| [Beer Industry Fair Dealing Act (815 ILCS 720)](https://ftp.ilga.gov/ILCS/Ch%200815/Act%200720/) | 11 | 2019-07-12 |
| [Labor Dispute Act (820 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200005/) | 6 | 2026-08-07 |
| [Collective Bargaining Successor Employer Act (820 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200010/) | 3 | 2026-10-30 |
| [Collective Bargaining Freedom Act (820 ILCS 12)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200012/) | 9 | 2024-01-01 |
| [Transportation Network Driver Labor Relations Act (820 ILCS 14)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200014/) | 26 | 2026-08-07 |
| [Employment Contract Act (820 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200015/) | 2 | 2026-10-30 |
| [Broadcast Industry Free Market Act (820 ILCS 17)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200017/) | 4 | 2002-01-01 |
| [Artistic Contracts by Minors Act (820 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200020/) | 4 | 2026-10-30 |
| [Advertisement for Strike Workers Act (820 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200025/) | 3 | 2026-10-30 |
| [Employment of Strikebreakers Act (820 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200030/) | 5 | 2004-01-01 |
| [Employee Arbitration Act (820 ILCS 35)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200035/) | 11 | 2023-06-30 |
| [Personnel Record Review Act (820 ILCS 40)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200040/) | 15 | 2026-01-01 |
| [Artificial Intelligence Video Interview Act (820 ILCS 42)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200042/) | 5 | 2022-01-01 |
| [Health Insurance Claim Filing Act (820 ILCS 45)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200045/) | 3 | 2026-10-30 |
| [Consumer Coverage Disclosure Act (820 ILCS 46)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200046/) | 7 | 2021-08-27 |
| [Right to Privacy in the Workplace Act (820 ILCS 55)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200055/) | 13 | 2026-08-21 |
| [Worker Freedom of Speech Act (820 ILCS 57)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200057/) | 8 | 2025-08-15 |
| [Union Employee Health and Benefits Protection Act (820 ILCS 60)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200060/) | 11 | 2026-10-30 |
| [Sexual Harassment Victim Representation Act (820 ILCS 61)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200061/) | 6 | 2020-07-01 |
| [Transportation Benefits Program Act (820 ILCS 63)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200063/) | 6 | 2026-06-01 |
| [Illinois Worker Adjustment and Retraining Notification Act (820 ILCS 65)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200065/) | 16 | 2021-09-15 |
| [Employee Credit Privacy Act (820 ILCS 70)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200070/) | 7 | 2021-08-20 |
| [Illinois Secure Choice Savings Program Act (820 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200080/) | 23 | 2025-08-01 |
| [Illinois Freedom to Work Act (820 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200090/) | 10 | 2025-08-15 |
| [Employee Misclassification Referral System Act (820 ILCS 92)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200092/) | 5 | 2018-06-01 |
| [Human Trafficking Recognition Training Act (820 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200095/) | 11 | 2026-01-01 |
| [Workplace Transparency Act (820 ILCS 96)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200096/) | 13 | 2026-01-01 |
| [Customized Employment for Individuals with Disabilities Act (820 ILCS 97)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200097/) | 10 | 2025-01-01 |
| [Workers' Rights and Worker Safety Act (820 ILCS 98)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200098/) | 7 | 2025-08-14 |
| [Minimum Wage Law (820 ILCS 105)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200105/) | 17 | 2026-07-01 |
| [Equal Wage Act (820 ILCS 110)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200110/) | 3 | 2026-10-30 |
| [Equal Pay Act of 2003 (820 ILCS 112)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200112/) | 15 | 2025-06-30 |
| [Illinois Wage Payment and Collection Act (820 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200115/) | 21 | 2026-06-01 |
| [Sales Representative Act (820 ILCS 120)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200120/) | 4 | 2026-10-30 |
| [Prevailing Wage Act (820 ILCS 130)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200130/) | 19 | 2026-08-21 |
| [Burial Rights Act (820 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200135/) | 8 | 2010-03-01 |
| [One Day Rest In Seven Act (820 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200140/) | 13 | 2025-03-21 |
| [Eight Hour Work Day Act (820 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200145/) | 3 | 2026-10-30 |
| [School Visitation Rights Act (820 ILCS 147)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200147/) | 11 | 2020-08-01 |
| [Civil Air Patrol Leave Act (820 ILCS 148)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200148/) | 8 | 2019-07-12 |
| [Employee Blood and Organ Donation Leave Act (820 ILCS 149)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200149/) | 5 | 2026-01-01 |
| [Employee Medical Contribution Act (820 ILCS 150)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200150/) | 3 | 1998-07-30 |
| [Military Leave Act (820 ILCS 151)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200151/) | 9 | 2025-08-01 |
| [Family Bereavement Leave Act (820 ILCS 154)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200154/) | 10 | 2025-06-16 |
| [Employer as Lessee Bond Act (820 ILCS 155)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200155/) | 6 | 2026-10-30 |
| [Child Extended Bereavement Leave Act (820 ILCS 156)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200156/) | 10 | 2024-01-01 |
| [Family Neonatal Intensive Care Leave Act (820 ILCS 157)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200157/) | 7 | 2026-06-16 |
| [Employee Benefit Contribution Act (820 ILCS 160)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200160/) | 3 | 2002-01-01 |
| [Personal Service Wage Refund Act (820 ILCS 165)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200165/) | 5 | 1999-07-29 |
| [Earned Income Tax Credit Information Act (820 ILCS 170)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200170/) | 5 | 2017-08-18 |
| [Day and Temporary Labor Services Act (820 ILCS 175)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200175/) | 31 | 2025-11-21 |
| [Victims' Economic Security and Safety Act (820 ILCS 180)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200180/) | 13 | 2026-08-21 |
| [Domestic Workers' Bill of Rights Act (820 ILCS 182)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200182/) | 9 | 2026-07-01 |
| [Employee Classification Act (820 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200185/) | 30 | 2026-06-16 |
| [Illinois Fringe Benefit Portability and Continuity Act (820 ILCS 190)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200190/) | 8 | 2007-08-27 |
| [Employee Sick Leave Act (820 ILCS 191)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200191/) | 8 | 2023-01-01 |
| [Paid Leave for All Workers Act (820 ILCS 192)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200192/) | 11 | 2026-06-16 |
| [Freelance Worker Protection Act (820 ILCS 193)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200193/) | 13 | 2026-08-21 |
| [Child Labor Law of 2024 (820 ILCS 206)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200206/) | 32 | 2026-08-21 |
| [Disclosure of Offenses Against Children Act (820 ILCS 210)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200210/) | 2 | 2026-10-30 |
| [Occupational Safety and Health Act (820 ILCS 219)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200219/) | 36 | 2025-08-14 |
| [Illinois Safe and Healthy Workplace Act (820 ILCS 226)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200226/) | 8 | 2025-08-14 |
| [OSHA Program Reorganization Act (820 ILCS 227)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200227/) | 17 | 2012-07-13 |
| [Employee Washroom Act (820 ILCS 230)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200230/) | 7 | 2022-06-10 |
| [Medical Examination of Employees Act (820 ILCS 235)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200235/) | 5 | 2026-10-30 |
| [Work Under Compressed Air Act (820 ILCS 245)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200245/) | 9 | 2022-06-10 |
| [Underground Sewer Employee Safety Act (820 ILCS 250)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200250/) | 8 | 2025-08-15 |
| [Toxic Substances Disclosure to Employees Act (820 ILCS 255)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200255/) | 21 | 2022-06-10 |
| [Nursing Mothers in the Workplace Act (820 ILCS 260)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200260/) | 5 | 2026-01-01 |
| [Substance Abuse Prevention on Public Works Projects Act (820 ILCS 265)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200265/) | 7 | 2008-01-01 |
| [Aerial Exhibitors Safety Act (820 ILCS 270)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200270/) | 4 | 2026-10-30 |
| [Workplace Violence Prevention Act (820 ILCS 275)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200275/) | 28 | 2018-08-14 |
| [Workers' Compensation Act (820 ILCS 305)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200305/) | 63 | 2026-08-07 |
| [Workers' Occupational Diseases Act (820 ILCS 310)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200310/) | 33 | 2022-05-27 |
| [Line of Duty Compensation Act (820 ILCS 315)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200315/) | 6 | 2024-07-01 |
| [Public Safety Employee Benefits Act (820 ILCS 320)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200320/) | 9 | 2024-01-01 |
| [Hotel and Casino Employee Safety Act (820 ILCS 325)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200325/) | 7 | 2021-03-01 |
| [Public Accountability and Performance System Act (30 ILCS 25)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200025/) | 7 | 2009-07-15 |

## Current wording selected from labelled ILCS alternatives

18 additional indexed acts retain current wording from the Illinois General Assembly compilation of 30 October 2026. Where a section supplies a pair labelled before and after amendment by the same Public Act, the before text is retained only when the after text has one explicit effective date later than 13 November 2026 and the before text has an effective date on or before that day. Acts with unlabelled future wording or ambiguous alternatives remain excluded. No earlier wording is reconstructed. The compilation is not official or authoritative; the publisher identifies the printed Secretary of State copy as official. Source words, act titles, article headings and current sections are retained in source order. Dates use the latest explicit effective date of retained source text. Per-document source digests and selected/excluded publisher labels appear in `data/ilcs-current-selection-q1910.json`.

| Act | Sections | Source date |
| --- | ---: | --- |
| [State Employee Housing Act (5 ILCS 412)](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200412/) | 9 | 2025-11-21 |
| [Department of Natural Resources Act (20 ILCS 801)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200801/) | 33 | 2026-06-16 |
| [Adult Education Act (105 ILCS 405)](https://ftp.ilga.gov/ILCS/Ch%200105/Act%200405/) | 11 | 2019-08-09 |
| [Behavioral Health Workforce Education Center of Illinois Act (110 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200185/) | 7 | 2021-04-27 |
| [Authorized Electronic Monitoring in Long-Term Care Facilities Act (210 ILCS 32)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200032/) | 17 | 2019-07-26 |
| [MC/DD Act (210 ILCS 46)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200046/) | 282 | 2026-07-01 |
| [ID/DD Community Care Act (210 ILCS 47)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200047/) | 232 | 2026-08-21 |
| [Unclaimed Life Insurance Benefits Act (215 ILCS 185)](https://ftp.ilga.gov/ILCS/Ch%200215/Act%200185/) | 9 | 2018-08-14 |
| [Community Services Act (405 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200030/) | 16 | 2022-06-10 |
| [Developmental Disability and Mental Disability Services Act (405 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200080/) | 32 | 2026-01-01 |
| [Housing is Recovery Pilot Program Act (405 ILCS 125)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200125/) | 20 | 2025-01-01 |
| [Ensuring a More Qualified, Competent, and Diverse Community Behavioral Health Workforce Act (405 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200145/) | 10 | 2023-06-30 |
| [Alzheimer's Disease Assistance Act (410 ILCS 405)](https://ftp.ilga.gov/ILCS/Ch%200410/Act%200405/) | 8 | 2020-01-01 |
| [Toll Highway Act (605 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200605/Act%200010/) | 65 | 2026-08-21 |
| [Public and Appellate Defender Immunity Act (745 ILCS 19)](https://ftp.ilga.gov/ILCS/Ch%200745/Act%200019/) | 3 | 2000-06-30 |
| [Domestic Violence Fatality Review Act (750 ILCS 62)](https://ftp.ilga.gov/ILCS/Ch%200750/Act%200062/) | 24 | 2021-08-20 |
| [Human Trafficking Resource Center Notice Act (775 ILCS 50)](https://ftp.ilga.gov/ILCS/Ch%200775/Act%200050/) | 5 | 2022-05-13 |
| [Medical Corporation Act (805 ILCS 15)](https://ftp.ilga.gov/ILCS/Ch%200805/Act%200015/) | 22 | 2018-08-14 |

## Current wording selected from labelled ILCS alternatives, 13 November 2026

17 additional indexed acts retain current wording from the Illinois General Assembly compilation of 30 October 2026. Where a section supplies a pair labelled before and after amendment by the same Public Act, the before text is retained only when the named amending Public Act has one explicit effective date later than 13 November 2026 and the before text has no future effective date. Acts with unlabelled future wording or ambiguous alternatives remain excluded. No earlier wording is reconstructed. The compilation is not official or authoritative; the publisher identifies the printed Secretary of State copy as official. Source words, act titles, article headings and current sections are retained in source order. Dates use the latest explicit effective date of retained source text, or the publisher compilation update date, 30 October 2026, when the retained text gives no effective date. Per-document source digests and selected/excluded publisher labels appear in `data/ilcs-current-selection-q1928.json`.

| Act | Sections | Source date |
| --- | ---: | --- |
| [State Budget Law of the Civil Administrative Code of Illinois (15 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200020/) | 13 | 2025-11-21 |
| [Illinois Identification Card Act (15 ILCS 335)](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200335/) | 32 | 2026-08-21 |
| [Energy Conservation and Coal Development Act (20 ILCS 1105)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201105/) | 17 | 2025-11-21 |
| [Department of Innovation and Technology Act (20 ILCS 1370)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201370/) | 37 | 2026-01-01 |
| [Balanced Budget Note Act (25 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200080/) | 6 | 2026-08-21 |
| [State Prompt Payment Act (30 ILCS 540)](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200540/) | 23 | 2024-06-05 |
| [Home Equity Assurance Act (65 ILCS 95)](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200095/) | 24 | 2025-01-01 |
| [Specialized Mental Health Rehabilitation Act of 2013 (210 ILCS 49)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200049/) | 110 | 2026-08-21 |
| [Community-Integrated Living Arrangements Licensure and Certification Act (210 ILCS 135)](https://ftp.ilga.gov/ILCS/Ch%200210/Act%200135/) | 21 | 2026-08-21 |
| [Birth Control Services to Minors Act (325 ILCS 10)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200010/) | 2 | 2026-10-30 |
| [Viet Nam Veterans Compensation Act (330 ILCS 30)](https://ftp.ilga.gov/ILCS/Ch%200330/Act%200030/) | 6 | 2025-08-15 |
| [Children's Mental Health Act (405 ILCS 49)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200049/) | 6 | 2025-08-15 |
| [Workforce Direct Care Expansion Act (405 ILCS 162)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200162/) | 7 | 2025-03-21 |
| [Illinois Solid Waste Management Act (415 ILCS 20)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200020/) | 19 | 2024-01-01 |
| [Responsible Outdoor Lighting Control Act (415 ILCS 200)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200200/) | 7 | 2025-01-01 |
| [Privacy of Child Victims of Criminal Sexual Offenses Act (725 ILCS 190)](https://ftp.ilga.gov/ILCS/Ch%200725/Act%200190/) | 3 | 2024-01-01 |
| [Unemployment Insurance Act (820 ILCS 405)](https://ftp.ilga.gov/ILCS/Ch%200820/Act%200405/) | 223 | 2026-01-01 |

## Later current wording from the static ILCS compilation, 13 November 2026

100 previously represented acts now have a later current-text version from the [Illinois General Assembly static compilation](https://ftp.ilga.gov/ILCS/), updated 30 October 2026 through Public Act 104-854. The publisher says this web copy is not official or authoritative; the printed copy maintained by the Secretary of State is official. Each version uses the latest explicit effective date in its source notes when one is present; otherwise it uses the publisher’s compilation update date. The earlier published versions remain in the history. The later versions are labelled correction overlays whose ranges begin on their source dates; no earlier wording was reconstructed. The table below and `data/versions.json` give the new dates; older act-folder README version counts have not yet been regenerated. The document inventory and official source byte digests are in `data/ilcs-current-refresh-q1951.json`.

| Act | Previous date | Source date | Source documents |
| --- | --- | --- | ---: |
| [5 ILCS 5](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200005/) | 2026-02-07 | 2026-10-30 | 3 |
| [5 ILCS 25](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200025/) | 2026-07-10 | 2026-10-30 | 3 |
| [5 ILCS 50](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200050/) | 2026-06-16 | 2026-10-30 | 3 |
| [5 ILCS 80](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200080/) | 2026-06-16 | 2026-08-21 | 63 |
| [5 ILCS 85](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200085/) | 2026-06-16 | 2026-10-30 | 3 |
| [5 ILCS 170](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200170/) | 2026-03-18 | 2026-10-30 | 6 |
| [5 ILCS 180](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200180/) | 2026-03-24 | 2026-08-21 | 12 |
| [5 ILCS 190](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200190/) | 2026-02-18 | 2026-10-30 | 4 |
| [5 ILCS 195](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200195/) | 2026-05-05 | 2026-10-30 | 5 |
| [5 ILCS 225](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200225/) | 2026-02-07 | 2026-06-01 | 11 |
| [5 ILCS 250](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200250/) | 2026-04-14 | 2026-10-30 | 3 |
| [5 ILCS 265](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200265/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 275](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200275/) | 2026-02-16 | 2026-10-30 | 12 |
| [5 ILCS 280](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200280/) | 2026-08-03 | 2026-10-30 | 3 |
| [5 ILCS 295](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200295/) | 2026-08-03 | 2026-10-30 | 4 |
| [5 ILCS 300](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200300/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 305](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200305/) | 2026-04-12 | 2026-10-30 | 3 |
| [5 ILCS 315](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200315/) | 2026-02-18 | 2026-07-01 | 35 |
| [5 ILCS 340](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200340/) | 2026-02-07 | 2026-07-01 | 10 |
| [5 ILCS 380](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200380/) | 2026-07-08 | 2026-10-30 | 3 |
| [5 ILCS 515](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200515/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 520](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200520/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 525](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200525/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 530](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200530/) | 2026-06-01 | 2026-10-30 | 5 |
| [5 ILCS 535](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200535/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 540](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200540/) | 2026-02-16 | 2026-10-30 | 3 |
| [5 ILCS 545](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200545/) | 2026-04-20 | 2026-10-30 | 3 |
| [5 ILCS 547](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200547/) | 2026-02-18 | 2026-10-30 | 6 |
| [5 ILCS 550](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200550/) | 2026-05-26 | 2026-10-30 | 3 |
| [5 ILCS 555](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200555/) | 2026-02-07 | 2026-10-30 | 3 |
| [5 ILCS 560](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200560/) | 2026-02-07 | 2026-10-30 | 4 |
| [5 ILCS 565](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200565/) | 2026-02-07 | 2026-10-30 | 3 |
| [5 ILCS 570](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200570/) | 2026-04-22 | 2026-10-30 | 3 |
| [5 ILCS 575](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200575/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 580](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200580/) | 2026-02-18 | 2026-10-30 | 3 |
| [5 ILCS 590](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200590/) | 2026-07-19 | 2026-10-30 | 7 |
| [5 ILCS 595](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200595/) | 2026-02-18 | 2026-10-30 | 4 |
| [5 ILCS 600](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200600/) | 2026-02-07 | 2026-10-30 | 6 |
| [5 ILCS 605](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200605/) | 2026-05-18 | 2026-10-30 | 4 |
| [5 ILCS 610](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200610/) | 2026-02-16 | 2026-10-30 | 3 |
| [5 ILCS 865](https://ftp.ilga.gov/ILCS/Ch%200005/Act%200865/) | 2026-02-18 | 2026-08-21 | 6 |
| [15 ILCS 5](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200005/) | 2026-06-06 | 2026-10-30 | 3 |
| [15 ILCS 323](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200323/) | 2026-05-02 | 2026-06-16 | 9 |
| [15 ILCS 420](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200420/) | 2026-03-08 | 2026-10-30 | 3 |
| [15 ILCS 520](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200520/) | 2026-05-19 | 2026-08-25 | 35 |
| [15 ILCS 530](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200530/) | 2026-05-05 | 2026-10-30 | 3 |
| [15 ILCS 535](https://ftp.ilga.gov/ILCS/Ch%200015/Act%200535/) | 2026-04-25 | 2026-10-30 | 3 |
| [20 ILCS 15](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200015/) | 2026-04-21 | 2026-08-21 | 5 |
| [20 ILCS 35](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200035/) | 2026-04-21 | 2026-08-21 | 12 |
| [20 ILCS 105](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200105/) | 2026-05-15 | 2026-07-01 | 83 |
| [20 ILCS 420](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200420/) | 2026-02-11 | 2026-10-30 | 3 |
| [20 ILCS 655](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200655/) | 2026-05-11 | 2026-08-21 | 37 |
| [20 ILCS 665](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200665/) | 2026-04-16 | 2026-08-07 | 19 |
| [20 ILCS 686](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200686/) | 2026-06-07 | 2026-08-21 | 34 |
| [20 ILCS 805](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200805/) | 2026-07-05 | 2026-08-21 | 74 |
| [20 ILCS 845](https://ftp.ilga.gov/ILCS/Ch%200020/Act%200845/) | 2026-08-27 | 2026-10-30 | 3 |
| [20 ILCS 1010](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201010/) | 2026-04-11 | 2026-10-30 | 4 |
| [20 ILCS 1345](https://ftp.ilga.gov/ILCS/Ch%200020/Act%201345/) | 2026-03-10 | 2026-08-21 | 16 |
| [20 ILCS 2505](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202505/) | 2026-05-13 | 2026-06-16 | 76 |
| [20 ILCS 3115](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203115/) | 2026-04-04 | 2026-10-30 | 4 |
| [20 ILCS 3310](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203310/) | 2026-03-08 | 2026-06-26 | 27 |
| [20 ILCS 3900](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203900/) | 2026-02-16 | 2026-07-01 | 111 |
| [20 ILCS 3915](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203915/) | 2026-05-20 | 2026-06-16 | 9 |
| [20 ILCS 3935](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203935/) | 2026-04-26 | 2026-10-30 | 6 |
| [20 ILCS 3953](https://ftp.ilga.gov/ILCS/Ch%200020/Act%203953/) | 2026-04-10 | 2026-08-21 | 8 |
| [20 ILCS 4139](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204139/) | 2026-02-16 | 2026-06-01 | 5 |
| [20 ILCS 4140](https://ftp.ilga.gov/ILCS/Ch%200020/Act%204140/) | 2026-02-16 | 2026-06-01 | 16 |
| [25 ILCS 85](https://ftp.ilga.gov/ILCS/Ch%200025/Act%200085/) | 2026-02-03 | 2026-10-30 | 8 |
| [30 ILCS 10](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200010/) | 2026-06-10 | 2026-08-21 | 16 |
| [30 ILCS 122](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200122/) | 2026-03-31 | 2026-07-01 | 9 |
| [30 ILCS 238](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200238/) | 2026-05-14 | 2026-08-21 | 9 |
| [30 ILCS 245](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200245/) | 2026-04-15 | 2026-10-30 | 4 |
| [30 ILCS 310](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200310/) | 2026-05-14 | 2026-10-30 | 8 |
| [30 ILCS 320](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200320/) | 2026-07-26 | 2026-10-30 | 9 |
| [30 ILCS 385](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200385/) | 2026-04-09 | 2026-10-30 | 6 |
| [30 ILCS 520](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200520/) | 2026-05-09 | 2026-10-30 | 5 |
| [30 ILCS 538](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200538/) | 2026-05-21 | 2026-06-26 | 40 |
| [30 ILCS 570](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200570/) | 2026-06-01 | 2026-06-16 | 17 |
| [30 ILCS 575](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200575/) | 2026-04-12 | 2026-08-21 | 30 |
| [30 ILCS 725](https://ftp.ilga.gov/ILCS/Ch%200030/Act%200725/) | 2026-07-12 | 2026-08-21 | 18 |
| [35 ILCS 55](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200055/) | 2026-05-14 | 2026-08-21 | 15 |
| [35 ILCS 105](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200105/) | 2026-05-12 | 2026-07-10 | 67 |
| [35 ILCS 130](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200130/) | 2026-05-28 | 2026-06-16 | 61 |
| [35 ILCS 145](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200145/) | 2026-05-19 | 2026-06-16 | 14 |
| [35 ILCS 165](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200165/) | 2026-02-16 | 2026-06-01 | 19 |
| [35 ILCS 405](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200405/) | 2026-03-20 | 2026-08-21 | 19 |
| [35 ILCS 815](https://ftp.ilga.gov/ILCS/Ch%200035/Act%200815/) | 2026-04-21 | 2026-06-01 | 5 |
| [40 ILCS 10](https://ftp.ilga.gov/ILCS/Ch%200040/Act%200010/) | 2026-06-02 | 2026-10-30 | 3 |
| [40 ILCS 15](https://ftp.ilga.gov/ILCS/Ch%200040/Act%200015/) | 2026-05-16 | 2026-07-01 | 13 |
| [45 ILCS 5](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200005/) | 2026-05-11 | 2026-10-30 | 8 |
| [45 ILCS 10](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200010/) | 2026-05-11 | 2026-10-30 | 9 |
| [45 ILCS 15](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200015/) | 2026-05-11 | 2026-10-30 | 11 |
| [45 ILCS 25](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200025/) | 2026-05-16 | 2026-10-30 | 6 |
| [45 ILCS 55](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200055/) | 2026-05-11 | 2026-10-30 | 8 |
| [45 ILCS 60](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200060/) | 2026-05-11 | 2026-10-30 | 7 |
| [45 ILCS 70](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200070/) | 2026-05-16 | 2026-10-30 | 3 |
| [45 ILCS 90](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200090/) | 2026-05-18 | 2026-10-30 | 6 |
| [45 ILCS 95](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200095/) | 2026-05-11 | 2026-10-30 | 5 |
| [45 ILCS 100](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200100/) | 2026-05-16 | 2026-10-30 | 6 |
| [45 ILCS 141](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200141/) | 2026-05-11 | 2026-06-01 | 10 |

## Later current wording from the static ILCS compilation, 13 November 2026 (second batch)

20 previously represented acts have a later current-text version from the [Illinois General Assembly static ILCS compilation](https://ftp.ilga.gov/ILCS/), updated 30 October 2026 through Public Act 104-854. The publisher says this web copy is not official or authoritative. Each date is the latest explicit effective date in the source notes, or the publisher compilation update date where no effective date is given. The new versions are labelled correction overlays; earlier published commits remain. The per-document source inventory is in `data/ilcs-current-refresh-q1973.json`.

| Act | Previous date | Source date | Documents |
| --- | --- | --- | ---: |
| [45 ILCS 145](https://ftp.ilga.gov/ILCS/Ch%200045/Act%200145/) | 2026-05-11 | 2026-10-30 | 6 |
| [50 ILCS 5](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200005/) | 2026-02-16 | 2026-10-30 | 5 |
| [50 ILCS 10](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200010/) | 2026-04-03 | 2026-10-30 | 9 |
| [50 ILCS 25](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200025/) | 2026-02-16 | 2026-10-30 | 5 |
| [50 ILCS 40](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200040/) | 2026-02-16 | 2026-08-21 | 4 |
| [50 ILCS 115](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200115/) | 2026-02-16 | 2026-10-30 | 3 |
| [50 ILCS 220](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200220/) | 2026-02-16 | 2026-10-30 | 9 |
| [50 ILCS 305](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200305/) | 2026-06-30 | 2026-10-30 | 3 |
| [50 ILCS 315](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200315/) | 2026-02-16 | 2026-10-30 | 4 |
| [50 ILCS 325](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200325/) | 2026-02-16 | 2026-10-30 | 3 |
| [50 ILCS 330](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200330/) | 2026-02-17 | 2026-06-01 | 6 |
| [50 ILCS 335](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200335/) | 2026-06-10 | 2026-10-30 | 7 |
| [50 ILCS 360](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200360/) | 2026-02-17 | 2026-08-21 | 10 |
| [50 ILCS 415](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200415/) | 2026-04-02 | 2026-10-30 | 5 |
| [50 ILCS 440](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200440/) | 2026-02-16 | 2026-10-30 | 3 |
| [50 ILCS 720](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200720/) | 2026-04-20 | 2026-08-21 | 7 |
| [50 ILCS 730](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200730/) | 2026-07-13 | 2026-10-30 | 3 |
| [50 ILCS 810](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200810/) | 2026-02-16 | 2026-10-30 | 4 |
| [50 ILCS 815](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200815/) | 2026-02-16 | 2026-10-30 | 7 |
| [50 ILCS 820](https://ftp.ilga.gov/ILCS/Ch%200050/Act%200820/) | 2026-04-15 | 2026-10-30 | 9 |

## Later current wording from the static ILCS compilation, 13 November 2026 (third batch)

20 previously represented acts have a later current-text version from the [Illinois General Assembly static ILCS compilation](https://ftp.ilga.gov/ILCS/), updated 30 October 2026 through Public Act 104-854. The publisher says this web copy is not official or authoritative. Each date is the latest explicit effective date in the source notes, or the publisher compilation update date where no effective date is given. The new versions are labelled correction overlays; earlier published commits remain. The per-document source inventory is in `data/ilcs-current-refresh-q1989.json`.

| Act | Previous date | Source date | Documents |
| --- | --- | --- | ---: |
| [55 ILCS 40](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200040/) | 2026-04-17 | 2026-10-30 | 6 |
| [55 ILCS 50](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200050/) | 2026-04-13 | 2026-10-30 | 5 |
| [55 ILCS 55](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200055/) | 2026-05-13 | 2026-10-30 | 4 |
| [55 ILCS 60](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200060/) | 2026-04-15 | 2026-10-30 | 3 |
| [55 ILCS 65](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200065/) | 2026-05-12 | 2026-10-30 | 10 |
| [55 ILCS 95](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200095/) | 2026-05-16 | 2026-10-30 | 4 |
| [55 ILCS 100](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200100/) | 2026-04-11 | 2026-10-30 | 8 |
| [55 ILCS 110](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200110/) | 2026-05-13 | 2026-10-30 | 9 |
| [55 ILCS 115](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200115/) | 2026-06-08 | 2026-10-30 | 7 |
| [55 ILCS 125](https://ftp.ilga.gov/ILCS/Ch%200055/Act%200125/) | 2026-05-11 | 2026-10-30 | 5 |
| [65 ILCS 30](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200030/) | 2026-07-11 | 2026-10-30 | 3 |
| [65 ILCS 70](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200070/) | 2026-04-21 | 2026-10-30 | 3 |
| [65 ILCS 75](https://ftp.ilga.gov/ILCS/Ch%200065/Act%200075/) | 2026-08-06 | 2026-10-30 | 3 |
| [70 ILCS 210](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200210/) | 2026-04-16 | 2026-08-21 | 50 |
| [70 ILCS 415](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200415/) | 2026-04-12 | 2026-10-30 | 3 |
| [70 ILCS 518](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200518/) | 2026-06-05 | 2026-08-07 | 19 |
| [70 ILCS 610](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200610/) | 2026-03-16 | 2026-10-30 | 3 |
| [70 ILCS 705](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200705/) | 2026-07-23 | 2026-07-24 | 125 |
| [70 ILCS 710](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200710/) | 2026-04-21 | 2026-10-30 | 3 |
| [70 ILCS 815](https://ftp.ilga.gov/ILCS/Ch%200070/Act%200815/) | 2026-04-21 | 2026-10-30 | 3 |

## Later ILCS wording recorded but not yet included, 13 November 2026

The Illinois General Assembly static ILCS compilation identifies later wording for 20 acts that is not yet included in this repository's law history. The cited Public Acts and their explicit effective dates are recorded in `data/ilcs-later-wording-held-q2000.json`. The compilation is not official or authoritative; the publisher identifies the printed copy maintained by the Secretary of State as official. The existing law files retain their previously published wording and dates.

## Static ILCS compilation additions, 30 October 2026

4 additional complete indexed acts from the [Illinois General Assembly compilation](https://ftp.ilga.gov/ILCS/) are included. The compilation incorporates Public Acts through 104-854. The publisher states that these provisions have NOT been edited for publication and are NOT the official text; this copy should not be cited as official or authoritative. The only official copy is the printed copy maintained by the Secretary of State’s office.

Each addition retains all sections, act-title documents and article headings in the publisher’s Section Sequence. Dates use the latest explicit amendment effective date in the source, otherwise the compilation’s own update date, 2026-10-30. This date fallback does not claim a commencement date the source does not identify. Future-effective text and normative images are held. Existing records retain their historical dates and text; their inclusion above does not establish equality with this static compilation. Public Acts, administrative rules and earlier wording are not added.

| Act | Sections | Source date |
| --- | ---: | --- |
| [Illinois State University Law (110 ILCS 675)](https://ftp.ilga.gov/ILCS/Ch%200110/Act%200675/) | 60 | 2026-08-07 |
| [Health Care Workplace Violence Prevention Act (405 ILCS 90)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200090/) | 14 | 2025-11-21 |
| [Mental Health Inpatient Facility Access Act (405 ILCS 140)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200140/) | 6 | 2023-06-30 |
| [Illinois Cool Cities Act (415 ILCS 145)](https://ftp.ilga.gov/ILCS/Ch%200415/Act%200145/) | 5 | 2007-08-27 |

These four current-text acts include source notices of repeal effective 1 January 2027. Their existing text remains in force on 13 November 2026; the future repeal is not applied. The date of each version is the explicit effective date of its latest currently cited Public Act. The per-document source and date evidence is in `data/ilcs-future-repeal-q2023.json`.

## Further current ILCS texts, 13 November 2026

7 additional indexed acts from the [Illinois General Assembly static ILCS compilation](https://ftp.ilga.gov/ILCS/) retain current text selected only by explicit publisher version labels and source effective dates. Future repeal notices remain; future amendment alternatives are excluded. The compilation is updated 30 October 2026 through Public Act 104-854 and is publisher-labelled non-authoritative. Each date is the explicit effective date of the latest currently cited Public Act. The source document and date inventory is in `data/ilcs-depth-q2034.json`.

| Act | Source date | Documents |
| --- | --- | ---: |
| [Advisory Council on Early Identification and Treatment of Mental Health Conditions Act (405 ILCS 115)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200115/) | 2018-08-14 | 4 |
| [Afterschool Youth Development Project Act (325 ILCS 27)](https://ftp.ilga.gov/ILCS/Ch%200325/Act%200027/) | 2017-09-08 | 9 |
| [Strengthening and Transforming Behavioral Health Crisis Care in Illinois Act (405 ILCS 160)](https://ftp.ilga.gov/ILCS/Ch%200405/Act%200160/) | 2023-07-28 | 9 |
| [Department of Healthcare and Family Services Law of the Civil Administrative Code of Illinois (20 ILCS 2205)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202205/) | 2023-08-04 | 16 |
| [Rehabilitation of Persons with Disabilities Act (20 ILCS 2405)](https://ftp.ilga.gov/ILCS/Ch%200020/Act%202405/) | 2025-08-15 | 27 |
| [Public-Private Partnerships for Transportation Act (630 ILCS 5)](https://ftp.ilga.gov/ILCS/Ch%200630/Act%200005/) | 2025-08-15 | 32 |
| [Illinois Optometric Practice Act of 1987 (225 ILCS 80)](https://ftp.ilga.gov/ILCS/Ch%200225/Act%200080/) | 2026-08-07 | 57 |
