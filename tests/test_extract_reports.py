from __future__ import annotations

import csv
from pathlib import Path

from tests.report_builder import build_report
from tools.grader_tools.extract_reports import parse_team_name, run_extraction


def write_team(root: Path, team_dir: str, text: str | None) -> None:
    directory = root / team_dir
    directory.mkdir(parents=True)
    if text is not None:
        (directory / "feedback.md").write_text(text, encoding="utf-8")


def test_parse_team_name() -> None:
    assert parse_team_name("Team 3_12345_assignsubmission_file") == "Team 3"
    assert parse_team_name("misc") == "misc"


def test_extraction_writes_dev_md_and_csv(tmp_path: Path) -> None:
    feedback_dir = tmp_path / "A1" / "feedback" / "markdown"
    write_team(feedback_dir, "Team 10_1_assignsubmission_file", build_report("A1", team=10))
    write_team(feedback_dir, "Team 2_2_assignsubmission_file", build_report("A1", statuses={3: "partial", 4: "unverified"}, gaps={4}, team=2))
    write_team(feedback_dir, "Team 5_3_assignsubmission_file", None)
    write_team(feedback_dir, "Team 7_4_assignsubmission_file", "# not a report\n")
    dev = tmp_path / "A1" / "dev.md"
    release = tmp_path / "A1" / "feedback_release.csv"

    assert run_extraction("A1", feedback_dir, dev, release) == 0

    dev_lines = dev.read_text(encoding="utf-8").splitlines()
    rows = [line for line in dev_lines if line.startswith("| [Team") or line.startswith("| Team")]
    assert [row.split("|")[1].strip().split("]")[0].lstrip("[") for row in rows] == ["Team 2", "Team 5", "Team 7", "Team 10"]
    assert "met 7 · partial 1 · unverified 1" in rows[0]
    assert "feedback/markdown/Team%202_2_assignsubmission_file/feedback.md#unresolved-evidence-gaps" in rows[0]
    assert "feedback file is missing" in rows[1]
    assert "feedback file is malformed" in rows[2]
    assert "First shortfall. <br> - Second shortfall." in rows[3]

    with open(release, encoding="utf-8", newline="") as handle:
        records = list(csv.DictReader(handle, delimiter="|"))
    assert list(records[0]) == ["group", *[f"s{n}" for n in range(1, 10)], "manual_review", "feedback"]
    assert records[0]["s3"] == "partial"
    assert records[0]["s4"] == "unverified"
    assert records[0]["manual_review"] == "yes"
    assert records[1]["s1"] == ""
    assert records[3]["feedback"].startswith("- First shortfall.\\n")


def test_missing_input_dir(tmp_path: Path) -> None:
    assert run_extraction("A1", tmp_path / "nope", tmp_path / "dev.md", tmp_path / "out.csv") == 1
