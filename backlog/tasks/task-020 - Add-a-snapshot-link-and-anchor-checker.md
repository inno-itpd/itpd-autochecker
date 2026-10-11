---
id: TASK-020
title: Add a snapshot link and anchor checker
status: Done
assignee: []
created_date: '2026-10-11 14:23'
updated_date: '2026-10-11 15:56'
labels: []
dependencies: []
modified_files:
  - tools/grader_tools/snapshot_links.py
  - scripts/check_snapshot_links.py
  - tests/test_snapshot_links.py
ordinal: 20000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sessions grepped for pre-cut anchors and one grader hand-wrote a relative-link checker for the snapshot.
Add scripts/check_snapshot_links.py with signature check_snapshot_links.py <work_dir> that walks Markdown in the snapshot and verifies relative links and heading anchors using GitHub slug rules.
Support --issue-bodies <issues.json> to check anchors referenced from dumped issue bodies and report pre-cut anchors such as #gap-01-<title> separately.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Broken relative links and missing anchors are reported with the file, the line, and the target
- [x] #2 Pre-cut anchor occurrences matching #(alt|gap|vp)-NN- are listed separately
- [x] #3 --issue-bodies checks anchors from dumped issue bodies against snapshot headings
- [x] #4 Unit tests cover slug rules, relative paths, and the old-anchor pattern and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added tools/grader_tools/snapshot_links.py and scripts/check_snapshot_links.py.

Mechanics: check_snapshot_links.py <work_dir> walks the snapshots .md files (sorted, .git skipped) and resolves every relative link from the file that contains it; root-absolute paths and issue-body paths resolve from the snapshot root; percent-encoded paths and fragments are decoded; #Lnn fragments and directory targets are not anchor errors; links inside fenced and inline code are ignored; findings print as file:line: target (detail), grouped into broken relative links, missing anchors, and pre-cut anchors. Anchors implement GitHubs rules: lowercase, punctuation dropped except hyphens and connector punctuation such as _, spaces hyphenated, duplicate slugs suffixed -1, -2, ..., raw HTML headings with an id use it verbatim, and heading formatting (code, links, emphasis, entities) is stripped first; setext headings are supported. The pre-cut pattern is #(alt|gap|vp)-[0-9]{2}- and is grep-like (it also reports text and code occurrences), matching the A2 prompts grep; it is reported separately from broken/missing findings. --issue-bodies issues.json reads the live-evidence dump and checks anchors from full GitHub blob URLs (longest suffix that exists in the snapshot), relative paths, and bare URLs against the snapshot headings; links to other repositories or missing files are skipped. Exit codes: 0 clean, 1 findings, 2 cannot run (missing snapshot or unparsable issue dump); one-line errors.

Decisions: self-contained, no lychee dependency, because lychee is network-bound and does not report pre-cut anchors or issue bodies; pre-cut occurrences are exit-1 findings because A2 S3 makes any remaining one a shortfall; absolute external links are lychees job, so the snapshot pass checks only relative targets while issue bodies accept the full GitHub URLs the requirements require there.

Validation: uv run pytest -> 121 passed, with 25 new tests in tests/test_snapshot_links.py covering slug rules (punctuation, inline code, emphasis, entities, Unicode, emoji, duplicates), relative paths (nested, parent, root-absolute, escaping, percent-encoded), code masking, setext and raw HTML headings, the pre-cut pattern with its two-digit guard, issue bodies (blob URLs, relative links, bare URLs, external repos, missing files), and run exit codes 0/1/2. Real runs: A2 work dirs Team 1/2/4/5/6/7/9 match the saved reviews (Team 1s DEC-nnn placeholder anchor missing; Team 6s six missing + six pre-cut snapshot anchors and 14 pre-cut occurrences across issues #27-#34; Team 7s 40 pre-cut occurrences and none missing because its headings were never cut; the rest clean); --issue-bodies over tmp/A2 issues.json matches the saved feedback counts; A1/itpd (pinned course materials, checks clean with lychee) reports no broken links or missing anchors, only the one intentional pre-cut example in guides/comparison-and-synthesis.md. markdownlint-cli2 over the repo reports only the pre-existing untracked TODO.md findings; no Markdown changed (backlog/** is ignored).
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
