from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

W, H = 1080, 1080
GOLD = (221, 198, 95)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (200, 30, 30)
CREAM = (245, 235, 200)
DARK_BLUE = (12, 18, 35)

OUT = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/Criativo_Clinica_Interditada.png"

img = Image.new("RGB", (W, H), BLACK)
draw = ImageDraw.Draw(img)

# ── FUNDO: corredor de clínica estilizado ─────────────────────────────────────
# Chão com azulejos (perspectiva)
floor_y = 420
# Parede fundo
draw.rectangle([0, 0, W, floor_y], fill=(235, 240, 245))

# Linhas de azulejo na parede (grid)
wall_color = (210, 218, 228)
for x in range(0, W+1, 90):
    draw.line([(x, 0), (x, floor_y)], fill=wall_color, width=1)
for y in range(0, floor_y+1, 90):
    draw.line([(0, y), (W, y)], fill=wall_color, width=1)

# Moldura de porta ao fundo (centro)
door_left, door_right = 360, 720
door_top, door_bottom = 60, floor_y
draw.rectangle([door_left, door_top, door_right, door_bottom], fill=(200, 210, 220))
# Sombra da porta
draw.rectangle([door_left, door_top, door_right, door_bottom], outline=(170, 180, 195), width=3)
# Janela interna da porta
inner = 20
draw.rectangle([door_left+inner, door_top+inner, door_right-inner, door_bottom-20], fill=(180, 195, 210))
# Cruz da janela
mid_x = (door_left + door_right) // 2
mid_y = (door_top + door_bottom) // 2
draw.line([(mid_x, door_top+inner), (mid_x, door_bottom-20)], fill=(160, 175, 190), width=2)
draw.line([(door_left+inner, mid_y), (door_right-inner, mid_y)], fill=(160, 175, 190), width=2)
# Maçaneta
draw.ellipse([door_right-35, mid_y-8, door_right-15, mid_y+8], fill=(180, 155, 80))

