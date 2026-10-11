from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.check_snapshot_links import run
from tools.grader_tools.snapshot_links import (
    SnapshotLinksError,
    check_snapshot_links,
    github_slug,
    parse_markdown,
)


def make_snapshot(tmp_path: Path, files: dict[str, str]) -> Path:
    work = tmp_path / "work"
    work.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        target = work / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    return work


@pytest.mark.parametrize(
    ("heading", "expected"),
    [
        ("Hello, World!", "hello-world"),
        ("`main` branch", "main-branch"),
        ("[Identifier Rules](#identifier-rules)", "identifier-rules"),
        ("**Bold** and _emphasis_", "bold-and-emphasis"),
        ("C++ & Rust", "c--rust"),
        ("S3 — Markdown CI", "s3--markdown-ci"),
        ("Привет, мир", "привет-мир"),
        ("foo_bar baz", "foo_bar-baz"),
        ("Hello 🎉", "hello-"),
        ("API v2.0", "api-v20"),
    ],
)
def test_github_slug_rules(heading: str, expected: str) -> None:
    assert github_slug(heading) == expected


def test_duplicate_headings_and_html_ids_are_anchors(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {"doc.md": "# Notes\n## Notes\n## Notes\n<h2 id=\"stable\">Notes</h2>\n"},
    )
    parsed = parse_markdown((work / "doc.md").read_text(encoding="utf-8"))
    assert parsed.anchors == frozenset({"notes", "notes-1", "notes-2", "stable"})


def test_broken_links_and_missing_anchors_report_file_line_and_target(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "README.md": (
                "# Root\n"
                "[guide](docs/guide.md#first-section)\n"
                "[gone](docs/nope.md)\n"
                "[bad anchor](docs/guide.md#missing)\n"
            ),
            "docs/guide.md": "# First Section\n",
        },
    )
    result = check_snapshot_links(work)
    assert [(finding.kind, finding.path, finding.line, finding.target) for finding in result.findings] == [
        ("broken-link", "README.md", 3, "docs/nope.md"),
        ("missing-anchor", "README.md", 4, "docs/guide.md#missing"),
    ]
    assert result.broken_links[0].detail == "missing file"
    assert result.missing_anchors[0].detail == "no such heading"
    assert result.has_findings


def test_relative_paths_resolve_from_the_linking_file(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/sub/page.md": (
                "## Local Heading\n"
                "[self](#local-heading)\n"
                "[up](../guide.md#other-heading)\n"
                "[root](/docs/guide.md#other-heading)\n"
                "[escaped](../../../outside.md)\n"
            ),
            "docs/guide.md": "## Other Heading\n",
        },
    )
    result = check_snapshot_links(work)
    assert [(finding.kind, finding.target, finding.detail) for finding in result.findings] == [
        ("broken-link", "../../../outside.md", "target is outside the snapshot"),
    ]


def test_percent_encoded_targets_resolve(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/with space.md": "## A Section\n",
            "README.md": "[s](docs/with%20space.md#a-section)\n",
        },
    )
    assert check_snapshot_links(work).findings == ()


def test_line_fragments_and_directory_links_are_not_anchor_errors(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/guide.md": "# Guide\n",
            "README.md": "[line](docs/guide.md#L12)\n[dir](docs/)\n",
        },
    )
    assert check_snapshot_links(work).findings == ()


def test_setext_and_raw_html_headings_supply_anchors(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "doc.md": "Setext Title\n===\n\n[ok](#setext-title)\n",
            "docs/decisions.md": '<h2 id="the-decision">The Decision</h2>\n',
            "README.md": "[d](docs/decisions.md#the-decision)\n",
        },
    )
    assert check_snapshot_links(work).findings == ()


def test_heading_formatting_is_stripped_before_slugging(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/guide.md": "## `main` and **bold** — done\n",
            "README.md": "[x](docs/guide.md#main-and-bold--done)\n",
        },
    )
    assert check_snapshot_links(work).findings == ()


def test_links_in_code_are_ignored(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "doc.md": (
                "```markdown\n[broken](missing.md#nope)\n```\n"
                "Use `[broken](missing.md#nope)` here.\n"
                "[real](target.md#here)\n"
            ),
            "target.md": "# Here\n",
        },
    )
    assert check_snapshot_links(work).findings == ()


