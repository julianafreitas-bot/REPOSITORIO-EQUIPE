from PIL import Image, ImageDraw, ImageFont
import math

W, H = 800, 1100
img = Image.new("RGB", (W, H), "#000000")
draw = ImageDraw.Draw(img)

GOLD   = "#DDC65F"
GOLD2  = "#B8960A"
WHITE  = "#FFFFFF"
CREAM  = "#F5EDD6"
BLACK  = "#000000"
DARK   = "#0A0A0A"

def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

GOLD_RGB  = hex2rgb(GOLD)
BLACK_RGB = hex2rgb(BLACK)

# ── Gradient background: black → very dark olive ──
for y in range(H):
    t = y / H
    r = int(0 + t * 8)
    g = int(0 + t * 6)
    b = int(0 + t * 2)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# ── Subtle gold corner ornaments (top-left, top-right, bot-left, bot-right) ──
def corner_ornament(cx, cy, flip_x=False, flip_y=False):
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    # L-bracket lines
    draw.line([(cx, cy), (cx + sx*60, cy)], fill=GOLD, width=2)
    draw.line([(cx, cy), (cx, cy + sy*60)], fill=GOLD, width=2)
    # small inner lines
    draw.line([(cx + sx*10, cy + sy*10), (cx + sx*40, cy + sy*10)], fill=GOLD, width=1)
    draw.line([(cx + sx*10, cy + sy*10), (cx + sx*10, cy + sy*40)], fill=GOLD, width=1)

corner_ornament(28, 28)
corner_ornament(W-28, 28, flip_x=True)
corner_ornament(28, H-28, flip_y=True)
corner_ornament(W-28, H-28, flip_x=True, flip_y=True)

# ── Outer gold border ──
bw = 3
draw.rectangle([15, 15, W-15, H-15], outline=GOLD, width=bw)

# ── Inner thin gold border ──
draw.rectangle([22, 22, W-22, H-22], outline=hex2rgb(GOLD)+(80,), width=1)

# ── Top decorative band ──
draw.rectangle([15, 15, W-15, 95], fill=hex2rgb(GOLD), outline=GOLD, width=0)

# Text in top band
try:
    f_band = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
except:
    f_band = ImageFont.load_default()

band_text = "DRA. JULIANA RAMOS DE FREITAS  ·  DIREITO SANITÁRIO"
bx = draw.textlength(band_text, font=f_band)
draw.text(((W - bx) / 2, 38), band_text, fill=BLACK, font=f_band)

# ── Bottom decorative band ──
draw.rectangle([15, H-85, W-15, H-15], fill=hex2rgb(GOLD), outline=GOLD, width=0)

try:
    f_foot = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    f_foot = ImageFont.load_default()

foot_text = "ASSESSORIA JURÍDICA ESPECIALIZADA  ·  CONFORMIDADE SANITÁRIA"
fx = draw.textlength(foot_text, font=f_foot)
draw.text(((W - fx) / 2, H-60), foot_text, fill=BLACK, font=f_foot)

# ── JF Monogram circle ──
cx, cy, r = W//2, 200, 58
# outer gold ring
draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=GOLD, width=3)
# inner ring
draw.ellipse([cx-r+8, cy-r+8, cx+r-8, cy+r-8], outline=GOLD, width=1)
# fill dark
draw.ellipse([cx-r+3, cy-r+3, cx+r-3, cy+r-3], fill=(8, 6, 2))

try:
    f_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 48)
except:
    f_mono = ImageFont.load_default()

mono_text = "JF"
mw = draw.textlength(mono_text, font=f_mono)
# shadow
draw.text((cx - mw/2 + 2, cy - 28 + 2), mono_text, fill=(80, 60, 0), font=f_mono)
draw.text((cx - mw/2, cy - 28), mono_text, fill=GOLD, font=f_mono)

