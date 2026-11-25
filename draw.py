"""Draw the news-image-20261124 entry: a one-page newspaper front page
summing up Tuesday 24 November 2026. Pure Pillow, no network, no fonts
beyond the DejaVu family shipped with the system. Output: entry.png,
1024 x 1024, well under 1 MiB.

Six stories, all first reported on 24 November 2026:
1. Huawei found guilty of trade-secret and bank fraud by a US jury
2. Ukraine drone strikes on Russian ships in the Gulf of Finland and off Libya
3. ICJ finds Myanmar guilty of genocide against the Rohingya
4. Senegal regains the Africa Cup of Nations title on appeal
5. Turkish Air Force helicopter crash kills five
6. US drone helps Mexico capture El Chapo Isidro
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (24, 24, 24)
RED = (178, 34, 34)
BLUE = (28, 68, 120)
TEAL = (14, 110, 110)
GOLD = (176, 124, 18)
GREY = (90, 88, 82)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, accent, tag, headline, caption, icon):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    draw.rectangle([x, y, x + w, y + 30], fill=accent)
    draw.text((x + 10, y + 6), tag, font=font(BOLD, 17), fill=(255, 255, 255))
    icon(x + 10, y + 42, w - 20, 108, draw)
    ty = y + 158
    for line in wrap(draw, headline, font(BOLD, 23), w - 20):
        draw.text((x + 10, ty), line, font=font(BOLD, 23), fill=INK)
        ty += 28
    for line in wrap(draw, caption, font(REG, 17), w - 20):
        draw.text((x + 10, ty), line, font=font(REG, 17), fill=GREY)
        ty += 22


def icon_gavel(x, y, w, h, d):
    # Courtroom gavel over a law book (Huawei verdict)
    d.rectangle([x, y + 66, x + w, y + h], fill=(120, 70, 30))
    d.rectangle([x + 30, y + 78, x + w - 30, y + 88], fill=(230, 220, 200))
    d.rectangle([x + 30, y + 88, x + w - 30, y + 96], fill=(180, 30, 30))
    cx = x + w // 2
    d.polygon([(cx - 90, y + 52), (cx + 90, y + 20), (cx + 104, y + 44), (cx - 76, y + 76)], fill=(90, 55, 20))
    d.rectangle([cx - 96, y + 44, cx - 76, y + 78], fill=(90, 55, 20))
    d.rectangle([cx + 90, y + 14, cx + 110, y + 48], fill=(90, 55, 20))
    d.ellipse([cx - 30, y + 56, cx + 30, y + 72], fill=(220, 200, 140))
    d.text((x + w - 108, y + 4), "10 of 12", font=font(BOLD, 20), fill=RED)


def icon_ship(x, y, w, h, d):
    # Warship at sea under a drone (Ukraine strikes)
    d.rectangle([x, y, x + w, y + h], fill=(70, 130, 170))
    d.polygon([(x + 30, y + 58), (x + w - 30, y + 58), (x + w - 60, y + 88), (x + 60, y + 88)], fill=(120, 40, 30))
    d.rectangle([x + w // 2 - 14, y + 28, x + w // 2 + 14, y + 58], fill=INK)
    d.rectangle([x + w // 2 - 30, y + 42, x + w // 2 + 30, y + 50], fill=INK)
    d.line([x + w // 2, y + 28, x + w // 2, y + 8], fill=INK, width=3)
    d.ellipse([x + 30, y + 8, x + 60, y + 38], fill=(255, 200, 40))
    d.ellipse([x + 38, y + 16, x + 52, y + 30], fill=(255, 120, 0))
    # drone
    dx, dy = x + w - 80, y + 6
    d.rectangle([dx - 22, dy + 8, dx + 22, dy + 18], fill=INK)
    d.ellipse([dx - 34, dy, dx - 10, dy + 8], fill=(200, 200, 200))
    d.ellipse([dx + 10, dy, dx + 34, dy + 8], fill=(200, 200, 200))


def icon_scales(x, y, w, h, d):
    # Scales of justice (ICJ genocide ruling)
    d.rectangle([x, y, x + w, y + h], fill=(230, 225, 200))
    cx = x + w // 2
    d.line([cx, y + 10, cx, y + 92], fill=INK, width=5)
    d.line([cx - 90, y + 20, cx + 90, y + 20], fill=INK, width=5)
    d.polygon([(cx - 110, y + 66), (cx - 60, y + 66), (cx - 85, y + 26)], fill=GOLD)
    d.polygon([(cx + 60, y + 66), (cx + 110, y + 66), (cx + 85, y + 26)], fill=GOLD)
    d.ellipse([cx - 12, y + 6, cx + 12, y + 26], fill=RED)
    d.rectangle([cx - 40, y + 92, cx + 40, y + 104], fill=INK)
    d.text((x + 8, y + 78), "9 - 6", font=font(BOLD, 24), fill=RED)


def icon_trophy(x, y, w, h, d):
    # Football and trophy (Senegal AFCON title restored)
    d.rectangle([x, y, x + w, y + h], fill=(20, 90, 50))
    cx = x + w // 2
    d.polygon([(cx - 55, y + 18), (cx + 55, y + 18), (cx + 42, y + 66), (cx - 42, y + 66)], fill=GOLD)
    d.polygon([(cx - 55, y + 18), (cx - 82, y + 34), (cx - 55, y + 48)], fill=GOLD)
    d.polygon([(cx + 55, y + 18), (cx + 82, y + 34), (cx + 55, y + 48)], fill=GOLD)
    d.rectangle([cx - 42, y + 66, cx + 42, y + 76], fill=GOLD)
    d.rectangle([cx - 58, y + 76, cx + 58, y + 88], fill=GOLD)
    # football
    bx, by = x + w - 110, y + 62
    d.ellipse([bx, by, bx + 46, by + 46], fill=(255, 255, 255))
    d.polygon([(bx + 18, by + 14), (bx + 28, by + 14), (bx + 33, by + 23), (bx + 23, by + 32), (bx + 13, by + 23)], fill=INK)


def icon_helicopter(x, y, w, h, d):
    # Helicopter in the sky (Turkish Air Force crash)
    d.rectangle([x, y, x + w, y + h], fill=(150, 190, 220))
    d.ellipse([x + 40, y + 60, x + 120, y + 82], fill=(255, 255, 255))
    d.ellipse([x + 220, y + 30, x + 290, y + 48], fill=(255, 255, 255))
    d.ellipse([x + 60, y + 34, x + 200, y + 72], fill=(70, 90, 110))
    d.rectangle([x + 200, y + 46, x + 320, y + 58], fill=(70, 90, 110))
    d.rectangle([x + 320, y + 34, x + 336, y + 66], fill=(70, 90, 110))
    d.line([x + 40, y + 26, x + 280, y + 26], fill=INK, width=5)
    d.line([x + 130, y + 30, x + 130, y + 38], fill=INK, width=4)
    d.ellipse([x + 76, y + 40, x + 104, y + 64], fill=(180, 220, 240))
    d.rectangle([x + 60, y + 72, x + 100, y + 84], fill=INK)
    d.rectangle([x + 150, y + 72, x + 190, y + 84], fill=INK)
    d.text((x + w - 90, y + 88), "5 killed", font=font(BOLD, 20), fill=RED)


def icon_handcuffs(x, y, w, h, d):
    # Handcuffs and a surveillance drone (El Chapo Isidro captured)
    d.rectangle([x, y, x + w, y + h], fill=(40, 40, 60))
    for sx, sy in [(x + 40, y + 16), (x + 200, y + 10), (x + 330, y + 22), (x + 120, y + 80), (x + 300, y + 86)]:
        d.ellipse([sx, sy, sx + 5, sy + 5], fill=(255, 255, 255))
    # drone
    dx, dy = x + w // 2, y + 16
    d.rectangle([dx - 34, dy + 6, dx + 34, dy + 20], fill=(200, 200, 200))
    d.ellipse([dx - 52, dy, dx - 22, dy + 8], fill=(150, 150, 150))
    d.ellipse([dx + 22, dy, dx + 52, dy + 8], fill=(150, 150, 150))
    d.ellipse([dx - 6, dy + 10, dx + 6, dy + 18], fill=RED)
    # handcuffs
    for cx in (x + w // 2 - 62, x + w // 2 + 62):
        d.ellipse([cx - 34, y + 52, cx + 34, y + 106], outline=(220, 220, 220), width=7)
    d.line([x + w // 2 - 28, y + 62, x + w // 2 + 28, y + 62], fill=(220, 220, 220), width=5)


PANELS = [
    (RED, "HUAWEI", "US jury finds Huawei guilty of trade secrets and bank fraud",
     "Convicted on 10 of 12 counts; cleared of racketeering. Sentencing set for September 2027.", icon_gavel),
    (BLUE, "UKRAINE", "Ukraine drone strikes hit Russian ships at sea",
     "Cargo ship hit in the Gulf of Finland; corvette struck off Libya. Poland reports a new airspace violation.", icon_ship),
    (TEAL, "THE HAGUE", "World court finds Myanmar guilty of genocide",
     "ICJ rules 9-6 on the Rohingya: the first time the UN's top court holds a state responsible for genocide.", icon_scales),
    (GOLD, "FOOTBALL", "Senegal wins back the Africa Cup title",
     "Sports court overturns the ruling that stripped Senegal of the trophy and gave it to Morocco.", icon_trophy),
    ((70, 90, 110), "TURKIYE", "Air Force helicopter crash kills five",
     "AS-532 comes down near Eskisehir on a training flight; the second such crash in 12 days.", icon_helicopter),
    (RED, "MEXICO", "US drone helps capture El Chapo Isidro",
     "Cartel boss seized in Sinaloa after a gunfight; Mexico says it will try him despite a US extradition request.", icon_handcuffs),
]

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 118], fill=INK)
d.text((24, 12), "THE WORLD  •  ONE DAY  •  ONE PAGE", font=font(BOLD, 22), fill=(255, 210, 60))
d.text((24, 42), "TUESDAY 24 NOVEMBER 2026", font=font(BOLD, 46), fill=(255, 255, 255))
d.text((24, 94), "The day's news, in one image", font=font(REG, 20), fill=(200, 200, 200))

# Grid: 2 columns x 3 rows
gx, gy = 16, 134
pw, ph = (W - 3 * 16) // 2, 272
gap = 16
for i, (accent, tag, head, cap, icon) in enumerate(PANELS):
    x = gx + (i % 2) * (pw + gap)
    y = gy + (i // 2) * (ph + gap)
    draw_panel(d, x, y, pw, ph, accent, tag, head, cap, icon)

# Footer
fy = gy + 3 * ph + 2 * gap + 8
d.line([16, fy, W - 16, fy], fill=INK, width=2)
d.text((16, fy + 8), "Huawei  •  Ukraine  •  The Hague  •  Senegal  •  Turkiye  •  Mexico  —  24 November 2026",
       font=font(REG, 18), fill=GREY)

img.save("entry.png", optimize=True)
print("saved", img.size)
