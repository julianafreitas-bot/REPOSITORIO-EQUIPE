#!/usr/bin/env python3
"""Monta um PARECER no timbrado oficial, no padrao dos pareceres da equipe JF
(copiado do 20260911_Parecer_ContratoPrestacaoServicos, Face Doctor): Century Gothic,
espacamento 1,15, titulos "I. CONSULTA" com espaco antes, subtitulos "III.1.", marcadores
"•" com recuo pendente, fecho "É o parecer, salvo melhor juízo.", data e assinaturas
centralizadas. Margens e cabecalho/rodape vem do TIMBRADO.docx (nunca recriados).

Uso:
    python montar_parecer.py --texto PARECER.txt --saida PARECER.docx [--timbrado caminho.docx]

Marcacao do texto (uma linha = um paragrafo):
    # TITULO              titulo centralizado em negrito (ex.: # PARECER JURÍDICO)
    ## I. CONSULTA        titulo de topico (negrito, espaco antes)
    ### III.1. Assunto    subtitulo (negrito)
    - item                marcador "•" com recuo
    @data Brasília/DF, 17 de novembro de 2026.
    @assina NOME EM CAIXA ALTA | OAB/DF nº 00.000
    (linha vazia)         ignorada
    qualquer outra linha  corpo justificado
"""
import argparse
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parents[3]
TIMBRADO = RAIZ / 'SISTEMA' / 'backend' / 'app' / 'juridico' / 'modelos' / 'TIMBRADO.docx'

FONTE = ('<w:rFonts w:ascii="Century Gothic" w:cs="Century Gothic" '
         'w:eastAsia="Century Gothic" w:hAnsi="Century Gothic"/>')


def _run(t, bold, ital):
    b = '<w:b w:val="1"/><w:bCs w:val="1"/>' if bold else ''
    i = '<w:i w:val="1"/><w:iCs w:val="1"/>' if ital else ''
    return f'<w:r><w:rPr>{FONTE}{b}{i}<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">{escape(t)}</w:t></w:r>'


def par(texto, *, sp='', jc='', ind='', bold=False, ital=False):
    """Dentro do texto: **negrito** e _italico_ (como a equipe usa para partes e citacoes)."""
    ppr = f'<w:pPr>{sp}{ind}{jc}<w:rPr>{FONTE}</w:rPr></w:pPr>'
    runs = ''
    for pedaco in re.split(r'(\*\*.+?\*\*|_.+?_)', texto or ''):
        if not pedaco:
            continue
        if pedaco.startswith('**') and pedaco.endswith('**'):
            runs += _run(pedaco[2:-2], True, ital)
        elif pedaco.startswith('_') and pedaco.endswith('_') and len(pedaco) > 2:
            runs += _run(pedaco[1:-1], bold, True)
        else:
            runs += _run(pedaco, bold, ital)
    return f'<w:p>{ppr}{runs}</w:p>'


SP = lambda **k: '<w:spacing ' + ' '.join(f'w:{a}="{v}"' for a, v in k.items()) + ' w:lineRule="auto"/>'
CENTRO, JUST = '<w:jc w:val="center"/>', '<w:jc w:val="both"/>'


def montar(linhas):
    out = []
    for ln in linhas:
        ln = ln.rstrip()
        if not ln.strip():
            continue
        if ln.startswith('### '):
            out.append(par(ln[4:], sp=SP(after=80, before=200), bold=True, ital=True))
        elif ln.startswith('## '):
            out.append(par(ln[3:], sp=SP(before=320), bold=True))
        elif ln.startswith('# '):
            out += [par(ln[2:], sp=SP(after=80), jc=CENTRO, bold=True), par('', sp=SP(after=120))]
        elif ln.startswith('- '):
            out.append(par('•  ' + ln[2:], sp=SP(after=120, line=276), jc=JUST,
                           ind='<w:ind w:left="425" w:hanging="227"/>'))
        elif ln.startswith('@data '):
            out += [par('', sp=SP(after=120)), par(ln[6:], jc=CENTRO), par('', sp=SP(after=120))]
        elif ln.startswith('@assina '):
            nome, oab = [x.strip() for x in ln[8:].split('|', 1)]
            s = SP(after=0, line=276)
            out += [par(nome, sp=s, jc=CENTRO, bold=True), par(oab, sp=s, jc=CENTRO, bold=True),
                    par('', sp=s, jc=CENTRO)]
        elif ln.startswith('É o parecer'):
            out += [par('', sp=SP(after=120)), par(ln)]
        else:
            out.append(par(ln, sp=SP(line=276), jc=JUST))
    return ''.join(out)


def gerar(texto, saida, timbrado=TIMBRADO):
    with zipfile.ZipFile(timbrado) as z:
        partes = {n: z.read(n) for n in z.namelist()}
    doc = partes['word/document.xml'].decode('utf8')
    corpo_ini = doc.index('<w:body>') + len('<w:body>')
    sect = doc.rindex('<w:sectPr')
    doc = doc[:corpo_ini] + montar(texto.splitlines()) + doc[sect:]
    partes['word/document.xml'] = doc.encode('utf8')
    with zipfile.ZipFile(saida, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, b in partes.items():
            z.writestr(n, b)
    return saida


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--texto', required=True)
    ap.add_argument('--saida', required=True)
    ap.add_argument('--timbrado', default=str(TIMBRADO))
    a = ap.parse_args()
    print(gerar(Path(a.texto).read_text(encoding='utf-8'), a.saida, a.timbrado))
