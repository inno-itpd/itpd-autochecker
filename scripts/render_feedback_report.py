#!/usr/bin/env python3
"""Render a complete feedback report from one structured JSON payload.

Usage:

```console
uv run python scripts/render_feedback_report.py <assignment> <payload.json>
```

This is the full-review counterpart of the structured `segment_updates`
payloads that `scripts/patch_feedback_report.py` and
`scripts/regrade_feedback_segments.py` apply to an existing report: it builds
the whole `agent-feedback.md` (metadata preamble, overall assessment, segments table,
unresolved gaps, summary, strengths, main issues, and segment details) in one
pass.

The payload may be incomplete, so the report can reach disk as soon as part of
the review is decided: every segment that `segment_updates` does not cover is
written as an explicit `unverified` placeholder with `Evidence gaps: yes`, and
the report still validates.  A later render that supplies the segment replaces
the placeholder.

Payload shape (all keys are required unless marked optional):

```json
{
  "output_path": "itpd-assignments-feedback/A1/feedback/<team_dir>/agent-feedback.md",
  "team": 3,
  "repository": "https://github.com/<org>/<repo>",
  "snapshot": "<full 40-character lowercase commit SHA>",
  "summary": ["3 to 5 one-line bullets"],
  "strengths": ["at least one one-line bullet"],
  "main_issues_to_fix": ["at least one one-line bullet"],
  "segment_updates": {
    "S1": {
      "status": "met",
      "evidence_gaps": false,
      "evidence": ["at least one one-line bullet"],
      "verified_shortfalls": [],
      "unverified_checks": []
    }
  },
  "unresolved_evidence_gaps": {"S2": ["one bullet per unresolved check"]}
}
```

Rules:

- `output_path` is required; relative paths resolve from the current working
  directory.  The parent directory is created when it does not exist.
- `repository` and `snapshot` may be `null` (or omitted) when the submission
  has no resolvable snapshot; then `snapshot_notes` is required instead and
  `Primary index reviewed` renders as `none`.
- `snapshot_notes` must be absent when both `repository` and `snapshot` are
  present.
- `segment_updates` uses the same per-segment shape as
  `scripts/regrade_feedback_segments.py`, with an optional `name` that must
  match the assignment.  It may cover any subset of the assignment's segments;
  it must not contain a key that is not a segment of the assignment.
  - Every omitted segment renders as a placeholder with `Status: unverified`
    and `Evidence gaps: yes`, so an early or resumed render still validates.
  - The placeholder `**Evidence:**` bullet reads `Not reviewed: the run stopped
    before this segment was reviewed, so no evidence was checked.`
  - The placeholder `**Why not met (unverified):**` bullet, reused as the
    `## Unresolved evidence gaps` bullet for the segment, reads `The run
    stopped before reviewing this segment; it stays unverified pending a later
    review.`
  - A placeholder is never `met` and is not a verified shortfall; supplying the
    segment in a later payload replaces it.
- `status` is one of `met`, `partial`, `missing`, `unverified`.  `partial` and
  `missing` need `verified_shortfalls` bullets, `met` must not have any, and
  `evidence_gaps: true` needs `unverified_checks` bullets.
- `unresolved_evidence_gaps` (optional) must contain one non-empty bullet list
  per decided segment with `evidence_gaps: true` and no other keys.
  A bullet list for a segment with `evidence_gaps: false` is rejected.
  An omitted placeholder segment gets the generated placeholder bullet;
  supplying its bullet list replaces the placeholder.

The report is validated against the shared contract before anything is
written, so a malformed payload fails with `ERROR: ...` (exit code 2) and
leaves any existing report untouched.  An incomplete but well-formed payload
renders, validates, and leaves the omitted segments as unverified placeholders.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    REPOSITORY_URL_PATTERN,
    SHA_PATTERN,
    SHORTFALL_STATUSES,
    STATUSES,
    ReportMetadata,
    SegmentBlock,
    SegmentDefs,
    bullet_list,
    parse_feedback_text,
    render_preamble,
    render_report,
    render_segment_block,
    segment_selector_to_int,
)
from tools.grader_tools.validate import validate_report

REPOSITORY_PATTERN = REPOSITORY_URL_PATTERN
PAYLOAD_KEYS = {
    "output_path",
    "team",
    "repository",
    "snapshot",
    "snapshot_notes",
    "summary",
    "strengths",
    "main_issues_to_fix",
    "segment_updates",
    "unresolved_evidence_gaps",
}
SEGMENT_UPDATE_KEYS = {"name", "status", "evidence_gaps", "evidence", "verified_shortfalls", "unverified_checks"}

# Fixed wording for a segment that a partial payload does not cover yet.
# It has to explain itself, so the placeholder stays visible in the report and
# in the unresolved-gaps section instead of reading like a judged result.
INCOMPLETE_SEGMENT_EVIDENCE = (
    "Not reviewed: the run stopped before this segment was reviewed, so no evidence was checked."
)
INCOMPLETE_SEGMENT_PLACEHOLDER = (
    "The run stopped before reviewing this segment; it stays unverified pending a later review."
)


def _unexpected_keys(seen: set[str], allowed: set[str], label: str) -> None:
    unexpected = sorted(seen - allowed)
    if unexpected:
        raise ValueError(f"Unexpected payload {label}: {', '.join(unexpected)}; allowed: {', '.join(sorted(allowed))}")


def _optional_text(payload: dict[str, object], key: str) -> str | None:
    value = payload.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"`{key}` must be a non-empty string or null")
    return value.strip()


def _output_path(payload: dict[str, object]) -> Path:
    value = payload.get("output_path")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("`output_path` must be a non-empty path string")
    return Path(value.strip()).expanduser()


def _render_preamble(assignment: str, payload: dict[str, object]) -> str:
    team = payload.get("team")
    if not isinstance(team, int) or isinstance(team, bool) or team < 1:
        raise ValueError("`team` must be a positive integer")

    repository = _optional_text(payload, "repository")
    if repository is not None and not REPOSITORY_PATTERN.fullmatch(repository):
        raise ValueError("`repository` must be `https://github.com/<org>/<repo>`")
    snapshot = _optional_text(payload, "snapshot")
    if snapshot is not None and not SHA_PATTERN.fullmatch(snapshot):
        raise ValueError("`snapshot` must be a full 40-character lowercase commit SHA")
    notes = _optional_text(payload, "snapshot_notes")

    return render_preamble(
        assignment,
        ReportMetadata(
            title=f"# Assignment {assignment[1:]} Feedback Report",
            team=team,
            repository=repository,
            snapshot=snapshot,
            primary_index=ASSIGNMENT_CONFIG[assignment]["primary_index"],
            notes=notes,
        ),
        notes_field="snapshot_notes",
    )


def _placeholder_segment(seg_num: int, name: str) -> SegmentBlock:
    """Build the fail-safe block for a segment that the payload does not cover yet."""
    evidence = [INCOMPLETE_SEGMENT_EVIDENCE]
    unverified = [INCOMPLETE_SEGMENT_PLACEHOLDER]
    return SegmentBlock(
        seg_num=seg_num,
        name=name,
        markdown=render_segment_block(seg_num, name, "unverified", True, evidence, [], unverified),
        status="unverified",
        evidence_gaps=True,
        evidence=evidence,
        verified_shortfalls=[],
        unverified_checks=unverified,
    )


def _parse_segment_updates(
    payload: dict[str, object], segment_defs: SegmentDefs
) -> tuple[dict[int, SegmentBlock], set[int]]:
    raw = payload.get("segment_updates")
    if not isinstance(raw, dict):
        raise ValueError("`segment_updates` must be an object keyed by segment IDs such as S1")

    blocks: dict[int, SegmentBlock] = {}
    for selector, update in raw.items():
        if not isinstance(selector, str):
            raise ValueError("`segment_updates` keys must be segment ID strings such as S1")
        if not isinstance(update, dict):
            raise ValueError(f"`segment_updates.{selector}` must be an object")
        seg_num = segment_selector_to_int(selector)
        if seg_num not in segment_defs:
            raise ValueError(f"`segment_updates.{selector}` is not a segment of this assignment")
        if seg_num in blocks:
            raise ValueError(f"`segment_updates` repeats S{seg_num} under another spelling")
        _unexpected_keys(set(update), SEGMENT_UPDATE_KEYS, f"key(s) in segment_updates.{selector}")

        name = segment_defs[seg_num]["name"]
        update_name = update.get("name")
        if update_name is not None and update_name != name:
            raise ValueError(f"`segment_updates.{selector}.name` must be `{name}`")

        status = update.get("status")
        if not isinstance(status, str) or status not in STATUSES:
            raise ValueError(f"`segment_updates.{selector}.status` must be one of: {', '.join(STATUSES)}")
        evidence_gaps = update.get("evidence_gaps")
        if not isinstance(evidence_gaps, bool):
            raise ValueError(f"`segment_updates.{selector}.evidence_gaps` must be a boolean")

        evidence = bullet_list(update.get("evidence"), f"segment_updates.{selector}.evidence", minimum=1)
        verified = bullet_list(update.get("verified_shortfalls", []), f"segment_updates.{selector}.verified_shortfalls")
        unverified = bullet_list(update.get("unverified_checks", []), f"segment_updates.{selector}.unverified_checks")

        if status in SHORTFALL_STATUSES and not verified:
            raise ValueError(
                f"`segment_updates.{selector}` is `{status}`, so `verified_shortfalls` needs at least one bullet"
            )
        if status == "met" and verified:
            raise ValueError(f"`segment_updates.{selector}` is `met`, so `verified_shortfalls` must be empty")
        if evidence_gaps and not unverified:
            raise ValueError(
                f"`segment_updates.{selector}` has `evidence_gaps: true`, so `unverified_checks` needs at least one bullet"
            )
        if not evidence_gaps and unverified:
            raise ValueError(
                f"`segment_updates.{selector}` has `evidence_gaps: false`, so `unverified_checks` must be empty"
            )
        if status == "unverified" and not evidence_gaps:
            raise ValueError(f"`segment_updates.{selector}` is `unverified`, so `evidence_gaps` must be true")

        blocks[seg_num] = SegmentBlock(
            seg_num=seg_num,
            name=name,
            markdown=render_segment_block(seg_num, name, status, evidence_gaps, evidence, verified, unverified),
            status=status,
            evidence_gaps=evidence_gaps,
            evidence=evidence,
            verified_shortfalls=verified,
            unverified_checks=unverified,
        )

    missing = sorted(set(segment_defs) - set(blocks))
    placeholder_segments: set[int] = set()
    for seg_num in missing:
        name = segment_defs[seg_num]["name"]
        blocks[seg_num] = _placeholder_segment(seg_num, name)
        placeholder_segments.add(seg_num)
    return blocks, placeholder_segments


def _parse_unresolved(
    payload: dict[str, object],
    segment_defs: SegmentDefs,
    blocks: dict[int, SegmentBlock],
    placeholder_segments: set[int],
) -> dict[int, list[str]]:
    raw = payload.get("unresolved_evidence_gaps")
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise ValueError("`unresolved_evidence_gaps` must be an object keyed by segment IDs when present")

    parsed: dict[int, list[str]] = {}
    for selector, bullets in raw.items():
        if not isinstance(selector, str):
            raise ValueError("`unresolved_evidence_gaps` keys must be segment ID strings such as S1")
        seg_num = segment_selector_to_int(selector)
        if seg_num not in segment_defs:
            raise ValueError(f"`unresolved_evidence_gaps.{selector}` is not a segment of this assignment")
        if seg_num in parsed:
            raise ValueError(f"`unresolved_evidence_gaps` repeats S{seg_num} under another spelling")
        if not blocks[seg_num].evidence_gaps:
            raise ValueError(f"`unresolved_evidence_gaps.{selector}` is only allowed for segments with `evidence_gaps: true`")
        parsed[seg_num] = bullet_list(bullets, f"unresolved_evidence_gaps.{selector}", minimum=1)

    missing = sorted(seg_num for seg_num, block in blocks.items() if block.evidence_gaps and seg_num not in parsed)
    decided = [seg_num for seg_num in missing if seg_num not in placeholder_segments]
    if decided:
        raise ValueError(
            "`unresolved_evidence_gaps` needs bullets for: " + ", ".join(f"S{seg_num}" for seg_num in decided)
        )
    for seg_num in missing:
        parsed[seg_num] = [INCOMPLETE_SEGMENT_PLACEHOLDER]
    return parsed


def render_feedback_report(assignment: str, payload: dict[str, object]) -> tuple[str, Path]:
    """Validate one render payload and return the rendered report text and output path."""
    if assignment not in ASSIGNMENT_CONFIG:
        raise ValueError(f"Unknown assignment `{assignment}`; expected one of: {', '.join(sorted(ASSIGNMENT_CONFIG))}")

    _unexpected_keys(set(payload), PAYLOAD_KEYS, "key(s)")
    segment_defs = ASSIGNMENT_CONFIG[assignment]["segment_defs"]
    output_path = _output_path(payload)
    preamble = _render_preamble(assignment, payload)
    blocks, placeholder_segments = _parse_segment_updates(payload, segment_defs)
    unresolved = _parse_unresolved(payload, segment_defs, blocks, placeholder_segments)
    summary = bullet_list(payload.get("summary"), "summary", minimum=3, maximum=5)
    strengths = bullet_list(payload.get("strengths"), "strengths", minimum=1)
    main_issues = bullet_list(payload.get("main_issues_to_fix"), "main_issues_to_fix", minimum=1)

    rendered = render_report(
        preamble=preamble,
        segment_defs=segment_defs,
        segment_blocks=blocks,
        unresolved_gaps=unresolved,
        summary_body="\n".join(f"- {bullet}" for bullet in summary),
        strengths_body="\n".join(f"- {bullet}" for bullet in strengths),
        main_issues_body="\n".join(f"- {bullet}" for bullet in main_issues),
    )

    errors = validate_report(assignment, parse_feedback_text(rendered, segment_defs))
    if errors:
        raise ValueError("Rendered report would not validate:\n" + "\n".join(f"- {error}" for error in errors))
    return rendered, output_path


def load_payload(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read payload {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Cannot parse payload {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a JSON object")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Render a complete agent-feedback.md from one structured JSON payload. "
            "The payload shape is documented in this script's module docstring."
        )
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG), help="Assignment directory such as A1")
    parser.add_argument("payload", help="Path to the JSON render payload")
    return parser


def run(argv: Sequence[str], *, out: Callable[[str], None] = print) -> int:
    args = build_parser().parse_args(argv)
    try:
        rendered, output_path = render_feedback_report(args.assignment, load_payload(Path(args.payload)))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    except (ValueError, OSError) as exc:
        out(f"ERROR: {exc}")
        return 2
    out(f"Wrote {output_path}")
    return 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
