from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1080, 1080
OUT = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL"

GOLD  = (221, 198, 95)
GOLDD = (160, 130, 30)
GOLDB = (255, 235, 140)
WHITE = (255, 255, 255)
CREAM = (245, 237, 210)
BLACK = (0, 0, 0)
RED   = (190, 30, 30)
DARK  = (8, 6, 2)

def load_fonts():
    base = "/usr/share/fonts/truetype/dejavu/"
    try:
        return {
            "bold_lg":  ImageFont.truetype(base+"DejaVuSans-Bold.ttf", 34),
            "bold_xl":  ImageFont.truetype(base+"DejaVuSans-Bold.ttf", 46),
            "bold_xxl": ImageFont.truetype(base+"DejaVuSerif-Bold.ttf", 76),
            "bold_md":  ImageFont.truetype(base+"DejaVuSans-Bold.ttf", 26),
            "bold_sm":  ImageFont.truetype(base+"DejaVuSans-Bold.ttf", 20),
            "reg_md":   ImageFont.truetype(base+"DejaVuSans.ttf", 24),
            "reg_sm":   ImageFont.truetype(base+"DejaVuSans.ttf", 19),
            "serif_xl": ImageFont.truetype(base+"DejaVuSerif-Bold.ttf", 58),
            "serif_lg": ImageFont.truetype(base+"DejaVuSerif-Bold.ttf", 44),
            "serif_md": ImageFont.truetype(base+"DejaVuSerif-Bold.ttf", 32),
            "cta":      ImageFont.truetype(base+"DejaVuSans-Bold.ttf", 32),
        }
    except:
        d = ImageFont.load_default()
        return {k: d for k in ["bold_lg","bold_xl","bold_xxl","bold_md","bold_sm","reg_md","reg_sm","serif_xl","serif_lg","serif_md","cta"]}

F = load_fonts()

def bg_gradient(draw, color_top=(8,4,0), color_bot=(20,14,4)):
    for y in range(H):
        t = y/H
        r = int(color_top[0]*(1-t) + color_bot[0]*t)
        g = int(color_top[1]*(1-t) + color_bot[1]*t)
        b = int(color_top[2]*(1-t) + color_bot[2]*t)
        draw.line([(0,y),(W,y)], fill=(r,g,b))

def border(draw, color=GOLD, w=6):
    draw.rectangle([0,0,W-1,H-1], outline=color, width=w)
    draw.rectangle([10,10,W-11,H-11], outline=GOLDD, width=1)

def ctext(draw, text, y, font, color, shadow_color=None, offset=2):
    tw = draw.textlength(text, font=font)
    x = (W-tw)/2
    if shadow_color:
        draw.text((x+offset, y+offset), text, fill=shadow_color, font=font)
    draw.text((x, y), text, fill=color, font=font)

def ltext(draw, text, x, y, font, color):
    draw.text((x, y), text, fill=color, font=font)

