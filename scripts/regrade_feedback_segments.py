#!/usr/bin/env python3
"""Apply structured segment regrades, validate the result, and regenerate the exports."""

from __future__ import annotations

import argparse
import contextlib
import io
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.patch_feedback_report import patch_report
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.extract_reports import run_extraction
from tools.grader_tools.feedback_report import (
    SegmentBlock,
    apply_structured_segment_update,
    compute_report_impact,
    diff_segment_block,
    format_status_counts,
    fresh_segment_state_from_update,
    load_fresh_segment_updates,
    load_patch_payload,
    parse_feedback_report,
    parse_feedback_text,
    parse_unresolved_section,
    segment_selector_to_int,
)
from tools.grader_tools.validate import validate_report


def build_subset_payload(
    payload: dict[str, object],
    fresh_updates: dict[str, dict[str, object]],
    selectors: list[str],
    predicted_blocks: dict[int, SegmentBlock],
    saved_unresolved: dict[int, list[str]],
) -> dict[str, object]:
    """Keep only the selected updates, and carry over unresolved bullets for untouched gap segments."""
    missing = [selector for selector in selectors if selector not in fresh_updates]
    if missing:
        raise ValueError(f"Fresh payload is missing updates for: {', '.join(missing)}")
    subset: dict[str, object] = {"segment_updates": {selector: fresh_updates[selector] for selector in selectors}}

    unresolved = payload.get("unresolved_evidence_gaps")
    if unresolved is not None and not isinstance(unresolved, dict):
        raise ValueError("Payload `unresolved_evidence_gaps` must be an object when present")

    merged: dict[str, list[str]] = {}
    for seg_num, block in sorted(predicted_blocks.items()):
        if not block.evidence_gaps:
            continue
        selector = f"S{seg_num}"
        if unresolved and selector in unresolved:
            merged[selector] = unresolved[selector]
        elif seg_num in saved_unresolved:
            merged[selector] = saved_unresolved[seg_num]
        else:
            raise ValueError(f"{selector} still has evidence gaps, but no unresolved evidence gaps bullets were provided")
    subset["unresolved_evidence_gaps"] = merged
    return subset


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply structured segment regrades and rerun the exports.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to feedback.md")
    parser.add_argument("fresh_payload", help="Path to a structured fresh payload JSON")
    parser.add_argument("segments", nargs="+", help="Segment IDs such as S1 S4")
    parser.add_argument("--quiet", action="store_true", help="Print only a one-line result")
    parser.add_argument("--dry-run", action="store_true", help="Show the predicted impact without patching")
    args = parser.parse_args()

    segment_defs = ASSIGNMENT_CONFIG[args.assignment]["segment_defs"]
    feedback_path = Path(args.feedback_path)
    payload_path = Path(args.fresh_payload)
    report = parse_feedback_report(feedback_path, segment_defs)
    saved_unresolved = parse_unresolved_section(report.unresolved_body, segment_defs)
    fresh_updates = load_fresh_segment_updates(payload_path)
    predicted_blocks = dict(report.segment_blocks)

    rows: list[str] = []
    for selector in args.segments:
        seg_num = segment_selector_to_int(selector)
        if selector not in fresh_updates:
            raise ValueError(f"Fresh payload is missing update for {selector}")
        name = segment_defs[seg_num]["name"]
        saved = report.segment_blocks[seg_num]
        fresh = fresh_segment_state_from_update(seg_num, name, fresh_updates[selector])
        predicted_blocks[seg_num] = apply_structured_segment_update(saved, fresh_updates[selector], name)
        diff = diff_segment_block(saved, fresh)
        changes: list[str] = []
        if diff.status_changed:
            changes.append(f"status {saved.status}->{fresh.status}")
        if diff.evidence_gaps_changed:
            changes.append(f"evidence_gaps {'yes' if saved.evidence_gaps else 'no'}->{'yes' if fresh.evidence_gaps else 'no'}")
        if diff.evidence_added or diff.evidence_removed:
            changes.append("evidence updated")
        if diff.verified_shortfalls_added or diff.verified_shortfalls_removed:
            changes.append("verified shortfalls updated")
        if diff.unverified_checks_added or diff.unverified_checks_removed:
            changes.append("unverified checks updated")
        rows.append(f"- {selector}: {', '.join(changes) if changes else 'no changes'}")

    impact = compute_report_impact(report, segment_defs, predicted_blocks)
    touched = {segment_selector_to_int(selector) for selector in args.segments}
    remaining = [f"S{n}" for n, block in sorted(predicted_blocks.items()) if block.evidence_gaps and n not in touched]
    impact_line = (
        f"statuses [{format_status_counts(impact.saved_counts)}] -> [{format_status_counts(impact.predicted_counts)}], "
        f"manual_review {impact.saved_manual_review_required} -> {impact.predicted_manual_review_required}"
    )
    if not args.quiet:
        print("Dry run." if args.dry_run else "Regrade preview.")
        print("\n".join(rows))
        print(f"Remaining unresolved gaps outside the regraded set: {', '.join(remaining) if remaining else 'none'}")
        print(f"Report impact: {impact_line}")
    if args.dry_run:
        if args.quiet:
            print(f"DRY RUN {args.assignment}: {impact_line}")
        return

    subset = build_subset_payload(load_patch_payload(payload_path), fresh_updates, args.segments, predicted_blocks, saved_unresolved)
    rendered = patch_report(args.assignment, report, subset)
    errors = validate_report(args.assignment, parse_feedback_text(rendered, segment_defs))
    if errors:
        raise SystemExit("Patched report would be invalid:\n" + "\n".join(f"- {error}" for error in errors))
    feedback_path.write_text(rendered, encoding="utf-8")

    markdownlint = shutil.which("markdownlint-cli2")
    if markdownlint:
        subprocess.run([markdownlint, "--fix", str(feedback_path)], check=True, cwd=ROOT, stdout=subprocess.DEVNULL if args.quiet else None)

    # feedback.md lives at <assignment root>/feedback/markdown/<team_dir>/feedback.md.
    feedback_dir = feedback_path.parent.parent
    assignment_root = feedback_dir.parent.parent
    dev_output = assignment_root / "dev.md"
    release_output = assignment_root / "feedback_release.csv"
    if args.quiet:
        with contextlib.redirect_stdout(io.StringIO()):
            status = run_extraction(args.assignment, feedback_dir, dev_output, release_output)
        print(f"OK {args.assignment}: {impact_line}")
    else:
        status = run_extraction(args.assignment, feedback_dir, dev_output, release_output)
    raise SystemExit(status)


if __name__ == "__main__":
    main()
