from __future__ import annotations

from pathlib import Path
import struct
import zlib

import pytest

from scripts.image_info import run
from tools.grader_tools.image_info import (
    ImageInfoError,
    collect_image_info,
    read_image_info,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + chunk_type + data + struct.pack(">I", crc)


def write_png(
    path: Path,
    width: int = 640,
    height: int = 480,
    *,
    color_type: int = 2,
    trns: bool = False,
) -> Path:
    ihdr = struct.pack(">IIBBBBB", width, height, 8, color_type, 0, 0, 0)
    parts = [PNG_SIGNATURE, png_chunk(b"IHDR", ihdr)]
    if color_type == 3:
        parts.append(png_chunk(b"PLTE", b"\x00\x00\x00"))
    if trns:
        parts.append(png_chunk(b"tRNS", b"\x00"))
    parts.append(png_chunk(b"IDAT", b"\x00"))
    parts.append(png_chunk(b"IEND", b""))
    path.write_bytes(b"".join(parts))
    return path


def write_jpeg(
    path: Path,
    width: int = 1024,
    height: int = 768,
    *,
    sof_marker: int = 0xC0,
) -> Path:
    app0 = b"JFIF\x00\x01\x02\x00\x00\x01\x00\x01\x00\x00"
    app1 = b"Exif\x00\x00metadata"
    comment = b"a comment"
    dqt = b"\x00" + bytes(64)
    frame = struct.pack(">BHHB", 8, height, width, 1) + b"\x01\x11\x00"
    segments = [
        b"\xff\xd8",
        b"\xff\xe0" + struct.pack(">H", len(app0) + 2) + app0,
        b"\xff\xe1" + struct.pack(">H", len(app1) + 2) + app1,
        b"\xff\xfe" + struct.pack(">H", len(comment) + 2) + comment,
        b"\xff\xdb" + struct.pack(">H", len(dqt) + 2) + dqt,
        bytes([0xFF, sof_marker]) + struct.pack(">H", len(frame) + 2) + frame,
        b"\xff\xd9",
    ]
    path.write_bytes(b"".join(segments))
    return path


def test_reads_png_dimensions_size_and_opacity(tmp_path: Path) -> None:
    path = write_png(tmp_path / "board.png", 800, 600)
    info = read_image_info(path)
    assert (info.format, info.width, info.height, info.byte_size, info.transparent) == (
        "PNG",
        800,
        600,
        path.stat().st_size,
        False,
    )
    assert info.dimensions == "800x600"
    assert info.summary_line == f"{path.as_posix()}: PNG 800x600, {info.byte_size} bytes"
    assert "transparent" not in info.summary_line


@pytest.mark.parametrize("color_type", [4, 6])
def test_alpha_png_color_types_are_transparent(tmp_path: Path, color_type: int) -> None:
    info = read_image_info(write_png(tmp_path / "alpha.png", color_type=color_type))
    assert info.transparent is True
    assert info.summary_line.endswith(", transparent")


def test_palette_png_transparency_follows_the_trns_chunk(tmp_path: Path) -> None:
    transparent = read_image_info(write_png(tmp_path / "with-trns.png", color_type=3, trns=True))
    opaque = read_image_info(write_png(tmp_path / "without-trns.png", color_type=3, trns=False))
    assert transparent.transparent is True
    assert opaque.transparent is False


def test_reads_jpeg_dimensions_past_metadata_segments(tmp_path: Path) -> None:
    path = write_jpeg(tmp_path / "screenshot.jpg", 1280, 720)
    info = read_image_info(path)
    assert (info.format, info.width, info.height, info.byte_size, info.transparent) == (
        "JPEG",
        1280,
        720,
        path.stat().st_size,
        False,
    )
    assert info.summary_line == f"{path.as_posix()}: JPEG 1280x720, {info.byte_size} bytes"


@pytest.mark.parametrize("sof_marker", [0xC1, 0xC2])
def test_reads_progressive_and_extended_jpegs(tmp_path: Path, sof_marker: int) -> None:
    info = read_image_info(write_jpeg(tmp_path / "photo.jpg", sof_marker=sof_marker))
    assert (info.format, info.width, info.height) == ("JPEG", 1024, 768)


def test_format_is_detected_from_content_not_the_extension(tmp_path: Path) -> None:
    png_in_a_jpg_name = write_png(tmp_path / "diagram.jpg", 320, 200)
    assert read_image_info(png_in_a_jpg_name).format == "PNG"


def test_rejects_unsupported_and_truncated_files(tmp_path: Path) -> None:
    text = tmp_path / "notes.txt"
    text.write_bytes(b"just text")
    with pytest.raises(ImageInfoError, match="not a PNG or JPEG"):
        read_image_info(text)

    truncated_png = tmp_path / "cut.png"
    truncated_png.write_bytes(PNG_SIGNATURE)
    with pytest.raises(ImageInfoError, match="truncated PNG header"):
        read_image_info(truncated_png)

    truncated_jpeg = tmp_path / "cut.jpg"
    truncated_jpeg.write_bytes(b"\xff\xd8")
    with pytest.raises(ImageInfoError, match="no JPEG frame header"):
        read_image_info(truncated_jpeg)

    directory = tmp_path / "folder"
    directory.mkdir()
    with pytest.raises(ImageInfoError, match="not a file"):
        read_image_info(directory)

    with pytest.raises(ImageInfoError, match="not a file"):
        read_image_info(tmp_path / "gone.png")


def test_collect_keeps_good_files_and_reports_errors(tmp_path: Path) -> None:
    good = write_png(tmp_path / "good.png")
    bad = tmp_path / "bad.png"
    bad.write_bytes(b"nope")
    result = collect_image_info([good, bad])
    assert [image.path for image in result.images] == [good]
    assert len(result.errors) == 1
    assert result.ok is False
    assert result.summary_lines[-2].startswith("ERROR: ")
    assert result.summary_lines[-1] == "result: 1 read, 1 failed"


def test_run_prints_each_file_and_returns_exit_codes(tmp_path: Path) -> None:
    good = write_png(tmp_path / "good.png", 320, 200)
    transparent = write_png(tmp_path / "alpha.png", color_type=6)
    bad = tmp_path / "bad.png"
    bad.write_bytes(b"nope")

    lines: list[str] = []
    assert run([str(good), str(transparent)], out=lines.append) == 0
    assert "PNG 320x200" in lines[0]
    assert lines[1].endswith(", transparent")
    assert lines[-1] == "result: 2 image(s) read"

    lines = []
    assert run([str(good), str(bad)], out=lines.append) == 1
    assert lines[1].startswith("ERROR: ")
    assert lines[-1] == "result: 1 read, 1 failed"

    with pytest.raises(SystemExit):
        run([])
