from __future__ import annotations

import json
from pathlib import Path
import re

import pytest

from scripts.collect_github_evidence import run as collect_run
from tools.grader_tools.live_evidence import (
    EDIT_FIELDS,
    ISSUE_FIELDS,
    ISSUE_LIMIT,
    LABEL_FIELDS,
    LABEL_LIMIT,
    PATH_COMMIT_FIELDS,
    PR_FIELDS,
    PR_LIMIT,
    RUN_FIELDS,
    RUN_LIMIT,
    RUN_SHA_FIELDS,
    USER_CONTENT_EDITS_QUERY,
    LiveEvidenceError,
    LiveEvidenceResult,
    collect_github_evidence,
)
from tools.grader_tools.live_evidence import (
    comments_command,
    commits_command,
    edits_command,
    issues_command,
    labels_command,
    path_commits_command,
    prs_command,
    runs_main_command,
    runs_sha_command,
    timeline_command,
)
from tools.grader_tools.submission_pdf import CommandResult

ROOT = Path(__file__).resolve().parents[1]
TEAM = "Team 1 - Absolute Cinema_10937_assignsubmission_file"
REPO = "example-org/example-repo"
SHA = "1234567890abcdef1234567890abcdef12345678"


class FakeGh:
    def __init__(self, responses: dict[tuple[str, ...], str]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, ...]] = []

    def __call__(self, args: list[str]) -> CommandResult:
        key = tuple(args)
        self.calls.append(key)
        if key not in self.responses:
            raise AssertionError(f"unexpected gh call: {key}")
        return CommandResult(returncode=0, stdout=self.responses[key], stderr="")


def write_pdf_info(tmp_path: Path, repo: object = REPO, sha: object = SHA) -> Path:
    scratch = tmp_path / "itpd-assignments-feedback" / "A2" / "work" / TEAM
    scratch.mkdir(parents=True)
    (scratch / "pdf-info.json").write_text(
        json.dumps({"assignment": "A2", "team_dir": TEAM, "repo": repo, "sha": sha}),
        encoding="utf-8",
    )
    return scratch


def base_responses() -> dict[tuple[str, ...], str]:
    return {
        tuple(labels_command(REPO)): json.dumps(
            [{"name": "task", "description": "", "ignored": "x"}],
        ),
        tuple(issues_command(REPO)): json.dumps([{"number": 50, "title": "Edit the root README"}]),
        tuple(prs_command(REPO)): json.dumps([{"number": 51, "title": "Edit the root README"}]),
        tuple(runs_main_command(REPO)): json.dumps([{"databaseId": 1, "conclusion": "success"}]),
        tuple(runs_sha_command(REPO, SHA)): json.dumps(
            {
                "total_count": 1,
                "workflow_runs": [
                    {
                        "name": "Markdown check",
                        "event": "push",
                        "conclusion": "success",
                        "html_url": "https://example.com/run/1",
                        "ignored": "x",
                    }
                ],
            }
        ),
        tuple(commits_command(REPO, SHA)): json.dumps([{"sha": "a" * 40, "commit": {"message": "one"}}]),
    }


def test_collect_writes_the_base_dumps_and_a_compact_summary(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(base_responses()))

    assert json.loads((scratch / "labels.json").read_text(encoding="utf-8")) == [
        {"name": "task", "description": "", "ignored": "x"}
    ]
    assert json.loads((scratch / "issues.json").read_text(encoding="utf-8")) == [
        {"number": 50, "title": "Edit the root README"}
    ]
    assert json.loads((scratch / "prs.json").read_text(encoding="utf-8")) == [
        {"number": 51, "title": "Edit the root README"}
    ]
    assert json.loads((scratch / "runs_main.json").read_text(encoding="utf-8")) == [
        {"databaseId": 1, "conclusion": "success"}
    ]
    assert json.loads((scratch / "commits.json").read_text(encoding="utf-8")) == [
        {"sha": "a" * 40, "commit": {"message": "one"}}
    ]
    assert (scratch / "labels.json").stat().st_mode & 0o777 == 0o600

    runs_sha = json.loads((scratch / "runs_sha.json").read_text(encoding="utf-8"))
    assert runs_sha == [
        {
            "name": "Markdown check",
            "event": "push",
            "conclusion": "success",
            "html_url": "https://example.com/run/1",
        }
    ]
    assert list(runs_sha[0]) == list(RUN_SHA_FIELDS)

    assert [file.label for file in result.files] == [
        "labels",
        "issues",
        "prs",
        "runs (main)",
        "runs (sha)",
        "commits",
    ]
    assert [file.count for file in result.files] == [1, 1, 1, 1, 1, 1]
    summary = "\n".join(result.summary_lines)
    assert "itpd-assignments-feedback/A2/work/" in summary
    assert "labels: 1 -> itpd-assignments-feedback/A2/work/" in summary
    assert f"repo: {REPO} @ {SHA}" in summary
    assert '{"name"' not in summary
    assert '"workflow_runs"' not in summary


