#!/usr/bin/env python3
"""Patch selected segment blocks, metadata, or overall-assessment sections.

The payload is a JSON object.  It may contain any of:

```json
{
  "report": {
    "repository": "org/repo or https://github.com/org/repo or null",
    "snapshot": "<full 40-character lowercase SHA> or null",
    "primary_index": "reports/week-NN/README.md or null",
    "notes": "<single-line prose> or null"
  },
  "sections": {
    "summary": ["3 to 5 one-line bullets"],
    "strengths": ["at least one one-line bullet"],
    "main_issues_to_fix": ["at least one one-line bullet"]
  },
  "summary": "- an existing string body\n- kept for compatibility",
  "strengths": "...",
  "main_issues_to_fix": "...",
  "segments": {"S4": "<full replacement Markdown>"},
  "segment_updates": {"S4": {"status": "met", "...": "..."}},
  "unresolved_evidence_gaps": {"S2": ["one bullet per unresolved check"]}
}
```

`report` rules:

- The object and every field are optional.  When `report` is omitted the
  metadata preamble is left byte-for-byte alone.
- `snapshot` and `repository` are each optional.  Omitting one keeps the saved
  value; `null` marks that side unresolved; a string replaces it.  `repository`
  accepts either `org/repo` or `https://github.com/org/repo` and is always
  rendered as the URL.
- `primary_index` defaults to the assignment's configured path.  `null` also
  selects the default; any other path is rejected.
- `notes` is a single-line prose bullet.  Omitting it keeps the saved value;
  `null` removes it.  It is required while either `repository` or `snapshot`
  is unresolved, and rejected when the pair is resolved.  Resolving the pair
  always removes the saved notes bullet.
- The title and team number are read from the saved report and kept unchanged.

`sections` rules:

- The object and every field are optional.  An omitted section keeps the saved
  body.
- `summary` takes 3-5 one-line bullets, `strengths` and `main_issues_to_fix`
  take at least one.  The names match `render_feedback_report.py`.  A
  `main_issues` alias is accepted for `main_issues_to_fix`.
- The top-level string `summary`, `strengths`, and `main_issues_to_fix` keys
  remain supported.  Supplying the same section both ways is rejected.

The rendered report is re-parsed and validated exactly like a full render, so
an invalid payload prints `ERROR: ...` (exit code 2) and leaves the report file
untouched.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    ParsedFeedbackReport,
    ReportMetadata,
    SHA_PATTERN,
    apply_structured_segment_update,
    bullet_list,
    load_patch_payload,
    normalize_repository,
    parse_feedback_report,
    parse_feedback_text,
    parse_preamble,
    parse_segment_blocks,
    parse_unresolved_section,
    render_preamble,
    render_report,
    segment_selector_to_int,
    single_line_text,
)
from tools.grader_tools.validate import validate_report

REPORT_KEYS = {"snapshot", "repository", "primary_index", "notes"}
SECTION_BODY_KEYS = ("summary", "strengths", "main_issues_to_fix")
SECTION_ALIASES = {"main_issues": "main_issues_to_fix"}
SECTION_BULLET_LIMITS = {
    "summary": (3, 5),
    "strengths": (1, None),
    "main_issues_to_fix": (1, None),
}


def _reject_unexpected(seen: set[object], allowed: set[str], label: str) -> None:
    unexpected = sorted(str(key) for key in seen if key not in allowed)
    if unexpected:
        raise ValueError(f"Unexpected {label}: {', '.join(unexpected)}; allowed: {', '.join(sorted(allowed))}")


def raw_sections_requested(payload: dict[str, object]) -> bool:
    return "sections" in payload or any(key in payload for key in SECTION_BODY_KEYS)


def resolve_report_metadata(
    assignment: str,
    saved: ReportMetadata,
    payload: dict[str, object],
) -> ReportMetadata:
    """Apply the payload's optional `report` object to the saved metadata."""
    raw = payload.get("report")
    if not isinstance(raw, dict):
        raise ValueError("Patch payload `report` must be an object")
    _reject_unexpected(set(raw), REPORT_KEYS, "key(s) in `report`")

    snapshot = saved.snapshot
    if "snapshot" in raw:
        value = raw["snapshot"]
        if value is None:
            snapshot = None
        elif isinstance(value, str) and SHA_PATTERN.fullmatch(value.strip()):
            snapshot = value.strip()
        else:
            raise ValueError("`report.snapshot` must be a full 40-character lowercase commit SHA or null")

    repository = saved.repository
    if "repository" in raw:
        value = raw["repository"]
        if value is None:
            repository = None
        elif isinstance(value, str):
            repository = normalize_repository(value)
        else:
            raise ValueError(
                "`report.repository` must be `org/repo`, `https://github.com/<org>/<repo>`, or null"
            )

    config_index = ASSIGNMENT_CONFIG[assignment]["primary_index"]
    if "primary_index" in raw:
        value = raw["primary_index"]
        if value is not None and (not isinstance(value, str) or value.strip() != config_index):
            raise ValueError(f"`report.primary_index` must be `{config_index}` or null")

    resolved = repository is not None and snapshot is not None
    notes = saved.notes
    if resolved:
        if "notes" in raw and raw["notes"] is not None:
            raise ValueError("`report.notes` is not allowed when `repository` and `snapshot` are both resolved")
        notes = None
    elif "notes" in raw:
        if raw["notes"] is None:
            raise ValueError("`report.notes` is required when `repository` or `snapshot` is unresolved")
        notes = single_line_text(raw["notes"], "report.notes")
    elif notes is None:
        raise ValueError("`report.notes` is required when `repository` or `snapshot` is unresolved")
    else:
        notes = single_line_text(notes, "report.notes")

    return ReportMetadata(
        title=saved.title,
        team=saved.team,
        repository=repository,
        snapshot=snapshot,
        primary_index=config_index if resolved else None,
        notes=notes,
    )


