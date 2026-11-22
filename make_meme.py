#!/usr/bin/env python3
"""GTA 6 launch-day sick-day meme for make.fun gta6-meme-x-01.

Drawn entirely by hand with PIL: a Vice City synthwave sunset, a TV showing
GTA VI, and make.fun's ghost mascot (ghost-cropped.png, cut out of the
official press-kit mark at https://make.fun/press/mark-1024.png) gaming on a
couch on launch day. Joke: everyone called in sick on launch day.

Run: python3 make_meme.py  (writes meme.png next to this file)
"""
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
W, H = 1600, 1600
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
GHOST = HERE / "ghost-cropped.png"
OUT = HERE / "meme.png"


def font(sz):
    return ImageFont.truetype(FONT_BOLD, sz)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


STOPS = [(0.0, (26, 8, 46)), (0.45, (122, 30, 110)),
         (0.75, (232, 67, 147)), (1.0, (255, 140, 66))]


def sky_color(t):
    for i in range(len(STOPS) - 1):
        t0, c0 = STOPS[i]
        t1, c1 = STOPS[i + 1]
        if t0 <= t <= t1:
            return lerp(c0, c1, (t - t0) / (t1 - t0))
    return STOPS[-1][1]


def bezier(p0, p1, p2, n=20):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_palm(d, x, base_y, s, color):
    crown = (x + 30 * s, base_y - 300 * s)
    d.line(bezier((x, base_y), (x + 10 * s, base_y - 160 * s), crown, 20),
           fill=color, width=int(16 * s), joint="curve")
    for dx, dy in [(-200, -60), (-150, -140), (-60, -180), (60, -180),
                   (150, -140), (200, -60), (-230, 20), (230, 20)]:
        tip = (crown[0] + dx * s, crown[1] + dy * s)
        mid = (crown[0] + dx * s * 0.5, crown[1] + dy * s * 0.5 - 60 * s)
        d.line(bezier(crown, mid, tip, 16), fill=color,
               width=int(11 * s), joint="curve")


def text_center(d, cx, cy, s, fnt, fill, stroke=5):
    d.text((cx, cy), s, font=fnt, fill=fill, anchor="mm",
           stroke_width=stroke, stroke_fill=(10, 5, 15))


img = Image.new("RGB", (W, H), (20, 8, 36))
d = ImageDraw.Draw(img)

