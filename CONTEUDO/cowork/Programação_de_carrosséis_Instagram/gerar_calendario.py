import json
import openpyxl
from openpyxl.styles import (PatternFill, Font, Alignment, Border, Side, GradientFill)
from openpyxl.utils import get_column_letter
from datetime import date, timedelta

# ── Carregar dados do Trello ──────────────────────────────────────────────────
with open('/sessions/intelligent-kind-wozniak/mnt/uploads/HdoDrpoz - we-dona-juliana-ramos-de-freitas.json', 'r') as f:
    data = json.load(f)

carrossel_list_id = '6a401213a71b0d94ad645b0a'
cards = [c for c in data.get('cards', []) if c.get('idList') == carrossel_list_id and not c.get('closed') and c.get('name')]

# ── Legendas sugeridas por eixo ────────────────────────────────────────────────
legendas = {
    '01 · Caso Empresa Prevencao': "A Natura abriu capital em 2004 e a estrutura sustentou tudo.\n\nNão foi sorte. Foi prevenção jurídica e sanitária antes do crescimento.\n\nSe você quer escalar sua clínica de estética, precisa de base antes de altura.\n\n👇 {cta}",
    '02 · Tecnico Vigilancia Sanitaria': "Sabe o que a Vigilância Sanitária vai exigir na sua clínica de estética?\n\nA maioria dos profissionais descobre isso só quando é fiscalizada.\n\nNão espere a intimação para se regularizar.\n\n👇 {cta}",
    '03 · Metodo Clinica Segura': "Existe um método para transformar sua clínica numa operação segura — juridicamente e sanitariamente.\n\nAdequação não é burocracia. É estratégia de crescimento.\n\n👇 {cta}",
    '04 · Caso Negligencia Juridica': "A Volkswagen pagou bilhões por ignorar regulação.\n\nSua clínica não vai pagar bilhões — mas pode perder tudo que construiu.\n\nNegligência regulatória tem um preço. Sempre.\n\n👇 {cta}",
    '05 · Mito Contrato Internet': "\"Peguei um modelo de contrato na internet, tá bom.\"\n\nEsse é o mito que mais coloca clínicas de estética em risco.\n\nVem que eu explico por quê.\n\n👇 {cta}",
    '06 · Dados Mercado Estetica': "O mercado de estética brasileiro cresce explosivamente.\n\nMas a maioria das clínicas cresce sem estrutura — e é aí que mora o perigo.\n\nVeja os dados que você precisa conhecer.\n\n👇 {cta}",
    '07 · Filosofia Prevenir Remediar': "Prevenir é sempre mais barato do que remediar.\n\nNa sua clínica de estética, isso não é filosofia — é matemática.\n\n👇 {cta}",
    '08 · Tecnico Responsabilidade': "Você sabe a diferença entre responsabilidade civil da clínica e do profissional de estética?\n\nSe não, você está exposta a riscos que nem sabe que existem.\n\n👇 {cta}",
    '09 · Mito Juridico E Gasto': "\"Jurídico é gasto e só serve quando dá problema.\"\n\nEsse pensamento já custou muito caro para muita gente.\n\nVem entender por que jurídico é investimento, não despesa.\n\n👇 {cta}",
    '10 · Documentos Essenciais': "Sua clínica de estética tem todos os documentos essenciais?\n\nA maioria acha que tem. Poucas realmente têm.\n\n👇 {cta}",
    '11 · Caso Empreendedora Segura': "Luiza Helena Trajano construiu o Magazine Luiza com estrutura e gestão antes de crescer.\n\nO resultado: uma das maiores redes do Brasil.\n\nEstrutura primeiro. Crescimento depois.\n\n👇 {cta}",
    '12 · Dados Fiscalizacao Multas': "A ANVISA revelou dados alarmantes sobre fiscalização no setor de estética.\n\nSe você ainda não está regularizada, esse carrossel é urgente pra você.\n\n👇 {cta}",
    '13 · Tecnico Clinica Regularizada': "Na prática, o que é uma clínica de estética regularizada?\n\nVem ver o checklist completo que eu uso com minhas clientes.\n\n👇 {cta}",
    '14 · Filosofia Juridico Estrategia': "Segurança jurídica não é obrigação chata.\n\nÉ a estratégia mais inteligente para crescer com tranquilidade.\n\n👇 {cta}",
    '15 · Mito Clinica Pequena': "\"Minha clínica é pequena, não preciso me preocupar com isso.\"\n\nEsse mito já interditou clínicas, gerou processos e destruiu reputações.\n\nTamanho não protege. Estrutura protege.\n\n👇 {cta}",
    '16 · Caso Clinica Interditada': "Clínica interditada. Equipamentos apreendidos. Profissional respondendo na justiça.\n\nIsso acontece com quem não se regulariza — independente do tamanho.\n\n👇 {cta}",
    '17 · Tecnico Cnpj Responsavel': "Ter CNPJ não é suficiente. Ter o responsável técnico correto é que protege sua clínica.\n\nEntenda como funciona na prática.\n\n👇 {cta}",
    '18 · Mito Sem Responsavel Tecnico': "\"Não preciso de responsável técnico na minha clínica.\"\n\nEsse mito pode custar sua licença de funcionamento.\n\n👇 {cta}",
    '19 · Dados Mercado Informalidade': "Mais de 60% das clínicas de estética no Brasil operam na informalidade.\n\nOs dados mostram o tamanho do risco que o setor corre.\n\n👇 {cta}",
    '20 · Especialidade Pasta Sanitaria': "Você sabe o que precisa ter na sua pasta sanitária?\n\nEsse documento é o que a Vigilância pede primeiro numa fiscalização.\n\n👇 {cta}",
    '21 · Caso Processo Resultado': "Uma cliente chegou até mim com processo aberto, clínica em risco e dívida crescendo.\n\nVeja o que foi feito e qual foi o resultado.\n\n👇 {cta}",
    '22 · Filosofia Dormir Tranquila': "Dormir tranquila sabendo que sua clínica está protegida.\n\nIsso é o que a adequação jurídica e sanitária entrega na prática.\n\n👇 {cta}",
    '23 · Tecnico Lgpd Fotos Pacientes': "Você tira fotos dos seus pacientes antes e depois dos procedimentos?\n\nEntão você precisa conhecer a LGPD e saber como se proteger.\n\n👇 {cta}",
    '24 · Mito Contrato Afasta Cliente': "\"Pedir cliente assinar contrato afasta o cliente.\"\n\nNa verdade acontece o contrário — e eu vou te mostrar por quê.\n\n👇 {cta}",
    '25 · Dados Acoes Judiciais': "As ações judiciais contra clínicas de estética cresceram 300% nos últimos anos.\n\nConheça os dados e entenda como não fazer parte dessa estatística.\n\n👇 {cta}",
    '26 · Especialidade Termo Consentimento': "O Termo de Consentimento Livre e Esclarecido é muito mais do que uma formalidade.\n\nÉ a sua proteção jurídica mais importante em cada procedimento.\n\n👇 {cta}",
    '27 · Caso Harmonizacao Processo': "Procedimento de harmonização. Paciente insatisfeita. Processo na justiça.\n\nVeja como uma estrutura jurídica sólida resolveu esse caso.\n\n👇 {cta}",
    '28 · Filosofia Castelo Na Areia': "Clínica construída sem estrutura jurídica é castelo na areia.\n\nCresce, cresce — e quando vem a maré, leva tudo.\n\n👇 {cta}",
    '29 · Tecnico Rdc Anvisa': "A RDC da ANVISA que todo profissional de estética precisa conhecer.\n\nSe você não conhece, está operando no escuro.\n\n👇 {cta}",
    '30 · Mito Mei Regular': "\"Sou MEI, então minha situação já está regular.\"\n\nEsse é o mito mais perigoso do setor de estética.\n\n👇 {cta}",
}

