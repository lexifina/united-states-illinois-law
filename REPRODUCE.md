# How this repository was made (United States (Illinois))

This file is written by the build on 2026-11-13, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Illinois General Assembly static ILCS compilation (non-authoritative) | <https://ftp.ilga.gov/ILCS/> | 2027-12-31 | Government statute text; not official or authoritative. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `ilcs-110-675` | Illinois State University Law | 1 | 2026-08-07 to 2026-08-07 |
| `ilcs-405-90` | Health Care Workplace Violence Prevention Act | 1 | 2025-11-21 to 2025-11-21 |
| `ilcs-405-140` | Mental Health Inpatient Facility Access Act | 1 | 2023-06-30 to 2023-06-30 |
| `ilcs-415-145` | Illinois Cool Cities Act | 1 | 2007-08-27 to 2007-08-27 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | baseline texts where the record starts |
| 0 | named laws, court decisions and treaties |
| 0 | changes no amendment note explains, credited to the publisher |
| 0 | corrections to the existing record |
| 0 | printing or layout changes |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-13.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Explicit effective date of latest currently cited Public Act; future repeal excluded. https://ftp.ilga.gov/ILCS/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `2c376304b67c9b021005175b35ab2e74077558c7b03f45947552d6af30d6301d` (142418 bytes).
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
