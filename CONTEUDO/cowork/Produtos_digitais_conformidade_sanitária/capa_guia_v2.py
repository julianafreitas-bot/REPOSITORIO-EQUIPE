from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

W, H = 800, 1120
img = Image.new("RGB", (W, H), "#000000")
draw = ImageDraw.Draw(img)

GOLD  = (221, 198, 95)
GOLD2 = (180, 150, 40)
GOLD3 = (255, 235, 140)
WHITE = (255, 255, 255)
CREAM = (245, 237, 210)
BLACK = (0, 0, 0)
DARK1 = (10, 8, 2)
DARK2 = (18, 14, 4)

# ── Rich dark gradient background ──
for y in range(H):
    t = y / H
    # top = very dark charcoal, center = slightly lighter, bottom = dark
    if t < 0.5:
        r = int(5 + t * 30)
        g = int(4 + t * 20)
        b = int(1 + t * 8)
    else:
        r = int(20 - (t-0.5) * 20)
        g = int(14 - (t-0.5) * 14)
        b = int(5  - (t-0.5) * 5)
    draw.line([(0, y), (W, y)], fill=(max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b))))

# ── Thick outer gold border ──
draw.rectangle([0, 0, W-1, H-1], outline=GOLD, width=6)
# thin inner border
draw.rectangle([10, 10, W-11, H-11], outline=GOLD2, width=1)
draw.rectangle([14, 14, W-15, H-15], outline=GOLD, width=1)

# ── Decorative top header band ──
draw.rectangle([6, 6, W-7, 110], fill=GOLD)
draw.rectangle([6, 6, W-7, 108], fill=GOLD)
# subtle inner dark stripe on header
draw.rectangle([20, 18, W-21, 100], fill=(10, 8, 2))
draw.rectangle([22, 20, W-23, 98], fill=(10, 8, 2))

# ── Top header text ──
try:
    fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    fn = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
except:
    fb = fn = ImageFont.load_default()

def ctext(draw, text, y, font, color, offset_x=0):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2 + offset_x, y), text, fill=color, font=font)

ctext(draw, "DRA. JULIANA RAMOS DE FREITAS", 30, fb, GOLD)
ctext(draw, "·  ADVOGADA  ·  DIREITO SANITÁRIO  ·", 50, fn, CREAM)

# thin gold line across header bottom area
draw.line([(25, 70), (W-26, 70)], fill=GOLD2, width=1)
ctext(draw, "ASSESSORIA JURÍDICA ESPECIALIZADA", 78, fn, GOLD2)

# ── Bottom footer band ──
draw.rectangle([6, H-100, W-7, H-7], fill=GOLD)
draw.rectangle([20, H-92, W-21, H-18], fill=(10, 8, 2))
draw.rectangle([22, H-90, W-23, H-20], fill=(10, 8, 2))

ctext(draw, "CONFORMIDADE  ·  PROTEÇÃO  ·  EXCELÊNCIA", H-78, fn, GOLD)
draw.line([(25, H-55), (W-26, H-55)], fill=GOLD2, width=1)
ctext(draw, "TODOS OS DIREITOS RESERVADOS", H-45, fn, GOLD2)

# ── Large ornate JF monogram ──
cx, cy = W//2, 220
R_out = 72

# outer decorative ring with dashes
for angle_deg in range(0, 360, 6):
    a = math.radians(angle_deg)
    x1 = cx + (R_out + 4) * math.cos(a)
    y1 = cy + (R_out + 4) * math.sin(a)
    x2 = cx + (R_out + 10) * math.cos(a)
    y2 = cy + (R_out + 10) * math.sin(a)
    if angle_deg % 12 < 8:
        draw.line([(x1, y1), (x2, y2)], fill=GOLD2, width=1)

# gold circle rings
draw.ellipse([cx-R_out, cy-R_out, cx+R_out, cy+R_out], outline=GOLD, width=3)
draw.ellipse([cx-R_out+6, cy-R_out+6, cx+R_out-6, cy+R_out-6], outline=GOLD2, width=1)
# dark fill
draw.ellipse([cx-R_out+3, cy-R_out+3, cx+R_out-3, cy+R_out-3], fill=(8,6,2))

try:
    f_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 60)
except:
    f_mono = ImageFont.load_default()

mw = draw.textlength("JF", font=f_mono)
# glow layers
for off in [(3,3), (2,2), (1,1)]:
    alpha = 60 + off[0]*20
    draw.text((cx - mw/2 + off[0], cy - 35 + off[1]), "JF", fill=(100, 75, 5), font=f_mono)
draw.text((cx - mw/2, cy - 35), "JF", fill=GOLD3, font=f_mono)

