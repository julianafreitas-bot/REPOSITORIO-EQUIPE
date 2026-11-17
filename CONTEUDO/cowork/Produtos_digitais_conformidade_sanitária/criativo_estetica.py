from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

W, H = 1080, 1080
OUT = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/Criativo_Estetica_Interditada.png"

GOLD   = (221, 198, 95)
GOLD2  = (180, 155, 60)
BLACK  = (8, 8, 8)
WHITE  = (255, 255, 255)
RED    = (190, 25, 25)
CREAM  = (240, 228, 195)
WARN_Y = (255, 200, 0)
WARN_B = (18, 18, 18)

# ─── BASE: ambiente clínica de estética moderna ─────────────────────────────
img = Image.new("RGB", (W, H), (245, 240, 238))
draw = ImageDraw.Draw(img)

# Parede de fundo — rosê claro, elegante
for y in range(0, 520):
    t = y / 520
    r = int(238 - t*15)
    g = int(228 - t*18)
    b = int(225 - t*20)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Rodapé de parede / skirting board
draw.rectangle([0, 495, W, 510], fill=(200, 192, 188))
draw.rectangle([0, 510, W, 515], fill=(185, 175, 170))

# Chão de mármore (bege/cinza claro com veias)
for y in range(510, H):
    t = (y - 510) / (H - 510)
    r = int(218 + t*5)
    g = int(210 + t*5)
    b = int(205 + t*5)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Veias do mármore
random.seed(42)
for _ in range(8):
    x0 = random.randint(0, W)
    y0 = 510
    points = [(x0, y0)]
    for _ in range(random.randint(4, 8)):
        x0 += random.randint(-60, 80)
        y0 += random.randint(20, 80)
        points.append((x0, min(y0, H)))
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=(195, 188, 183), width=1)

# ─── PAREDE LATERAL direita com espelho ─────────────────────────────────────
# Espelho grande na parede (perspectiva)
mir_pts = [(700, 60), (900, 80), (900, 430), (700, 450)]
draw.polygon(mir_pts, fill=(200, 215, 225))
# Moldura do espelho
for offset in range(0, 10, 3):
    pts = [
        (700-offset, 60-offset),
        (900+offset, 80-offset),
        (900+offset, 430+offset),
        (700-offset, 450+offset)
    ]
    draw.polygon(pts, outline=(210, 195, 160), width=1)
draw.polygon(mir_pts, outline=(200, 180, 120), width=3)
# Reflexo suave no espelho
draw.rectangle([710, 90, 890, 420], fill=(208, 220, 228))
for i in range(3):
    draw.line([(720+i*50, 90), (720+i*50+30, 420)], fill=(220, 230, 240), width=8)

# ─── MACA DE ESTÉTICA (centro, perspectiva 3/4) ──────────────────────────────
# Base da maca — pernas cromadas
for x in [330, 360, 560, 590]:
    draw.rectangle([x, 440, x+8, 510], fill=(160, 160, 168))
    draw.ellipse([x-4, 438, x+12, 446], fill=(145, 145, 152))

# Corpo da maca (colchão)
maca_pts = [(310, 320), (610, 310), (615, 445), (315, 455)]
draw.polygon(maca_pts, fill=(248, 242, 238))
# Contorno
draw.polygon(maca_pts, outline=(220, 210, 205), width=2)
# Textura acolchoada (linhas suaves)
for i in range(1, 5):
    x_off = i * 60
    draw.line([(310+x_off, 320), (315+x_off, 455)], fill=(235, 228, 222), width=1)
draw.line([(310, 380), (615, 370)], fill=(235, 228, 222), width=1)

# Encosto reclinado
back_pts = [(310, 180), (420, 178), (420, 325), (310, 325)]
draw.polygon(back_pts, fill=(245, 238, 234))
draw.polygon(back_pts, outline=(220, 210, 205), width=2)
draw.line([(310, 255), (420, 252)], fill=(235, 228, 222), width=1)
# Apoio de cabeça (pequeno)
draw.rectangle([318, 155, 412, 185], fill=(240, 233, 228))
draw.rectangle([318, 155, 412, 185], outline=(215, 205, 200), width=2)

# Papel protetor (lençol descartável)
paper_pts = [(312, 310), (612, 300), (614, 385), (312, 395)]
draw.polygon(paper_pts, fill=(252, 250, 248))
draw.polygon(paper_pts, outline=(230, 225, 220), width=1)
# Linhas do papel crepe
for i in range(10):
    y_p = 308 + i*9
    draw.line([(312, y_p), (612, y_p-4)], fill=(242, 240, 238), width=1)

# Almofada
draw.ellipse([318, 160, 415, 195], fill=(248, 243, 240))
draw.ellipse([320, 162, 413, 193], outline=(225, 215, 210), width=1)