# ── Montar schedule 3x/semana: Ter/Qui/Sáb às 12h ────────────────────────────
start = date(2026, 8, 18)  # Próxima terça
post_days = []
d = start
while len(post_days) < 30:
    if d.weekday() in (1, 3, 5):  # Ter=1, Qui=3, Sáb=5
        post_days.append(d)
    d += timedelta(days=1)

MESES_PT = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',
            7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
DIAS_PT = {0:'Segunda',1:'Terça',2:'Quarta',3:'Quinta',4:'Sexta',5:'Sábado',6:'Domingo'}

# ── Criar workbook ─────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Calendário de Posts"

# Cores
ROXO_ESCURO  = "4A1080"
ROXO_MEDIO   = "7B2FBE"
ROXO_CLARO   = "E8D5F5"
ROSA         = "F0C4FF"
CINZA_CLARO  = "F5F5F5"
BRANCO       = "FFFFFF"
VERDE        = "D4EDDA"
AZUL_CLARO   = "D0E8FF"
LARANJA_CLARO= "FFF3CD"

def cor(hex):
    return PatternFill("solid", fgColor=hex)

def borda():
    s = Side(style='thin', color='CCCCCC')
    return Border(left=s, right=s, top=s, bottom=s)

def borda_forte():
    s = Side(style='medium', color=ROXO_ESCURO)
    return Border(left=s, right=s, top=s, bottom=s)

# ── Cabeçalho ─────────────────────────────────────────────────────────────────
ws.merge_cells('A1:H1')
ws['A1'] = '📅  CALENDÁRIO DE POSTAGENS · WE DONA · INSTAGRAM'
ws['A1'].font = Font(name='Arial', size=16, bold=True, color=BRANCO)
ws['A1'].fill = cor(ROXO_ESCURO)
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
ws['A1'].border = borda_forte()
ws.row_dimensions[1].height = 36