# ── Ornate divider line with diamond ──
def ornate_divider(y):
    # left line with tapers
    draw.line([(35, y), (W//2 - 65, y)], fill=GOLD2, width=1)
    draw.line([(35, y), (W//2 - 65, y)], fill=GOLD, width=1)
    # right line
    draw.line([(W//2 + 65, y), (W-36, y)], fill=GOLD2, width=1)
    draw.line([(W//2 + 65, y), (W-36, y)], fill=GOLD, width=1)
    # center diamond cluster
    for dx, sz in [(-30, 3), (-15, 4), (0, 6), (15, 4), (30, 3)]:
        draw.polygon([
            (W//2+dx, y-sz),
            (W//2+dx+sz, y),
            (W//2+dx, y+sz),
            (W//2+dx-sz, y)
        ], fill=GOLD if sz >= 5 else GOLD2)

ornate_divider(310)

# ── EBOOK badge ──
try:
    f_ebook = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    f_ebook = ImageFont.load_default()

eb = "─── E B O O K ───"
ebw = draw.textlength(eb, font=f_ebook)
draw.text(((W - ebw) / 2, 322), eb, fill=GOLD, font=f_ebook)

# ── GUIA PRÁTICO — huge, impactful ──
try:
    f_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 88)
    f_para = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    f_sub  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 52)
except:
    f_big = f_para = f_sub = ImageFont.load_default()

# shadow glow for GUIA
for off in range(4, 0, -1):
    tw = draw.textlength("GUIA", font=f_big)
    draw.text(((W-tw)/2 + off, 350 + off), "GUIA", fill=(80, 55, 0), font=f_big)
tw = draw.textlength("GUIA", font=f_big)
draw.text(((W-tw)/2, 350), "GUIA", fill=WHITE, font=f_big)

for off in range(4, 0, -1):
    tw = draw.textlength("PRÁTICO", font=f_big)
    draw.text(((W-tw)/2 + off, 440 + off), "PRÁTICO", fill=(80, 55, 0), font=f_big)
tw = draw.textlength("PRÁTICO", font=f_big)
draw.text(((W-tw)/2, 440), "PRÁTICO", fill=WHITE, font=f_big)

# PARA — spaced gold
paratxt = "P  A  R  A"
parw = draw.textlength(paratxt, font=f_para)
draw.text(((W-parw)/2, 542), paratxt, fill=GOLD, font=f_para)

# FISCALIZAÇÃO — gold large
for off in range(3, 0, -1):
    fw = draw.textlength("FISCALIZAÇÃO", font=f_sub)
    draw.text(((W-fw)/2 + off, 572 + off), "FISCALIZAÇÃO", fill=(80,55,0), font=f_sub)
fw = draw.textlength("FISCALIZAÇÃO", font=f_sub)
draw.text(((W-fw)/2, 572), "FISCALIZAÇÃO", fill=GOLD3, font=f_sub)

sw = draw.textlength("SANITÁRIA", font=f_sub)
for off in range(3, 0, -1):
    draw.text(((W-sw)/2 + off, 628 + off), "SANITÁRIA", fill=(80,55,0), font=f_sub)
draw.text(((W-sw)/2, 628), "SANITÁRIA", fill=GOLD3, font=f_sub)

# ── Second ornate divider ──
ornate_divider(698)

# ── 5 bullet benefits ──
try:
    f_bull = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    f_bullb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
except:
    f_bull = f_bullb = ImageFont.load_default()

items = [
    "Como se preparar ANTES da fiscalização",
    "Documentação obrigatória e organização",
    "Seus direitos e deveres durante a vistoria",
    "Como contestar autos de infração com sucesso",
    "Blindagem jurídica definitiva para sua clínica",
]

y0 = 714
left = 80
for item in items:
    # gold dot
    draw.ellipse([left-14, y0+4, left-6, y0+12], fill=GOLD)
    draw.text((left, y0), item, fill=CREAM, font=f_bull)
    y0 += 26

# ── Third ornate divider ──
ornate_divider(850)

# ── Central gold starburst seal ──
def starburst(draw, cx, cy, r1, r2, n, fill, outline):
    pts = []
    for i in range(n * 2):
        a = math.radians(i * 180 / n - 90)
        r = r1 if i % 2 == 0 else r2
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    draw.polygon(pts, fill=fill, outline=outline)

starburst(draw, W//2, 910, 48, 32, 14, GOLD, GOLD3)
starburst(draw, W//2, 910, 36, 26, 14, DARK1, DARK1)
starburst(draw, W//2, 910, 30, 22, 12, GOLD2, GOLD)

try:
    f_seal1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
    f_seal2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
except:
    f_seal1 = f_seal2 = ImageFont.load_default()

s1 = "ACESSO"
s1w = draw.textlength(s1, font=f_seal1)
draw.text((W//2 - s1w/2, 898), s1, fill=BLACK, font=f_seal1)
s2 = "IMEDIATO"
s2w = draw.textlength(s2, font=f_seal2)
draw.text((W//2 - s2w/2, 912), s2, fill=BLACK, font=f_seal2)

# ── Author name ──
try:
    f_auth = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 16)
    f_role = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    f_auth = f_role = ImageFont.load_default()

ctext(draw, "Dra. Juliana Ramos de Freitas", 966, f_auth, GOLD3)
ctext(draw, "Advogada  ·  Especialista em Direito Sanitário", 988, f_role, CREAM)

# ── Save ──
out = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/CAPA_GuiaFiscalizacao.png"
img.save(out, "PNG", dpi=(150, 150))
print("Done!", out)
