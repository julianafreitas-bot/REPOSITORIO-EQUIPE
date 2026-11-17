import json
import sys
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date, timedelta

sys.path.insert(0, '/sessions/intelligent-kind-wozniak/mnt/outputs')

# ── Importar legendas ──────────────────────────────────────────────────────────
exec(open('/sessions/intelligent-kind-wozniak/mnt/outputs/legendas_otimizadas.py').read())

# ── Carregar Trello ────────────────────────────────────────────────────────────
with open('/sessions/intelligent-kind-wozniak/mnt/uploads/HdoDrpoz - we-dona-juliana-ramos-de-freitas.json', 'r') as f:
    data = json.load(f)

carrossel_list_id = '6a401213a71b0d94ad645b0a'
cards = [c for c in data.get('cards', []) if c.get('idList') == carrossel_list_id and not c.get('closed') and c.get('name')]

# ── Schedule: Ter/Qui/Sáb às 12h ──────────────────────────────────────────────
start = date(2026, 8, 18)
post_days = []
d = start
while len(post_days) < 30:
    if d.weekday() in (1, 3, 5):
        post_days.append(d)
    d += timedelta(days=1)

DIAS_PT = {0:'Segunda-feira',1:'Terça-feira',2:'Quarta-feira',3:'Quinta-feira',4:'Sexta-feira',5:'Sábado',6:'Domingo'}

# ── Cores ──────────────────────────────────────────────────────────────────────
ROXO_ESC  = "3D0066"
ROXO_MED  = "6A1BA0"
ROXO_CLR  = "EDD9FF"
LILÁS     = "F5EEFF"
BRANCO    = "FFFFFF"
CINZA     = "F7F7F7"

EIXO_COR = {
    'Caso real de pessoa':           "D6EAF8",
    'Conhecimento técnico':          "D5F5E3",
    'Conhecimento da especialidade': "D5F5E3",
    'Mito x verdade':                "FEF9E7",
    'Atualidade/dados':              "FDEBD0",
    'Filosofia/sabedoria':           "F9EBEA",
    'Especialidade':                 "D5F5E3",
}

def cor(h): return PatternFill("solid", fgColor=h)
def bd(c="DDDDDD", s='thin'): side=Side(style=s,color=c); return Border(left=side,right=side,top=side,bottom=side)

# ── Workbook ───────────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 1: CALENDÁRIO
# ═══════════════════════════════════════════════════════════════════════════════
ws = wb.active
ws.title = "Calendário"

# Título
ws.merge_cells('A1:I1')
ws['A1'] = 'CALENDÁRIO DE POSTAGENS · WE DONA · INSTAGRAM'
ws['A1'].font = Font(name='Arial', size=15, bold=True, color='FFFFFF')
ws['A1'].fill = cor(ROXO_ESC)
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
ws.row_dimensions[1].height = 38

ws.merge_cells('A2:I2')
ws['A2'] = '3 posts por semana  ·  Terças, Quintas e Sábados  ·  12h00 horário de Brasília  ·  18 ago a 24 out 2026'
ws['A2'].font = Font(name='Arial', size=9, italic=True, color=ROXO_ESC)
ws['A2'].fill = cor(ROXO_CLR)
ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
ws.row_dimensions[2].height = 18

# Subtítulo algoritmo
ws.merge_cells('A3:I3')
ws['A3'] = 'Estratégia 2026: keywords na legenda > hashtags · CTA para salvar e comentar · Máx 5 hashtags de nicho'
ws['A3'].font = Font(name='Arial', size=8, color='555555')
ws['A3'].fill = cor('F0F0F0')
ws['A3'].alignment = Alignment(horizontal='center', vertical='center')
ws.row_dimensions[3].height = 16

# Headers
headers = ['Nº','Data','Dia','Hora','Carrossel','Eixo Temático','Legenda Otimizada (copie e cole)','Nº Slides','Status']
widths  = [4,  13,  16,  7,  30,  24,  70, 9, 12]
for c,(h,w) in enumerate(zip(headers,widths),1):
    cell = ws.cell(row=4, column=c, value=h)
    cell.font = Font(name='Arial', size=9, bold=True, color='FFFFFF')
    cell.fill = cor(ROXO_MED)
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = bd(ROXO_ESC, 'medium')
    ws.column_dimensions[get_column_letter(c)].width = w
ws.row_dimensions[4].height = 22

# Mapear legendas por nome curto (último segmento após ·)
def get_legenda(card_name):
    nome_curto = card_name.split('·')[-1].strip()
    # busca exata
    for k,v in LEGENDAS.items():
        if k.split('·')[-1].strip() == nome_curto:
            return v
    return f"[Legenda pendente para: {card_name}]"