def test_collect_uses_the_encoded_field_lists(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    runner = FakeGh(base_responses())
    collect_github_evidence("A2", TEAM, tmp_path, runner=runner)

    json_fields = {call[call.index("--json") + 1] for call in runner.calls if "--json" in call}
    assert json_fields == {
        ",".join(LABEL_FIELDS),
        ",".join(ISSUE_FIELDS),
        ",".join(PR_FIELDS),
        ",".join(RUN_FIELDS),
    }
    limits = {call[call.index("--limit") + 1] for call in runner.calls if "--limit" in call}
    assert limits == {str(LABEL_LIMIT), str(ISSUE_LIMIT), str(PR_LIMIT), str(RUN_LIMIT)}


def test_collect_merges_paginated_commit_pages(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(commits_command(REPO, SHA))] = json.dumps([{"sha": "1" * 40}]) + "\n" + json.dumps(
        [{"sha": "2" * 40}, {"sha": "3" * 40}]
    )
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))

    commits = json.loads((scratch / "commits.json").read_text(encoding="utf-8"))
    assert [commit["sha"] for commit in commits] == ["1" * 40, "2" * 40, "3" * 40]
    assert next(file for file in result.files if file.label == "commits").count == 3


def test_collect_merges_paginated_run_pages(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(runs_sha_command(REPO, SHA))] = json.dumps(
        {"total_count": 2, "workflow_runs": [{"name": "Markdown check", "conclusion": "success"}]}
    ) + json.dumps({"total_count": 2, "workflow_runs": [{"name": "Link check", "conclusion": "failure"}]})
    collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))

    runs = json.loads((scratch / "runs_sha.json").read_text(encoding="utf-8"))
    assert [run["name"] for run in runs] == ["Markdown check", "Link check"]


def test_collect_issue_drilldowns(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(comments_command(REPO, 11))] = json.dumps([{"body": "first"}]) + json.dumps([{"body": "second"}])
    responses[tuple(timeline_command(REPO, 11))] = json.dumps([{"event": "labeled", "label": {"name": "task"}}])
    responses[tuple(edits_command(REPO, 11))] = json.dumps(
        {
            "data": {
                "repository": {
                    "issue": {
                        "lastEditedAt": "2026-10-10T20:00:00Z",
                        "userContentEdits": {"nodes": [{"editedAt": "2026-10-10T20:00:00Z", "diff": "-a\n+b"}]},
                    }
                }
            }
        }
    )
    result = collect_github_evidence("A2", TEAM, tmp_path, issues=[11, 11], runner=FakeGh(responses))

    assert json.loads((scratch / "issues" / "11.comments.json").read_text(encoding="utf-8")) == [
        {"body": "first"},
        {"body": "second"},
    ]
    assert json.loads((scratch / "issues" / "11.timeline.json").read_text(encoding="utf-8")) == [
        {"event": "labeled", "label": {"name": "task"}}
    ]
    assert json.loads((scratch / "issues" / "11.edits.json").read_text(encoding="utf-8")) == {
        "lastEditedAt": "2026-10-10T20:00:00Z",
        "userContentEdits": {"nodes": [{"editedAt": "2026-10-10T20:00:00Z", "diff": "-a\n+b"}]},
    }
    assert [file.label for file in result.files] == [
        "labels",
        "issues",
        "prs",
        "runs (main)",
        "runs (sha)",
        "commits",
        "issue 11 comments",
        "issue 11 timeline",
        "issue 11 edits",
    ]
    assert [file.count for file in result.files[-3:]] == [2, 1, 1]
    assert "issue 11 comments: 2 -> itpd-assignments-feedback/A2/work/" in "\n".join(result.summary_lines)


def test_collect_issue_edits_reports_graphql_errors(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(comments_command(REPO, 11))] = json.dumps([])
    responses[tuple(timeline_command(REPO, 11))] = json.dumps([])
    responses[tuple(edits_command(REPO, 11))] = json.dumps(
        {"data": None, "errors": [{"message": "Could not resolve to an issue"}]}
    )
    with pytest.raises(LiveEvidenceError, match="Could not resolve to an issue"):
        collect_github_evidence("A2", TEAM, tmp_path, issues=[11], runner=FakeGh(responses))


