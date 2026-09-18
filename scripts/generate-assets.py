#!/usr/bin/env python3
"""Generate Sequoia-light wallpapers and Omarchy preview images (stdlib only)."""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path

THEME = Path(__file__).resolve().parents[1]
BACKGROUNDS = THEME / "backgrounds"

# Apple HIG / Sequoia light
BLUE = (0, 122, 255)
CLOSE = (255, 95, 87)
MINIMIZE = (254, 188, 46)
ZOOM = (40, 200, 64)
LABEL = (29, 29, 31)
CHROME = (229, 229, 234)
WINDOW = (255, 255, 255)
DESK = (242, 242, 247)
GRAY = (199, 199, 204)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def mix(c0: tuple[int, int, int], c1: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))

    return (
        int(lerp(c0[0], c1[0], t)),
        int(lerp(c0[1], c1[1], t)),
        int(lerp(c0[2], c1[2], t)),
    )


def png_rgb(path: Path, width: int, height: int, pixels: bytes) -> None:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = bytearray()
    stride = width * 3

    for y in range(height):
        raw.append(0)
        start = y * stride
        raw.extend(pixels[start : start + stride])

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    payload = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    path.write_bytes(payload)


def wallpaper_sequoia(width: int, height: int) -> bytes:
    """Soft Sequoia-like daylight: pale sky, horizon haze, quiet hills."""
    sky_top = (186, 214, 236)
    sky_mid = (214, 228, 240)
    haze = (236, 239, 244)
    ground = (226, 228, 234)
    hill_a = (196, 210, 222)
    hill_b = (208, 218, 228)
    sun = (255, 248, 232)
    buf = bytearray(width * height * 3)
    cx, cy = int(width * 0.72), int(height * 0.22)
    radius = width * 0.42

    for y in range(height):
        fy = y / (height - 1)

        if fy < 0.42:
            base = mix(sky_top, sky_mid, fy / 0.42)
        elif fy < 0.62:
            base = mix(sky_mid, haze, (fy - 0.42) / 0.20)
        else:
            base = mix(haze, ground, (fy - 0.62) / 0.38)

        for x in range(width):
            nx = x / max(1, width - 1)
            ridge = 0.64 + 0.025 * math.sin(nx * math.pi * 2.2) + 0.012 * math.sin(nx * math.pi * 5.1)
            color = base

            if fy > ridge:
                t = min(1.0, (fy - ridge) * 7)
                color = mix(color, hill_a, t * 0.4)

            if fy > 0.80:
                t = min(1.0, (fy - 0.80) / 0.20)
                color = mix(color, hill_b, t * 0.75)

            dx = x - cx
            dy = y - cy
            d = (dx * dx + dy * dy) ** 0.5 / radius
            if d < 1.0:
                color = mix(color, sun, (1.0 - d) ** 2 * 0.45)

            i = (y * width + x) * 3
            buf[i : i + 3] = bytes(color)

    return bytes(buf)


def wallpaper_sonoma_chrome(width: int, height: int) -> bytes:
    """Quiet Sonoma desktop: off-white field, light gray chrome wash, System Blue glow."""
    top = (245, 245, 247)
    bottom = (229, 229, 234)
    glow = (179, 215, 255)
    buf = bytearray(width * height * 3)
    cx, cy = width // 2, int(height * 0.18)
    radius = width * 0.55

    for y in range(height):
        fy = y / (height - 1)
        row = mix(top, bottom, fy ** 1.15)

        for x in range(width):
            dx = (x - cx) / radius
            dy = (y - cy) / radius
            d = (dx * dx + dy * dy) ** 0.5
            color = mix(row, glow, max(0.0, 1.0 - d) ** 1.8 * 0.28)
            i = (y * width + x) * 3
            buf[i : i + 3] = bytes(color)

    return bytes(buf)


def fill(buf: bytearray, width: int, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]) -> None:
    x0, x1 = max(0, x0), min(width, x1)
    y0, y1 = max(0, y0), min(len(buf) // (width * 3), y1)
    pixel = bytes(color)

    for y in range(y0, y1):
        row = y * width * 3
        for x in range(x0, x1):
            i = row + x * 3
            buf[i : i + 3] = pixel


def circle(buf: bytearray, width: int, cx: int, cy: int, r: int, color: tuple[int, int, int]) -> None:
    rr = r * r
    pixel = bytes(color)

    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= rr:
                if 0 <= x < width and 0 <= y:
                    i = (y * width + x) * 3
                    if i + 2 < len(buf):
                        buf[i : i + 3] = pixel


def preview_desktop(width: int = 1600, height: int = 900) -> bytes:
    wallpaper = wallpaper_sequoia(width, height)
    buf = bytearray(wallpaper)

    # Menu / waybar chrome
    fill(buf, width, 0, 0, width, 36, CHROME)
    fill(buf, width, 18, 14, 86, 22, BLUE)
    fill(buf, width, width - 220, 14, width - 40, 22, mix(LABEL, CHROME, 0.55))

    # Window
    wx, wy, ww, wh = 280, 110, 1040, 660
    fill(buf, width, wx + 8, wy + 10, wx + ww + 8, wy + wh + 10, mix(GRAY, (0, 0, 0), 0.12))
    fill(buf, width, wx, wy, wx + ww, wy + wh, WINDOW)
    fill(buf, width, wx, wy, wx + ww, wy + 44, CHROME)
    circle(buf, width, wx + 28, wy + 22, 8, CLOSE)
    circle(buf, width, wx + 52, wy + 22, 8, MINIMIZE)
    circle(buf, width, wx + 76, wy + 22, 8, ZOOM)

    # Content cards
    fill(buf, width, wx + 28, wy + 72, wx + 300, wy + wh - 28, DESK)
    fill(buf, width, wx + 324, wy + 72, wx + ww - 28, wy + 260, mix(WINDOW, BLUE, 0.06))
    fill(buf, width, wx + 324, wy + 284, wx + ww - 28, wy + wh - 28, DESK)

    # Palette chips
    chips = [BLUE, CLOSE, MINIMIZE, ZOOM, (255, 59, 48), (255, 204, 0), (52, 199, 89), GRAY]
    cx0, cy0 = wx + 348, wy + 100

    for i, color in enumerate(chips):
        fill(buf, width, cx0 + i * 78, cy0, cx0 + i * 78 + 64, cy0 + 48, color)

    return bytes(buf)


def unlock_card(width: int = 640, height: int = 360) -> bytes:
    wallpaper = wallpaper_sonoma_chrome(width, height)
    buf = bytearray(wallpaper)
    wx, wy, ww, wh = 170, 120, 300, 48
    fill(buf, width, wx, wy, wx + ww, wy + wh, WINDOW)
    fill(buf, width, wx, wy, wx + ww, wy + 2, BLUE)
    fill(buf, width, wx + 16, wy + 20, wx + ww - 80, wy + 28, mix(LABEL, WINDOW, 0.72))
    circle(buf, width, wx + ww - 28, wy + 24, 8, BLUE)

    return bytes(buf)


def main() -> None:
    THEME.mkdir(parents=True, exist_ok=True)

    # Wallpapers live in backgrounds/ as Unsplash JPEGs — do not overwrite them.
    png_rgb(THEME / "preview.png", 1600, 900, preview_desktop())
    png_rgb(THEME / "preview-unlock.png", 640, 360, unlock_card())
    png_rgb(THEME / "unlock.png", 640, 360, unlock_card())
    print(f"wrote preview assets under {THEME}")


if __name__ == "__main__":
    main()