ws.merge_cells('A2:H2')
ws['A2'] = 'Frequência: 3x por semana  ·  Terça, Quinta e Sábado  ·  Horário: 12h00 (Brasília)  ·  30 carrosséis · 10 semanas'
ws['A2'].font = Font(name='Arial', size=10, color=ROXO_ESCURO)
ws['A2'].fill = cor(ROXO_CLARO)
ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
ws['A2'].border = borda()
ws.row_dimensions[2].height = 22

# ── Headers das colunas ────────────────────────────────────────────────────────
headers = ['#', 'Data', 'Dia', 'Horário', 'Carrossel', 'Eixo', 'Legenda Sugerida', 'CTA']
widths  = [5,    14,    12,    10,         32,          22,     60,                  22]

for col, (h, w) in enumerate(zip(headers, widths), 1):
    cell = ws.cell(row=3, column=col, value=h)
    cell.font = Font(name='Arial', size=10, bold=True, color=BRANCO)
    cell.fill = cor(ROXO_MEDIO)
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = borda()
    ws.column_dimensions[get_column_letter(col)].width = w
ws.row_dimensions[3].height = 24

# ── Cores por eixo ─────────────────────────────────────────────────────────────
EIXO_COR = {
    'Caso real de pessoa':        AZUL_CLARO,
    'Conhecimento técnico':       VERDE,
    'Conhecimento da especialidade': VERDE,
    'Mito x verdade':            LARANJA_CLARO,
    'Atualidade/dados':          "FFE5D0",
    'Filosofia/sabedoria':       ROSA,
    'Especialidade':             VERDE,
}

# ── Linhas de dados ────────────────────────────────────────────────────────────
for i, (card, dt) in enumerate(zip(cards, post_days), 1):
    row = i + 3

    # Extrair info
    nome_curto = card['name'].split('·')[-1].strip() if '·' in card['name'] else card['name']
    nome_key = card['name'].strip()
    
    desc = card.get('desc','')
    lines = [l.strip() for l in desc.split('\n') if l.strip()]
    eixo = ''
    for l in lines:
        if l.startswith('Eixo:'):
            eixo = l.replace('Eixo:', '').strip()

    legenda_raw = legendas.get(nome_curto, legendas.get(nome_key, f"Carrossel sobre: {lines[0] if lines else nome_curto}\n\n👇 comenta SEGURA"))
    cta = "comenta SEGURA"
    legenda = legenda_raw.replace('{cta}', cta)

    dia_str = DIAS_PT[dt.weekday()]
    data_str = f"{dt.day:02d}/{dt.month:02d}/{dt.year}"
    fill_cor = CINZA_CLARO if i % 2 == 0 else BRANCO

    eixo_cor = EIXO_COR.get(eixo, fill_cor)

    vals = [i, data_str, dia_str, '12:00', card['name'], eixo, legenda, cta]
    for col, val in enumerate(vals, 1):
        cell = ws.cell(row=row, column=col, value=val)
        cell.font = Font(name='Arial', size=9)
        cell.alignment = Alignment(vertical='top', wrap_text=True, horizontal='center' if col in (1,4) else 'left')
        cell.border = borda()
        # Colorir por eixo nas colunas de eixo e legenda
        if col in (5, 6, 7, 8):
            cell.fill = cor(eixo_cor.replace('#',''))
        else:
            cell.fill = cor(fill_cor)

    ws.row_dimensions[row].height = 90

# ── Legenda de cores ───────────────────────────────────────────────────────────
legend_row = len(cards) + 5
ws.cell(row=legend_row, column=1, value='LEGENDA POR EIXO:').font = Font(name='Arial', size=9, bold=True)
ws.merge_cells(f'A{legend_row}:B{legend_row}')

for idx, (eixo, hexcor) in enumerate(EIXO_COR.items()):
    r = legend_row + 1 + idx
    ws.cell(row=r, column=1, value='  ' + eixo)
    ws.cell(row=r, column=1).fill = cor(hexcor)
    ws.cell(row=r, column=1).font = Font(name='Arial', size=8)
    ws.merge_cells(f'A{r}:C{r}')

# ── Congelar painel ────────────────────────────────────────────────────────────
ws.freeze_panes = 'A4'

# ── Salvar ─────────────────────────────────────────────────────────────────────
out = '/sessions/intelligent-kind-wozniak/mnt/outputs/Calendario_Posts_Instagram_WE_DONA.xlsx'
wb.save(out)
print(f"Salvo: {out}")
print(f"Total de posts agendados: {len(cards)}")
print(f"Período: {post_days[0].strftime('%d/%m/%Y')} a {post_days[-1].strftime('%d/%m/%Y')}")
