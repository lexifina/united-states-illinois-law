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
| `ilcs-20-1105` | Energy Conservation and Coal Development Act | 1 | 2025-11-21 to 2025-11-21 |
| `ilcs-25-80` | Balanced Budget Note Act | 1 | 2026-08-21 to 2026-08-21 |
| `ilcs-325-10` | Birth Control Services to Minors Act | 1 | 2026-10-30 to 2026-10-30 |
| `ilcs-15-20` | State Budget Law of the Civil Administrative Code of Illinois | 1 | 2025-11-21 to 2025-11-21 |
| `ilcs-15-335` | Illinois Identification Card Act | 1 | 2026-08-21 to 2026-08-21 |
| `ilcs-20-1370` | Department of Innovation and Technology Act | 1 | 2026-01-01 to 2026-01-01 |
| `ilcs-30-540` | State Prompt Payment Act | 1 | 2024-06-05 to 2024-06-05 |
| `ilcs-65-95` | Home Equity Assurance Act | 1 | 2025-01-01 to 2025-01-01 |
| `ilcs-210-49` | Specialized Mental Health Rehabilitation Act of 2013 | 1 | 2026-08-21 to 2026-08-21 |
| `ilcs-210-135` | Community-Integrated Living Arrangements Licensure and Certification Act | 1 | 2026-08-21 to 2026-08-21 |
| `ilcs-330-30` | Viet Nam Veterans Compensation Act | 1 | 2025-08-15 to 2025-08-15 |
| `ilcs-405-49` | Children's Mental Health Act | 1 | 2025-08-15 to 2025-08-15 |
| `ilcs-405-162` | Workforce Direct Care Expansion Act | 1 | 2025-03-21 to 2025-03-21 |
| `ilcs-415-20` | Illinois Solid Waste Management Act | 1 | 2024-01-01 to 2024-01-01 |
| `ilcs-415-200` | Responsible Outdoor Lighting Control Act | 1 | 2025-01-01 to 2025-01-01 |
| `ilcs-725-190` | Privacy of Child Victims of Criminal Sexual Offenses Act | 1 | 2024-01-01 to 2024-01-01 |
| `ilcs-820-405` | Unemployment Insurance Act | 1 | 2026-01-01 to 2026-01-01 |

The build made 17 commits:

| Commits | Kind |
| ---: | --- |
| 17 | baseline texts where the record starts |
| 0 | named laws, court decisions and treaties |
| 0 | changes no amendment note explains, credited to the publisher |
| 0 | corrections to the existing record |
| 0 | printing or layout changes |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-13.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 17 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Latest explicit source effective date; otherwise publisher compilation update 2026-10-30. https://ftp.ilga.gov/ILCS/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `3dc022775d376808c6bafd197f26857fc72a874c861ef2c4d24dbdd6f06b94d9` (1133050 bytes).
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
