"""Validation of feedback reports against `docs/grading-feedback-format.md`."""

from __future__ import annotations

import re
from pathlib import Path

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    HEADER_NEXT_STEPS,
    HEADING_UNVERIFIED,
    HEADING_VERIFIED,
    NO_REVIEW_TEXT,
    SHORTFALL_STATUSES,
    STATUSES,
    ParsedFeedbackReport,
    SegmentDefs,
    has_subheading,
    parse_feedback_report,
    parse_preamble,
    parse_unresolved_section,
    render_overall_assessment,
    render_segments_table,
    status_counts,
)

METADATA_PREFIXES = [
    "- Team:",
    "- Repository reviewed:",
    "- Snapshot reviewed:",
    "- Primary index reviewed:",
]
NOTES_PREFIX = "- Notes about the snapshot:"
TEAM_LINE = re.compile(r"^- Team: \d+$")
REPOSITORY_LINE = re.compile(r"^- Repository reviewed: (`https://github\.com/[^/`\s]+/[^/`\s]+`|none)$")
SNAPSHOT_LINE = re.compile(r"^- Snapshot reviewed: (`[0-9a-f]{40}`|none)$")
ASSESSMENT_COUNT_LINE = re.compile(
    r"^-\s*(Met|Partial|Missing|Unverified):\s*`(\d+)/(\d+)`\s*$", re.MULTILINE | re.IGNORECASE
)

NEXT_STEPS_MIN = 1
NEXT_STEPS_MAX = 3
MENTOR_WORDING = re.compile(r"\bmentor", re.IGNORECASE)
NEXT_STEPS_EMPTY_BODY = "`## Suggested next steps` must be omitted rather than left empty"
BLOB_LINK = re.compile(
    r"https://github\.com/(?P<owner>[^/\s`)]+)/(?P<repo>[^/\s`]+)/blob/(?P<ref>[^/\s`)]+)(?:/[^\s`)]*)?"
)
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
COURSE_REPOSITORY = "inno-itpd/itpd"


def _format_counts(counts: dict[str, int], total: int) -> str:
    return " · ".join(f"{status} {counts[status]}/{total}" for status in STATUSES)


def _declared_assessment_counts(body: str) -> tuple[dict[str, int], int] | None:
    """Return the four declared counts and their total, or None when unreadable."""
    declared: dict[str, int] = {}
    totals: set[int] = set()
    for match in ASSESSMENT_COUNT_LINE.finditer(body):
        status = match.group(1).lower()
        if status in declared:
            return None
        declared[status] = int(match.group(2))
        totals.add(int(match.group(3)))
    if set(declared) != set(STATUSES) or len(totals) != 1:
        return None
    return declared, totals.pop()


def _validate_preamble(assignment: str, preamble: str, primary_index: str) -> list[str]:
    errors: list[str] = []
    lines = [line.strip() for line in preamble.splitlines() if line.strip()]
    if len(lines) < 5:
        return ["Preamble must include the title and four repository metadata bullets"]

    expected_title = f"# Assignment {assignment[1:]} Feedback Report"
    if lines[0] != expected_title:
        errors.append(f"Title must be `{expected_title}`")

    metadata = lines[1:5]
    for expected_prefix, line in zip(METADATA_PREFIXES, metadata, strict=True):
        if not line.startswith(expected_prefix):
            errors.append(f"Metadata line must start with `{expected_prefix}`")
    if errors:
        return errors

    if not TEAM_LINE.fullmatch(metadata[0]):
        errors.append("`- Team:` must be a plain team number")
    if not REPOSITORY_LINE.fullmatch(metadata[1]):
        errors.append("`- Repository reviewed:` must be a backticked `https://github.com/<org>/<repo>` URL or `none`")
    if not SNAPSHOT_LINE.fullmatch(metadata[2]):
        errors.append("`- Snapshot reviewed:` must be a backticked full 40-character SHA or `none`")

    primary_content = metadata[3][len("- Primary index reviewed:") :].strip()
    canonical_primary = re.compile(rf"^\[`{re.escape(primary_index)}`\]\(https://github\.com/[^)]+/blob/[0-9a-f]{{40}}/{re.escape(primary_index)}\)$")
    if primary_content != "none" and not canonical_primary.fullmatch(primary_content):
        errors.append(
            f"`Primary index reviewed` must be `` [`{primary_index}`](https://github.com/<org>/<repo>/blob/<sha>/{primary_index}) `` or `none`"
        )

    extra = lines[5:]
    if primary_content == "none":
        if len(extra) != 1 or not extra[0].startswith(NOTES_PREFIX):
            errors.append(f"`{NOTES_PREFIX}` must follow the metadata when the primary index is `none`")
    elif extra:
        if extra[0].startswith(NOTES_PREFIX):
            errors.append(f"`{NOTES_PREFIX}` is only allowed when `Primary index reviewed` is `none`")
        else:
            errors.append("Do not add extra preamble content before `## Overall assessment`")
    return errors


