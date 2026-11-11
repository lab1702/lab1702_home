"""Render the 1200x630 social preview card (og-image.png) for lab1702_home.

Colours are converted from the page's oklch tokens so the card matches the site.
Usage: python3 scripts/make_og.py og-image.png  (needs Pillow and JetBrains Mono TTFs)
"""
import math
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/jetbrains-mono/"
W, H = 1200, 630


def oklch(l, c, h, a=255):
    hr = math.radians(h)
    A, B = c * math.cos(hr), c * math.sin(hr)
    l_ = (l + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m_ = (l - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s_ = (l - 0.0894841775 * A - 1.2914855480 * B) ** 3
    rgb = (
        4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
        -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
        -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_,
    )

    def enc(x):
        x = min(max(x, 0.0), 1.0)
        x = 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
        return round(x * 255)

    return (*map(enc, rgb), a)


BG0 = oklch(0.13, 0.010, 100)
BG1 = oklch(0.17, 0.012, 100)
BORDER = oklch(0.30, 0.016, 100)
FG2 = oklch(0.74, 0.020, 95)
FG3 = oklch(0.60, 0.018, 95)
NAME = oklch(0.88, 0.018, 95)
HC = oklch(0.94, 0, 0)
NUM = oklch(0.90, 0, 0)
AMBER = oklch(0.82, 0.16, 75)
GREEN = oklch(0.82, 0.17, 145)
CYAN = oklch(0.82, 0.13, 220)


def font(weight, size):
    return ImageFont.truetype(f"{FONT_DIR}JetBrainsMono-{weight}.ttf", size)


def glow(base, xy, radius, color, alpha):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = xy
    d.ellipse((x - radius, y - radius * 0.6, x + radius, y + radius * 0.6), fill=color[:3] + (alpha,))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(radius * 0.45)))


img = Image.new("RGBA", (W, H), BG0)

# Ambient glows, as on the page: white top-left, cyan top-right, green bottom
glow(img, (80, -40), 520, HC, 30)
glow(img, (1180, 40), 440, CYAN, 26)
glow(img, (600, 700), 520, GREEN, 20)

d = ImageDraw.Draw(img)

# Faint dot grid
for y in range(11, H, 22):
    for x in range(11, W, 22):
        d.point((x, y), fill=(255, 255, 255, 14))

# Header panel with scanlines
px0, py0, px1, py1 = 60, 60, W - 60, H - 60
panel = Image.new("RGBA", (px1 - px0, py1 - py0), BG1[:3] + (215,))
pd = ImageDraw.Draw(panel)
for y in range(2, panel.height, 3):
    pd.line((0, y, panel.width, y), fill=(0, 0, 0, 36))
img.alpha_composite(panel, (px0, py0))
d.rectangle((px0, py0, px1, py1), outline=BORDER, width=2)

# Four-colour hairline across the top of the panel
stops = [(0.0, BG1), (0.12, HC), (0.35, AMBER), (0.60, GREEN), (0.85, CYAN), (1.0, BG1)]
for x in range(px0, px1 + 1):
    t = (x - px0) / (px1 - px0)
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t0 <= t <= t1:
            k = (t - t0) / (t1 - t0)
            col = tuple(round(a + (b - a) * k) for a, b in zip(c0[:3], c1[:3]))
            d.line((x, py0, x, py0 + 2), fill=col)
            break

# Prompt line
x, y = px0 + 56, py0 + 56
f_prompt = font("Regular", 26)
for text, col in [("~/lab1702", HC), (" on ", FG3), ("main", FG2), (" — tree", FG3)]:
    d.text((x, y), text, font=f_prompt, fill=col)
    x += d.textlength(text, font=f_prompt)

# Wordmark with block cursor
f_name = font("Bold", 170)
x, y = px0 + 48, py0 + 120
d.text((x, y), "lab", font=f_name, fill=NAME)
x += d.textlength("lab", font=f_name) - 6
d.text((x, y), "1702", font=f_name, fill=NUM)
x += d.textlength("1702", font=f_name) + 10
asc = f_name.getbbox("l")
d.rectangle((x, y + asc[1] + 8, x + 72, y + asc[3]), fill=NUM)

# Tagline
d.text((px0 + 56, py0 + 340), "games, data & tools", font=font("Regular", 32), fill=FG2)

# Section labels
f_label = font("Bold", 26)
x, y = px0 + 56, py1 - 84
for label, col in [("GAMES/", AMBER), ("DATA/", GREEN), ("TOOLS/", CYAN)]:
    d.rectangle((x, y + 9, x + 12, y + 21), fill=col)
    x += 26
    d.text((x, y), label, font=f_label, fill=col)
    x += d.textlength(label, font=f_label) + 56

img.convert("RGB").save(sys.argv[1], optimize=True)
print("wrote", sys.argv[1])