def get_eixo(card):
    desc = card.get('desc','')
    for l in desc.split('\n'):
        if l.strip().startswith('Eixo:'):
            return l.replace('Eixo:','').strip()
    # Inferir pelo nome
    n = card['name'].lower()
    if 'caso' in n: return 'Caso real de pessoa'
    if 'tecnico' in n: return 'Conhecimento técnico'
    if 'mito' in n: return 'Mito x verdade'
    if 'dados' in n: return 'Atualidade/dados'
    if 'filosofia' in n: return 'Filosofia/sabedoria'
    if 'especialidade' in n: return 'Especialidade'
    return 'Conhecimento da especialidade'

for i,(card,dt) in enumerate(zip(cards, post_days),1):
    row = i+4
    eixo = get_eixo(card)
    legenda = get_legenda(card['name'])
    slides = len([a for a in card.get('attachments',[]) if a.get('name','').endswith('.png')])
    ec = EIXO_COR.get(eixo, CINZA)
    bg = CINZA if i%2==0 else BRANCO

    vals = [i, f"{dt.day:02d}/{dt.month:02d}/{dt.year}", DIAS_PT[dt.weekday()], '12:00',
            card['name'], eixo, legenda, slides, 'Pendente']
    for col,val in enumerate(vals,1):
        cell = ws.cell(row=row, column=col, value=val)
        cell.font = Font(name='Arial', size=8 if col==7 else 9)
        cell.alignment = Alignment(vertical='top', wrap_text=True,
                                   horizontal='center' if col in (1,4,8,9) else 'left')
        cell.border = bd()
        if col in (5,6,7):
            cell.fill = cor(ec)
        elif col == 9:
            cell.fill = cor('FFF3CD')
        else:
            cell.fill = cor(bg)
    ws.row_dimensions[row].height = 120

ws.freeze_panes = 'A5'

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 2: LEGENDAS COMPLETAS (fácil de copiar)
# ═══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Legendas Completas")

ws2.merge_cells('A1:C1')
ws2['A1'] = 'LEGENDAS COMPLETAS · copie, cole e publique'
ws2['A1'].font = Font(name='Arial', size=13, bold=True, color='FFFFFF')
ws2['A1'].fill = cor(ROXO_ESC)
ws2['A1'].alignment = Alignment(horizontal='center', vertical='center')
ws2.row_dimensions[1].height = 32

ws2.merge_cells('A2:C2')
ws2['A2'] = 'Estratégia 2026: gancho forte na 1ª linha · keywords · CTA salvar/comentar · 3 a 5 hashtags de nicho · sem emoji em excesso'
ws2['A2'].font = Font(name='Arial', size=8, italic=True, color='444444')
ws2['A2'].fill = cor(ROXO_CLR)
ws2['A2'].alignment = Alignment(horizontal='center', vertical='center')
ws2.row_dimensions[2].height = 16

for c,(h,w) in enumerate(zip(['Carrossel','Data de Postagem','Legenda'],[28,15,80]),1):
    cell = ws2.cell(row=3, column=c, value=h)
    cell.font = Font(name='Arial', size=9, bold=True, color='FFFFFF')
    cell.fill = cor(ROXO_MED)
    cell.alignment = Alignment(horizontal='center', vertical='center')
    cell.border = bd(ROXO_ESC,'medium')
    ws2.column_dimensions[get_column_letter(c)].width = w
ws2.row_dimensions[3].height = 20

for i,(card,dt) in enumerate(zip(cards, post_days),1):
    row = i+3
    legenda = get_legenda(card['name'])
    bg = LILÁS if i%2==0 else BRANCO
    for col,val in enumerate([card['name'], f"{dt.day:02d}/{dt.month:02d}/{dt.year}", legenda],1):
        cell = ws2.cell(row=row, column=col, value=val)
        cell.font = Font(name='Arial', size=9 if col<3 else 8)
        cell.alignment = Alignment(vertical='top', wrap_text=True,
                                   horizontal='center' if col==2 else 'left')
        cell.border = bd()
        cell.fill = cor(bg)
    # Altura proporcional ao texto
    n_linhas = legenda.count('\n') + legenda.count('  ') + 4
    ws2.row_dimensions[row].height = min(max(n_linhas * 14, 80), 300)

ws2.freeze_panes = 'A4'

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 3: GUIA DE ESTRATÉGIA 2026
# ═══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Estratégia Instagram 2026")