# ─── EQUIPAMENTO de estética (lateral esquerda) ─────────────────────────────
# Aparelho sobre carrinho
draw.rectangle([100, 290, 240, 460], fill=(235, 230, 228))
draw.rectangle([100, 290, 240, 460], outline=(210, 200, 195), width=2)
# Tela do aparelho
draw.rectangle([112, 300, 228, 365], fill=(30, 35, 50))
draw.rectangle([115, 303, 225, 362], fill=(20, 130, 180))
# "tela apagada" — simulando desligado
draw.line([(140, 325), (200, 345)], fill=(15, 100, 140), width=2)
# Botões do aparelho
for i, col in enumerate([(200,200,200),(180,60,60),(60,160,60)]):
    draw.ellipse([118+i*30, 372, 138+i*30, 392], fill=col)
    draw.ellipse([119+i*30, 373, 137+i*30, 391], outline=(160,160,160), width=1)
# Rodas do carrinho
draw.rectangle([105, 458, 235, 475], fill=(180, 175, 172))
for rx in [120, 170, 220]:
    draw.ellipse([rx-10, 468, rx+10, 488], fill=(100,100,100))
# Ponteira/cabo do equipamento saindo
draw.line([(170, 290), (290, 240)], fill=(120, 115, 112), width=6)
draw.ellipse([285, 232, 300, 248], fill=(80, 75, 72))

# ─── LUZ DE TETO (spotlight dramático) ──────────────────────────────────────
light_img = Image.new("RGBA", (W, H), (0,0,0,0))
light_draw = ImageDraw.Draw(light_img)
# Cone de luz do teto em direção à maca
cx, cy = 465, 0
for radius in range(300, 0, -10):
    alpha = int(18 * (1 - radius/300))
    light_draw.ellipse([cx-radius, cy, cx+radius, cy+radius*2], fill=(255, 248, 230, alpha))
img = Image.alpha_composite(img.convert("RGBA"), light_img).convert("RGB")
draw = ImageDraw.Draw(img)

# Luminária no teto
draw.ellipse([430, 5, 500, 28], fill=(220, 215, 210))
draw.ellipse([435, 8, 495, 25], fill=(255, 255, 240))
draw.ellipse([450, 12, 480, 22], fill=(255, 255, 200))

# ─── PLACA NA PAREDE ─────────────────────────────────────────────────────────
draw.rectangle([140, 80, 280, 120], fill=(248, 244, 235))
draw.rectangle([140, 80, 280, 120], outline=(200, 180, 100), width=2)
try:
    fp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    draw.text((148, 87), "CLINICA DE ESTETICA", font=fp, fill=(80, 60, 20))
    fp2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    draw.text((148, 103), "Alvara Sanitario n. ----", font=fp2, fill=(120, 100, 60))
except:
    pass

# ─── OVERLAY DRAMÁTICO (gradiente escuro de baixo pra cima, mais forte) ──────
ov = Image.new("RGBA", (W, H), (0,0,0,0))
ov_d = ImageDraw.Draw(ov)
for y in range(H):
    # Escuro no topo (cena), muito mais escuro na metade inferior (texto)
    if y < 520:
        alpha = int(80 * (y / 520))
    else:
        alpha = int(80 + 155 * ((y-520)/(H-520)))
    ov_d.line([(0,y),(W,y)], fill=(0,0,0,alpha))
img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
draw = ImageDraw.Draw(img)

