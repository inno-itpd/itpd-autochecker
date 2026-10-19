from __future__ import annotations

from dataclasses import dataclass
import json
import re
from pathlib import Path

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG

STATUSES = ("met", "partial", "missing", "unverified")
SHORTFALL_STATUSES = ("partial", "missing")

NO_REVIEW_TEXT = "No manual review required. All evidence was accessible"
ASSESSMENT_NOTE = (
    "This assessment reflects currently checked evidence and may change after instructor review of unresolved evidence gaps."
)

HEADER_ASSESSMENT = "## Overall assessment"
HEADER_SEGMENTS = "## Segments"
HEADER_UNRESOLVED = "## Unresolved evidence gaps"
HEADER_SUMMARY = "## Summary"
HEADER_STRENGTHS = "## Strengths"
HEADER_MAIN_ISSUES = "## Main issues to fix"
HEADER_DETAILS = "## Segment details"

SECTION_ORDER = [
    HEADER_ASSESSMENT,
    HEADER_SEGMENTS,
    HEADER_UNRESOLVED,
    HEADER_SUMMARY,
    HEADER_STRENGTHS,
    HEADER_MAIN_ISSUES,
    HEADER_DETAILS,
]

HEADING_EVIDENCE = "Evidence"
HEADING_VERIFIED = "Why not met (verified)"
HEADING_UNVERIFIED = "Why not met (unverified)"

HEADING_PATTERNS = {
    heading: re.compile(rf"^{re.escape(heading)}\s*$", re.MULTILINE)
    for heading in SECTION_ORDER
}
NEXT_H2 = re.compile(r"^##\s", re.MULTILINE)

# The canonical repository metadata lines.  `render_preamble` writes them and
# `parse_preamble` reads them, so the regrade payload cannot drift from a full
# render.
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
REPOSITORY_URL_PATTERN = re.compile(r"^https://github\.com/[^/`\s]+/[^/`\s]+$")
REPOSITORY_SLUG_PATTERN = re.compile(r"^[^/`\s]+/[^/`\s]+$")
PREAMBLE_TITLE_LINE = re.compile(r"^# Assignment \d+ Feedback Report$")
PREAMBLE_TEAM_LINE = re.compile(r"^- Team: (\d+)$")
PREAMBLE_REPOSITORY_LINE = re.compile(
    r"^- Repository reviewed: (`(https://github\.com/[^/`\s]+/[^/`\s]+)`|none)$"
)
PREAMBLE_SNAPSHOT_LINE = re.compile(r"^- Snapshot reviewed: (`([0-9a-f]{40})`|none)$")
PREAMBLE_PRIMARY_LINE = re.compile(
    r"^- Primary index reviewed: (none|\[`([^`]+)`\]\((https://github\.com/[^)]+)\))$"
)
PREAMBLE_NOTES_LINE = re.compile(r"^- Notes about the snapshot: (.+)$")
SEGMENT_SELECTOR_PATTERN = re.compile(r"^S\d+$", re.IGNORECASE)
SEGMENT_HEADING = re.compile(r"^###\s*S(\d+):\s*(.*?)\s*$", re.MULTILINE)
TOP_GAP_BULLET = re.compile(r"^- \[S(\d+)\]\((#[^)]+)\)$")
STATUS_ALTERNATION = "|".join(STATUSES)
SEGMENT_ROW = re.compile(
    r"\|\s*(?:\[S(\d+):\s*(.*?)\]\((#[^)]+)\)|S(\d+):\s*(.*?))\s*"
    rf"\|\s*({STATUS_ALTERNATION})\s*\|\s*(yes|no)\s*\|",
    re.IGNORECASE,
)
MANUAL_REVIEW_ROW = re.compile(r"\|\s*Manual review required\s*\|\s*(yes|no)\s*\|\s*\|", re.IGNORECASE)

SegmentDefs = dict[int, dict[str, str]]


def normalize_line_endings(text: str) -> str:
    return text.replace("\r\n", "\n")