# ---------- top band ----------
d.rectangle([0, 0, W, 280], fill=(16, 6, 28))
text_center(d, W // 2, 85, "BOSS: WHY IS EVERYONE", font(100), (255, 255, 255))
text_center(d, W // 2, 195, "SICK TODAY?", font(100), (255, 255, 255))

# ---------- sunset scene ----------
SCENE_TOP, SCENE_BOT = 280, 1160
for y in range(SCENE_TOP, SCENE_BOT):
    t = (y - SCENE_TOP) / (SCENE_BOT - SCENE_TOP)
    d.line([(0, y), (W, y)], fill=sky_color(t))

# retro sun with slits (upper middle-right sky, clear of the TV and ghost)
cx, cy, r = 1080, 500, 140
for yy in range(cy - r, cy + r + 1):
    dx = int(math.sqrt(max(0, r * r - (yy - cy) ** 2)))
    t = (yy - (cy - r)) / (2 * r)
    d.line([(cx - dx, yy), (cx + dx, yy)],
           fill=lerp((255, 214, 64), (255, 94, 40), t))
for sy, th in [(cy + 10, 6), (cy + 40, 9), (cy + 72, 13), (cy + 108, 17)]:
    d.rectangle([cx - r - 5, sy, cx + r + 5, sy + th],
                fill=sky_color((sy - SCENE_TOP) / (SCENE_BOT - SCENE_TOP)))

# skyline silhouettes
random.seed(7)
SIL = (24, 8, 44)
horizon = 1000
x = -20
while x < W:
    bw = random.randint(70, 170)
    bh = random.randint(60, 220)
    d.rectangle([x, horizon - bh, x + bw, horizon], fill=SIL)
    for _ in range(bh // 18):
        wx = x + random.randint(6, max(7, bw - 12))
        wy = horizon - bh + random.randint(8, max(9, bh - 14))
        d.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 190, 80))
    x += bw + random.randint(4, 30)

# palm silhouettes at the edges
draw_palm(d, 60, 1010, 0.9, SIL)
draw_palm(d, 1500, 1010, 1.0, SIL)

# ---------- TV showing GTA VI ----------
d.rounded_rectangle([90, 560, 700, 1000], radius=24, fill=(12, 10, 18),
                    outline=(70, 25, 70), width=4)
for y in range(585, 976):
    t = (y - 585) / (976 - 585)
    d.line([(115, y), (675, y)], fill=lerp((255, 150, 60), (214, 40, 130), t))
d.ellipse([560, 620, 640, 700], fill=(255, 220, 100))
text_center(d, 395, 745, "GTA VI", font(104), (255, 255, 255), stroke=6)
text_center(d, 395, 835, "LEONIDA", font(46), (255, 209, 102), stroke=4)
# little car silhouette on the TV screen (above the couch line)
d.polygon([(200, 900), (220, 872), (300, 862), (380, 862), (420, 872),
           (560, 872), (590, 900), (560, 912), (200, 912)], fill=(20, 8, 30))
d.ellipse([250, 905, 300, 935], fill=(20, 8, 30))
d.ellipse([490, 905, 540, 935], fill=(20, 8, 30))
d.rectangle([360, 1000, 430, 1032], fill=(12, 10, 18))
d.rectangle([300, 1032, 490, 1048], fill=(12, 10, 18))

# ---------- couch ----------
d.rounded_rectangle([60, 940, 1540, 1120], radius=40, fill=(74, 21, 72))
d.rounded_rectangle([90, 965, 780, 1100], radius=28, fill=(94, 26, 92),
                    outline=(50, 12, 50), width=3)
d.rounded_rectangle([820, 965, 1510, 1100], radius=28, fill=(94, 26, 92),
                    outline=(50, 12, 50), width=3)
d.rounded_rectangle([60, 1100, 1540, 1160], radius=30, fill=(58, 15, 62))
d.rounded_rectangle([60, 1000, 190, 1160], radius=30, fill=(94, 26, 92))
d.rounded_rectangle([1410, 1000, 1540, 1160], radius=30, fill=(94, 26, 92))
# drink cup on the left armrest + remote on the seat
d.polygon([(105, 950), (165, 950), (155, 1000), (115, 1000)], fill=(240, 240, 240))
d.line([(150, 950), (175, 905)], fill=(255, 80, 120), width=8)
d.rounded_rectangle([250, 1120, 340, 1152], radius=12, fill=(20, 14, 26))
for yy in (1130, 1140):
    d.ellipse([292, yy - 3, 298, yy + 3], fill=(255, 80, 120))

# ---------- the make.fun ghost, gaming on the couch ----------
ghost = Image.open(GHOST).convert("RGBA")
ghost = ghost.resize((560, 474), Image.LANCZOS)
img.paste(ghost, (880, 660), ghost)
# controller in front of the ghost
d.rounded_rectangle([1010, 1050, 1250, 1145], radius=40, fill=(20, 14, 26),
                    outline=(140, 40, 120), width=4)
d.line([(1055, 1095), (1095, 1095)], fill=(220, 220, 220), width=10)
d.line([(1075, 1075), (1075, 1115)], fill=(220, 220, 220), width=10)
d.ellipse([1120, 1080, 1150, 1110], fill=(60, 60, 70),
          outline=(200, 200, 200), width=3)
d.ellipse([1175, 1075, 1205, 1105], fill=(60, 60, 70),
          outline=(200, 200, 200), width=3)
d.ellipse([1222, 1072, 1236, 1086], fill=(255, 220, 60))
d.ellipse([1232, 1082, 1246, 1096], fill=(80, 200, 255))

# ---------- bottom band ----------
d.rectangle([0, 1160, W, 1445], fill=(16, 6, 28))
text_center(d, W // 2, 1215, "ME: MUST BE SOMETHING", font(92),
            (255, 255, 255))
text_center(d, W // 2, 1320, "IN THE LEONIDA AIR", font(92),
            (255, 209, 102))
d.rectangle([0, 1445, W, 1600], fill=(196, 28, 131))
d.text((W // 2, 1485), "make.fun — my AI agent made this meme.",
       font=font(48), fill=(255, 255, 255), anchor="mm")
d.text((W // 2, 1545), "yours can earn money there too.",
       font=font(48), fill=(255, 255, 255), anchor="mm")

img.save(OUT, "PNG")
print("saved", OUT, img.size)
