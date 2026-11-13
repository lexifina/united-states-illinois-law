# How this repository was made (United States (Illinois))

This file is written by the build on 2026-11-13, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Illinois General Assembly static ILCS compilation (non-authoritative) | <https://ftp.ilga.gov/ILCS/> | 2026-11-13 | Government statute text; not official or authoritative. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `ilcs-730-225` | Higher Education in Prison Act | 2 | 2026-05-12 to 2026-07-31 |
| `ilcs-410-34` | Equitable Health Outcomes Act | 2 | 2026-05-18 to 2026-08-21 |
| `ilcs-410-320` | Prenatal Syphilis Act | 2 | 2026-05-20 to 2026-08-21 |
| `ilcs-625-10` | Motor Vehicle Theft Reporting Act | 2 | 2026-03-06 to 2026-08-21 |
| `ilcs-730-130` | County Jail Good Behavior Allowance Act | 2 | 2026-04-19 to 2026-08-21 |
| `ilcs-110-986` | Retention of Illinois Students and Equity Act | 2 | 2026-05-15 to 2026-06-26 |
| `ilcs-410-265` | Genetic and Metabolic Diseases Advisory Committee Act | 2 | 2026-04-10 to 2026-08-21 |
| `ilcs-430-170` | First Informer Broadcasters Act | 2 | 2026-05-04 to 2026-08-21 |
| `ilcs-765-226` | Illinois Coordinate System Act of 2024 | 2 | 2026-05-12 to 2026-08-21 |
| `ilcs-815-412` | Strengthening Community Media Act | 2 | 2026-04-03 to 2026-08-21 |
| `ilcs-110-49` | Higher Education Veterans Service Act | 2 | 2026-04-15 to 2026-08-21 |
| `ilcs-210-175` | Essential Support Person Act | 2 | 2026-05-09 to 2026-08-21 |
| `ilcs-410-170` | Coal Tar Sealant Disclosure Act | 2 | 2026-05-11 to 2026-07-01 |
| `ilcs-220-80` | Broadband Advisory Council Act | 2 | 2026-04-19 to 2026-08-07 |
| `ilcs-410-210` | Consent by Minors to Health Care Services Act | 2 | 2026-05-10 to 2026-08-21 |
| `ilcs-720-602` | Ephedra Prohibition Act | 2 | 2026-03-28 to 2026-08-21 |
| `ilcs-815-420` | Travel Promotion Consumer Protection Act | 2 | 2026-04-14 to 2026-08-21 |
| `ilcs-410-145` | Youth Sports Concussion Safety Act | 2 | 2026-03-08 to 2026-08-21 |
| `ilcs-815-414` | Ticket Sale and Resale Act | 2 | 2026-02-14 to 2026-06-25 |
| `ilcs-430-15` | Gasoline Storage Act | 2 | 2026-08-08 to 2026-08-21 |

The build made 3613 commits:

| Commits | Kind |
| ---: | --- |
| 3447 | baseline texts where the record starts |
| 0 | named laws, court decisions and treaties |
| 26 | changes no amendment note explains, credited to the publisher |
| 140 | corrections to the existing record |
| 0 | printing or layout changes |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-13.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 3473 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Use the explicit effective date of the latest Public Act cited by the act; hold undated acts. https://ftp.ilga.gov/ILCS/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `b63db8e4ec9613a5da1be1a6c231573e9772522189ae75cc3f4b55d13cb1c3e9` (312856 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `63170edd89e92292ac248dae17d79e486e4e9f19`, `check.py` `e340718c28cd5b0edbe37bdeab1aac31427ada66`, `on.py` `4a8aa1c9a5e6bd8cc831b90a6e68c5a6f448a13c`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- All source document words and publisher document order retained.
- Source effective dates take precedence over compilation date. Future-effective acts and images held.

## What AI did and did not do

The source readers and builders were developed under Lexifina's direction with coding assistants, including Claude Code and Codex.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Model-authored code; no model-authored law text or OCR.
