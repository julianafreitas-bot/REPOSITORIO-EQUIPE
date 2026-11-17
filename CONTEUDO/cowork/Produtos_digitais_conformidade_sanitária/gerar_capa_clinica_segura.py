from PIL import Image, ImageDraw, ImageFont
import os

W, H = 800, 1100
img = Image.new("RGB", (W, H), "#000000")
draw = ImageDraw.Draw(img)

# Gold color
GOLD = "#DDC65F"
WHITE = "#FFFFFF"
GRAY = "#999999"

# Top gold bar
draw.rectangle([(0, 0), (W, 6)], fill=GOLD)

# Bottom gold bar
draw.rectangle([(0, H-6), (W, H)], fill=GOLD)

# Decorative side lines
draw.rectangle([(40, 40), (44, H-40)], fill=GOLD)
draw.rectangle([(W-44, 40), (W-40, H-40)], fill=GOLD)

# Corner decorations
for x, y in [(40, 40), (W-40, 40), (40, H-40), (W-40, H-40)]:
    draw.ellipse([(x-5, y-5), (x+5, y+5)], fill=GOLD)

# Logo / Initials
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 72)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 28)
    font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    font_price = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 40)
    font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_name = font_title
    font_tag = font_title
    font_desc = font_title
    font_price = font_title
    font_badge = font_title

# Monogram circle at top
cx, cy = W//2, 160
r = 70
draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)], outline=GOLD, width=2)
draw.ellipse([(cx-r+8, cy-r+8), (cx+r-8, cy+r-8)], outline=GOLD, width=1)
# Letters JF
draw.text((cx, cy), "JF", font=font_title, fill=GOLD, anchor="mm")

# Thin gold line under monogram
draw.rectangle([(W//2-60, cy+r+20), (W//2+60, cy+r+22)], fill=GOLD)

# CLÍNICA SEGURA - main title
y_start = 310
draw.text((W//2, y_start), "CLÍNICA", font=font_sub, fill=GOLD, anchor="mm")
draw.text((W//2, y_start+50), "SEGURA", font=font_sub, fill=WHITE, anchor="mm")

# Gold divider
draw.rectangle([(W//2-100, y_start+90), (W//2+100, y_start+92)], fill=GOLD)

# Subtitle
draw.text((W//2, y_start+120), "Consultoria Premium em", font=font_name, fill=GRAY, anchor="mm")
draw.text((W//2, y_start+148), "Conformidade Sanitária", font=font_name, fill=GRAY, anchor="mm")

# Benefits section
y_benefits = 580
benefits = [
    "✦  Adequação completa à Vigilância Sanitária",
    "✦  Documentação clínica personalizada",
    "✦  Proteção jurídica e protocolar",
    "✦  Blindagem contra autuações e interdições",
    "✦  Acompanhamento contínuo especializado",
]
for i, b in enumerate(benefits):
    draw.text((W//2, y_benefits + i*42), b, font=font_badge, fill=WHITE if i % 2 == 0 else GRAY, anchor="mm")

# Gold line
draw.rectangle([(80, 800), (W-80, 802)], fill=GOLD)

# Price badge area
draw.rounded_rectangle([(160, 820), (W-160, 890)], radius=4, outline=GOLD, width=1)
draw.text((W//2, 855), "Investimento: R$ 20.000", font=font_price, fill=GOLD, anchor="mm")

# Author
draw.text((W//2, 940), "Dra. Juliana Ramos de Freitas", font=font_desc, fill=WHITE, anchor="mm")
draw.text((W//2, 974), "Advogada · Direito Sanitário", font=font_name, fill=GRAY, anchor="mm")

# Bottom gold line accent
draw.rectangle([(W//2-40, 1010), (W//2+40, 1012)], fill=GOLD)

out = "/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/CAPA_ClinicaSegura.png"
img.save(out, "PNG")
print(f"Salvo: {out}")
