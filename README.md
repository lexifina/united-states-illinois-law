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

527 additional complete indexed acts from the [Illinois General Assembly compilation](https://ftp.ilga.gov/ILCS/) are included. The compilation incorporates Public Acts through 104-854. The publisher states that these provisions have NOT been edited for publication and are NOT the official text; this copy should not be cited as official or authoritative. The only official copy is the printed copy maintained by the Secretary of State’s office.

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
