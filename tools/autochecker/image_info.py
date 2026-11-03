"""Read PNG and JPEG pixel metadata without ImageMagick.

Grader sessions sometimes run where ``identify`` is unavailable, so this module
reads the pixel dimensions, the byte size, and PNG transparency directly from
the file headers.  The format is detected from the content, never the file
name.  A PNG is transparent when its color type carries an alpha channel
(grayscale+alpha or RGBA) or when it holds a ``tRNS`` chunk (palette,
grayscale, or truecolor with a transparent color).  JPEG has no alpha channel,
so a JPEG is never transparent.

``scripts/image_info.py`` prints one line per file; the exit code is 0 when
every file was read, 1 when one or more failed, and 2 when the arguments are
unusable.
"""

from __future__ import annotations

import struct
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_IHDR = b"IHDR"
PNG_TRANSPARENCY = b"tRNS"
PNG_ALPHA_COLOR_TYPES = frozenset({4, 6})
JPEG_SOI = b"\xff\xd8"
JPEG_EOI = 0xD9
JPEG_SOS = 0xDA
# 0xC0-0xCF are SOF markers apart from DHT (0xC4), JPG (0xC8), and DAC (0xCC).
JPEG_SOF_MARKERS = frozenset(range(0xC0, 0xD0)) - {0xC4, 0xC8, 0xCC}
JPEG_STANDALONE_MARKERS = frozenset({0x01, 0xD8}) | frozenset(range(0xD0, 0xD8))


class ImageInfoError(RuntimeError):
    """The file is missing, unreadable, or not a decodable PNG or JPEG."""


@dataclass(frozen=True)
class ImageInfo:
    path: Path
    format: str
    width: int
    height: int
    byte_size: int
    transparent: bool

    @property
    def dimensions(self) -> str:
        return f"{self.width}x{self.height}"

    @property
    def summary_line(self) -> str:
        flag = ", transparent" if self.transparent else ""
        return f"{self.path.as_posix()}: {self.format} {self.dimensions}, {self.byte_size} bytes{flag}"


@dataclass(frozen=True)
class ImageInfoResult:
    images: tuple[ImageInfo, ...]
    errors: tuple[str, ...]
    summary_lines: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors

    @property
    def transparent_images(self) -> tuple[ImageInfo, ...]:
        return tuple(image for image in self.images if image.transparent)


def read_image_info(path: Path) -> ImageInfo:
    """Return the metadata of one PNG or JPEG file, or raise ImageInfoError."""
    source = Path(path)
    try:
        if not source.is_file():
            raise ImageInfoError(f"{source.as_posix()}: not a file")
        byte_size = source.stat().st_size
        with source.open("rb") as handle:
            magic = handle.read(8)
            if magic.startswith(JPEG_SOI):
                handle.seek(0)
                width, height = _read_jpeg(handle, source)
                return ImageInfo(source, "JPEG", width, height, byte_size, transparent=False)
            if magic.startswith(PNG_SIGNATURE):
                handle.seek(0)
                width, height, transparent = _read_png(handle, source)
                return ImageInfo(source, "PNG", width, height, byte_size, transparent)
    except OSError as exc:
        raise ImageInfoError(f"{source.as_posix()}: cannot read: {exc}") from exc
    raise ImageInfoError(f"{source.as_posix()}: not a PNG or JPEG file")


def collect_image_info(paths: Sequence[Path]) -> ImageInfoResult:
    images: list[ImageInfo] = []
    errors: list[str] = []
    lines: list[str] = []
    for path in paths:
        try:
            image = read_image_info(path)
        except ImageInfoError as exc:
            errors.append(str(exc))
            lines.append(f"ERROR: {exc}")
            continue
        images.append(image)
        lines.append(image.summary_line)
    if errors:
        lines.append(f"result: {len(images)} read, {len(errors)} failed")
    else:
        lines.append(f"result: {len(images)} image(s) read")
    return ImageInfoResult(tuple(images), tuple(errors), tuple(lines))


def _read_png(handle: BinaryIO, path: Path) -> tuple[int, int, bool]:
    if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
        raise ImageInfoError(f"{path.as_posix()}: not a PNG file")
    header = handle.read(8)
    if len(header) != 8:
        raise ImageInfoError(f"{path.as_posix()}: truncated PNG header")
    length, chunk_type = struct.unpack(">I4s", header)
    if chunk_type != PNG_IHDR or length != 13:
        raise ImageInfoError(f"{path.as_posix()}: PNG does not start with an IHDR chunk")
    ihdr = handle.read(13)
    if len(ihdr) != 13:
        raise ImageInfoError(f"{path.as_posix()}: truncated PNG IHDR chunk")
    width, height, _depth, color_type = struct.unpack(">IIBB", ihdr[:10])
    if width < 1 or height < 1:
        raise ImageInfoError(f"{path.as_posix()}: PNG IHDR has no dimensions")
    handle.seek(4, 1)
    transparent = color_type in PNG_ALPHA_COLOR_TYPES or _png_has_transparency_chunk(handle, path)
    return width, height, transparent


def _png_has_transparency_chunk(handle: BinaryIO, path: Path) -> bool:
    while True:
        header = handle.read(8)
        if not header:
            return False
        if len(header) != 8:
            raise ImageInfoError(f"{path.as_posix()}: truncated PNG chunk header")
        length, chunk_type = struct.unpack(">I4s", header)
        if chunk_type == PNG_TRANSPARENCY:
            return True
        if chunk_type == b"IEND":
            return False
        handle.seek(length + 4, 1)


def _read_jpeg(handle: BinaryIO, path: Path) -> tuple[int, int]:
    if handle.read(len(JPEG_SOI)) != JPEG_SOI:
        raise ImageInfoError(f"{path.as_posix()}: not a JPEG file")
    while True:
        byte = handle.read(1)
        while byte and byte != b"\xff":
            byte = handle.read(1)
        if not byte:
            raise ImageInfoError(f"{path.as_posix()}: no JPEG frame header found")
        marker = handle.read(1)
        while marker == b"\xff":
            marker = handle.read(1)
        if not marker:
            raise ImageInfoError(f"{path.as_posix()}: truncated JPEG marker")
        code = marker[0]
        if code == 0x00 or code in JPEG_STANDALONE_MARKERS:
            continue
        if code == JPEG_EOI:
            raise ImageInfoError(f"{path.as_posix()}: no JPEG frame header before end of image")
        length_bytes = handle.read(2)
        if len(length_bytes) != 2:
            raise ImageInfoError(f"{path.as_posix()}: truncated JPEG segment")
        length = struct.unpack(">H", length_bytes)[0]
        if length < 2:
            raise ImageInfoError(f"{path.as_posix()}: invalid JPEG segment length")
        if code in JPEG_SOF_MARKERS:
            frame = handle.read(5)
            if len(frame) != 5:
                raise ImageInfoError(f"{path.as_posix()}: truncated JPEG frame header")
            _precision, height, width = struct.unpack(">BHH", frame)
            if width < 1 or height < 1:
                raise ImageInfoError(f"{path.as_posix()}: JPEG frame has no dimensions")
            return width, height
        if code == JPEG_SOS:
            raise ImageInfoError(f"{path.as_posix()}: JPEG scan data before frame header")
        handle.seek(length - 2, 1)
