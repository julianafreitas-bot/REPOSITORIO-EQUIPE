"""
CAMPANHA: Guia Prático para Fiscalização Sanitária
Público: Donas/gestoras de clínicas de estética
CTA: Envie GUIA no direct (ManyChat)

Uso:
    python gerar_criativos.py

Gera 4 imagens 1080x1080px na mesma pasta do script.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random, os

# ─── CONFIG ──────────────────────────────────────────────────────────────────
W, H = 1080, 1080
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

GOLD   = (221, 198, 95)
GOLD2  = (170, 148, 55)
BLACK  = (8, 8, 8)
WHITE  = (255, 255, 255)
RED    = (190, 25, 25)
CREAM  = (240, 228, 195)
WARN_Y = (255, 200, 0)
WARN_B = (18, 18, 18)
DARK   = (12, 10, 10)

AUTOR  = "Dra. Juliana Ramos de Freitas"
SPEC   = "Especialista em proteger clinicas de estetica"
CTA_MANYCHAT = "Envie GUIA no direct  >>"

# ─── HELPERS ─────────────────────────────────────────────────────────────────
def font(size, bold=True):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    try: return ImageFont.truetype(p, size)
    except: return ImageFont.load_default()

def sans(size, bold=True):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    try: return ImageFont.truetype(p, size)
    except: return ImageFont.load_default()

def ctext(draw, text, y, fnt, color, shadow=None, wrap=960):
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        bb = draw.textbbox((0, 0), test, font=fnt)
        if bb[2] - bb[0] <= wrap:
            line = test
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    for l in lines:
        bb = draw.textbbox((0, 0), l, font=fnt)
        tw = bb[2] - bb[0]
        x = (W - tw) // 2
        if shadow:
            for dx, dy in [(-2,-2),(2,-2),(-2,2),(2,2),(0,3),(3,0),(-3,0)]:
                draw.text((x+dx, y+dy), l, font=fnt, fill=shadow)
        draw.text((x, y), l, font=fnt, fill=color)
        y += (bb[3] - bb[1]) + 10
    return y

def border_and_corners(draw):
    draw.rectangle([0, 0, W-1, H-1], outline=GOLD, width=5)
    draw.rectangle([10, 10, W-11, H-11], outline=GOLD2, width=1)
    for cx, cy, fx, fy in [(0,0,1,1),(W,0,-1,1),(0,H,1,-1),(W,H,-1,-1)]:
        for i in range(20, 50, 8):
            draw.line([(cx+fx*16, cy+fy*i),(cx+fx*i, cy+fy*i)], fill=GOLD, width=2)
            draw.line([(cx+fx*i, cy+fy*16),(cx+fx*i, cy+fy*i)], fill=GOLD, width=2)

def divider(draw, y):
    draw.line([(80, y), (W-80, y)], fill=GOLD2, width=1)
    draw.polygon([(W//2-6, y-6),(W//2, y-12),(W//2+6, y-6),(W//2, y)], fill=GOLD)
    return y + 16

def cta_button(draw, y, text=CTA_MANYCHAT):
    f_cta = sans(28, bold=True)
    bb = draw.textbbox((0, 0), text, font=f_cta)
    bw = bb[2] - bb[0] + 80
    bh = bb[3] - bb[1] + 30
    bx = (W - bw) // 2
    draw.rectangle([bx+5, y+5, bx+bw+5, y+bh+5], fill=(90, 70, 5))
    draw.rectangle([bx, y, bx+bw, y+bh], fill=GOLD)
    draw.rectangle([bx+3, y+3, bx+bw-3, y+bh-3], outline=BLACK, width=2)
    draw.text((bx+40, y+15), text, font=f_cta, fill=BLACK)
    return y + bh + 12

def footer(draw, y):
    f1 = sans(17, bold=True)
    f2 = sans(14, bold=False)
    ctext(draw, AUTOR, y, f1, GOLD)
    ctext(draw, SPEC, y + 22, f2, (150, 132, 55))

def dark_gradient(img, from_y=0, strength=200):
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(ov)
    for y in range(H):
        if y < from_y:
            alpha = 0
        else:
            alpha = int(strength * ((y - from_y) / (H - from_y)) ** 0.7)
        d.line([(0,y),(W,y)], fill=(0,0,0,alpha))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

def solid_panel(img, y_start, alpha=238):
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(ov)
    d.rectangle([0, y_start, W, H], fill=(6, 5, 5, alpha))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

def vgrad(draw, y1, y2, c1, c2):
    for y in range(y1, y2):
        t = (y - y1) / max(y2 - y1, 1)
        r = int(c1[0] + (c2[0]-c1[0])*t)
        g = int(c1[1] + (c2[1]-c1[1])*t)
        b = int(c1[2] + (c2[2]-c1[2])*t)
        draw.line([(0,y),(W,y)], fill=(r,g,b))

# ═════════════════════════════════════════════════════════════════════════════
# CRIATIVO 01 — DOR / MEDO
# "Sua clínica sobreviveria a uma fiscalização surpresa?"
# ═════════════════════════════════════════════════════════════════════════════
def criativo_01():
    img = Image.new("RGB", (W, H), BLACK)
    draw = ImageDraw.Draw(img)

    # Fundo: gradiente escuro com leve tom vermelho no topo
    vgrad(draw, 0, H, (35, 8, 8), (6, 4, 4))

    # Banner de alerta no topo
    draw.rectangle([0, 0, W, 88], fill=(170, 15, 15))
    f_alert = sans(26, bold=True)
    ctext(draw, "ATENCAO: VOCE PODE PERDER SUA CLINICA DE ESTETICA", 14, f_alert, WHITE)
    f_alert2 = sans(16, bold=False)
    ctext(draw, "em uma unica visita da Vigilancia Sanitaria", 50, f_alert2, (255, 200, 200))

    draw = ImageDraw.Draw(img)
    y = 100

    # Headline
    f_big = font(88, bold=True)
    y = ctext(draw, "SUA CLINICA DE", y, f_big, WHITE, shadow=(60,0,0)) - 4
    y = ctext(draw, "ESTETICA", y, f_big, WHITE, shadow=(60,0,0)) + 2
    y = ctext(draw, "SOBREVIVERIA", y, font(62, bold=True), GOLD, shadow=(80,60,0)) + 4
    y = ctext(draw, "a uma fiscalizacao SURPRESA?", y, font(40, bold=True), CREAM) + 18

    y = divider(draw, y) + 8

    # Lista de riscos
    f_label = sans(24, bold=True)
    f_item  = sans(23, bold=False)
    ctext(draw, "Quem nao se prepara, arrisca:", y, f_label, CREAM)
    y += 40
    risks = [
        "Multas de R$ 2.000 a R$ 75.000",
        "Embargo e interdicao imediata",
        "Processo administrativo e criminal",
        "Anos de trabalho perdidos em horas",
    ]
    for r in risks:
        draw.ellipse([90, y+4, 112, y+26], fill=RED)
        draw.text((125, y), r, font=f_item, fill=CREAM)
        y += 46

    y = divider(draw, y + 14) + 12

    f_sol = sans(22, bold=False)
    ctext(draw, "Existe uma saida. E mais simples do que voce imagina.", y, f_sol, GOLD)
    y += 38
    f_prod = font(30, bold=True)
    ctext(draw, "Guia Pratico para Fiscalizacao Sanitaria", y, f_prod, WHITE)
    y += 58

    y = cta_button(draw, y)
    footer(draw, y)
    border_and_corners(draw)

    out = os.path.join(OUT_DIR, "Criativo_01_Dor.png")
    img.save(out)
    print(f"[OK] {out}")


# ═════════════════════════════════════════════════════════════════════════════
# CRIATIVO 02 — CENA VISUAL (clínica interditada — mais impactante)
# ═════════════════════════════════════════════════════════════════════════════
def draw_tape_layer(base_img, y_center, angle_deg=-7, thickness=52):
    angle = math.radians(angle_deg)
    cx, cy = W // 2, y_center
    length = int(W / max(abs(math.cos(angle)), 0.01)) + 300
    x1 = int(cx - math.cos(angle) * length / 2)
    y1 = int(cy - math.sin(angle) * length / 2)
    perp = angle + math.pi / 2
    half = thickness // 2
    stripe_w = 52

    # sombra
    sh = Image.new("RGBA", (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(sh)
    n = int(length / stripe_w) + 4
    for i in range(n):
        sx = x1 + int(math.cos(angle)*i*stripe_w)+7
        sy = y1 + int(math.sin(angle)*i*stripe_w)+7
        ex = sx + int(math.cos(angle)*stripe_w)
        ey = sy + int(math.sin(angle)*stripe_w)
        pts = [(int(sx+math.cos(perp)*half*1.4), int(sy+math.sin(perp)*half*1.4)),
               (int(sx-math.cos(perp)*half*1.4), int(sy-math.sin(perp)*half*1.4)),
               (int(ex-math.cos(perp)*half*1.4), int(ey-math.sin(perp)*half*1.4)),
               (int(ex+math.cos(perp)*half*1.4), int(ey+math.sin(perp)*half*1.4))]
        sd.polygon(pts, fill=(0,0,0,90))

    # listras
    tp = Image.new("RGBA", (W, H), (0,0,0,0))
    td = ImageDraw.Draw(tp)
    for i in range(n):
        col = (*WARN_Y, 240) if i % 2 == 0 else (*WARN_B, 240)
        sx = x1 + int(math.cos(angle)*i*stripe_w)
        sy = y1 + int(math.sin(angle)*i*stripe_w)
        ex = sx + int(math.cos(angle)*stripe_w)
        ey = sy + int(math.sin(angle)*stripe_w)
        pts = [(int(sx+math.cos(perp)*half), int(sy+math.sin(perp)*half)),
               (int(sx-math.cos(perp)*half), int(sy-math.sin(perp)*half)),
               (int(ex-math.cos(perp)*half), int(ey-math.sin(perp)*half)),
               (int(ex+math.cos(perp)*half), int(ey+math.sin(perp)*half))]
        td.polygon(pts, fill=col)

    result = Image.alpha_composite(base_img.convert("RGBA"), sh)
    result = Image.alpha_composite(result, tp)
    return result.convert("RGB")


def criativo_02():
    img = Image.new("RGB", (W, H), (242, 237, 234))
    draw = ImageDraw.Draw(img)

    # Parede fundo rosê claro
    vgrad(draw, 0, 510, (238, 230, 226), (215, 205, 200))

    # Azulejos parede
    wall_line = (208, 198, 194)
    for x in range(0, W+1, 108): draw.line([(x,0),(x,510)], fill=wall_line, width=1)
    for y in range(0, 511, 108): draw.line([(0,y),(W,y)], fill=wall_line, width=1)

    # Skirting board
    draw.rectangle([0, 492, W, 510], fill=(192, 182, 177))
    draw.rectangle([0, 510, W, 516], fill=(178, 168, 162))

    # Chão mármore
    vgrad(draw, 516, H, (215, 207, 202), (225, 218, 214))
    random.seed(7)
    for _ in range(7):
        x0 = random.randint(0, W)
        pts = [(x0, 516)]
        for _ in range(random.randint(4,7)):
            x0 += random.randint(-70, 90)
            pts.append((x0, min(pts[-1][1]+random.randint(25,70), H)))
        for i in range(len(pts)-1):
            draw.line([pts[i], pts[i+1]], fill=(193, 185, 180), width=1)

    # Espelho
    mir = [(680, 55), (885, 75), (885, 430), (680, 450)]
    draw.polygon(mir, fill=(195, 212, 222))
    draw.polygon(mir, outline=(195, 172, 110), width=4)
    draw.rectangle([692, 80, 875, 425], fill=(205, 220, 230))
    for i in range(3):
        draw.line([(705+i*45, 80),(718+i*45, 425)], fill=(215, 228, 238), width=9)

    # Maca estética
    for x in [318, 348, 552, 582]:
        draw.rectangle([x, 438, x+8, 512], fill=(152, 152, 160))
        draw.ellipse([x-4, 435, x+12, 444], fill=(138, 138, 145))
    maca = [(295, 315),(605, 305),(610, 442),(300, 452)]
    draw.polygon(maca, fill=(248, 242, 238))
    draw.polygon(maca, outline=(218, 208, 203), width=2)
    for i in range(1, 5):
        draw.line([(295+i*62, 315),(300+i*62, 452)], fill=(235, 228, 222), width=1)
    draw.line([(295, 378),(610, 368)], fill=(232, 225, 220), width=1)
    # Encosto
    back = [(295, 175),(415, 173),(415, 318),(295, 320)]
    draw.polygon(back, fill=(245, 238, 234))
    draw.polygon(back, outline=(218, 208, 203), width=2)
    draw.rectangle([303, 148, 408, 180], fill=(240, 233, 228))
    draw.rectangle([303, 148, 408, 180], outline=(213, 203, 198), width=2)
    # Papel
    paper = [(297, 308),(607, 298),(609, 382),(299, 392)]
    draw.polygon(paper, fill=(252, 250, 248))
    for i in range(10):
        draw.line([(297, 308+i*9),(607, 300+i*9)], fill=(242, 240, 238), width=1)

    # Aparelho estético
    draw.rectangle([90, 285, 230, 458], fill=(232, 226, 223))
    draw.rectangle([90, 285, 230, 458], outline=(205, 195, 190), width=2)
    draw.rectangle([102, 295, 218, 362], fill=(28, 33, 48))
    draw.rectangle([105, 298, 215, 358], fill=(18, 125, 175))
    for i, c in enumerate([(195,195,195),(175,55,55),(55,155,55)]):
        draw.ellipse([108+i*32, 368, 128+i*32, 388], fill=c)
    draw.rectangle([95, 455, 225, 472], fill=(175, 170, 166))
    for rx in [115, 160, 210]:
        draw.ellipse([rx-10, 465, rx+10, 485], fill=(95,95,95))
    draw.line([(160, 285),(285, 235)], fill=(115,110,107), width=6)
    draw.ellipse([280, 227, 295, 243], fill=(75,70,67))

    # Placa na parede
    draw.rectangle([130, 75, 278, 116], fill=(248, 243, 234))
    draw.rectangle([130, 75, 278, 116], outline=(195, 175, 95), width=2)
    try:
        fp = sans(11, bold=True)
        draw.text((138, 82), "CLINICA DE ESTETICA", font=fp, fill=(75, 55, 15))
        fp2 = sans(9, bold=False)
        draw.text((138, 99), "Alvara Sanitario n. ----", font=fp2, fill=(115, 95, 55))
    except: pass

    # Luminária
    draw.ellipse([428, 4, 498, 27], fill=(218, 212, 206))
    draw.ellipse([433, 7, 493, 24], fill=(255, 255, 240))
    draw.ellipse([448, 11, 478, 21], fill=(255, 255, 200))
    light = Image.new("RGBA", (W, H), (0,0,0,0))
    ld = ImageDraw.Draw(light)
    for r in range(280, 0, -10):
        a = int(16*(1-r/280))
        ld.ellipse([463-r, 0, 463+r, r*2], fill=(255,248,228,a))
    img = Image.alpha_composite(img.convert("RGBA"), light).convert("RGB")

    # Gradiente escuro
    img = dark_gradient(img, from_y=0, strength=110)
    img = solid_panel(img, y_start=450, alpha=242)
    draw = ImageDraw.Draw(img)

    # Fitas de interdição
    img = draw_tape_layer(img, 310, angle_deg=-7, thickness=52)
    img = draw_tape_layer(img, 372, angle_deg=-7, thickness=52)
    draw = ImageDraw.Draw(img)

    # Texto "INTERDITADO" nas fitas
    try: f_tape = sans(22, bold=True)
    except: f_tape = ImageFont.load_default()
    tt = Image.new("RGBA", (W, H), (0,0,0,0))
    ttd = ImageDraw.Draw(tt)
    for xp in range(-60, W+120, 195):
        ttd.text((xp, 322), "INTERDITADO", font=f_tape, fill=(10,10,10,215))
        ttd.text((xp+95, 384), "INTERDITADO", font=f_tape, fill=(10,10,10,215))
    tt_rot = tt.rotate(-7, expand=False, resample=Image.BICUBIC)
    img = Image.alpha_composite(img.convert("RGBA"), tt_rot).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Lacre vermelho
    scx, scy = 775, 235
    draw.ellipse([scx-54,scy-54,scx+54,scy+54], fill=(180,18,18))
    draw.ellipse([scx-47,scy-47,scx+47,scy+47], fill=(198,28,28))
    draw.ellipse([scx-40,scy-40,scx+40,scy+40], outline=(218,178,178), width=2)
    for ang in range(0, 360, 30):
        r2 = math.radians(ang)
        draw.line([(int(scx+math.cos(r2)*53),int(scy+math.sin(r2)*53)),
                   (int(scx+math.cos(r2)*61),int(scy+math.sin(r2)*61))], fill=(198,28,28), width=2)
    try:
        fs = sans(9, bold=True)
        fl = sans(13, bold=True)
        draw.text((scx-30,scy-20), "VIGILANCIA", font=fl, fill=WHITE)
        draw.text((scx-28,scy-4), "SANITARIA", font=fl, fill=WHITE)
        draw.text((scx-26,scy+13), "INTERDITADO", font=fs, fill=(255,215,215))
    except: pass

    # Linha separadora
    draw.line([(60, 460),(W-60, 460)], fill=GOLD, width=2)

    y = 474
    f_tag = sans(20, bold=False)
    y = ctext(draw, "Sua clinica de estetica passaria em uma fiscalizacao hoje?", y, f_tag, CREAM) + 4
    f_big = font(80, bold=True)
    y = ctext(draw, "FECHADA PELA", y, f_big, WHITE, shadow=(65,0,0)) - 6
    y = ctext(draw, "VIGILANCIA", y, f_big, RED, shadow=(55,0,0)) - 6
    y = ctext(draw, "SANITARIA.", y, font(56, bold=True), RED, shadow=(45,0,0)) + 8
    y = ctext(draw, "Isso acontece todo dia com clinicas de estetica.", y + 2, sans(22, bold=False), CREAM) + 4
    y = ctext(draw, "Eu ajudo a sua a nunca ser uma delas.", y, sans(22, bold=True), GOLD) + 16

    y = divider(draw, y) + 4
    y = cta_button(draw, y)
    footer(draw, y)
    border_and_corners(draw)

    out = os.path.join(OUT_DIR, "Criativo_02_Cena.png")
    img.save(out)
    print(f"[OK] {out}")


# ═════════════════════════════════════════════════════════════════════════════
# CRIATIVO 03 — CURIOSIDADE
# "3 erros que fazem clínicas de estética serem autuadas"
# ═════════════════════════════════════════════════════════════════════════════
def criativo_03():
    img = Image.new("RGB", (W, H), BLACK)
    draw = ImageDraw.Draw(img)
    vgrad(draw, 0, H, (14, 18, 38), (6, 8, 18))

    # Header
    draw.rectangle([0, 0, W, 78], fill=(20, 28, 60))
    f_h = sans(22, bold=True)
    ctext(draw, "GUIA PRATICO PARA FISCALIZACAO SANITARIA", 12, f_h, GOLD)
    f_h2 = sans(15, bold=False)
    ctext(draw, "Clinicas de Estetica | Dra. Juliana Ramos de Freitas", 44, f_h2, CREAM)

    draw = ImageDraw.Draw(img)
    y = 96

    f_tag2 = sans(24, bold=False)
    y = ctext(draw, "3 erros que fazem", y, f_tag2, CREAM) + 2
    f_big = font(82, bold=True)
    y = ctext(draw, "CLINICAS DE", y, f_big, GOLD, shadow=(80, 60, 0)) - 4
    y = ctext(draw, "ESTETICA", y, f_big, GOLD, shadow=(80, 60, 0)) - 4
    y = ctext(draw, "SEREM AUTUADAS", y, font(54, bold=True), WHITE, shadow=(40,40,40)) + 4
    y = ctext(draw, "(e voce provavelmente comete pelo menos 1)", y + 2, sans(20, bold=False), (180, 165, 105)) + 16

    y = divider(draw, y) + 8

    erros = [
        ("01", "Alvara Sanitario desatualizado ou em local errado"),
        ("02", "Documentacao dos profissionais incompleta"),
        ("03", "Ausencia de protocolo de descarte de residuos"),
    ]
    f_num = sans(28, bold=True)
    f_err = sans(22, bold=True)
    for num, txt in erros:
        r = 28
        cx2, cy2 = 108, y + r
        draw.ellipse([cx2-r, cy2-r, cx2+r, cy2+r], fill=GOLD)
        draw.ellipse([cx2-r+3, cy2-r+3, cx2+r-3, cy2+r-3], fill=BLACK)
        bb = draw.textbbox((0,0), num, font=f_num)
        draw.text((cx2-(bb[2]-bb[0])//2, cy2-(bb[3]-bb[1])//2), num, font=f_num, fill=GOLD)
        draw.text((148, y + 4), txt, font=f_err, fill=WHITE)
        y += 68

    y = divider(draw, y + 6) + 6

    f_sub = sans(22, bold=True)
    y = ctext(draw, "Ha muito mais no guia completo.", y, f_sub, GOLD) + 2
    f_sub2 = sans(20, bold=False)
    y = ctext(draw, "Checklists. Seus direitos. Como contestar autuacoes.", y, f_sub2, CREAM) + 18

    y = cta_button(draw, y)

    # JF monogram
    mx, my = W//2, y + 20
    draw.ellipse([mx-28, my-28, mx+28, my+28], fill=BLACK)
    draw.ellipse([mx-28, my-28, mx+28, my+28], outline=GOLD, width=2)
    try:
        f_jf = sans(20, bold=True)
        draw.text((mx-13, my-12), "JF", font=f_jf, fill=GOLD)
    except: pass
    y = my + 36

    footer(draw, y + 4)
    border_and_corners(draw)

    out = os.path.join(OUT_DIR, "Criativo_03_Curiosidade.png")
    img.save(out)
    print(f"[OK] {out}")


# ═════════════════════════════════════════════════════════════════════════════
# CRIATIVO 04 — AUTORIDADE / TRANSFORMAÇÃO (Antes x Depois)
# "Você nunca mais vai ter medo de uma fiscalização"
# ═════════════════════════════════════════════════════════════════════════════
def criativo_04():
    img = Image.new("RGB", (W, H), BLACK)
    draw = ImageDraw.Draw(img)
    vgrad(draw, 0, H, (8, 8, 10), (15, 12, 8))

    # Header dourado — autoridade
    draw.rectangle([0, 0, W, 80], fill=GOLD)
    f_name = sans(22, bold=True)
    bb = draw.textbbox((0,0), AUTOR, font=f_name)
    draw.text(((W-(bb[2]-bb[0]))//2, 12), AUTOR, font=f_name, fill=BLACK)
    f_spec2 = sans(17, bold=False)
    bb2 = draw.textbbox((0,0), SPEC, font=f_spec2)
    draw.text(((W-(bb2[2]-bb2[0]))//2, 46), SPEC, font=f_spec2, fill=(30, 25, 5))

    draw = ImageDraw.Draw(img)
    y = 98

    f_intro = sans(22, bold=False)
    y = ctext(draw, "Depois desse guia...", y, f_intro, CREAM) + 4

    f_big = font(74, bold=True)
    y = ctext(draw, "VOCE NUNCA MAIS", y, f_big, WHITE, shadow=(50,50,50)) - 2
    f_big2 = font(50, bold=True)
    y = ctext(draw, "vai ter medo de uma", y, f_big2, CREAM) - 2
    y = ctext(draw, "FISCALIZACAO", y, font(68, bold=True), GOLD, shadow=(80,60,0)) + 14

    y = divider(draw, y) + 10

    # Colunas Antes x Depois
    col_w = 460
    col_h = 220
    margin = 30
    col_y = y

    # ANTES — fundo vermelho escuro
    draw.rectangle([margin, col_y, margin+col_w, col_y+col_h], fill=(55, 10, 10))
    draw.rectangle([margin, col_y, margin+col_w, col_y+col_h], outline=RED, width=2)
    f_col_title = sans(26, bold=True)
    draw.text((margin+20, col_y+12), "ANTES", font=f_col_title, fill=RED)
    f_col_item = sans(18, bold=False)
    antes = ["x Entrava em panico", "x Nao sabia seus direitos",
             "x Se sentia indefesa", "x Improvisava na hora"]
    for i, a in enumerate(antes):
        draw.text((margin+20, col_y+52+i*38), a, font=f_col_item, fill=(220,180,180))

    # DEPOIS — fundo verde escuro
    d_x = W - margin - col_w
    draw.rectangle([d_x, col_y, d_x+col_w, col_y+col_h], fill=(8, 45, 20))
    draw.rectangle([d_x, col_y, d_x+col_w, col_y+col_h], outline=(40, 160, 80), width=2)
    draw.text((d_x+20, col_y+12), "DEPOIS", font=f_col_title, fill=(60, 200, 100))
    depois = ["+ Sabe exatamente o que fazer", "+ Conhece seus direitos",
              "+ Documenta tudo certo", "+ Fica tranquila na vistoria"]
    for i, d in enumerate(depois):
        draw.text((d_x+20, col_y+52+i*38), d, font=f_col_item, fill=(170, 230, 190))

    y = col_y + col_h + 20

    f_auth = sans(20, bold=True)
    ctext(draw, "Aprenda com quem ja acompanhou dezenas", y, f_auth, CREAM)
    y += 30
    ctext(draw, "de fiscalizacoes em clinicas de estetica pelo Brasil.", y, f_auth, CREAM)
    y += 42

    # Mini capa do produto
    pc_w, pc_h = 180, 54
    pc_x = (W - pc_w) // 2
    draw.rectangle([pc_x, y, pc_x+pc_w, y+pc_h], fill=(20, 18, 15))
    draw.rectangle([pc_x, y, pc_x+pc_w, y+pc_h], outline=GOLD, width=2)
    f_mini = sans(13, bold=True)
    bb = draw.textbbox((0,0), "GUIA PRATICO", font=f_mini)
    draw.text((pc_x+(pc_w-(bb[2]-bb[0]))//2, y+8), "GUIA PRATICO", font=f_mini, fill=GOLD)
    f_mini2 = sans(11, bold=False)
    bb2 = draw.textbbox((0,0), "Fiscalizacao Sanitaria", font=f_mini2)
    draw.text((pc_x+(pc_w-(bb2[2]-bb2[0]))//2, y+30), "Fiscalizacao Sanitaria", font=f_mini2, fill=CREAM)
    y += pc_h + 16

    y = cta_button(draw, y)
    footer(draw, y)
    border_and_corners(draw)

    out = os.path.join(OUT_DIR, "Criativo_04_Autoridade.png")
    img.save(out)
    print(f"[OK] {out}")


# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Gerando criativos...\n")
    criativo_01()
    criativo_02()
    criativo_03()
    criativo_04()
    print("\nTodos os criativos gerados com sucesso!")
    print(f"Pasta: {OUT_DIR}")