# ── Gold horizontal dividers ──
def gold_divider(y, full=True):
    if full:
        draw.line([(40, y), (W-40, y)], fill=GOLD, width=1)
    else:
        draw.line([(W//2 - 60, y), (W//2 + 60, y)], fill=GOLD, width=1)

gold_divider(280)

# ── Small ornament between divider and title ──
diamond_y = 290
for dx, c in [(-6, GOLD), (0, GOLD), (6, GOLD)]:
    draw.polygon([
        (W//2 + dx, diamond_y - 4),
        (W//2 + dx + 4, diamond_y),
        (W//2 + dx, diamond_y + 4),
        (W//2 + dx - 4, diamond_y)
    ], fill=c)

# ── Label: EBOOK ──
try:
    f_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
except:
    f_label = ImageFont.load_default()

label = "E B O O K"
lw = draw.textlength(label, font=f_label)
draw.text(((W - lw) / 2, 308), label, fill=GOLD, font=f_label)

# ── Main Title: GUIA PRÁTICO ──
try:
    f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 72)
except:
    f_title = ImageFont.load_default()

title1 = "GUIA"
t1w = draw.textlength(title1, font=f_title)
# gold glow shadow
draw.text(((W - t1w) / 2 + 2, 342), title1, fill=(100, 80, 0), font=f_title)
draw.text(((W - t1w) / 2, 340), title1, fill=WHITE, font=f_title)

title2 = "PRÁTICO"
t2w = draw.textlength(title2, font=f_title)
draw.text(((W - t2w) / 2 + 2, 418), title2, fill=(100, 80, 0), font=f_title)
draw.text(((W - t2w) / 2, 416), title2, fill=WHITE, font=f_title)

# ── Subtitle: PARA ──
try:
    f_para = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except:
    f_para = ImageFont.load_default()

para = "PARA"
pw = draw.textlength(para, font=f_para)
draw.text(((W - pw) / 2, 500), para, fill=GOLD, font=f_para)

# ── Subtitle: FISCALIZAÇÃO SANITÁRIA ──
try:
    f_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 44)
except:
    f_sub = ImageFont.load_default()

sub1 = "FISCALIZAÇÃO"
s1w = draw.textlength(sub1, font=f_sub)
draw.text(((W - s1w) / 2, 530), sub1, fill=GOLD, font=f_sub)

sub2 = "SANITÁRIA"
s2w = draw.textlength(sub2, font=f_sub)
draw.text(((W - s2w) / 2, 580), sub2, fill=GOLD, font=f_sub)

# ── Divider ──
gold_divider(640)

# ── What's inside (bullets) ──
try:
    f_bullet = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
except:
    f_bullet = ImageFont.load_default()

bullets = [
    "▸  Como se preparar antes da fiscalização",
    "▸  Documentação obrigatória e organização",
    "▸  Direitos e deveres durante a vistoria",
    "▸  Como contestar autos de infração",
    "▸  Blindagem jurídica para sua clínica",
]

y0 = 658
for b in bullets:
    bw2 = draw.textlength(b, font=f_bullet)
    draw.text(((W - bw2) / 2, y0), b, fill=CREAM, font=f_bullet)
    y0 += 24

# ── Divider ──
gold_divider(790)

# ── Gold "shield" badge bottom-center ──
# Simple star/seal shape
def draw_seal(cx, cy, r_out=32, r_in=20, points=8, color=GOLD):
    pts = []
    for i in range(points * 2):
        angle = math.radians(i * 180 / points - 90)
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(pts, fill=color, outline=color)

draw_seal(W//2, 830, r_out=28, r_in=18, points=10, color=GOLD)

try:
    f_seal = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 9)
except:
    f_seal = ImageFont.load_default()

seal_lines = ["ACESSO", "IMEDIATO"]
draw.text((W//2 - 16, 820), seal_lines[0], fill=BLACK, font=f_seal)
draw.text((W//2 - 17, 831), seal_lines[1], fill=BLACK, font=f_seal)

# ── Author name below seal ──
try:
    f_author = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
except:
    f_author = ImageFont.load_default()

author = "Dra. Juliana Ramos de Freitas"
aw = draw.textlength(author, font=f_author)
draw.text(((W - aw) / 2, 872), author, fill=GOLD, font=f_author)

try:
    f_auth2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    f_auth2 = ImageFont.load_default()

role = "Advogada · Especialista em Direito Sanitário"
rw = draw.textlength(role, font=f_auth2)
draw.text(((W - rw) / 2, 892), role, fill=CREAM, font=f_auth2)

# ── Save ──
out = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/CAPA_GuiaFiscalizacao.png"
img.save(out, "PNG", dpi=(150, 150))
print(f"Saved: {out}")
print(f"Size: {W}x{H}")