def _validate_segments(report: ParsedFeedbackReport, segment_defs: SegmentDefs) -> list[str]:
    errors: list[str] = []
    table = report.segments_table
    blocks = report.segment_blocks

    for seg_num, segment_def in sorted(segment_defs.items()):
        if seg_num not in table.statuses:
            errors.append(f"Missing S{seg_num} in the segments table")
            continue
        if seg_num not in blocks:
            errors.append(f"Missing segment details block for S{seg_num}")
            continue

        expected_name = segment_def["name"]
        if table.seen_names.get(seg_num) != expected_name:
            errors.append(f"S{seg_num} name is `{table.seen_names.get(seg_num, '')}`, expected `{expected_name}`")

        block = blocks[seg_num]
        if block.status != table.statuses[seg_num]:
            errors.append(f"S{seg_num} details status `{block.status}` does not match table status `{table.statuses[seg_num]}`")
        if block.evidence_gaps != table.evidence_gaps[seg_num]:
            errors.append(f"S{seg_num} details evidence-gaps line does not match the table")
        if block.status == "unverified" and not block.evidence_gaps:
            errors.append(f"S{seg_num} is `unverified`, so it must have `Evidence gaps: yes`")

        if not block.evidence:
            errors.append(f"S{seg_num} needs at least one `**Evidence:**` bullet")

        has_verified = has_subheading(block.markdown, HEADING_VERIFIED)
        if block.status in SHORTFALL_STATUSES and not block.verified_shortfalls:
            errors.append(f"S{seg_num} is `{block.status}`, so it needs `**{HEADING_VERIFIED}:**` bullets")
        if block.status == "met" and has_verified:
            errors.append(f"S{seg_num} is `met`, so it must not contain `**{HEADING_VERIFIED}:**`")

        has_unverified = has_subheading(block.markdown, HEADING_UNVERIFIED)
        if block.evidence_gaps and not block.unverified_checks:
            errors.append(f"S{seg_num} has evidence gaps, so it needs `**{HEADING_UNVERIFIED}:**` bullets")
        if not block.evidence_gaps and has_unverified:
            errors.append(f"S{seg_num} has `Evidence gaps: no`, so it must not contain `**{HEADING_UNVERIFIED}:**`")

    expected_review = "yes" if any(table.evidence_gaps.values()) else "no"
    if table.manual_review_required is None:
        errors.append("Missing `Manual review required` row")
    elif table.manual_review_required != expected_review:
        errors.append("`Manual review required` does not match the segment `Evidence gaps` flags")

    if not errors:
        if report.segments_body.strip() != render_segments_table(segment_defs, blocks).strip():
            errors.append("`## Segments` must use the canonical table formatting")
        statuses = [blocks[seg_num].status for seg_num in sorted(segment_defs)]
        computed_counts = status_counts(statuses)
        canonical_assessment = render_overall_assessment(statuses, expected_review == "yes")
        if report.assessment_body.strip() != canonical_assessment.strip():
            declared = _declared_assessment_counts(report.assessment_body)
            if declared is None:
                errors.append(
                    "`## Overall assessment` must use the canonical formatting and match the segment statuses: "
                    f"computed {_format_counts(computed_counts, len(statuses))}"
                )
            else:
                declared_counts, declared_total = declared
                message = (
                    "`## Overall assessment` does not match the segment statuses: "
                    f"declared {_format_counts(declared_counts, declared_total)}; "
                    f"computed {_format_counts(computed_counts, len(statuses))}"
                )
                if declared_counts == computed_counts and declared_total == len(statuses):
                    message += " (the counts agree; check the formatting and the automatic review status)"
                errors.append(message)
    return errors


def _validate_unresolved(report: ParsedFeedbackReport, segment_defs: SegmentDefs) -> list[str]:
    gap_segments = {seg_num for seg_num, has_gap in report.segments_table.evidence_gaps.items() if has_gap}
    body = report.unresolved_body.strip()
    if not gap_segments:
        if body != NO_REVIEW_TEXT:
            return [f"`## Unresolved evidence gaps` must be exactly `{NO_REVIEW_TEXT}` when no gaps remain"]
        return []
    if body == NO_REVIEW_TEXT:
        return ["`## Unresolved evidence gaps` cannot use the no-review sentence while a segment has `Evidence gaps: yes`"]

    try:
        unresolved = parse_unresolved_section(body, segment_defs)
    except ValueError as exc:
        return [str(exc)]
    if set(unresolved) != gap_segments:
        expected = ", ".join(f"S{n}" for n in sorted(gap_segments))
        actual = ", ".join(f"S{n}" for n in sorted(unresolved)) or "none"
        return [f"Unresolved evidence gaps bullets do not match the segment gap flags (expected {expected}; got {actual})"]
    empty = [f"S{n}" for n, bullets in sorted(unresolved.items()) if not bullets]
    if empty:
        return [f"Unresolved evidence gaps need nested bullets for: {', '.join(empty)}"]
    return []


def _validate_summary(summary_body: str) -> list[str]:
    bullets = [line for line in summary_body.splitlines() if line.strip().startswith("- ")]
    if not 3 <= len(bullets) <= 5:
        return ["`## Summary` must contain 3-5 bullets"]
    return []