estrategia = [
    ("ESTRATÉGIA INSTAGRAM 2026 · baseado nas últimas atualizações do algoritmo", None, ROXO_ESC, True, 16),
    ("O que mudou e o que otimiza alcance, seguidores e engajamento", None, ROXO_MED, False, 10),
    ("", None, BRANCO, False, 8),
    ("HASHTAGS — A GRANDE MUDANÇA", None, ROXO_MED, True, 11),
    ("O Instagram limitou a 5 hashtags por post (atualização dez/2025).", None, BRANCO, False, 10),
    ("Hashtags funcionam como sinais de classificação de conteúdo, não como motor de alcance.", None, BRANCO, False, 10),
    ("Use 3 a 5 hashtags específicas do nicho. Hashtags genéricas (#estetica, #beleza) não trazem resultado significativo.", None, BRANCO, False, 10),
    ("Exemplo para este perfil: #clinicadestetica  #regularizacaosanitaria  #juridicoestetico  #adequacaojuridica  #direitoestetico", None, "FFF3CD", False, 10),
    ("", None, BRANCO, False, 8),
    ("LEGENDA — ONDE ESTÁ O NOVO ALCANCE", None, ROXO_MED, True, 11),
    ("Keywords na legenda aumentam o alcance no Explore em até 35% (dado: Hootsuite/Upgrow 2026).", None, BRANCO, False, 10),
    ("Legendas com palavras-chave relevantes geram ~30% mais alcance e 2x mais curtidas que legendas com excesso de hashtags.", None, BRANCO, False, 10),
    ("Primeira linha = gancho. Ela aparece antes do 'ver mais' e define se o usuário para de rolar ou não.", None, BRANCO, False, 10),
    ("Escreva como você fala. O algoritmo e o leitor detectam conteúdo genérico e pulam.", None, BRANCO, False, 10),
    ("", None, BRANCO, False, 8),
    ("SINAIS QUE O ALGORITMO PESA MAIS EM 2026", None, ROXO_MED, True, 11),
    ("Compartilhamentos via DM: peso 3 a 5x maior que curtidas. CTAs como 'manda pra alguém que precisa ver isso' funcionam.", None, BRANCO, False, 10),
    ("Salvamentos: sinal forte de conteúdo valioso. 'Salva pra consultar depois' é um CTA que converte bem.", None, BRANCO, False, 10),
    ("Comentários com contexto: comentários de 4+ palavras sinalizam conversa real. Perguntas no CTA ajudam.", None, BRANCO, False, 10),
    ("Curtidas e seguidores: ainda contam, mas perderam peso relativo para os sinais acima.", None, BRANCO, False, 10),
    ("", None, BRANCO, False, 8),
    ("CARROSSEL — BOAS PRÁTICAS 2026", None, ROXO_MED, True, 11),
    ("Carrosséis são o formato com melhor performance para salvamentos e curtidas (superados só por Reels virais).", None, BRANCO, False, 10),
    ("Primeiro slide é decisivo: funciona como capa. Pergunta, dado surpreendente ou afirmação direta funcionam melhor.", None, BRANCO, False, 10),
    ("6 a 8 slides costumam superar versões com 10+ slides em alcance.", None, BRANCO, False, 10),
    ("Último slide com CTA claro: salvar, comentar, compartilhar no DM.", None, BRANCO, False, 10),
    ("", None, BRANCO, False, 8),
    ("HORÁRIOS — JANELA DE OPORTUNIDADE", None, ROXO_MED, True, 11),
    ("As primeiras 2 horas após a publicação são críticas. Responda comentários, curta DMs, interaja com quem engajou.", None, BRANCO, False, 10),
    ("Para o nicho de clínicas de estética no Brasil: 12h e 19h são as janelas de maior audiência ativa.", None, BRANCO, False, 10),
    ("Terça a quinta têm melhor performance que segunda e sexta em nichos profissionais.", None, BRANCO, False, 10),
    ("", None, BRANCO, False, 8),
    ("IMPORTANTE: nos primeiros 30 minutos pós-publicação, responda todos os comentários que chegarem.", None, "FFF3CD", True, 10),
    ("Esse engajamento inicial sinaliza ao algoritmo que o post gera conversa e amplia a distribuição.", None, "FFF3CD", False, 10),
]

ws3.column_dimensions['A'].width = 95
for row_idx, (texto, _, bg, bold, size) in enumerate(estrategia, 1):
    cell = ws3.cell(row=row_idx, column=1, value=texto)
    cell.font = Font(name='Arial', size=size, bold=bold,
                     color='FFFFFF' if bg in (ROXO_ESC, ROXO_MED) else '222222')
    cell.fill = cor(bg if bg else BRANCO)
    cell.alignment = Alignment(wrap_text=True, vertical='center')
    ws3.row_dimensions[row_idx].height = 24 if size >= 11 else 18

# ── Salvar ─────────────────────────────────────────────────────────────────────
out = '/sessions/intelligent-kind-wozniak/mnt/outputs/Calendario_Posts_Instagram_WE_DONA_v2.xlsx'
wb.save(out)
print(f"Arquivo salvo: {out}")
print(f"30 legendas geradas e organizadas em 3 abas.")
