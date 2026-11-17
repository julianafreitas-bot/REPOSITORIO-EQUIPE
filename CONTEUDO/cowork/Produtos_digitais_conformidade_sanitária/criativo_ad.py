from PIL import Image, ImageDraw, ImageFont
import math

# 1080x1080 — formato quadrado Instagram (funciona no feed e stories cortado)
W, H = 1080, 1080
img = Image.new("RGB", (W, H), "#000000")
draw = ImageDraw.Draw(img)

GOLD  = (221, 198, 95)
GOLDD = (160, 130, 30)
WHITE = (255, 255, 255)
CREAM = (245, 237, 210)
RED   = (220, 50, 50)
DARK  = (8, 6, 2)

# ── Fundo: gradiente preto para dark marrom ──
for y in range(H):
    t = y / H
    r = int(8  + t * 20)
    g = int(6  + t * 12)
    b = int(2  + t * 4)
    draw.line([(0,y),(W,y)], fill=(r,g,b))

# ── Borda dourada ──
draw.rectangle([0,0,W-1,H-1], outline=GOLD, width=8)
draw.rectangle([12,12,W-13,H-13], outline=GOLDD, width=2)

# ── Faixa de alerta vermelha no topo ──
draw.rectangle([0, 0, W, 90], fill=(180, 30, 30))
draw.rectangle([0, 86, W, 90], fill=GOLD)

try:
    f_alert = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    f_big   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 72)
    f_med   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 46)
    f_sub   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    f_body  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)
    f_cta   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    f_price = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 58)
    f_prsmall = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except:
    f_alert = f_small = f_big = f_med = f_sub = f_body = f_cta = f_price = f_prsmall = ImageFont.load_default()

def ctext(text, y, font, color, shadow=False):
    w = draw.textlength(text, font=font)
    x = (W - w) / 2
    if shadow:
        draw.text((x+2, y+2), text, fill=(40,30,0), font=font)
    draw.text((x, y), text, fill=color, font=font)

# ── Faixa alerta texto ──
alert = "⚠  A VIGILÂNCIA SANITÁRIA NÃO AVISA ANTES DE CHEGAR  ⚠"
aw = draw.textlength(alert, font=f_alert)
draw.text(((W-aw)/2, 22), alert, fill=WHITE, font=f_alert)

# ── Pergunta principal ──
ctext("Sua clínica está", 118, f_sub, CREAM)

ctext("PREPARADA", 154, f_big, WHITE, shadow=True)

ctext("para uma fiscalização", 234, f_sub, CREAM)
ctext("SURPRESA?", 270, f_big, GOLD, shadow=True)

# ── Divisor dourado ──
draw.line([(60, 358), (W-60, 358)], fill=GOLD, width=2)
# diamantes
for dx in [-60, -30, 0, 30, 60]:
    draw.polygon([(W//2+dx, 352),(W//2+dx+6,358),(W//2+dx,364),(W//2+dx-6,358)], fill=GOLD)

# ── O que você aprende ──
ctext("O GUIA QUE TODO DONO DE CLÍNICA PRECISAVA", 380, f_small, GOLD)

items = [
    "► Como se preparar ANTES da fiscalização",
    "► Documentação obrigatória — checklist completo",
    "► Seus direitos durante a vistoria",
    "► Como contestar autos de infração",
    "► Blindagem jurídica para seu negócio",
]

y0 = 416
for item in items:
    iw = draw.textlength(item, font=f_body)
    draw.text(((W-iw)/2, y0), item, fill=CREAM, font=f_body)
    y0 += 36

# ── Divisor ──
draw.line([(60, 610), (W-60, 610)], fill=GOLDD, width=1)

# ── Caixa preta central com preço ──
draw.rectangle([120, 630, W-120, 810], fill=(0,0,0))
draw.rectangle([120, 630, W-120, 810], outline=GOLD, width=3)

# acima
ctext("ACESSO IMEDIATO  |  EBOOK DIGITAL", 645, f_small, GOLD)

# De por
ctext("de R$ 197  por apenas", 680, f_prsmall, CREAM)

# Preço
ctext("R$ 47,00", 700, f_price, GOLD, shadow=True)

# Garantia
ctext("► Garantia de 7 dias", 775, f_prsmall, CREAM)

# ── CTA ──
# botão
draw.rectangle([180, 830, W-180, 920], fill=GOLD)
draw.rectangle([182, 832, W-182, 918], fill=GOLDD)
draw.rectangle([185, 835, W-185, 915], fill=GOLD)

cta = "QUERO MEU GUIA AGORA →"
ctaw = draw.textlength(cta, font=f_cta)
draw.text(((W-ctaw)/2 + 1, 858), cta, fill=(10,8,2), font=f_cta)
draw.text(((W-ctaw)/2, 857), cta, fill=(0,0,0), font=f_cta)

# ── Assinatura ──
ctext("Dra. Juliana Ramos de Freitas  ·  Advogada  ·  Direito Sanitário", 940, f_small, GOLDD)

# ── Cantos ornamentais ──
def corner(cx, cy, fx, fy):
    draw.line([(cx, cy),(cx+fx*40, cy)], fill=GOLD, width=2)
    draw.line([(cx, cy),(cx, cy+fy*40)], fill=GOLD, width=2)
corner(22,22,1,1); corner(W-22,22,-1,1); corner(22,H-22,1,-1); corner(W-22,H-22,-1,-1)

out = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/Criativo_Ad_GuiaFiscalizacao.png"
img.save(out, "PNG", dpi=(150,150))
print("Saved:", out)