def slugify_heading(text: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug


def segment_anchor(seg_num: int, segment_name: str) -> str:
    return "#" + slugify_heading(f"S{seg_num}: {segment_name}")


def segments_table_label(seg_num: int, segment_name: str) -> str:
    return f"[S{seg_num}: {segment_name}]({segment_anchor(seg_num, segment_name)})"


def section_body(text: str, start_match: re.Match[str]) -> str:
    after = text[start_match.end() :]
    next_heading = NEXT_H2.search(after)
    return after[: next_heading.start()].strip() if next_heading else after.strip()


@dataclass(frozen=True)
class ParsedSegmentsTable:
    statuses: dict[int, str]
    evidence_gaps: dict[int, bool]
    seen_names: dict[int, str]
    manual_review_required: str | None


@dataclass(frozen=True)
class SegmentBlock:
    seg_num: int
    name: str
    markdown: str
    status: str
    evidence_gaps: bool
    evidence: list[str]
    verified_shortfalls: list[str]
    unverified_checks: list[str]


@dataclass(frozen=True)
class ParsedFeedbackReport:
    text: str
    preamble: str
    assessment_body: str
    segments_body: str
    unresolved_body: str
    summary_body: str
    strengths_body: str
    main_issues_body: str
    details_body: str
    segments_table: ParsedSegmentsTable
    segment_blocks: dict[int, SegmentBlock]


@dataclass(frozen=True)
class ReportMetadata:
    """The repository metadata bullets of a feedback report."""

    title: str
    team: int
    repository: str | None
    snapshot: str | None
    primary_index: str | None
    notes: str | None


@dataclass(frozen=True)
class FreshSegmentState:
    seg_num: int
    name: str
    status: str
    evidence_gaps: bool
    evidence: list[str]
    verified_shortfalls: list[str]
    unverified_checks: list[str]
    source: str | None
    checked_at: str | None
    notes: list[str]


@dataclass(frozen=True)
class SegmentDiff:
    status_changed: bool
    evidence_gaps_changed: bool
    evidence_added: list[str]
    evidence_removed: list[str]
    verified_shortfalls_added: list[str]
    verified_shortfalls_removed: list[str]
    unverified_checks_added: list[str]
    unverified_checks_removed: list[str]


@dataclass(frozen=True)
class ReportImpact:
    saved_counts: dict[str, int]
    predicted_counts: dict[str, int]
    saved_manual_review_required: str
    predicted_manual_review_required: str


def status_counts(statuses: list[str]) -> dict[str, int]:
    return {status: statuses.count(status) for status in STATUSES}


def format_status_counts(counts: dict[str, int]) -> str:
    parts = [f"{status} {counts[status]}" for status in STATUSES if counts.get(status)]
    return " · ".join(parts)


def extract_required_sections(text: str) -> dict[str, tuple[re.Match[str], str]]:
    sections: dict[str, tuple[re.Match[str], str]] = {}
    for heading in SECTION_ORDER:
        match = HEADING_PATTERNS[heading].search(text)
        if not match:
            raise ValueError(f"Missing {heading} section")
        sections[heading] = (match, section_body(text, match))

    positions = [sections[heading][0].start() for heading in SECTION_ORDER]
    if positions != sorted(positions):
        raise ValueError("Sections must appear in this order: " + ", ".join(SECTION_ORDER))
    return sections


def parse_segments_table(table_text: str, segment_defs: SegmentDefs) -> ParsedSegmentsTable:
    statuses: dict[int, str] = {}
    evidence_gaps: dict[int, bool] = {}
    seen_names: dict[int, str] = {}

    for line in table_text.splitlines():
        match = SEGMENT_ROW.match(line.strip())
        if not match:
            continue
        if match.group(1) is not None:
            seg_num, seg_name = int(match.group(1)), match.group(2).strip()
        else:
            seg_num, seg_name = int(match.group(4)), match.group(5).strip()
        if seg_num not in segment_defs:
            continue
        seen_names[seg_num] = seg_name
        statuses[seg_num] = match.group(6).lower()
        evidence_gaps[seg_num] = match.group(7).lower() == "yes"

    manual_review_match = MANUAL_REVIEW_ROW.search(table_text)
    return ParsedSegmentsTable(
        statuses=statuses,
        evidence_gaps=evidence_gaps,
        seen_names=seen_names,
        manual_review_required=manual_review_match.group(1).lower() if manual_review_match else None,
    )


def _extract_bullets(block: str, heading: str) -> list[str]:
    pattern = re.compile(rf"^\*\*{re.escape(heading)}:\*\*\s*$", re.MULTILINE)
    match = pattern.search(block)
    if not match:
        return []
    after = block[match.end() :]
    next_subheading = re.search(r"^\*\*[^\n]+:\*\*\s*$", after, re.MULTILINE)
    body = after[: next_subheading.start()] if next_subheading else after
    return [line.strip()[2:].strip() for line in body.splitlines() if line.strip().startswith("- ")]


def has_subheading(block: str, heading: str) -> bool:
    return f"**{heading}:**" in block


def parse_segment_blocks(details_text: str, segment_defs: SegmentDefs) -> dict[int, SegmentBlock]:
    matches = list(SEGMENT_HEADING.finditer(details_text))
    blocks: dict[int, SegmentBlock] = {}
    for index, match in enumerate(matches):
        seg_num = int(match.group(1))
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(details_text)
        block = details_text[match.start() : next_start].strip()
        if seg_num not in segment_defs:
            continue
        expected_name = segment_defs[seg_num]["name"]

        status_match = re.search(rf"^Status:\s*({STATUS_ALTERNATION})\s*$", block, re.MULTILINE | re.IGNORECASE)
        gap_match = re.search(r"^Evidence gaps:\s*(yes|no)\s*$", block, re.MULTILINE | re.IGNORECASE)
        if not status_match or not gap_match:
            raise ValueError(f"Missing status or evidence-gaps line for S{seg_num}")
        if match.group(2).strip() != expected_name:
            raise ValueError(f"S{seg_num} heading name is `{match.group(2).strip()}`, expected `{expected_name}`")

        blocks[seg_num] = SegmentBlock(
            seg_num=seg_num,
            name=expected_name,
            markdown=block,
            status=status_match.group(1).lower(),
            evidence_gaps=gap_match.group(1).lower() == "yes",
            evidence=_extract_bullets(block, HEADING_EVIDENCE),
            verified_shortfalls=_extract_bullets(block, HEADING_VERIFIED),
            unverified_checks=_extract_bullets(block, HEADING_UNVERIFIED),
        )
    return blocks


def parse_feedback_text(text: str, segment_defs: SegmentDefs) -> ParsedFeedbackReport:
    text = normalize_line_endings(text)
    sections = extract_required_sections(text)
    return ParsedFeedbackReport(
        text=text,
        preamble=text[: sections[HEADER_ASSESSMENT][0].start()].strip(),
        assessment_body=sections[HEADER_ASSESSMENT][1],
        segments_body=sections[HEADER_SEGMENTS][1],
        unresolved_body=sections[HEADER_UNRESOLVED][1],
        summary_body=sections[HEADER_SUMMARY][1],
        strengths_body=sections[HEADER_STRENGTHS][1],
        main_issues_body=sections[HEADER_MAIN_ISSUES][1],
        details_body=sections[HEADER_DETAILS][1],
        segments_table=parse_segments_table(sections[HEADER_SEGMENTS][1], segment_defs),
        segment_blocks=parse_segment_blocks(sections[HEADER_DETAILS][1], segment_defs),
    )


def parse_feedback_report(path: Path, segment_defs: SegmentDefs) -> ParsedFeedbackReport:
    return parse_feedback_text(path.read_text(encoding="utf-8"), segment_defs)


def single_line_text(value: object, field_name: str) -> str:
    """Validate a non-empty, single-line prose field."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"`{field_name}` must be a non-empty string")
    text = value.strip()
    if "\n" in text or "\r" in text:
        raise ValueError(f"`{field_name}` must be a single line")
    return text


def normalize_repository(value: str) -> str:
    """Normalize `org/repo` or a GitHub URL to the canonical repository URL."""
    text = value.strip()
    if REPOSITORY_URL_PATTERN.fullmatch(text):
        return text
    if REPOSITORY_SLUG_PATTERN.fullmatch(text):
        return f"https://github.com/{text}"
    raise ValueError("`repository` must be `org/repo` or `https://github.com/<org>/<repo>`")


def parse_preamble(preamble: str) -> ReportMetadata:
    """Read the title and repository metadata bullets of an existing report."""
    lines = [line.strip() for line in normalize_line_endings(preamble).splitlines() if line.strip()]
    if not lines:
        raise ValueError("Report preamble is empty")
    if len(lines) < 5:
        raise ValueError("Report preamble must include the title and four repository metadata bullets")
    if not PREAMBLE_TITLE_LINE.fullmatch(lines[0]):
        raise ValueError("Report preamble must start with `# Assignment <N> Feedback Report`")

    team_match = PREAMBLE_TEAM_LINE.fullmatch(lines[1])
    if not team_match:
        raise ValueError("Report preamble `- Team:` line is missing or malformed")
    repository_match = PREAMBLE_REPOSITORY_LINE.fullmatch(lines[2])
    if not repository_match:
        raise ValueError("Report preamble `- Repository reviewed:` line is missing or malformed")
    snapshot_match = PREAMBLE_SNAPSHOT_LINE.fullmatch(lines[3])
    if not snapshot_match:
        raise ValueError("Report preamble `- Snapshot reviewed:` line is missing or malformed")
    primary_match = PREAMBLE_PRIMARY_LINE.fullmatch(lines[4])
    if not primary_match:
        raise ValueError("Report preamble `- Primary index reviewed:` line is missing or malformed")

    repository = repository_match.group(2) if repository_match.group(1) != "none" else None
    snapshot = snapshot_match.group(2) if snapshot_match.group(1) != "none" else None
    primary_index = None if primary_match.group(1) == "none" else primary_match.group(2)

    notes: str | None = None
    extra = lines[5:]
    if extra:
        notes_match = PREAMBLE_NOTES_LINE.fullmatch(extra[0])
        if not notes_match:
            raise ValueError("Report preamble has unexpected content after the repository metadata")
        if len(extra) > 1:
            raise ValueError("Report preamble has unexpected content after the snapshot notes")
        notes = notes_match.group(1).strip()

    return ReportMetadata(
        title=lines[0],
        team=int(team_match.group(1)),
        repository=repository,
        snapshot=snapshot,
        primary_index=primary_index,
        notes=notes,
    )


def render_preamble(assignment: str, metadata: ReportMetadata, *, notes_field: str = "notes") -> str:
    """Render the canonical title and repository metadata bullets.

    A resolved `repository` + `snapshot` pair renders the primary-index
    permalink and forbids notes.  An unresolved pair renders
    `Primary index reviewed: none` and requires a notes bullet.  `notes_field`
    names the payload field in error messages so the full render and the
    regrade payload can report their own key.
    """
    if assignment not in ASSIGNMENT_CONFIG:
        raise ValueError(f"Unknown assignment `{assignment}`; expected one of: {', '.join(sorted(ASSIGNMENT_CONFIG))}")
    config_index = ASSIGNMENT_CONFIG[assignment]["primary_index"]

    title = single_line_text(metadata.title, "title")
    if not isinstance(metadata.team, int) or isinstance(metadata.team, bool) or metadata.team < 1:
        raise ValueError("`team` must be a positive integer")

    repository = metadata.repository.strip() if metadata.repository is not None else None
    if repository is not None and not REPOSITORY_URL_PATTERN.fullmatch(repository):
        raise ValueError("`repository` must be `https://github.com/<org>/<repo>`")
    snapshot = metadata.snapshot.strip() if metadata.snapshot is not None else None
    if snapshot is not None and not SHA_PATTERN.fullmatch(snapshot):
        raise ValueError("`snapshot` must be a full 40-character lowercase commit SHA")
    primary_index = metadata.primary_index.strip() if metadata.primary_index is not None else None
    if primary_index is not None and primary_index != config_index:
        raise ValueError(f"`primary_index` must be `{config_index}`")
    notes = single_line_text(metadata.notes, notes_field) if metadata.notes is not None else None

    lines = [
        title,
        "",
        f"- Team: {metadata.team}",
        f"- Repository reviewed: `{repository}`" if repository is not None else "- Repository reviewed: none",
        f"- Snapshot reviewed: `{snapshot}`" if snapshot is not None else "- Snapshot reviewed: none",
    ]
    if repository is not None and snapshot is not None:
        if notes is not None:
            raise ValueError(f"`{notes_field}` is only allowed when `repository` or `snapshot` is missing")
        index = primary_index or config_index
        lines.append(f"- Primary index reviewed: [`{index}`]({repository}/blob/{snapshot}/{index})")
    else:
        if notes is None:
            raise ValueError(f"`{notes_field}` is required when `repository` or `snapshot` is missing")
        lines.append("- Primary index reviewed: none")
        lines.append(f"- Notes about the snapshot: {notes}")
    return "\n".join(lines)


def bullet_list(value: object, field_name: str, *, minimum: int = 0, maximum: int | None = None) -> list[str]:
    """Validate a list of non-empty, single-line prose bullets."""
    if value is None:
        raise ValueError(f"`{field_name}` is required as a list of one-line strings")
    if not isinstance(value, list):
        raise ValueError(f"`{field_name}` must be a list of one-line strings")
    bullets: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"`{field_name}` must be a list of non-empty one-line strings")
        if "\n" in item:
            raise ValueError(f"`{field_name}` bullets must be single lines")
        bullets.append(item.strip())
    if len(bullets) < minimum:
        raise ValueError(f"`{field_name}` needs at least {minimum} bullet(s), got {len(bullets)}")
    if maximum is not None and len(bullets) > maximum:
        raise ValueError(f"`{field_name}` allows at most {maximum} bullet(s), got {len(bullets)}")
    return bullets


def _normalize_string_list(value: object, field_name: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"Structured patch field `{field_name}` must be a string list")
    return [item.strip() for item in value]


def _validate_status(value: object) -> str:
    if not isinstance(value, str) or value not in STATUSES:
        raise ValueError(f"Structured patch `status` must be one of: {', '.join(STATUSES)}")
    return value


def render_segment_block(
    seg_num: int,
    name: str,
    status: str,
    evidence_gaps: bool,
    evidence: list[str],
    verified_shortfalls: list[str],
    unverified_checks: list[str],
) -> str:
    lines = [
        f"### S{seg_num}: {name}",
        "",
        f"Status: {status}",
        "",
        f"Evidence gaps: {'yes' if evidence_gaps else 'no'}",
        "",
        f"**{HEADING_EVIDENCE}:**",
        "",
    ]
    lines.extend(f"- {bullet}" for bullet in evidence)
    if status in SHORTFALL_STATUSES or verified_shortfalls:
        lines.extend(["", f"**{HEADING_VERIFIED}:**", ""])
        lines.extend(f"- {bullet}" for bullet in verified_shortfalls)
    if evidence_gaps or unverified_checks:
        lines.extend(["", f"**{HEADING_UNVERIFIED}:**", ""])
        lines.extend(f"- {bullet}" for bullet in unverified_checks)
    return "\n".join(lines)


def apply_structured_segment_update(
    block: SegmentBlock,
    update: dict[str, object],
    expected_name: str,
) -> SegmentBlock:
    if not isinstance(update, dict):
        raise ValueError("Structured segment update must be an object")

    name = update.get("name", block.name)
    if name != expected_name:
        raise ValueError(f"Structured patch name must be `{expected_name}`")

    status = _validate_status(update.get("status", block.status))

    evidence_gaps = update.get("evidence_gaps", block.evidence_gaps)
    if not isinstance(evidence_gaps, bool):
        raise ValueError("Structured patch `evidence_gaps` must be a boolean")

    evidence = _normalize_string_list(update.get("evidence", block.evidence), "evidence")
    raw_verified = update.get("verified_shortfalls", block.verified_shortfalls)
    verified_shortfalls = _normalize_string_list(raw_verified, "verified_shortfalls") if raw_verified else []
    raw_unverified = update.get("unverified_checks", block.unverified_checks)
    unverified_checks = _normalize_string_list(raw_unverified, "unverified_checks") if raw_unverified else []

    markdown = render_segment_block(
        seg_num=block.seg_num,
        name=expected_name,
        status=status,
        evidence_gaps=evidence_gaps,
        evidence=evidence,
        verified_shortfalls=verified_shortfalls,
        unverified_checks=unverified_checks,
    )
    return SegmentBlock(
        seg_num=block.seg_num,
        name=expected_name,
        markdown=markdown,
        status=status,
        evidence_gaps=evidence_gaps,
        evidence=evidence,
        verified_shortfalls=verified_shortfalls,
        unverified_checks=unverified_checks,
    )


def fresh_segment_state_from_update(seg_num: int, expected_name: str, update: dict[str, object]) -> FreshSegmentState:
    if not isinstance(update, dict):
        raise ValueError("Fresh segment update must be an object")

    name = update.get("name", expected_name)
    if not isinstance(name, str) or name != expected_name:
        raise ValueError(f"Fresh segment name must be `{expected_name}`")

    if "status" not in update:
        raise ValueError("Fresh segment `status` is required")
    status = _validate_status(update["status"])

    evidence_gaps = update.get("evidence_gaps")
    if not isinstance(evidence_gaps, bool):
        raise ValueError("Fresh segment `evidence_gaps` must be a boolean")

    source = update.get("source")
    if source is not None and not isinstance(source, str):
        raise ValueError("Fresh segment `source` must be a string when present")
    checked_at = update.get("checked_at")
    if checked_at is not None and not isinstance(checked_at, str):
        raise ValueError("Fresh segment `checked_at` must be a string when present")
    notes_raw = update.get("notes", [])

    return FreshSegmentState(
        seg_num=seg_num,
        name=expected_name,
        status=status,
        evidence_gaps=evidence_gaps,
        evidence=_normalize_string_list(update.get("evidence", []), "evidence"),
        verified_shortfalls=_normalize_string_list(update.get("verified_shortfalls", []), "verified_shortfalls"),
        unverified_checks=_normalize_string_list(update.get("unverified_checks", []), "unverified_checks"),
        source=source,
        checked_at=checked_at,
        notes=_normalize_string_list(notes_raw, "notes") if notes_raw else [],
    )


def _diff_list(saved: list[str], fresh: list[str]) -> tuple[list[str], list[str]]:
    added = [item for item in fresh if item not in saved]
    removed = [item for item in saved if item not in fresh]
    return added, removed


def diff_segment_block(saved: SegmentBlock, fresh: FreshSegmentState) -> SegmentDiff:
    evidence_added, evidence_removed = _diff_list(saved.evidence, fresh.evidence)
    verified_added, verified_removed = _diff_list(saved.verified_shortfalls, fresh.verified_shortfalls)
    unverified_added, unverified_removed = _diff_list(saved.unverified_checks, fresh.unverified_checks)
    return SegmentDiff(
        status_changed=saved.status != fresh.status,
        evidence_gaps_changed=saved.evidence_gaps != fresh.evidence_gaps,
        evidence_added=evidence_added,
        evidence_removed=evidence_removed,
        verified_shortfalls_added=verified_added,
        verified_shortfalls_removed=verified_removed,
        unverified_checks_added=unverified_added,
        unverified_checks_removed=unverified_removed,
    )


def segment_block_to_dict(block: SegmentBlock, unresolved_evidence_gaps: list[str]) -> dict[str, object]:
    return {
        "name": block.name,
        "status": block.status,
        "evidence_gaps": block.evidence_gaps,
        "evidence": block.evidence,
        "verified_shortfalls": block.verified_shortfalls,
        "unverified_checks": block.unverified_checks,
        "unresolved_evidence_gaps": unresolved_evidence_gaps,
        "markdown": block.markdown,
    }


def fresh_segment_state_to_dict(state: FreshSegmentState) -> dict[str, object]:
    return {
        "name": state.name,
        "status": state.status,
        "evidence_gaps": state.evidence_gaps,
        "evidence": state.evidence,
        "verified_shortfalls": state.verified_shortfalls,
        "unverified_checks": state.unverified_checks,
        "source": state.source,
        "checked_at": state.checked_at,
        "notes": state.notes,
    }


def segment_diff_to_dict(diff: SegmentDiff) -> dict[str, object]:
    return {
        "status_changed": diff.status_changed,
        "evidence_gaps_changed": diff.evidence_gaps_changed,
        "evidence_added": diff.evidence_added,
        "evidence_removed": diff.evidence_removed,
        "verified_shortfalls_added": diff.verified_shortfalls_added,
        "verified_shortfalls_removed": diff.verified_shortfalls_removed,
        "unverified_checks_added": diff.unverified_checks_added,
        "unverified_checks_removed": diff.unverified_checks_removed,
    }


def _manual_review(blocks: dict[int, SegmentBlock]) -> str:
    return "yes" if any(block.evidence_gaps for block in blocks.values()) else "no"


def compute_report_impact(
    report: ParsedFeedbackReport,
    segment_defs: SegmentDefs,
    updated_blocks: dict[int, SegmentBlock],
) -> ReportImpact:
    saved = report.segment_blocks
    return ReportImpact(
        saved_counts=status_counts([saved[n].status for n in sorted(segment_defs) if n in saved]),
        predicted_counts=status_counts([updated_blocks[n].status for n in sorted(segment_defs)]),
        saved_manual_review_required=report.segments_table.manual_review_required or _manual_review(saved),
        predicted_manual_review_required=_manual_review(updated_blocks),
    )


def load_patch_payload(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Patch payload must be a JSON object")
    return payload


def fresh_segment_updates_from_payload(payload: dict[str, object]) -> dict[str, dict[str, object]]:
    updates = payload.get("segment_updates")
    if updates is None:
        updates = {
            key: value
            for key, value in payload.items()
            if isinstance(key, str) and SEGMENT_SELECTOR_PATTERN.fullmatch(key.strip())
        }
    if not isinstance(updates, dict) or not updates:
        raise ValueError("Fresh payload must be a non-empty `segment_updates` object or a top-level segment map")
    normalized: dict[str, dict[str, object]] = {}
    for selector, update in updates.items():
        if not isinstance(update, dict):
            raise ValueError(f"Fresh payload update for {selector} must be an object")
        normalized[selector] = update
    return normalized


def load_fresh_segment_updates(path: Path) -> dict[str, dict[str, object]]:
    return fresh_segment_updates_from_payload(load_patch_payload(path))


def render_overall_assessment(statuses: list[str], manual_review_required: bool) -> str:
    counts = status_counts(statuses)
    total = len(statuses)
    review_status = "pending review" if manual_review_required else "complete"
    return "\n".join(
        [
            f"- Met: `{counts['met']}/{total}`",
            f"- Partial: `{counts['partial']}/{total}`",
            f"- Missing: `{counts['missing']}/{total}`",
            f"- Unverified: `{counts['unverified']}/{total}`",
            f"- Automatic review status: `{review_status}`",
            "",
            ASSESSMENT_NOTE,
        ]
    )


def render_segments_table(segment_defs: SegmentDefs, segment_blocks: dict[int, SegmentBlock]) -> str:
    lines = [
        "| Segment | Status | Evidence gaps |",
        "|---------|--------|---------------|",
    ]
    for seg_num in sorted(segment_defs):
        block = segment_blocks[seg_num]
        label = segments_table_label(seg_num, segment_defs[seg_num]["name"])
        lines.append(f"| {label} | {block.status} | {'yes' if block.evidence_gaps else 'no'} |")
    lines.append(f"| Manual review required | {_manual_review(segment_blocks)} | |")
    return "\n".join(lines)


def render_unresolved_section(
    segment_defs: SegmentDefs,
    segment_blocks: dict[int, SegmentBlock],
    unresolved_gaps: dict[int, list[str]],
) -> str:
    gap_segments = [seg_num for seg_num, block in sorted(segment_blocks.items()) if block.evidence_gaps]
    if not gap_segments:
        return NO_REVIEW_TEXT

    lines: list[str] = []
    for seg_num in gap_segments:
        if not unresolved_gaps.get(seg_num):
            raise ValueError(f"Missing unresolved evidence gaps bullets for S{seg_num}")
        lines.append(f"- [S{seg_num}]({segment_anchor(seg_num, segment_defs[seg_num]['name'])})")
        lines.extend(f"  - {bullet}" for bullet in unresolved_gaps[seg_num])
    return "\n".join(lines)


def render_report(
    preamble: str,
    segment_defs: SegmentDefs,
    segment_blocks: dict[int, SegmentBlock],
    unresolved_gaps: dict[int, list[str]],
    summary_body: str,
    strengths_body: str,
    main_issues_body: str,
) -> str:
    ordered = [segment_blocks[seg_num] for seg_num in sorted(segment_defs)]
    sections = [
        preamble.strip(),
        "",
        HEADER_ASSESSMENT,
        "",
        render_overall_assessment([block.status for block in ordered], _manual_review(segment_blocks) == "yes"),
        "",
        HEADER_SEGMENTS,
        "",
        render_segments_table(segment_defs, segment_blocks),
        "",
        HEADER_UNRESOLVED,
        "",
        render_unresolved_section(segment_defs, segment_blocks, unresolved_gaps),
        "",
        HEADER_SUMMARY,
        "",
        summary_body.strip(),
        "",
        HEADER_STRENGTHS,
        "",
        strengths_body.strip(),
        "",
        HEADER_MAIN_ISSUES,
        "",
        main_issues_body.strip(),
        "",
        HEADER_DETAILS,
        "",
        "\n\n".join(block.markdown.strip() for block in ordered),
    ]
    return "\n".join(sections).rstrip() + "\n"


def parse_unresolved_section(unresolved_text: str, segment_defs: SegmentDefs) -> dict[int, list[str]]:
    if unresolved_text.strip() == NO_REVIEW_TEXT:
        return {}
    grouped: dict[int, list[str]] = {}
    current_seg: int | None = None
    for line in unresolved_text.splitlines():
        top_match = TOP_GAP_BULLET.match(line.strip())
        if top_match:
            seg_num = int(top_match.group(1))
            if seg_num not in segment_defs:
                raise ValueError(f"Unresolved evidence gaps reference unknown segment S{seg_num}")
            expected_anchor = segment_anchor(seg_num, segment_defs[seg_num]["name"])
            if top_match.group(2) != expected_anchor:
                raise ValueError(
                    f"S{seg_num} unresolved-evidence anchor is `{top_match.group(2)}`, expected `{expected_anchor}`"
                )
            grouped[seg_num] = []
            current_seg = seg_num
            continue
        if line.startswith("  - ") and current_seg is not None:
            grouped[current_seg].append(line[4:].strip())
            continue
        if line.strip():
            raise ValueError("Unresolved evidence gaps section contains malformed bullets")
    return grouped


def segment_selector_to_int(selector: str) -> int:
    match = re.fullmatch(r"S(\d+)", selector.strip(), re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid segment selector `{selector}`")
    return int(match.group(1))