def divider_gold(draw, y, margin=60):
    draw.line([(margin, y),(W-margin, y)], fill=GOLDD, width=1)
    for dx in [-40,-20,0,20,40]:
        sz=5 if dx==0 else 4
        draw.polygon([(W//2+dx,y-sz),(W//2+dx+sz,y),(W//2+dx,y+sz),(W//2+dx-sz,y)], fill=GOLD)

def cta_button(draw, text, y_center, bg=GOLD, fg=BLACK):
    bh = 72
    y0 = y_center - bh//2
    y1 = y_center + bh//2
    draw.rectangle([100, y0, W-100, y1], fill=bg)
    draw.rectangle([104, y0+4, W-104, y1-4], fill=GOLDD)
    draw.rectangle([108, y0+8, W-108, y1-8], fill=bg)
    tw = draw.textlength(text, font=F["cta"])
    draw.text(((W-tw)/2+1, y_center-18), text, fill=(10,8,0), font=F["cta"])
    draw.text(((W-tw)/2, y_center-19), text, fill=fg, font=F["cta"])

def author_line(draw, y):
    t = "Dra. Juliana Ramos de Freitas  -  Advogada  -  Direito Sanitario"
    ctext(draw, t, y, F["reg_sm"], GOLDD)

def corner_brackets(draw):
    for cx,cy,sx,sy in [(22,22,1,1),(W-22,22,-1,1),(22,H-22,1,-1),(W-22,H-22,-1,-1)]:
        draw.line([(cx,cy),(cx+sx*44,cy)], fill=GOLD, width=2)
        draw.line([(cx,cy),(cx,cy+sy*44)], fill=GOLD, width=2)


# ═══════════════════════════════════════════════════════
# CRIATIVO A — ANGULO DA DOR / MEDO
# Gancho: "Você pode perder sua clínica em uma tarde"
# ═══════════════════════════════════════════════════════
img = Image.new("RGB",(W,H))
draw = ImageDraw.Draw(img)
bg_gradient(draw, (10,2,2), (18,8,4))
border(draw)
corner_brackets(draw)

# Faixa vermelha topo
draw.rectangle([0,0,W,88], fill=(160,20,20))
draw.rectangle([0,84,W,88], fill=GOLD)
ctext(draw, "ATENCAO: VOCE PODE PERDER SUA CLINICA", 18, F["bold_lg"], WHITE)
ctext(draw, "em uma unica visita da Vigilancia Sanitaria", 56, F["bold_sm"], CREAM)

# Headline
ctext(draw, "SUA CLINICA", 120, F["serif_lg"], WHITE, (80,20,20))
ctext(draw, "SOBREVIVERIA", 170, F["bold_xxl"], WHITE, (80,20,20))
ctext(draw, "a uma fiscalizacao", 258, F["serif_lg"], GOLDB, (60,40,0))
ctext(draw, "SURPRESA?", 308, F["bold_xxl"], GOLDB, (60,40,0))

divider_gold(draw, 402)

# O que acontece quem nao esta preparado
ctext(draw, "Quem nao se prepara, arrisca:", 418, F["bold_md"], CREAM)

risks = [
    "  Multas de R$ 2.000 a R$ 75.000",
    "  Embargo e interdição imediata",
    "  Processo administrativo e criminal",
    "  Anos de trabalho perdidos em horas",
]
y0 = 456
for r in risks:
    tw = draw.textlength("X "+r, font=F["reg_md"])
    x0 = (W-tw)/2 - 10
    draw.ellipse([x0-2, y0+6, x0+12, y0+20], fill=RED)
    draw.text((x0+18, y0), r, fill=CREAM, font=F["reg_md"])
    y0 += 38

divider_gold(draw, 618)

# CTA
ctext(draw, "Existe uma saida. E e mais simples do que voce imagina.", 638, F["bold_sm"], GOLD)
ctext(draw, "Guia Pratico para Fiscalizacao Sanitaria", 668, F["serif_md"], WHITE)

cta_button(draw, "QUERO ME PROTEGER AGORA  >>", 800)

author_line(draw, 870)
ctext(draw, "Clique no link do perfil", 900, F["reg_sm"], GOLDD)

img.save(f"{OUT}/Criativo_A_Dor.png","PNG",dpi=(150,150))
print("Criativo A salvo.")


# ═══════════════════════════════════════════════════════
# CRIATIVO B — ANGULO DA CURIOSIDADE / ERRO
# Gancho: "3 erros que fazem clínicas serem autuadas"
# ═══════════════════════════════════════════════════════
img = Image.new("RGB",(W,H))
draw = ImageDraw.Draw(img)
bg_gradient(draw, (4,6,10), (8,12,20))
border(draw, GOLD, 6)
corner_brackets(draw)

# Faixa azul-escuro topo
draw.rectangle([0,0,W,88], fill=(20,40,80))
draw.rectangle([0,84,W,88], fill=GOLD)
ctext(draw, "GUIA PRATICO PARA FISCALIZACAO SANITARIA", 20, F["bold_md"], GOLD)
ctext(draw, "Dra. Juliana Ramos de Freitas  -  Direito Sanitario", 54, F["bold_sm"], CREAM)

# Headline curiosidade
ctext(draw, "3 erros que fazem", 112, F["serif_md"], CREAM)
ctext(draw, "CLINICAS SEREM", 152, F["bold_xxl"], GOLDB, (40,50,80))
ctext(draw, "AUTUADAS", 238, F["bold_xxl"], GOLDB, (40,50,80))
ctext(draw, "(e voce provavelmente comete pelo menos 1)", 328, F["bold_sm"], CREAM)

divider_gold(draw, 378)

# Os 3 erros
erros = [
    ("01", "Alvara Sanitario desatualizado ou em local errado"),
    ("02", "Documentacao dos profissionais incompleta"),
    ("03", "Ausencia de protocolo de descarte de residuos"),
]
y0 = 404
for num, texto in erros:
    # numero em circulo
    draw.ellipse([80, y0-4, 130, y0+44], fill=GOLD)
    nw = draw.textlength(num, font=F["bold_md"])
    draw.text((80+(50-nw)/2, y0+6), num, fill=(10,8,0), font=F["bold_md"])
    # texto
    draw.text((150, y0+2), texto, fill=WHITE, font=F["bold_md"])
    y0 += 68

divider_gold(draw, 614)

ctext(draw, "Ha muito mais no guia completo.", 634, F["bold_md"], GOLDB)
ctext(draw, "Checklists. Direitos. Como contestar autuacoes.", 668, F["reg_md"], CREAM)

cta_button(draw, "VER O GUIA COMPLETO  >>", 790)

author_line(draw, 862)
ctext(draw, "Clique no link do perfil", 890, F["reg_sm"], GOLDD)

# Monograma JF pequeno
cx2, cy2, r2 = 540, 960, 34
draw.ellipse([cx2-r2,cy2-r2,cx2+r2,cy2+r2], outline=GOLD, width=2)
draw.ellipse([cx2-r2+3,cy2-r2+3,cx2+r2-3,cy2+r2-3], fill=(4,6,10))
jfw = draw.textlength("JF", font=F["bold_md"])
draw.text((cx2-jfw/2, cy2-14), "JF", fill=GOLD, font=F["bold_md"])

img.save(f"{OUT}/Criativo_B_Curiosidade.png","PNG",dpi=(150,150))
print("Criativo B salvo.")


# ═══════════════════════════════════════════════════════
# CRIATIVO C — ANGULO DA AUTORIDADE / TRANSFORMACAO
# Gancho: "Depois desse guia, você nunca mais vai ter medo"
# ═══════════════════════════════════════════════════════
img = Image.new("RGB",(W,H))
draw = ImageDraw.Draw(img)
bg_gradient(draw, (4,4,2), (14,10,4))
border(draw)
corner_brackets(draw)

# Topo dourado
draw.rectangle([0,0,W,88], fill=GOLD)
draw.rectangle([0,84,W,88], fill=GOLDD)
t_top = "DRA. JULIANA RAMOS DE FREITAS  -  ADVOGADA"
ttw = draw.textlength(t_top, font=F["bold_md"])
draw.text(((W-ttw)/2, 14), t_top, fill=(8,6,0), font=F["bold_md"])
t2_top = "Especialista em Direito Sanitario"
t2w = draw.textlength(t2_top, font=F["bold_sm"])
draw.text(((W-t2w)/2, 52), t2_top, fill=(30,22,0), font=F["bold_sm"])

# Headline transformacao
ctext(draw, "Depois desse guia...", 110, F["serif_md"], GOLDB)

ctext(draw, "VOCE NUNCA MAIS", 158, F["bold_xxl"], WHITE, (60,50,0))
ctext(draw, "vai ter medo de uma", 248, F["serif_lg"], CREAM)
ctext(draw, "FISCALIZACAO", 296, F["bold_xxl"], GOLDB, (60,50,0))

divider_gold(draw, 392)

# Antes x Depois — 2 colunas
col_w = 430
# Antes
draw.rectangle([36, 412, 36+col_w, 590], fill=(40,10,10))
draw.rectangle([36, 412, 36+col_w, 590], outline=(160,30,30), width=2)
ltext(draw, "ANTES", 44, 420, F["bold_md"], (200,60,60))
antess = ["x Entrava em panico", "x Nao sabia seus direitos", "x Se sentia indefesa", "x Improvisava na hora"]
ya = 456
for a in antess:
    ltext(draw, a, 52, ya, F["reg_sm"], CREAM)
    ya += 34

# Depois
draw.rectangle([W-36-col_w, 412, W-36, 590], fill=(10,30,10))
draw.rectangle([W-36-col_w, 412, W-36, 590], outline=GOLDD, width=2)
ltext(draw, "DEPOIS", W-36-col_w+10, 420, F["bold_md"], GOLD)
depoisl = ["+ Sabe exatamente o que fazer", "+ Conhece seus direitos", "+ Documenta tudo certo", "+ Fica tranquila na vistoria"]
yd = 456
for d in depoisl:
    ltext(draw, d, W-36-col_w+10, yd, F["reg_sm"], CREAM)
    yd += 34

divider_gold(draw, 610)

# Credencial
ctext(draw, "Aprenda com quem ja acompanhou dezenas", 630, F["bold_sm"], CREAM)
ctext(draw, "de fiscalizacoes em clinicas pelo Brasil.", 656, F["bold_sm"], CREAM)

# Capa ebook pequena simulada
draw.rectangle([440, 680, 640, 760], fill=(20,15,5))
draw.rectangle([440, 680, 640, 760], outline=GOLD, width=2)
gt = "GUIA PRATICO"
gtw = draw.textlength(gt, font=F["bold_sm"])
draw.text(((1080-gtw)/2, 698), gt, fill=GOLDB, font=F["bold_sm"])
ft = "Fiscalizacao Sanitaria"
ftw = draw.textlength(ft, font=F["reg_sm"])
draw.text(((1080-ftw)/2, 726), ft, fill=CREAM, font=F["reg_sm"])

cta_button(draw, "QUERO ESSA TRANSFORMACAO  >>", 830)

author_line(draw, 905)
ctext(draw, "Clique no link do perfil", 932, F["reg_sm"], GOLDD)

img.save(f"{OUT}/Criativo_C_Autoridade.png","PNG",dpi=(150,150))
print("Criativo C salvo.")

print("\nTodos os criativos salvos!")
