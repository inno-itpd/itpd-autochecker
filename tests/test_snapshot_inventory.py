from __future__ import annotations

from pathlib import Path

import pytest

from scripts import snapshot_inventory as script
from scripts.snapshot_inventory import run
from tools.grader_tools.snapshot_inventory import (
    INVENTORY_FILENAME,
    SnapshotInventoryError,
    build_inventory,
    team_work_dir,
    write_inventory,
)

TEAM = "Team 2 - OK_10938_assignsubmission_file"


def make_snapshot(root: Path, files: dict[str, str], *, assignment: str = "A4") -> Path:
    snapshot = team_work_dir(root, assignment, TEAM) / "snapshot"
    snapshot.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        target = snapshot / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    return snapshot


SNAPSHOT_FILES = {
    "README.md": "# Project\n",
    "AGENTS.md": "# Agents\n",
    "CHANGELOG.md": "# Changelog\n",
    "mkdocs.yml": "site_name: Project\n",
    "docs/quality-requirements/README.md": "# QR index\n",
    "docs/quality-requirements/qr/QR-01.md": "# QR-01\n",
    "docs/quality-requirements/qr/QR-02.md": "# QR-02\n",
    "docs/quality-requirements/qr/QR-03.md": "# QR-03\n",
    "docs/functional-requirements/README.md": "# FR index\n",
    "docs/functional-requirements/fr/FR-001.md": "# FR-001\n",
    "docs/functional-requirements/fr/FR-002.md": "# FR-002\n",
    "docs/functional-requirements/fr/FR-003.md": "# FR-003\n",
    "docs/functional-requirements/fr/FR-004.md": "# FR-004\n",
    "docs/functional-requirements/fr/FR-005.md": "# FR-005\n",
    "docs/architecture/README.md": "# Architecture\n",
    "docs/architecture/adr/ADR-001.md": "# ADR-001\n",
    "docs/architecture/adr/ADR-002.md": "# ADR-002\n",
    "docs/architecture/adr/ADR-003.md": "# ADR-003\n",
    "docs/architecture/adr/TEMPLATE.md": "# Template\n",
    "reports/week-04/README.md": "# Week 4\n",
    "reports/week-03/meeting-report.md": "# Week 3\n",
    ".github/workflows/pages.yml": "name: Pages\n",
}


def test_build_inventory_counts_the_identifier_families(tmp_path: Path) -> None:
    snapshot = make_snapshot(tmp_path, SNAPSHOT_FILES)

    lines, counts = build_inventory(snapshot)
    text = "\n".join(lines)

    assert counts == {"QR": 3, "FR": 5, "ADR": 3}
    assert "- QR-nn files: 3" in text
    assert "- FR-nnn files: 5" in text
    assert "- ADR-nnn files: 3" in text
    assert "  - docs/architecture/adr/ADR-001.md" in text
    assert "docs/quality-requirements/qr/QR-01.md" in text
    assert "docs/functional-requirements/fr/FR-005.md" in text


def test_build_inventory_keeps_the_template_out_of_the_record_count(tmp_path: Path) -> None:
    snapshot = make_snapshot(tmp_path, SNAPSHOT_FILES)

    lines, counts = build_inventory(snapshot)

    assert counts["ADR"] == 3
    count_section = lines[lines.index("## Counts that decide segment minima") : lines.index("## docs/ tree")]
    assert not any("TEMPLATE.md" in line for line in count_section)


def test_build_inventory_lists_the_trees_workflows_and_site_configs(tmp_path: Path) -> None:
    snapshot = make_snapshot(tmp_path, SNAPSHOT_FILES)

    lines, _ = build_inventory(snapshot)
    text = "\n".join(lines)

    assert "- README.md" in lines
    assert "- AGENTS.md" in lines
    assert "- docs/" in lines
    assert "- reports/week-04/README.md" in lines
    assert "- .github/workflows/pages.yml" in lines
    assert "- mkdocs.yml" in lines


def test_build_inventory_skips_dot_entries(tmp_path: Path) -> None:
    files = dict(SNAPSHOT_FILES)
    files[".hidden/secret.md"] = "# Secret\n"
    snapshot = make_snapshot(tmp_path, files)

    lines, _ = build_inventory(snapshot)

    assert not any("secret" in line for line in lines)


def test_build_inventory_reports_an_absent_snapshot(tmp_path: Path) -> None:
    with pytest.raises(SnapshotInventoryError):
        build_inventory(tmp_path / "work" / TEAM / "snapshot")


def test_write_inventory_creates_the_digest_in_the_work_directory(tmp_path: Path) -> None:
    make_snapshot(tmp_path, SNAPSHOT_FILES)

    inventory = write_inventory(tmp_path, "A4", TEAM)

    assert inventory.path == team_work_dir(tmp_path, "A4", TEAM) / INVENTORY_FILENAME
    assert inventory.path.is_file()
    assert inventory.line_count == len(inventory.path.read_text(encoding="utf-8").splitlines())
    assert inventory.counts == {"QR": 3, "FR": 5, "ADR": 3}
    assert inventory.summary_lines[0].endswith(f"({inventory.line_count} lines)")
    assert inventory.summary_lines[1] == "counts: QR 3, FR 5, ADR 3"


def test_run_prints_counts_and_path_only(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    make_snapshot(tmp_path, SNAPSHOT_FILES)
    monkeypatch.setattr(script, "ROOT", tmp_path)
    printed: list[str] = []

    exit_code = run(["A4", TEAM], out=printed.append)

    assert exit_code == 0
    output = "\n".join(printed)
    assert "inventory:" in output
    assert "QR 3, FR 5, ADR 3" in output
    assert "# Project" not in output


def test_run_refuses_a_missing_snapshot(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(script, "ROOT", tmp_path)
    printed: list[str] = []

    exit_code = run(["A4", TEAM], out=printed.append)

    assert exit_code == 2
    assert printed[0].startswith("ERROR:")


def test_run_refuses_an_unknown_assignment(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(script, "ROOT", tmp_path)
    printed: list[str] = []

    exit_code = run(["A99", TEAM], out=printed.append)

    assert exit_code == 2
    assert "unknown assignment" in printed[0]
