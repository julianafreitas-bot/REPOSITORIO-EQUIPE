"""
Planilha de Teste e Autoavaliação de Desempenho dos Colaboradores
Baseada no Código de Cultura do Escritório
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule

# ==================== CONFIGURAÇÕES DE ESTILO ====================
FONT_NAME = "Arial"

# Cores institucionais
COR_PRIMARIA = "1F3864"     # Azul escuro institucional
COR_SECUNDARIA = "2E75B6"   # Azul médio
COR_DESTAQUE = "BDD7EE"     # Azul claro
COR_FUNDO_SECAO = "D9E1F2"  # Fundo de seção
COR_VERDE = "70AD47"
COR_AMARELO = "FFC000"
COR_VERMELHO = "C00000"
COR_CINZA = "F2F2F2"

# Estilos reutilizáveis
def estilo_titulo_principal():
    return {
        "font": Font(name=FONT_NAME, bold=True, size=18, color="FFFFFF"),
        "fill": PatternFill("solid", start_color=COR_PRIMARIA),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
    }

def estilo_subtitulo():
    return {
        "font": Font(name=FONT_NAME, bold=True, size=12, color="FFFFFF"),
        "fill": PatternFill("solid", start_color=COR_SECUNDARIA),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
    }

def estilo_secao():
    return {
        "font": Font(name=FONT_NAME, bold=True, size=11, color="1F3864"),
        "fill": PatternFill("solid", start_color=COR_FUNDO_SECAO),
        "alignment": Alignment(horizontal="left", vertical="center", wrap_text=True),
    }

def estilo_cabecalho_tabela():
    return {
        "font": Font(name=FONT_NAME, bold=True, size=10, color="FFFFFF"),
        "fill": PatternFill("solid", start_color=COR_PRIMARIA),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
    }

def estilo_celula():
    return {
        "font": Font(name=FONT_NAME, size=10),
        "alignment": Alignment(horizontal="left", vertical="center", wrap_text=True),
    }

def estilo_celula_numero():
    return {
        "font": Font(name=FONT_NAME, size=10),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
    }

def estilo_input():
    return {
        "font": Font(name=FONT_NAME, size=10, color="0000FF"),
        "fill": PatternFill("solid", start_color="FFF2CC"),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
    }

def borda_fina():
    side = Side(border_style="thin", color="808080")
    return Border(left=side, right=side, top=side, bottom=side)

def aplicar_estilo(celula, estilo):
    for k, v in estilo.items():
        setattr(celula, k, v)

def aplicar_borda(ws, range_str):
    for row in ws[range_str]:
        for cell in row:
            cell.border = borda_fina()

# ==================== DADOS DA AVALIAÇÃO ====================

# Valores Culturais (típicos de escritórios de advocacia)
# A usuária pode personalizar conforme o código de cultura real do escritório
VALORES_CULTURAIS = [
    {
        "valor": "Ética e Integridade",
        "descricao": "Atuação pautada por princípios éticos, sigilo profissional e honestidade em todas as relações.",
        "competencias": [
            "Mantém sigilo absoluto sobre informações confidenciais de clientes e do escritório.",
            "Age com transparência e honestidade em todas as situações profissionais.",
            "Cumpre rigorosamente o Código de Ética e Disciplina da OAB.",
            "Reconhece e admite erros, buscando soluções construtivas.",
        ],
    },
    {
        "valor": "Excelência Técnica e Jurídica",
        "descricao": "Compromisso com a qualidade, profundidade técnica e atualização constante na prática jurídica.",
        "competencias": [
            "Produz peças e pareceres com fundamentação jurídica sólida e bem estruturada.",
            "Mantém-se atualizado sobre legislação, jurisprudência e doutrina relevantes.",
            "Revisa o próprio trabalho com atenção a detalhes antes da entrega.",
            "Busca aprofundamento técnico em áreas de atuação do escritório.",
        ],
    },
    {
        "valor": "Compromisso com o Cliente",
        "descricao": "Foco em compreender, atender e superar as expectativas do cliente com presteza e cuidado.",
        "competencias": [
            "Compreende as necessidades do cliente e oferece soluções adequadas.",
            "Mantém o cliente informado sobre o andamento dos processos com clareza.",
            "Responde a contatos e demandas com agilidade e cordialidade.",
            "Demonstra empatia e cuidado no relacionamento com o cliente.",
        ],
    },
    {
        "valor": "Trabalho em Equipe e Colaboração",
        "descricao": "Cooperação ativa, generosidade técnica e construção coletiva de resultados.",
        "competencias": [
            "Compartilha conhecimentos, materiais e experiências com colegas.",
            "Colabora ativamente em projetos coletivos do escritório.",
            "Aceita e oferece feedback de forma construtiva.",
            "Apoia colegas em momentos de sobrecarga ou dúvida.",
        ],
    },
    {
        "valor": "Comunicação Clara e Eficaz",
        "descricao": "Expressão clara, escuta ativa e adequação da linguagem ao público (cliente, juízo, equipe).",
        "competencias": [
            "Comunica-se de forma clara, objetiva e respeitosa por escrito e oralmente.",
            "Escuta ativamente antes de responder ou tomar decisões.",
            "Adapta a linguagem ao interlocutor (cliente, juiz, parte contrária, equipe).",
            "Mantém comunicação tempestiva sobre prazos e pendências.",
        ],
    },
    {
        "valor": "Responsabilidade e Proatividade",
        "descricao": "Cumprimento de prazos, antecipação de problemas e iniciativa para entregar resultados.",
        "competencias": [
            "Cumpre prazos processuais e internos com rigor e antecedência.",
            "Antecipa-se a problemas e propõe soluções sem necessidade de cobrança.",
            "Assume responsabilidade pelos processos e tarefas sob sua condução.",
            "Gerencia bem o próprio tempo e prioriza demandas adequadamente.",
        ],
    },
    {
        "valor": "Aprendizado Contínuo e Desenvolvimento",
        "descricao": "Busca permanente de aprimoramento técnico, comportamental e profissional.",
        "competencias": [
            "Participa de cursos, palestras e eventos de atualização profissional.",
            "Está aberto a novas tecnologias, métodos e ferramentas de trabalho.",
            "Reflete sobre os próprios resultados e busca melhoria contínua.",
            "Compartilha aprendizados com a equipe.",
        ],
    },
    {
        "valor": "Respeito, Diversidade e Boa Convivência",
        "descricao": "Ambiente respeitoso, plural e livre de discriminação, com tratamento digno a todos.",
        "competencias": [
            "Trata colegas, clientes e prestadores com respeito e cordialidade.",
            "Valoriza a diversidade de opiniões, perfis e trajetórias.",
            "Contribui para um ambiente de trabalho saudável e livre de assédio.",
            "Resolve divergências de forma madura e respeitosa.",
        ],
    },
]

# ==================== CRIAÇÃO DA PLANILHA ====================
wb = Workbook()

# ----------- SHEET 1: INSTRUÇÕES -----------
ws1 = wb.active
ws1.title = "Instruções"

ws1.column_dimensions['A'].width = 4
ws1.column_dimensions['B'].width = 110

ws1.merge_cells("A1:B2")
aplicar_estilo(ws1["A1"], estilo_titulo_principal())
ws1["A1"] = "AVALIAÇÃO DE DESEMPENHO E AUTOAVALIAÇÃO DOS COLABORADORES"
ws1.row_dimensions[1].height = 30
ws1.row_dimensions[2].height = 30

ws1.merge_cells("A3:B3")
aplicar_estilo(ws1["A3"], estilo_subtitulo())
ws1["A3"] = "Baseada no Código de Cultura do Escritório"
ws1.row_dimensions[3].height = 24

# Conteúdo das instruções
linhas_instrucoes = [
    ("", ""),
    ("", "OBJETIVO"),
    ("", "Esta planilha tem como finalidade avaliar e desenvolver os colaboradores do escritório com base "
          "nos valores e competências definidos no Código de Cultura. A avaliação combina autoavaliação "
          "(visão do próprio colaborador) e avaliação do gestor, permitindo identificar pontos fortes, "
          "lacunas de desenvolvimento e construir um plano de ação individual."),
    ("", ""),
    ("", "ESTRUTURA DA PLANILHA"),
    ("", "1. Instruções — esta aba (orientações gerais)."),
    ("", "2. Dados do Colaborador — informações cadastrais e do ciclo de avaliação."),
    ("", "3. Autoavaliação — preenchida pelo próprio colaborador."),
    ("", "4. Avaliação do Gestor — preenchida pelo líder direto."),
    ("", "5. Resumo & Plano de Ação — consolidação automática + PDI (Plano de Desenvolvimento Individual)."),
    ("", ""),
    ("", "ESCALA DE AVALIAÇÃO (1 a 5)"),
    ("", "1 — Não atende: não demonstra a competência ou apresenta dificuldades significativas."),
    ("", "2 — Atende parcialmente: demonstra a competência de forma inconsistente, precisa de desenvolvimento."),
    ("", "3 — Atende: demonstra a competência de forma adequada e consistente ao esperado para o cargo."),
    ("", "4 — Supera: demonstra a competência acima do esperado, é referência interna."),
    ("", "5 — Excepcional: domina plenamente a competência, é referência inclusive externamente."),
    ("", "N/A — Não aplicável (use apenas quando a competência não for observável no cargo/contexto)."),
    ("", ""),
    ("", "ORIENTAÇÕES PARA PREENCHIMENTO"),
    ("", "• Preencha apenas as células com fundo amarelo (campos de entrada)."),
    ("", "• Seja honesto e específico nos comentários — quanto mais concreto, mais útil para o desenvolvimento."),
    ("", "• Os totais e médias são calculados automaticamente — não altere as células de fórmula."),
    ("", "• A autoavaliação deve ser feita ANTES da conversa com o gestor, para enriquecer a discussão."),
    ("", "• A conversa de feedback deve ocorrer presencialmente, com base nos resultados consolidados."),
    ("", ""),
    ("", "PERIODICIDADE SUGERIDA"),
    ("", "• Avaliação completa: anual ou semestral."),
    ("", "• Conversa de acompanhamento (check-in) do PDI: trimestral."),
    ("", ""),
    ("", "CONFIDENCIALIDADE"),
    ("", "Os resultados desta avaliação são confidenciais e devem ser tratados com sigilo, "
          "sendo utilizados exclusivamente para fins de desenvolvimento profissional, "
          "feedback estruturado e definição do PDI."),
    ("", ""),
    ("", "OBSERVAÇÃO IMPORTANTE"),
    ("", "Os valores culturais e competências apresentados nesta planilha são uma SUGESTÃO inicial, "
          "típica de escritórios de advocacia. Personalize-os conforme o Código de Cultura específico do escritório, "
          "editando as células das abas 'Autoavaliação' e 'Avaliação do Gestor'."),
]

linha = 4
for col_a, col_b in linhas_instrucoes:
    ws1.cell(row=linha, column=1, value=col_a)
    cell = ws1.cell(row=linha, column=2, value=col_b)
    cell.font = Font(name=FONT_NAME, size=11)
    cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    # Detectar títulos de seção (textos curtos em maiúsculas)
    if col_b and col_b.isupper() and len(col_b) < 60:
        cell.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
        cell.fill = PatternFill("solid", start_color=COR_FUNDO_SECAO)
        ws1.row_dimensions[linha].height = 22
    elif col_b == "":
        ws1.row_dimensions[linha].height = 8
    else:
        ws1.row_dimensions[linha].height = max(20, 18 * (len(col_b) // 100 + 1))

    linha += 1

# ----------- SHEET 2: DADOS DO COLABORADOR -----------
ws2 = wb.create_sheet("Dados do Colaborador")
ws2.column_dimensions['A'].width = 4
ws2.column_dimensions['B'].width = 30
ws2.column_dimensions['C'].width = 50

ws2.merge_cells("A1:C2")
aplicar_estilo(ws2["A1"], estilo_titulo_principal())
ws2["A1"] = "DADOS DO COLABORADOR E DO CICLO DE AVALIAÇÃO"
ws2.row_dimensions[1].height = 28
ws2.row_dimensions[2].height = 28

campos_colaborador = [
    ("INFORMAÇÕES DO COLABORADOR", None),
    ("Nome completo", ""),
    ("Cargo / Função", ""),
    ("Área / Departamento", ""),
    ("Data de admissão", ""),
    ("E-mail corporativo", ""),
    ("", None),
    ("INFORMAÇÕES DO GESTOR", None),
    ("Nome do gestor direto", ""),
    ("Cargo do gestor", ""),
    ("", None),
    ("CICLO DE AVALIAÇÃO", None),
    ("Período avaliado (de)", ""),
    ("Período avaliado (até)", ""),
    ("Data da autoavaliação", ""),
    ("Data da avaliação do gestor", ""),
    ("Data da conversa de feedback", ""),
    ("Tipo de avaliação", "Anual"),
]

linha = 4
for rotulo, valor in campos_colaborador:
    if valor is None:
        # Linha de seção
        ws2.merge_cells(start_row=linha, start_column=2, end_row=linha, end_column=3)
        cell = ws2.cell(row=linha, column=2, value=rotulo)
        aplicar_estilo(cell, estilo_secao())
        ws2.row_dimensions[linha].height = 22
    elif rotulo == "":
        ws2.row_dimensions[linha].height = 8
    else:
        cell_rot = ws2.cell(row=linha, column=2, value=rotulo)
        cell_rot.font = Font(name=FONT_NAME, size=10, bold=True)
        cell_rot.alignment = Alignment(horizontal="left", vertical="center")
        cell_rot.fill = PatternFill("solid", start_color=COR_CINZA)
        cell_rot.border = borda_fina()

        cell_val = ws2.cell(row=linha, column=3, value=valor)
        aplicar_estilo(cell_val, estilo_input())
        cell_val.border = borda_fina()
        ws2.row_dimensions[linha].height = 22
    linha += 1

# ----------- SHEET 3: AUTOAVALIAÇÃO -----------
ws3 = wb.create_sheet("Autoavaliação")
ws3.column_dimensions['A'].width = 4
ws3.column_dimensions['B'].width = 28
ws3.column_dimensions['C'].width = 55
ws3.column_dimensions['D'].width = 12
ws3.column_dimensions['E'].width = 45

ws3.merge_cells("A1:E2")
aplicar_estilo(ws3["A1"], estilo_titulo_principal())
ws3["A1"] = "AUTOAVALIAÇÃO DO COLABORADOR"
ws3.row_dimensions[1].height = 28
ws3.row_dimensions[2].height = 28

ws3.merge_cells("A3:E3")
cell = ws3.cell(row=3, column=1, value="Preenchida pelo próprio colaborador. Reflita honestamente sobre cada competência antes de pontuar.")
cell.font = Font(name=FONT_NAME, size=10, italic=True, color="595959")
cell.alignment = Alignment(horizontal="center", vertical="center")
ws3.row_dimensions[3].height = 20

# Cabeçalho da tabela
cabecalhos = ["#", "Valor Cultural", "Competência / Comportamento Observável", "Nota (1-5)", "Comentário / Exemplo Concreto"]
linha_cab = 5
for col_idx, txt in enumerate(cabecalhos, start=1):
    cell = ws3.cell(row=linha_cab, column=col_idx, value=txt)
    aplicar_estilo(cell, estilo_cabecalho_tabela())
    cell.border = borda_fina()
ws3.row_dimensions[linha_cab].height = 30

# Validação de dados (1-5)
dv = DataValidation(type="list", formula1='"1,2,3,4,5,N/A"', allow_blank=True)
dv.error = "Use apenas valores de 1 a 5 ou N/A"
dv.errorTitle = "Valor inválido"
dv.prompt = "Selecione 1, 2, 3, 4, 5 ou N/A"
dv.promptTitle = "Nota"
ws3.add_data_validation(dv)

# Preencher competências
linha = linha_cab + 1
contador = 1
linhas_inicio_valor = []  # Para usar nas fórmulas de média por valor
for valor_cultural in VALORES_CULTURAIS:
    linha_inicio_valor = linha
    n_competencias = len(valor_cultural["competencias"])

    for i, comp in enumerate(valor_cultural["competencias"]):
        cell_num = ws3.cell(row=linha, column=1, value=contador)
        aplicar_estilo(cell_num, estilo_celula_numero())
        cell_num.border = borda_fina()

        if i == 0:
            # Mesclar a coluna do valor cultural
            ws3.merge_cells(start_row=linha, start_column=2, end_row=linha + n_competencias - 1, end_column=2)
            cell_valor = ws3.cell(row=linha, column=2, value=valor_cultural["valor"])
            cell_valor.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
            cell_valor.fill = PatternFill("solid", start_color=COR_SECUNDARIA)
            cell_valor.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell_valor.border = borda_fina()

        cell_comp = ws3.cell(row=linha, column=3, value=comp)
        aplicar_estilo(cell_comp, estilo_celula())
        cell_comp.border = borda_fina()

        cell_nota = ws3.cell(row=linha, column=4, value="")
        aplicar_estilo(cell_nota, estilo_input())
        cell_nota.border = borda_fina()
        dv.add(cell_nota)

        cell_com = ws3.cell(row=linha, column=5, value="")
        aplicar_estilo(cell_com, estilo_input())
        cell_com.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell_com.border = borda_fina()

        ws3.row_dimensions[linha].height = 38
        linha += 1
        contador += 1

    linhas_inicio_valor.append((valor_cultural["valor"], linha_inicio_valor, linha - 1))

# Linha de total
linha_total = linha
ws3.merge_cells(start_row=linha_total, start_column=1, end_row=linha_total, end_column=3)
cell = ws3.cell(row=linha_total, column=1, value="MÉDIA GERAL DA AUTOAVALIAÇÃO")
cell.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
cell.fill = PatternFill("solid", start_color=COR_PRIMARIA)
cell.alignment = Alignment(horizontal="right", vertical="center")
cell.border = borda_fina()

# Fórmula que ignora N/A (texto) - AVERAGE só considera números
cell_media = ws3.cell(row=linha_total, column=4,
                       value=f"=IFERROR(AVERAGE(D{linha_cab+1}:D{linha_total-1}),0)")
cell_media.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
cell_media.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_media.alignment = Alignment(horizontal="center", vertical="center")
cell_media.number_format = "0.00"
cell_media.border = borda_fina()

ws3.cell(row=linha_total, column=5, value="").border = borda_fina()
ws3.row_dimensions[linha_total].height = 28

# Seção de pontos fortes / desenvolvimento
linha = linha_total + 2
secoes_reflexao = [
    ("PONTOS FORTES (3 maiores qualidades profissionais que você reconhece em si mesmo)", 4),
    ("PONTOS DE DESENVOLVIMENTO (3 aspectos que você gostaria de melhorar)", 4),
    ("CONQUISTAS RELEVANTES NO PERÍODO AVALIADO", 4),
    ("EXPECTATIVAS / OBJETIVOS PARA O PRÓXIMO CICLO", 4),
]

for titulo_sec, n_linhas in secoes_reflexao:
    ws3.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=5)
    cell = ws3.cell(row=linha, column=1, value=titulo_sec)
    aplicar_estilo(cell, estilo_secao())
    cell.border = borda_fina()
    ws3.row_dimensions[linha].height = 22
    linha += 1

    for i in range(n_linhas):
        ws3.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=5)
        cell = ws3.cell(row=linha, column=1, value="")
        aplicar_estilo(cell, estilo_input())
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = borda_fina()
        ws3.row_dimensions[linha].height = 24
        linha += 1
    linha += 1  # Espaçamento

linha_cab_auto = linha_cab
linha_total_auto = linha_total
linhas_valores_auto = linhas_inicio_valor.copy()

# ----------- SHEET 4: AVALIAÇÃO DO GESTOR -----------
ws4 = wb.create_sheet("Avaliação do Gestor")
ws4.column_dimensions['A'].width = 4
ws4.column_dimensions['B'].width = 28
ws4.column_dimensions['C'].width = 55
ws4.column_dimensions['D'].width = 12
ws4.column_dimensions['E'].width = 45

ws4.merge_cells("A1:E2")
aplicar_estilo(ws4["A1"], estilo_titulo_principal())
ws4["A1"] = "AVALIAÇÃO DO GESTOR"
ws4.row_dimensions[1].height = 28
ws4.row_dimensions[2].height = 28

ws4.merge_cells("A3:E3")
cell = ws4.cell(row=3, column=1, value="Preenchida pelo gestor direto. Use exemplos concretos e observáveis para fundamentar a nota.")
cell.font = Font(name=FONT_NAME, size=10, italic=True, color="595959")
cell.alignment = Alignment(horizontal="center", vertical="center")
ws4.row_dimensions[3].height = 20

# Cabeçalho
linha_cab = 5
for col_idx, txt in enumerate(cabecalhos, start=1):
    cell = ws4.cell(row=linha_cab, column=col_idx, value=txt)
    aplicar_estilo(cell, estilo_cabecalho_tabela())
    cell.border = borda_fina()
ws4.row_dimensions[linha_cab].height = 30

dv2 = DataValidation(type="list", formula1='"1,2,3,4,5,N/A"', allow_blank=True)
dv2.error = "Use apenas valores de 1 a 5 ou N/A"
dv2.errorTitle = "Valor inválido"
dv2.prompt = "Selecione 1, 2, 3, 4, 5 ou N/A"
dv2.promptTitle = "Nota"
ws4.add_data_validation(dv2)

linha = linha_cab + 1
contador = 1
linhas_inicio_valor_gestor = []
for valor_cultural in VALORES_CULTURAIS:
    linha_inicio_valor = linha
    n_competencias = len(valor_cultural["competencias"])

    for i, comp in enumerate(valor_cultural["competencias"]):
        cell_num = ws4.cell(row=linha, column=1, value=contador)
        aplicar_estilo(cell_num, estilo_celula_numero())
        cell_num.border = borda_fina()

        if i == 0:
            ws4.merge_cells(start_row=linha, start_column=2, end_row=linha + n_competencias - 1, end_column=2)
            cell_valor = ws4.cell(row=linha, column=2, value=valor_cultural["valor"])
            cell_valor.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
            cell_valor.fill = PatternFill("solid", start_color=COR_SECUNDARIA)
            cell_valor.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell_valor.border = borda_fina()

        cell_comp = ws4.cell(row=linha, column=3, value=comp)
        aplicar_estilo(cell_comp, estilo_celula())
        cell_comp.border = borda_fina()

        cell_nota = ws4.cell(row=linha, column=4, value="")
        aplicar_estilo(cell_nota, estilo_input())
        cell_nota.border = borda_fina()
        dv2.add(cell_nota)

        cell_com = ws4.cell(row=linha, column=5, value="")
        aplicar_estilo(cell_com, estilo_input())
        cell_com.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell_com.border = borda_fina()

        ws4.row_dimensions[linha].height = 38
        linha += 1
        contador += 1

    linhas_inicio_valor_gestor.append((valor_cultural["valor"], linha_inicio_valor, linha - 1))

linha_total_gestor = linha
ws4.merge_cells(start_row=linha_total_gestor, start_column=1, end_row=linha_total_gestor, end_column=3)
cell = ws4.cell(row=linha_total_gestor, column=1, value="MÉDIA GERAL DA AVALIAÇÃO DO GESTOR")
cell.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
cell.fill = PatternFill("solid", start_color=COR_PRIMARIA)
cell.alignment = Alignment(horizontal="right", vertical="center")
cell.border = borda_fina()

cell_media = ws4.cell(row=linha_total_gestor, column=4,
                       value=f"=IFERROR(AVERAGE(D{linha_cab+1}:D{linha_total_gestor-1}),0)")
cell_media.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
cell_media.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_media.alignment = Alignment(horizontal="center", vertical="center")
cell_media.number_format = "0.00"
cell_media.border = borda_fina()

ws4.cell(row=linha_total_gestor, column=5, value="").border = borda_fina()
ws4.row_dimensions[linha_total_gestor].height = 28

# Seções de feedback do gestor
linha = linha_total_gestor + 2
secoes_gestor = [
    ("PONTOS FORTES OBSERVADOS NO COLABORADOR", 4),
    ("PONTOS DE DESENVOLVIMENTO PRIORITÁRIOS", 4),
    ("RESULTADOS / ENTREGAS DESTACADAS NO PERÍODO", 4),
    ("RECOMENDAÇÕES E ORIENTAÇÕES PARA O PRÓXIMO CICLO", 4),
]

for titulo_sec, n_linhas in secoes_gestor:
    ws4.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=5)
    cell = ws4.cell(row=linha, column=1, value=titulo_sec)
    aplicar_estilo(cell, estilo_secao())
    cell.border = borda_fina()
    ws4.row_dimensions[linha].height = 22
    linha += 1

    for i in range(n_linhas):
        ws4.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=5)
        cell = ws4.cell(row=linha, column=1, value="")
        aplicar_estilo(cell, estilo_input())
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = borda_fina()
        ws4.row_dimensions[linha].height = 24
        linha += 1
    linha += 1

# ----------- SHEET 5: RESUMO & PLANO DE AÇÃO -----------
ws5 = wb.create_sheet("Resumo & Plano de Ação")
ws5.column_dimensions['A'].width = 4
ws5.column_dimensions['B'].width = 32
ws5.column_dimensions['C'].width = 16
ws5.column_dimensions['D'].width = 16
ws5.column_dimensions['E'].width = 18
ws5.column_dimensions['F'].width = 30

ws5.merge_cells("A1:F2")
aplicar_estilo(ws5["A1"], estilo_titulo_principal())
ws5["A1"] = "RESUMO CONSOLIDADO E PLANO DE DESENVOLVIMENTO INDIVIDUAL (PDI)"
ws5.row_dimensions[1].height = 28
ws5.row_dimensions[2].height = 28

# Cabeçalho da tabela de resumo por valor cultural
ws5.merge_cells("A4:F4")
cell = ws5.cell(row=4, column=1, value="RESULTADO POR VALOR CULTURAL")
aplicar_estilo(cell, estilo_secao())
ws5.row_dimensions[4].height = 22

cabecalhos_resumo = ["#", "Valor Cultural", "Autoavaliação", "Avaliação Gestor", "Diferença", "Interpretação"]
for col_idx, txt in enumerate(cabecalhos_resumo, start=1):
    cell = ws5.cell(row=5, column=col_idx, value=txt)
    aplicar_estilo(cell, estilo_cabecalho_tabela())
    cell.border = borda_fina()
ws5.row_dimensions[5].height = 28

# Linhas de resumo - uma por valor cultural
linha = 6
for idx, ((valor, ini_auto, fim_auto), (_, ini_ges, fim_ges)) in enumerate(
    zip(linhas_valores_auto, linhas_inicio_valor_gestor), start=1
):
    cell = ws5.cell(row=linha, column=1, value=idx)
    aplicar_estilo(cell, estilo_celula_numero())
    cell.border = borda_fina()

    cell = ws5.cell(row=linha, column=2, value=valor)
    cell.font = Font(name=FONT_NAME, size=10, bold=True)
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell.border = borda_fina()
    cell.fill = PatternFill("solid", start_color=COR_CINZA)

    # Média da autoavaliação para este valor
    cell_auto = ws5.cell(row=linha, column=3,
        value=f"=IFERROR(AVERAGE('Autoavaliação'!D{ini_auto}:D{fim_auto}),0)")
    cell_auto.font = Font(name=FONT_NAME, size=10, color="008000")  # verde - link interno
    cell_auto.alignment = Alignment(horizontal="center", vertical="center")
    cell_auto.number_format = "0.00"
    cell_auto.border = borda_fina()

    # Média da avaliação do gestor para este valor
    cell_ges = ws5.cell(row=linha, column=4,
        value=f"=IFERROR(AVERAGE('Avaliação do Gestor'!D{ini_ges}:D{fim_ges}),0)")
    cell_ges.font = Font(name=FONT_NAME, size=10, color="008000")
    cell_ges.alignment = Alignment(horizontal="center", vertical="center")
    cell_ges.number_format = "0.00"
    cell_ges.border = borda_fina()

    # Diferença
    cell_dif = ws5.cell(row=linha, column=5, value=f"=D{linha}-C{linha}")
    cell_dif.font = Font(name=FONT_NAME, size=10)
    cell_dif.alignment = Alignment(horizontal="center", vertical="center")
    cell_dif.number_format = "+0.00;-0.00;0.00"
    cell_dif.border = borda_fina()

    # Interpretação textual
    cell_int = ws5.cell(row=linha, column=6,
        value=f'=IF(ABS(E{linha})<0.5,"Visões alinhadas",IF(E{linha}>0,"Gestor enxerga acima","Autoavaliação acima"))')
    cell_int.font = Font(name=FONT_NAME, size=10, italic=True)
    cell_int.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell_int.border = borda_fina()

    ws5.row_dimensions[linha].height = 26
    linha += 1

# Linha de média geral
linha_media_geral = linha
cell = ws5.cell(row=linha_media_geral, column=1, value="")
ws5.merge_cells(start_row=linha_media_geral, start_column=1, end_row=linha_media_geral, end_column=2)
cell = ws5.cell(row=linha_media_geral, column=1, value="MÉDIA GERAL")
cell.font = Font(name=FONT_NAME, size=12, bold=True, color="FFFFFF")
cell.fill = PatternFill("solid", start_color=COR_PRIMARIA)
cell.alignment = Alignment(horizontal="right", vertical="center")
cell.border = borda_fina()

# Médias gerais (referência cruzada às abas)
cell_auto_geral = ws5.cell(row=linha_media_geral, column=3,
    value=f"=AVERAGE(C6:C{linha-1})")
cell_auto_geral.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
cell_auto_geral.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_auto_geral.alignment = Alignment(horizontal="center", vertical="center")
cell_auto_geral.number_format = "0.00"
cell_auto_geral.border = borda_fina()

cell_ges_geral = ws5.cell(row=linha_media_geral, column=4,
    value=f"=AVERAGE(D6:D{linha-1})")
cell_ges_geral.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
cell_ges_geral.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_ges_geral.alignment = Alignment(horizontal="center", vertical="center")
cell_ges_geral.number_format = "0.00"
cell_ges_geral.border = borda_fina()

cell_dif_geral = ws5.cell(row=linha_media_geral, column=5,
    value=f"=D{linha_media_geral}-C{linha_media_geral}")
cell_dif_geral.font = Font(name=FONT_NAME, size=12, bold=True)
cell_dif_geral.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_dif_geral.alignment = Alignment(horizontal="center", vertical="center")
cell_dif_geral.number_format = "+0.00;-0.00;0.00"
cell_dif_geral.border = borda_fina()

cell_class = ws5.cell(row=linha_media_geral, column=6,
    value=f'=IF(D{linha_media_geral}>=4.5,"Excepcional",IF(D{linha_media_geral}>=3.5,"Supera",IF(D{linha_media_geral}>=2.5,"Atende",IF(D{linha_media_geral}>=1.5,"Atende parcialmente","Não atende"))))')
cell_class.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
cell_class.fill = PatternFill("solid", start_color=COR_DESTAQUE)
cell_class.alignment = Alignment(horizontal="center", vertical="center")
cell_class.border = borda_fina()
ws5.row_dimensions[linha_media_geral].height = 28

# Aplicar formatação condicional de cor (escala) nas notas
range_auto = f"C6:C{linha_media_geral-1}"
range_ges = f"D6:D{linha_media_geral-1}"
color_rule = ColorScaleRule(
    start_type="num", start_value=1, start_color="F8696B",
    mid_type="num", mid_value=3, mid_color="FFEB84",
    end_type="num", end_value=5, end_color="63BE7B",
)
ws5.conditional_formatting.add(range_auto, color_rule)
ws5.conditional_formatting.add(range_ges, color_rule)

# ===== Plano de Desenvolvimento Individual (PDI) =====
linha = linha_media_geral + 3
ws5.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=6)
cell = ws5.cell(row=linha, column=1, value="PLANO DE DESENVOLVIMENTO INDIVIDUAL (PDI)")
aplicar_estilo(cell, estilo_secao())
cell.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
ws5.row_dimensions[linha].height = 24
linha += 1

ws5.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=6)
cell = ws5.cell(row=linha, column=1,
    value="Defina até 4 ações concretas de desenvolvimento, com responsável, prazo e como será medido o sucesso.")
cell.font = Font(name=FONT_NAME, size=10, italic=True, color="595959")
cell.alignment = Alignment(horizontal="left", vertical="center")
ws5.row_dimensions[linha].height = 20
linha += 1

cabecalhos_pdi = ["#", "Competência / Objetivo a desenvolver", "Ação concreta", "Responsável", "Prazo", "Como medir o sucesso"]
for col_idx, txt in enumerate(cabecalhos_pdi, start=1):
    cell = ws5.cell(row=linha, column=col_idx, value=txt)
    aplicar_estilo(cell, estilo_cabecalho_tabela())
    cell.border = borda_fina()
ws5.row_dimensions[linha].height = 30
linha += 1

for i in range(1, 5):
    cell = ws5.cell(row=linha, column=1, value=i)
    aplicar_estilo(cell, estilo_celula_numero())
    cell.border = borda_fina()
    for col_idx in range(2, 7):
        cell = ws5.cell(row=linha, column=col_idx, value="")
        aplicar_estilo(cell, estilo_input())
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = borda_fina()
    ws5.row_dimensions[linha].height = 50
    linha += 1

# Assinaturas
linha += 2
ws5.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=6)
cell = ws5.cell(row=linha, column=1, value="ASSINATURAS / CIÊNCIA")
aplicar_estilo(cell, estilo_secao())
cell.font = Font(name=FONT_NAME, size=12, bold=True, color="1F3864")
ws5.row_dimensions[linha].height = 24
linha += 2

# Linhas de assinatura
assinaturas = [
    ("Colaborador(a):", "Data:"),
    ("Gestor(a):", "Data:"),
    ("RH / Comitê:", "Data:"),
]
for lbl1, lbl2 in assinaturas:
    cell = ws5.cell(row=linha, column=2, value=lbl1)
    cell.font = Font(name=FONT_NAME, size=10, bold=True)
    cell.alignment = Alignment(horizontal="right", vertical="center")
    ws5.merge_cells(start_row=linha, start_column=3, end_row=linha, end_column=4)
    cell_lin = ws5.cell(row=linha, column=3, value="")
    cell_lin.border = Border(bottom=Side(border_style="thin", color="000000"))

    cell = ws5.cell(row=linha, column=5, value=lbl2)
    cell.font = Font(name=FONT_NAME, size=10, bold=True)
    cell.alignment = Alignment(horizontal="right", vertical="center")
    cell_lin = ws5.cell(row=linha, column=6, value="")
    cell_lin.border = Border(bottom=Side(border_style="thin", color="000000"))
    ws5.row_dimensions[linha].height = 32
    linha += 2

# ----------- Salvar -----------
output_path = "/sessions/dazzling-admiring-johnson/mnt/outputs/Avaliacao_Desempenho_Colaboradores.xlsx"
wb.save(output_path)
print(f"Arquivo salvo em: {output_path}")
