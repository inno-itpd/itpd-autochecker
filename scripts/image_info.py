#!/usr/bin/env python3
"""Print PNG and JPEG pixel dimensions, byte size, and PNG transparency.

The metadata is read straight from the file headers, so it works where
ImageMagick's ``identify`` is not installed.  Transparent PNGs are flagged.
The exit code is 0 when every file was read, 1 when one or more failed, and 2
when the arguments are unusable.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.image_info import collect_image_info


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Report pixel dimensions, byte size, and transparency for PNG and JPEG files "
            "by reading their headers, without ImageMagick. "
            "Transparent PNGs carry a `transparent` flag."
        )
    )
    parser.add_argument("files", nargs="+", metavar="FILE", help="PNG or JPEG file to inspect")
    return parser


def run(argv: Sequence[str], *, out: Callable[[str], None] = print) -> int:
    args = build_parser().parse_args(argv)
    result = collect_image_info([Path(name) for name in args.files])
    for line in result.summary_lines:
        out(line)
    return 0 if result.ok else 1


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