def _validate_next_steps(next_steps_body: str | None) -> list[str]:
    """Check the optional advice section's schema, or nothing when it is absent."""
    if next_steps_body is None:
        return []
    if not next_steps_body.strip():
        return [NEXT_STEPS_EMPTY_BODY]

    bullets: list[str] = []
    for line in next_steps_body.splitlines():
        if not line.strip():
            continue
        if line != line.lstrip():
            return [f"`{HEADER_NEXT_STEPS}` must contain a single-level bullet list, with no nested bullets"]
        if not line.startswith("- "):
            return [f"`{HEADER_NEXT_STEPS}` must contain only bullets"]
        bullet = line[2:].strip()
        if not bullet:
            return [f"`{HEADER_NEXT_STEPS}` must not contain an empty bullet"]
        bullets.append(bullet)

    errors: list[str] = []
    if not NEXT_STEPS_MIN <= len(bullets) <= NEXT_STEPS_MAX:
        errors.append(
            f"`{HEADER_NEXT_STEPS}` must contain {NEXT_STEPS_MIN}-{NEXT_STEPS_MAX} bullets, got {len(bullets)}"
        )
    for bullet in bullets:
        if MENTOR_WORDING.search(bullet):
            errors.append(f"`{HEADER_NEXT_STEPS}` must not use mentor wording: {bullet}")
        if bullet.strip().strip("`").strip().lower() == "none":
            errors.append(f"`{HEADER_NEXT_STEPS}` must be omitted rather than say `None`")
    return errors


def _repository_key(url: str | None) -> str | None:
    """Return `org/repo` from a canonical repository URL, or None."""
    if url is None:
        return None
    match = re.fullmatch(r"https://github\.com/([^/]+)/([^/]+)", url)
    return f"{match.group(1)}/{match.group(2)}" if match else None


def _positive_link_lines(text: str) -> list[str]:
    """Return the lines whose pinned links must cite the snapshot.

    `**Why not met (verified):**` and `**Why not met (unverified):**` bullets may
    cite an artifact at another commit to show that it is not in the snapshot, so
    they are exempt; positive evidence and prose must cite the reviewed snapshot.
    """
    negative_headings = (f"**{HEADING_VERIFIED}:**", f"**{HEADING_UNVERIFIED}:**")
    kept: list[str] = []
    in_negative = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped in negative_headings:
            in_negative = True
            continue
        if stripped.startswith("**") and stripped.endswith(":**"):
            in_negative = False
        elif stripped.startswith("## "):
            in_negative = False
        if not in_negative:
            kept.append(line)
    return kept


def _validate_blob_links(
    assignment: str,
    text: str,
    repository: str | None,
    snapshot: str | None,
) -> list[str]:
    """Check every pinned `blob/<sha>` body link against the repository it names.

    A branch ref such as `blob/main` is a live link, so it is exempt; only a
    full 40-character SHA is a pinned citation.  The report's own snapshot is
    exempt because the preamble already pins it, `inno-itpd/itpd` must cite the
    assignment's pinned course commit, the team repository must cite its
    snapshot, and any other repository is exempt.
    Negative-evidence bullets are exempt because they may cite a commit outside
    the snapshot to show that the artifact was not submitted.
    """
    course_commit = ASSIGNMENT_CONFIG[assignment].get("course_commit")
    team_repository = _repository_key(repository)
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    for line in _positive_link_lines(text):
        for match in BLOB_LINK.finditer(line):
            target = f"{match.group('owner')}/{match.group('repo')}"
            ref = match.group("ref")
            if not FULL_SHA.fullmatch(ref):
                continue
            if snapshot is not None and ref == snapshot:
                continue
            expected: str | None = None
            if target == COURSE_REPOSITORY:
                expected = course_commit
            elif team_repository is not None and target == team_repository:
                expected = snapshot
            if expected is None or ref == expected:
                continue
            key = (match.group(0), expected)
            if key in seen:
                continue
            seen.add(key)
            errors.append(
                f"Body link `{match.group(0)}` must point at `{expected}` for `{target}`, not `{ref}`"
            )
    return errors


def validate_report(assignment: str, report: ParsedFeedbackReport) -> list[str]:
    config = ASSIGNMENT_CONFIG[assignment]
    segment_defs = config["segment_defs"]
    errors = _validate_preamble(assignment, report.preamble, config["primary_index"])
    errors.extend(_validate_segments(report, segment_defs))
    errors.extend(_validate_unresolved(report, segment_defs))
    errors.extend(_validate_summary(report.summary_body))
    errors.extend(_validate_next_steps(report.next_steps_body))

    try:
        metadata = parse_preamble(report.preamble)
    except ValueError:
        repository, snapshot = None, None
    else:
        repository, snapshot = metadata.repository, metadata.snapshot
    errors.extend(_validate_blob_links(assignment, report.text, repository, snapshot))
    return errors


def validate_feedback_file(assignment: str, path: Path) -> list[str]:
    try:
        report = parse_feedback_report(path, ASSIGNMENT_CONFIG[assignment]["segment_defs"])
    except ValueError as exc:
        return [str(exc)]
    return validate_report(assignment, report)
