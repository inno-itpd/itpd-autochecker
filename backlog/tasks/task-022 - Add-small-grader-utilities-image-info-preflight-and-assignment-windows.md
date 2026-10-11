---
id: TASK-022
title: 'Add small grader utilities: image info, preflight, and assignment windows'
status: Done
assignee: []
created_date: '2026-10-11 14:24'
updated_date: '2026-10-11 16:44'
labels: []
dependencies: []
ordinal: 22000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sessions probed for the markdownlint binary and parsed PNG headers in Python because identify was unavailable.
Add scripts/image_info.py <files...> reporting pixel dimensions, byte size, and transparency for PNG and JPEG without ImageMagick.
Add scripts/preflight.py checking gh auth status, pdftotext, and markdownlint-cli2 before a grader batch.
Extend tools/grader_tools/assignment_config.py with issue_cutoff and week_window_start per assignment so the A2 hard-deadline facts live in one place.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 image_info.py reports dimensions and size for PNG and JPEG files and flags transparent PNGs
- [x] #2 preflight.py reports each required tool and exits non-zero when gh is not authenticated or a tool is missing
- [x] #3 assignment_config.py carries issue_cutoff and week_window_start for A1 and A2
- [x] #4 Tests cover image header parsing and preflight result shaping and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added tools/grader_tools/image_info.py, scripts/image_info.py, tools/grader_tools/preflight.py, and scripts/preflight.py.

Mechanics: image_info reads PNG chunk headers and JPEG marker segments directly (no ImageMagick), detects the format from content, and reports `PNG|JPEG WxH, N bytes`, appending a `transparent` flag for PNGs with an alpha color type (4/6) or a tRNS chunk; the exit code is 0 when every file was read, 1 when one or more failed. preflight checks gh auth status (via `gh auth status`, 15s timeout, injectable which/runner), pdftotext, and markdownlint-cli2, prints one ok/FAIL line per check, and exits 1 when gh is unauthenticated or a tool is missing. assignment_config now carries `week_window_start` (00:00 on the first day of the assignment week) and `issue_cutoff` (hard deadline) as ISO 8601 Innopolis (UTC+3) strings: A1 2026-09-25/2026-10-02, A2 2026-10-02/2026-10-10, matching the A2 prompt's ISSUE_CUTOFF literal and the published schedules.

Decisions: header parsing lives in tools/grader_tools with thin scripts wrappers, matching the privacy/link tool pattern, so tests exercise parsing without a CLI. image_info reports exact bytes rather than KiB. The transparent flag is printed only when true. preflight folds a missing gh into the gh auth check and never echoes gh output, so no token can reach stdout. Window facts stay as strings for direct comparison against gh timestamps; a test asserts the A2 literal still appears in the A2 prompt.

Validation: uv run pytest -> 180 passed (new tests/test_image_info.py, tests/test_preflight.py, and window tests in tests/test_assignment_prompts.py). Manual runs: image_info on generated fixtures and on real A2 work-dir PNG/JPEG files matched `file` output exactly (including a progressive JPEG and an RGBA PNG); preflight against the live dev shell reported all three checks ok and exit 0. markdownlint-cli2 "**/*.md" reports only the pre-existing .claude/.opencode MD041 findings and untracked TODO.md findings; no Markdown changed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