def test_collect_path_history_projects_sha_date_and_subject(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(path_commits_command(REPO, SHA, "reports/week-02/README.md"))] = json.dumps(
        [
            {
                "sha": "b" * 40,
                "commit": {
                    "committer": {"date": "2026-10-09T10:00:00Z"},
                    "message": "Write the week report\n\nDetails in the body.",
                },
            }
        ]
    )
    result = collect_github_evidence(
        "A2", TEAM, tmp_path, paths=["reports/week-02/README.md"], runner=FakeGh(responses)
    )

    payload = json.loads(
        (scratch / "paths" / "reports" / "week-02" / "README.md.json").read_text(encoding="utf-8")
    )
    assert payload == [{"sha": "b" * 40, "date": "2026-10-09T10:00:00Z", "message": "Write the week report"}]
    assert list(payload[0]) == list(PATH_COMMIT_FIELDS)
    assert result.files[-1].label == "path reports/week-02/README.md commits"
    assert result.files[-1].count == 1


def test_collect_rejects_path_traversal(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="invalid repository path"):
        collect_github_evidence("A2", TEAM, tmp_path, paths=["../outside.md"], runner=FakeGh(base_responses()))


def test_collect_rejects_non_positive_issue_numbers(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="invalid issue number"):
        collect_github_evidence("A2", TEAM, tmp_path, issues=[0], runner=FakeGh(base_responses()))


def test_collect_requires_the_scratch_metadata(tmp_path: Path) -> None:
    with pytest.raises(LiveEvidenceError, match="fetch_team_snapshot"):
        collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh({}))


def test_collect_stops_without_a_snapshot_repo(tmp_path: Path) -> None:
    write_pdf_info(tmp_path, repo=None, sha=None)
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh({}))

    assert result.skipped is True
    assert result.files == ()
    assert result.repo is None
    assert result.sha is None
    summary = "\n".join(result.summary_lines)
    assert "pdf-info.json has no repository and SHA" in summary
    assert "result: skipped (no snapshot)" in summary
    assert "--repo org/repo" in summary


def test_collect_cli_exits_zero_on_a_skipped_snapshot() -> None:
    skipped = LiveEvidenceResult(
        assignment="A2",
        team_dir=TEAM,
        repo=None,
        sha=None,
        work_dir=Path("work"),
        files=(),
        summary_lines=("result: skipped (no snapshot)",),
        skipped=True,
    )
    lines: list[str] = []
    status = collect_run(["A2", TEAM], out=lines.append, collect=lambda *args, **kwargs: skipped)

    assert status == 0
    assert lines == ["result: skipped (no snapshot)"]


def test_collect_rejects_unknown_assignment(tmp_path: Path) -> None:
    with pytest.raises(LiveEvidenceError, match="unknown assignment"):
        collect_github_evidence("A9", TEAM, tmp_path, runner=FakeGh({}))


def test_collect_raises_on_gh_failures_and_invalid_json(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(labels_command(REPO))] = "not json"
    with pytest.raises(LiveEvidenceError, match="invalid JSON"):
        collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))
    assert not (scratch / "labels.json").exists()


def test_collect_reports_gh_exit_codes(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="gh label list failed: HTTP 403"):
        collect_github_evidence(
            "A2",
            TEAM,
            tmp_path,
            runner=lambda command: CommandResult(returncode=1, stdout="", stderr="HTTP 403"),
        )


def _a2_step5() -> str:
    text = (ROOT / "A2" / "grading_prompt.md").read_text(encoding="utf-8")
    section = text.split("## Assignment-specific procedure deltas", 1)[1]
    step = section.split("5. Collect the live evidence", 1)[1].split("6. Judge every issue", 1)[0]
    return re.sub(r" +", " ", re.sub(r"\\\n\s+", " ", step))


def test_a2_step5_field_lists_match_the_collector() -> None:
    step5 = _a2_step5()
    assert f'gh label list --repo "$REPO" --limit {LABEL_LIMIT} --json {",".join(LABEL_FIELDS)}' in step5
    assert f'gh issue list --repo "$REPO" --state all --limit {ISSUE_LIMIT} --json {",".join(ISSUE_FIELDS)}' in step5
    assert f'gh pr list --repo "$REPO" --state all --limit {PR_LIMIT} --json {",".join(PR_FIELDS)}' in step5
    assert f'gh run list --repo "$REPO" --branch main --limit {RUN_LIMIT} --json {",".join(RUN_FIELDS)}' in step5
    sha_fields = ", ".join("." + field for field in RUN_SHA_FIELDS)
    assert f"--jq '.workflow_runs[] | [{sha_fields}] | @tsv'" in step5
    assert f".[] | [.{PATH_COMMIT_FIELDS[0]}, .commit.committer.date, (.commit.message | split(\"\\n\")[0])] | @tsv" in step5
    assert f"userContentEdits(first: 100) {{ nodes {{ {' '.join(EDIT_FIELDS)} }} }}" in USER_CONTENT_EDITS_QUERY
    assert f"userContentEdits(first: 100) {{ nodes {{ {' '.join(EDIT_FIELDS)} }} }}" in step5