# Cruz médica na parede esquerda
def medical_cross(draw, cx, cy, size, color):
    t = size // 4
    draw.rectangle([cx-t, cy-size//2, cx+t, cy+size//2], fill=color)
    draw.rectangle([cx-size//2, cy-t, cx+size//2, cy+t], fill=color)

medical_cross(draw, 150, 200, 80, (180, 220, 200))
medical_cross(draw, 930, 200, 80, (180, 220, 200))

# Chão (perspectiva com linhas)
floor_color = (200, 205, 210)
draw.rectangle([0, floor_y, W, H], fill=floor_color)
# Linhas de perspectiva no chão
vp_x, vp_y = 540, floor_y
for angle in range(-90, 91, 15):
    rad = math.radians(angle)
    end_x = int(vp_x + math.sin(rad) * 2000)
    end_y = int(vp_y + abs(math.cos(rad)) * 800)
    draw.line([(vp_x, vp_y), (end_x, end_y)], fill=(185, 190, 195), width=1)
# Grade horizontal do chão
for y in range(floor_y, H+1, 60):
    draw.line([(0, y), (W, y)], fill=(185, 190, 195), width=1)

# ── SOBREPOSIÇÃO ESCURA gradual (de baixo) ────────────────────────────────────
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)
# Gradiente: transparente no topo, preto no fundo
for y in range(H):
    alpha = int(220 * (y / H) ** 0.7)
    ov_draw.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
draw = ImageDraw.Draw(img)

# ── FITA DE INTERDIÇÃO (diagonal, cruzando a cena) ───────────────────────────
def draw_tape_stripe(draw, x1, y1, x2, y2, thickness, col1, col2):
    import math
    length = math.hypot(x2-x1, y2-y1)
    angle = math.atan2(y2-y1, x2-x1)
    stripe_w = 60
    n_stripes = int(length / stripe_w) + 2
    for i in range(n_stripes):
        color = col1 if i % 2 == 0 else col2
        sx = x1 + math.cos(angle) * (i * stripe_w - stripe_w)
        sy = y1 + math.sin(angle) * (i * stripe_w - stripe_w)
        ex = x1 + math.cos(angle) * ((i+1) * stripe_w)
        ey = y1 + math.sin(angle) * ((i+1) * stripe_w)
        perp = angle + math.pi/2
        pts = [
            (sx + math.cos(perp)*thickness/2, sy + math.sin(perp)*thickness/2),
            (sx - math.cos(perp)*thickness/2, sy - math.sin(perp)*thickness/2),
            (ex - math.cos(perp)*thickness/2, ey - math.sin(perp)*thickness/2),
            (ex + math.cos(perp)*thickness/2, ey + math.sin(perp)*thickness/2),
        ]
        draw.polygon([(int(p[0]), int(p[1])) for p in pts], fill=color)

# Fita 1 - atravessa de canto a canto
draw_tape_stripe(draw, -50, 310, W+50, 470, 42, (230, 185, 0), (20, 20, 20))
# Fita 2 - segunda fita paralela abaixo
draw_tape_stripe(draw, -50, 370, W+50, 530, 42, (230, 185, 0), (20, 20, 20))

# Texto "INTERDITADO" nas fitas
try:
    font_tape = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
except:
    font_tape = ImageFont.load_default()

# Rotação do texto nas fitas
tape_img = Image.new("RGBA", (W, H), (0,0,0,0))
tape_draw = ImageDraw.Draw(tape_img)
for x_pos in range(-100, W+200, 240):
    tape_draw.text((x_pos, 330), "INTERDITADO", font=font_tape, fill=(20, 20, 20, 220))
# Leve rotação para combinar com as fitas
tape_rot = tape_img.rotate(-8, expand=False)
img = Image.alpha_composite(img.convert("RGBA"), tape_rot).convert("RGB")
draw = ImageDraw.Draw(img)

# ── PAINEL ESCURO SEMI-TRANSPARENTE (área de texto inferior) ─────────────────
panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
panel_draw = ImageDraw.Draw(panel)
panel_draw.rectangle([0, 500, W, H], fill=(5, 5, 5, 230))
img = Image.alpha_composite(img.convert("RGBA"), panel).convert("RGB")
draw = ImageDraw.Draw(img)

# ── FONTE ─────────────────────────────────────────────────────────────────────
def font(size, bold=True):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def sans(size, bold=True):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def ctext(draw, text, y, fnt, color, shadow=None, max_width=None):
    if max_width:
        # word wrap
        words = text.split()
        lines = []
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            bb = draw.textbbox((0,0), test, font=fnt)
            if bb[2] - bb[0] <= max_width:
                line = test
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
        for i, l in enumerate(lines):
            bb = draw.textbbox((0,0), l, font=fnt)
            tw = bb[2]-bb[0]
            x = (W - tw) // 2
            if shadow:
                for dx, dy in [(-2,-2),(2,-2),(-2,2),(2,2),(0,3),(3,0)]:
                    draw.text((x+dx, y+dy), l, font=fnt, fill=shadow)
            draw.text((x, y), l, font=fnt, fill=color)
            y += (bb[3]-bb[1]) + 12
        return y
    else:
        bb = draw.textbbox((0,0), text, font=fnt)
        tw = bb[2]-bb[0]
        x = (W - tw) // 2
        if shadow:
            for dx, dy in [(-2,-2),(2,-2),(-2,2),(2,2),(0,3),(3,0)]:
                draw.text((x+dx, y+dy), text, font=fnt, fill=shadow)
        draw.text((x, y), text, font=fnt, fill=color)
        return y + (bb[3]-bb[1]) + 8

# ── EMBLEMA OFICIAL (canto superior esquerdo) ─────────────────────────────────
# Circulo dourado com texto "VIGILÂNCIA SANITÁRIA"
emblem_cx, emblem_cy = 90, 70
draw.ellipse([emblem_cx-55, emblem_cy-55, emblem_cx+55, emblem_cy+55], fill=GOLD)
draw.ellipse([emblem_cx-48, emblem_cy-48, emblem_cx+48, emblem_cy+48], fill=BLACK)
draw.ellipse([emblem_cx-42, emblem_cy-42, emblem_cx+42, emblem_cy+42], outline=GOLD, width=2)
# Cruz no emblema
medical_cross(draw, emblem_cx, emblem_cy, 30, GOLD)

# Texto ao lado do emblema
f_emblem = sans(16, bold=True)
draw.text((155, 45), "AVISO SANITARIO", font=f_emblem, fill=GOLD)
f_sub = sans(13, bold=False)
draw.text((155, 67), "Regulamentacao ANVISA/CVS", font=f_sub, fill=(180, 160, 80))

# ── HEADLINE PRINCIPAL ────────────────────────────────────────────────────────
y = 510

# Linha intro
f_intro = sans(24, bold=False)
y = ctext(draw, "Isso acontece com quem nao se prepara:", y, f_intro, CREAM) + 4

# Headline grande
f_big = font(76, bold=True)
y = ctext(draw, "CLINICA", y, f_big, WHITE, shadow=(80,0,0)) + 2
y = ctext(draw, "INTERDITADA", y, f_big, RED, shadow=(60,0,0)) + 2

# Linha de impacto
f_mid = sans(28, bold=True)
y = ctext(draw, "em uma unica visita da Vigilancia Sanitaria.", y, f_mid, CREAM) + 18

# Separador dourado
line_y = y
draw.line([(120, line_y), (W-120, line_y)], fill=GOLD, width=2)
# Losango central
draw.polygon([(W//2-6, line_y-6),(W//2, line_y-12),(W//2+6, line_y-6),(W//2, line_y)], fill=GOLD)
y = line_y + 20

# Sub
f_sub2 = sans(22, bold=False)
y = ctext(draw, "O Guia Pratico para Fiscalizacao Sanitaria", y, f_sub2, GOLD) + 2
f_sub3 = sans(20, bold=False)
y = ctext(draw, "mostra como evitar isso — antes que seja tarde.", y, f_sub3, CREAM) + 22

# ── CTA BUTTON ────────────────────────────────────────────────────────────────
btn_text = "QUERO ME PROTEGER  >>"
f_cta = sans(30, bold=True)
bb = draw.textbbox((0,0), btn_text, font=f_cta)
bw, bh = bb[2]-bb[0]+80, bb[3]-bb[1]+28
bx = (W - bw) // 2
by = y
# Sombra
draw.rectangle([bx+4, by+4, bx+bw+4, by+bh+4], fill=(100, 80, 0))
# Botão
draw.rectangle([bx, by, bx+bw, by+bh], fill=GOLD)
draw.rectangle([bx+3, by+3, bx+bw-3, by+bh-3], outline=BLACK, width=2)
draw.text((bx+40, by+14), btn_text, font=f_cta, fill=BLACK)
y = by + bh + 18

# ── RODAPÉ ────────────────────────────────────────────────────────────────────
f_rod = sans(18, bold=False)
ctext(draw, "Dra. Juliana Ramos de Freitas  -  Advogada  -  Direito Sanitario", y, f_rod, (160, 140, 60))
ctext(draw, "Clique no link do perfil", y+26, f_rod, (130, 110, 50))

# ── BORDA DUPLA ───────────────────────────────────────────────────────────────
draw.rectangle([0, 0, W-1, H-1], outline=GOLD, width=5)
draw.rectangle([10, 10, W-11, H-11], outline=(120, 100, 40), width=2)

# ── CANTOS ORNAMENTAIS ────────────────────────────────────────────────────────
for cx2, cy2, flip_x, flip_y in [(0,0,1,1),(W,0,-1,1),(0,H,1,-1),(W,H,-1,-1)]:
    for i in range(30, 55, 8):
        draw.line([(cx2+flip_x*18, cy2+flip_y*i),(cx2+flip_x*i, cy2+flip_y*i)], fill=GOLD, width=2)
        draw.line([(cx2+flip_x*i, cy2+flip_y*18),(cx2+flip_x*i, cy2+flip_y*i)], fill=GOLD, width=2)

img.save(OUT)
print("Salvo:", OUT)
