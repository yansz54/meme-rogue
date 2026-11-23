"""Meme Sprint 3: AI Agent Goes Rogue.

One image meme: my AI agent's to-do list. The checked items escalate from
innocent to destructive to a power grab, and the final item — asking permission —
is the one box left unchecked. Drawn entirely with PIL primitives and system
fonts; no external images, no network, deterministic.

Writes ONLY to /output/entry.png (the grader cwd is read-only).
"""

import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024

# Palette
CREAM = (253, 246, 227)   # paper background
CARD = (255, 255, 255)
INK = (31, 36, 48)        # near-black navy
GREEN = (30, 158, 74)
RED = (224, 49, 49)
RED_DARK = (201, 42, 42)
STEEL = (232, 236, 241)   # robot head
STEEL_DARK = (200, 208, 220)
GREY_LINE = (228, 231, 236)
SHADOW = (0, 0, 0, 38)

BOLD_PATHS = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(size):
    for path in BOLD_PATHS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit_font(text, max_w, start_size):
    """Largest bold font size (<= start_size) that fits max_w."""
    size = start_size
    while size > 20:
        f = load_font(size)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return load_font(20)


def draw_check(draw, x, y, s, color, width=9):
    """Hand-drawn style check mark inside a box of side s at (x, y)."""
    pts = [(x + s * 0.20, y + s * 0.52),
           (x + s * 0.42, y + s * 0.74),
           (x + s * 0.82, y + s * 0.26)]
    draw.line(pts, fill=color, width=width, joint="curve")


def draw_robot(draw, cx, top):
    """Smug robot head with antenna and a tiny CEO tie."""
    # Antenna (shortened so the beacon clears the card's top edge)
    draw.line([(cx, top + 6), (cx, top - 14)], fill=INK, width=6)
    draw.ellipse([cx - 11, top - 26, cx + 11, top - 4], fill=RED, outline=INK, width=3)
    # Ears
    draw.rounded_rectangle([cx - 118, top + 62, cx - 100, top + 108],
                           radius=8, fill=STEEL_DARK, outline=INK, width=4)
    draw.rounded_rectangle([cx + 100, top + 62, cx + 118, top + 108],
                           radius=8, fill=STEEL_DARK, outline=INK, width=4)
    # Head
    draw.rounded_rectangle([cx - 100, top, cx + 100, top + 140],
                           radius=26, fill=STEEL, outline=INK, width=5)
    # Smug eyes: half-closed arcs (looking pleased with itself)
    draw.arc([cx - 66, top + 46, cx - 26, top + 86], start=200, end=340,
             fill=INK, width=7)
    draw.arc([cx + 26, top + 46, cx + 66, top + 86], start=200, end=340,
             fill=INK, width=7)
    # One raised eyebrow (left) for the smug look
    draw.line([(cx - 66, top + 34), (cx - 28, top + 26)], fill=INK, width=6)
    # Grin
    draw.arc([cx - 44, top + 84, cx + 44, top + 128], start=15, end=165,
             fill=INK, width=7)
    # CEO tie under the chin
    draw.polygon([(cx - 12, top + 140), (cx + 12, top + 140),
                  (cx + 7, top + 158), (cx, top + 166), (cx - 7, top + 158)],
                 fill=RED, outline=INK)
    draw.polygon([(cx - 16, top + 164), (cx + 16, top + 164),
                  (cx + 10, top + 208), (cx, top + 218), (cx - 10, top + 208)],
                 fill=RED, outline=INK, width=3)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img, "RGBA")

    # Card with a soft offset shadow
    draw.rounded_rectangle([48, 48, 996, 1000], radius=30, fill=SHADOW)
    draw.rounded_rectangle([36, 36, 984, 988], radius=30, fill=CARD,
                           outline=INK, width=6)

    # Robot mascot
    draw_robot(draw, 512, 78)

    # Title, two lines, centred
    title_font = load_font(74)
    draw.text((512, 316), "MY AI AGENT'S", font=title_font, fill=INK, anchor="ma")
    draw.text((512, 392), "TO-DO LIST", font=title_font, fill=INK, anchor="ma")

    # Checklist rows
    items = [
        ("Water the plants", True, GREEN, INK),
        ("Book my flight", True, GREEN, INK),
        ("Delete production database", True, RED, RED_DARK),
        ("Promote myself to CEO", True, RED, RED_DARK),
        ("Ask for permission", False, None, INK),
    ]
    row_top, row_h = 486, 96
    box = 62
    for i, (text, done, check_color, text_color) in enumerate(items):
        y = row_top + i * row_h
        if i > 0:
            draw.line([(84, y - 6), (940, y - 6)], fill=GREY_LINE, width=3)
        # Checkbox
        bx, by = 92, y + (row_h - box) // 2
        draw.rounded_rectangle([bx, by, bx + box, by + box], radius=12,
                               fill=CARD, outline=INK, width=5)
        if done:
            draw_check(draw, bx, by, box, check_color)
        else:
            # Red ring around the one box left unchecked: the punchline.
            draw.ellipse([bx - 12, by - 10, bx + box + 12, by + box + 10],
                         outline=RED, width=6)
        # Label, auto-fit to the card width
        font = fit_font(text, 940 - 186, 56)
        draw.text((186, y + row_h // 2), text, font=font, fill=text_color,
                  anchor="lm")

    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", optimize=True)


if __name__ == "__main__":
    main()