# ─── FITA DE INTERDIÇÃO (realista, perspectiva, cruzando a cena) ─────────────
def draw_realistic_tape(draw, y_center, angle_deg, thickness, label="INTERDITADO"):
    """Fita mais realista com sombra, brilho e texto."""
    angle = math.radians(angle_deg)
    length = int(W / abs(math.cos(angle)) + 200) if abs(math.cos(angle)) > 0.01 else W + 200

    cx, cy = W//2, y_center
    x1 = int(cx - math.cos(angle)*length/2)
    y1 = int(cy - math.sin(angle)*length/2)
    x2 = int(cx + math.cos(angle)*length/2)
    y2 = int(cy + math.sin(angle)*length/2)

    perp = angle + math.pi/2
    half = thickness // 2

    stripe_w = 55
    n = int(length / stripe_w) + 4

    # Sombra da fita
    shadow_ov = Image.new("RGBA", (W, H), (0,0,0,0))
    shadow_d = ImageDraw.Draw(shadow_ov)
    for i in range(n):
        sx = x1 + int(math.cos(angle) * i * stripe_w) + 6
        sy = y1 + int(math.sin(angle) * i * stripe_w) + 6
        ex = sx + int(math.cos(angle) * stripe_w)
        ey = sy + int(math.sin(angle) * stripe_w)
        pts = [
            (int(sx + math.cos(perp)*half*1.3), int(sy + math.sin(perp)*half*1.3)),
            (int(sx - math.cos(perp)*half*1.3), int(sy - math.sin(perp)*half*1.3)),
            (int(ex - math.cos(perp)*half*1.3), int(ey - math.sin(perp)*half*1.3)),
            (int(ex + math.cos(perp)*half*1.3), int(ey + math.sin(perp)*half*1.3)),
        ]
        shadow_d.polygon(pts, fill=(0, 0, 0, 80))

    # Listras da fita
    tape_ov = Image.new("RGBA", (W, H), (0,0,0,0))
    tape_d = ImageDraw.Draw(tape_ov)
    for i in range(n):
        col = WARN_Y if i % 2 == 0 else WARN_B
        sx = x1 + int(math.cos(angle) * i * stripe_w)
        sy = y1 + int(math.sin(angle) * i * stripe_w)
        ex = sx + int(math.cos(angle) * stripe_w)
        ey = sy + int(math.sin(angle) * stripe_w)
        pts = [
            (int(sx + math.cos(perp)*half), int(sy + math.sin(perp)*half)),
            (int(sx - math.cos(perp)*half), int(sy - math.sin(perp)*half)),
            (int(ex - math.cos(perp)*half), int(ey - math.sin(perp)*half)),
            (int(ex + math.cos(perp)*half), int(ey + math.sin(perp)*half)),
        ]
        tape_d.polygon(pts, fill=(*col, 235))

    # Brilho na borda superior da fita
    highlight_ov = Image.new("RGBA", (W, H), (0,0,0,0))
    h_d = ImageDraw.Draw(highlight_ov)
    h_d.line(
        [(x1 + int(math.cos(perp)*half*0.7), y1 + int(math.sin(perp)*half*0.7)),
         (x2 + int(math.cos(perp)*half*0.7), y2 + int(math.sin(perp)*half*0.7))],
        fill=(255, 255, 255, 60), width=3
    )

    return shadow_ov, tape_ov, highlight_ov

# Fita 1 — cruzando diagonalmente
s1, t1, h1 = draw_realistic_tape(draw, 330, -7, 50)
img = Image.alpha_composite(img.convert("RGBA"), s1)
img = Image.alpha_composite(img, t1)
img = Image.alpha_composite(img, h1)

# Fita 2 — paralela abaixo
s2, t2, h2 = draw_realistic_tape(draw, 390, -7, 50)
img = Image.alpha_composite(img, s2)
img = Image.alpha_composite(img, t2)
img = Image.alpha_composite(img, h2)
img = img.convert("RGB")
draw = ImageDraw.Draw(img)

# Texto "INTERDITADO" nas fitas (rotacionado)
try:
    f_tape = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except:
    f_tape = ImageFont.load_default()

tape_text_img = Image.new("RGBA", (W, H), (0,0,0,0))
tape_text_draw = ImageDraw.Draw(tape_text_img)
for xp in range(-50, W+100, 190):
    tape_text_draw.text((xp, 322), "INTERDITADO", font=f_tape, fill=(10, 10, 10, 210))
    tape_text_draw.text((xp+95, 382), "INTERDITADO", font=f_tape, fill=(10, 10, 10, 210))
tape_rot = tape_text_img.rotate(-7, expand=False, resample=Image.BICUBIC)
img = Image.alpha_composite(img.convert("RGBA"), tape_rot).convert("RGB")
draw = ImageDraw.Draw(img)

# ─── LACRE OFICIAL (selo vermelho na porta/maca) ─────────────────────────────
seal_cx, seal_cy = 780, 240
draw.ellipse([seal_cx-52, seal_cy-52, seal_cx+52, seal_cy+52], fill=(185, 20, 20))
draw.ellipse([seal_cx-46, seal_cy-46, seal_cx+46, seal_cy+46], fill=(200, 30, 30))
draw.ellipse([seal_cx-40, seal_cy-40, seal_cx+40, seal_cy+40], outline=(220, 180, 180), width=2)
try:
    f_seal_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 9)
    f_seal_lg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    draw.text((seal_cx-32, seal_cy-18), "VIGILANCIA", font=f_seal_lg, fill=WHITE)
    draw.text((seal_cx-28, seal_cy-2), "SANITARIA", font=f_seal_lg, fill=WHITE)
    draw.text((seal_cx-24, seal_cy+14), "INTERDITADO", font=f_seal_sm, fill=(255,220,220))
except:
    pass
# Raios ao redor do lacre
for ang in range(0, 360, 30):
    r = math.radians(ang)
    x1s = int(seal_cx + math.cos(r)*52)
    y1s = int(seal_cy + math.sin(r)*52)
    x2s = int(seal_cx + math.cos(r)*60)
    y2s = int(seal_cy + math.sin(r)*60)
    draw.line([(x1s,y1s),(x2s,y2s)], fill=(200,30,30), width=2)