def test_precut_anchors_are_listed_separately(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/research/gap-analysis.md": "## GAP-01\n\nThe gap.\n",
            "docs/product-vision.md": (
                "## VP-01: Old Title\n"
                "[still resolves](#vp-01-old-title)\n"
                "Prose mentions `#vp-02-old-title`.\n"
                "```text\n#alt-02-old-title\n```\n"
            ),
            "reports/week-02/README.md": "[gap](../../docs/research/gap-analysis.md#gap-01-reviewing)\n",
        },
    )
    result = check_snapshot_links(work)
    assert [finding.target for finding in result.missing_anchors] == [
        "../../docs/research/gap-analysis.md#gap-01-reviewing"
    ]
    assert sorted((finding.path, finding.line, finding.target) for finding in result.precut_anchors) == [
        ("docs/product-vision.md", 2, "#vp-01-old-title"),
        ("docs/product-vision.md", 3, "#vp-02-old-title"),
        ("docs/product-vision.md", 5, "#alt-02-old-title"),
        ("reports/week-02/README.md", 1, "#gap-01-reviewing"),
    ]


def test_precut_pattern_requires_exactly_two_digits() -> None:
    parsed = parse_markdown("see #gap-1-x, #gap-123-y, and #GAP-04-z\n")
    assert [occurrence.target for occurrence in parsed.precut] == ["#GAP-04-z"]


def test_issue_bodies_check_anchors_against_snapshot_headings(tmp_path: Path) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "docs/assumptions.md": "## ASM-01\n",
            "docs/research/gap-analysis.md": "## GAP-01\n",
        },
    )
    repo = "https://github.com/example/team-repo"
    issues = [
        {
            "number": 7,
            "body": (
                f"[ok]({repo}/blob/main/docs/assumptions.md#asm-01)\n"
                f"[bad]({repo}/blob/main/docs/assumptions.md#asm-99)\n"
                "[relative](docs/assumptions.md#asm-01)\n"
                "Old `#gap-01-some-title` left.\n"
                "[course](https://github.com/inno-itpd/itpd/blob/abc123/requirements/gap.md#nothing)\n"
                f"Bare {repo}/blob/main/docs/assumptions.md#asm-99\n"
            ),
        },
        {"number": 8, "title": "No body"},
    ]
    issues_path = tmp_path / "issues.json"
    issues_path.write_text(json.dumps(issues), encoding="utf-8")

    result = check_snapshot_links(work, issue_bodies_path=issues_path)
    assert result.issue_bodies_checked == 1
    assert result.issue_anchor_targets == 4
    assert [(finding.kind, finding.line, finding.target) for finding in result.findings] == [
        ("missing-anchor", 2, f"{repo}/blob/main/docs/assumptions.md#asm-99"),
        ("missing-anchor", 6, f"{repo}/blob/main/docs/assumptions.md#asm-99"),
        ("precut-anchor", 4, "#gap-01-some-title"),
    ]
    assert result.findings[0].path == f"{issues_path.as_posix()} #7"


def test_issue_body_anchor_to_a_missing_file_is_skipped(tmp_path: Path) -> None:
    work = make_snapshot(tmp_path, {"README.md": "# Root\n"})
    issues_path = tmp_path / "issues.json"
    issues_path.write_text(
        json.dumps([{"number": 1, "body": "[x](docs/nope.md#nope)\n"}]),
        encoding="utf-8",
    )
    result = check_snapshot_links(work, issue_bodies_path=issues_path)
    assert result.findings == ()
    assert result.issue_bodies_checked == 1
    assert result.issue_anchor_targets == 0


def test_malformed_issue_bodies_raise(tmp_path: Path) -> None:
    work = make_snapshot(tmp_path, {"README.md": "# Root\n"})
    issues_path = tmp_path / "issues.json"
    issues_path.write_text('{"not": "a list"}', encoding="utf-8")
    with pytest.raises(SnapshotLinksError, match="JSON array"):
        check_snapshot_links(work, issue_bodies_path=issues_path)


def test_run_exit_codes_and_summary(tmp_path: Path) -> None:
    work = make_snapshot(tmp_path, {"README.md": "# Clean\n"})
    lines: list[str] = []
    assert run([str(work)], out=lines.append) == 0
    assert lines[-1].endswith("no findings")

    (work / "docs").mkdir()
    (work / "docs" / "x.md").write_text("[gone](missing.md)\n", encoding="utf-8")
    lines = []
    assert run([str(work)], out=lines.append) == 1
    assert any(line.strip() == "broken relative links: 1" for line in lines)
    assert any("docs/x.md:1: missing.md (missing file)" in line for line in lines)

    lines = []
    assert run([str(tmp_path / "nope")], out=lines.append) == 2
    assert lines[0].startswith("ERROR:")


def test_run_missing_issue_bodies_exits_2(tmp_path: Path) -> None:
    work = make_snapshot(tmp_path, {"README.md": "# Clean\n"})
    lines: list[str] = []
    assert run([str(work), "--issue-bodies", str(tmp_path / "missing.json")], out=lines.append) == 2
    assert lines[0].startswith("ERROR:")