def resolve_sections(payload: dict[str, object], saved_bodies: dict[str, str]) -> dict[str, str]:
    """Apply the payload's optional `sections` object and string overrides."""
    bodies = dict(saved_bodies)
    raw = payload.get("sections")
    if raw is not None:
        if not isinstance(raw, dict):
            raise ValueError("Patch payload `sections` must be an object")
        _reject_unexpected(set(raw), set(SECTION_BULLET_LIMITS) | set(SECTION_ALIASES), "key(s) in `sections`")

        normalized: dict[str, object] = {}
        for key, value in raw.items():
            canonical = SECTION_ALIASES.get(key, key)
            if canonical in normalized:
                raise ValueError(f"Patch payload `sections` repeats `{canonical}` under another spelling")
            if canonical in payload:
                raise ValueError(f"`{canonical}` is provided both in `sections` and at the top level; use one")
            normalized[canonical] = value

        for key, value in normalized.items():
            minimum, maximum = SECTION_BULLET_LIMITS[key]
            bullets = bullet_list(value, f"sections.{key}", minimum=minimum, maximum=maximum)
            bodies[key] = "\n".join(f"- {bullet}" for bullet in bullets)

    for key in SECTION_BODY_KEYS:
        if key not in payload:
            continue
        value = payload[key]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Patch payload `{key}` must be a non-empty string")
        bodies[key] = value.strip()
    return bodies


def patch_report(assignment: str, report: ParsedFeedbackReport, payload: dict[str, object]) -> str:
    segment_defs = ASSIGNMENT_CONFIG[assignment]["segment_defs"]
    segment_blocks = dict(report.segment_blocks)
    replacements = payload.get("segments")
    structured = payload.get("segment_updates")
    has_metadata = "report" in payload
    has_sections = raw_sections_requested(payload)
    if not isinstance(replacements, dict) and not isinstance(structured, dict) and not has_metadata and not has_sections:
        raise ValueError(
            "Patch payload must include a `report`, `sections`, `segments`, or `segment_updates` object"
        )
    if replacements is not None and not isinstance(replacements, dict):
        raise ValueError("Patch payload `segments` must be an object")
    if structured is not None and not isinstance(structured, dict):
        raise ValueError("Patch payload `segment_updates` must be an object")

    if isinstance(replacements, dict):
        for selector, markdown in replacements.items():
            seg_num = segment_selector_to_int(selector)
            if not isinstance(markdown, str) or not markdown.strip():
                raise ValueError(f"Replacement for {selector} must be a non-empty string")
            parsed = parse_segment_blocks(markdown.strip(), segment_defs)
            if list(parsed) != [seg_num]:
                raise ValueError(f"Replacement for {selector} must contain exactly one matching segment block")
            segment_blocks[seg_num] = parsed[seg_num]

    if isinstance(structured, dict):
        for selector, update in structured.items():
            seg_num = segment_selector_to_int(selector)
            segment_blocks[seg_num] = apply_structured_segment_update(
                segment_blocks[seg_num], update, segment_defs[seg_num]["name"]
            )

    unresolved = parse_unresolved_section(report.unresolved_body, segment_defs)
    payload_unresolved = payload.get("unresolved_evidence_gaps")
    if payload_unresolved is not None:
        if not isinstance(payload_unresolved, dict):
            raise ValueError("Patch payload `unresolved_evidence_gaps` must be an object")
        unresolved = {}
        for selector, bullets in payload_unresolved.items():
            if not isinstance(bullets, list) or not bullets or not all(isinstance(item, str) and item.strip() for item in bullets):
                raise ValueError(f"Unresolved bullets for {selector} must be a non-empty string list")
            unresolved[segment_selector_to_int(selector)] = [item.strip() for item in bullets]

    preamble = report.preamble
    if has_metadata:
        preamble = render_preamble(assignment, resolve_report_metadata(assignment, parse_preamble(preamble), payload))

    bodies = resolve_sections(
        payload,
        {
            "summary": report.summary_body,
            "strengths": report.strengths_body,
            "main_issues_to_fix": report.main_issues_body,
        },
    )

    rendered = render_report(
        preamble=preamble,
        segment_defs=segment_defs,
        segment_blocks=segment_blocks,
        unresolved_gaps=unresolved,
        summary_body=bodies["summary"],
        strengths_body=bodies["strengths"],
        main_issues_body=bodies["main_issues_to_fix"],
    )
    errors = validate_report(assignment, parse_feedback_text(rendered, segment_defs))
    if errors:
        raise ValueError("Patched report would not validate:\n" + "\n".join(f"- {error}" for error in errors))
    return rendered


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch selected segments or metadata in agent-feedback.md.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to agent-feedback.md")
    parser.add_argument("patch_payload", help="Path to JSON patch payload")
    args = parser.parse_args()

    feedback_path = Path(args.feedback_path)
    try:
        report = parse_feedback_report(feedback_path, ASSIGNMENT_CONFIG[args.assignment]["segment_defs"])
        rendered = patch_report(args.assignment, report, load_patch_payload(Path(args.patch_payload)))
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(2)
    feedback_path.write_text(rendered, encoding="utf-8")
    print(f"Patched {feedback_path}")


if __name__ == "__main__":
    main()