# ─── FONTES ──────────────────────────────────────────────────────────────────
def font(size, bold=True):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    try: return ImageFont.truetype(p, size)
    except: return ImageFont.load_default()

def sans(size, bold=True):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    try: return ImageFont.truetype(p, size)
    except: return ImageFont.load_default()

def ctext(draw, text, y, fnt, color, shadow=None, wrap=980):
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        bb = draw.textbbox((0,0), test, font=fnt)
        if bb[2]-bb[0] <= wrap:
            line = test
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    for l in lines:
        bb = draw.textbbox((0,0), l, font=fnt)
        tw = bb[2]-bb[0]
        x = (W-tw)//2
        if shadow:
            for dx,dy in [(-2,-2),(2,-2),(-2,2),(2,2),(0,3),(3,0),(-3,0)]:
                draw.text((x+dx,y+dy), l, font=fnt, fill=shadow)
        draw.text((x,y), l, font=fnt, fill=color)
        y += (bb[3]-bb[1]) + 10
    return y

# ─── PAINEL TEXTO (metade inferior, fundo escuro premium) ────────────────────
panel = Image.new("RGBA", (W, H), (0,0,0,0))
pd = ImageDraw.Draw(panel)
pd.rectangle([0, 450, W, H], fill=(6, 5, 5, 238))
img = Image.alpha_composite(img.convert("RGBA"), panel).convert("RGB")
draw = ImageDraw.Draw(img)

# Linha dourada separadora
draw.line([(60, 458), (W-60, 458)], fill=GOLD, width=2)

# ─── COPY ─────────────────────────────────────────────────────────────────────
y = 472

f_tag = sans(19, bold=False)
y = ctext(draw, "Sua clinica de estetica passaria em uma fiscalizacao hoje?", y, f_tag, CREAM) + 6

f_big = font(80, bold=True)
y = ctext(draw, "FECHADA PELA", y, f_big, WHITE, shadow=(70,0,0)) - 4
y = ctext(draw, "VIGILANCIA", y, f_big, RED, shadow=(60,0,0)) - 4
f_big2 = font(56, bold=True)
y = ctext(draw, "SANITARIA.", y, f_big2, RED, shadow=(50,0,0)) + 10

f_mid = sans(23, bold=False)
y = ctext(draw, "Isso acontece todo dia com clinicas de estetica no Brasil.", y, f_mid, CREAM) + 6
f_mid2 = sans(22, bold=True)
y = ctext(draw, "Eu ajudo a sua a nunca ser uma delas.", y, f_mid2, GOLD) + 18

# Linha separadora ornamental
line_y = y
draw.line([(100, line_y), (W-100, line_y)], fill=GOLD2, width=1)
draw.polygon([(W//2-5,line_y-5),(W//2,line_y-11),(W//2+5,line_y-5),(W//2,line_y+1)], fill=GOLD)
y = line_y + 16

# ─── CTA ──────────────────────────────────────────────────────────────────────
btn = "QUERO PROTEGER MINHA CLINICA  >>"
f_cta = sans(26, bold=True)
bb = draw.textbbox((0,0), btn, font=f_cta)
bw = bb[2]-bb[0]+70
bh = bb[3]-bb[1]+28
bx = (W-bw)//2
by = y
draw.rectangle([bx+5, by+5, bx+bw+5, by+bh+5], fill=(90, 70, 5))
draw.rectangle([bx, by, bx+bw, by+bh], fill=GOLD)
draw.rectangle([bx+3, by+3, bx+bw-3, by+bh-3], outline=(10,10,10), width=2)
draw.text((bx+35, by+14), btn, font=f_cta, fill=BLACK)
y = by + bh + 14

# ─── RODAPÉ ──────────────────────────────────────────────────────────────────
f_rod = sans(16, bold=True)
f_rod2 = sans(14, bold=False)
ctext(draw, "Dra. Juliana Ramos de Freitas", y, f_rod, GOLD)
ctext(draw, "Especialista em proteger clinicas de estetica  |  Link na bio", y+22, f_rod2, (150, 132, 55))

# ─── BORDA DUPLA ─────────────────────────────────────────────────────────────
draw.rectangle([0,0,W-1,H-1], outline=GOLD, width=5)
draw.rectangle([9,9,W-10,H-10], outline=GOLD2, width=1)

# Cantos
for cx2, cy2, fx, fy in [(0,0,1,1),(W,0,-1,1),(0,H,1,-1),(W,H,-1,-1)]:
    for i in range(20, 50, 8):
        draw.line([(cx2+fx*16, cy2+fy*i),(cx2+fx*i, cy2+fy*i)], fill=GOLD, width=2)
        draw.line([(cx2+fx*i, cy2+fy*16),(cx2+fx*i, cy2+fy*i)], fill=GOLD, width=2)

img.save(OUT, quality=95)
print("Salvo:", OUT)
