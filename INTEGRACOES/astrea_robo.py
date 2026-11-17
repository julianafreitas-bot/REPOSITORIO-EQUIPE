# -*- coding: utf-8 -*-
"""Robo do Astrea por login e senha (usuario da Dra. Juliana), via Playwright.

CREDENCIAIS (nunca no Git, nunca no chat):
    Mac:      Chaves do macOS, servico 'astrea-jf'
              security add-generic-password -s astrea-jf -a <email-de-login> -w
              (o comando pede a senha escondida; nao digite a senha na linha de comando)
    Servidor: ASTREA_EMAIL e ASTREA_SENHA no .env (config/ fica fora do Git)

SESSAO: config/astrea_sessao.json (cookies do login; gitignored). Enquanto valer, nao refaz login.

USO (sempre com o Python do .venv):
    .venv/bin/python INTEGRACOES/astrea_robo.py login     abre o navegador, faz login, salva a sessao
                                                         (se o Astrea pedir codigo/2FA, digite na janela)
    .venv/bin/python INTEGRACOES/astrea_robo.py testar    confere se a sessao salva ainda esta logada
    .venv/bin/python INTEGRACOES/astrea_robo.py mapear    fotografa as telas logadas em config/astrea_mapa/
                                                         (usado para mapear os seletores das acoes)
"""
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SESSAO = RAIZ / 'config' / 'astrea_sessao.json'
MAPA = RAIZ / 'config' / 'astrea_mapa'
URL_BASE = os.getenv('ASTREA_URL', 'https://astrea.net.br/')
SERVICO_CHAVES = 'astrea-jf'


# ------------------------------------------------------------------ credenciais
def credenciais():
    email, senha = os.getenv('ASTREA_EMAIL'), os.getenv('ASTREA_SENHA')
    if email and senha:
        return email, senha
    if sys.platform == 'darwin':
        try:
            senha = subprocess.run(['security', 'find-generic-password', '-s', SERVICO_CHAVES, '-w'],
                                   capture_output=True, text=True, check=True).stdout.strip()
            info = subprocess.run(['security', 'find-generic-password', '-s', SERVICO_CHAVES],
                                  capture_output=True, text=True, check=True).stdout
            for linha in info.splitlines():
                if '"acct"' in linha:
                    email = linha.split('=', 1)[1].strip().strip('"')
            if email and senha:
                return email, senha
        except subprocess.CalledProcessError:
            pass
    raise SystemExit("Credencial do Astrea nao encontrada. No Mac rode no Terminal:\n"
                     "  security add-generic-password -s astrea-jf -a <email-de-login> -w\n"
                     "No servidor: ASTREA_EMAIL e ASTREA_SENHA no .env")


# ------------------------------------------------------------------ navegador
def _abrir(p, visivel=False):
    nav = p.chromium.launch(headless=not visivel)
    ctx = nav.new_context(storage_state=str(SESSAO) if SESSAO.exists() else None,
                          locale='pt-BR', viewport={'width': 1440, 'height': 900})
    return nav, ctx


def _na_tela_de_login(page):
    page.wait_for_timeout(2500)  # SPA: deixa o app renderizar
    try:
        return page.locator('input[type="password"]').first.is_visible(timeout=3000)
    except Exception:
        return False


def _salvar(ctx):
    SESSAO.parent.mkdir(parents=True, exist_ok=True)
    ctx.storage_state(path=str(SESSAO))
    os.chmod(SESSAO, 0o600)


def fazer_login(page, ctx, esperar_humano=False):
    email, senha = credenciais()
    page.goto(URL_BASE, wait_until='domcontentloaded')
    if not _na_tela_de_login(page):
        # alguns fluxos tem botao "Entrar" antes do formulario
        for txt in ('Entrar', 'Login', 'Acessar'):
            b = page.get_by_role('link', name=txt).or_(page.get_by_role('button', name=txt)).first
            if b.count():
                b.click()
                page.wait_for_load_state('domcontentloaded')
                break
    campo_email = page.locator('input[type="email"], input[name*="mail" i], input[name*="login" i], '
                               'input[name*="user" i], input[id*="mail" i], input[id*="login" i]').first
    campo_email.fill(email)
    pw = page.locator('input[type="password"]').first
    if not pw.is_visible():  # fluxo em duas etapas (email -> continuar -> senha)
        page.keyboard.press('Enter')
        pw.wait_for(state='visible', timeout=15000)
    pw.fill(senha)
    pw.press('Enter')
    limite = 180000 if esperar_humano else 30000
    page.wait_for_function("() => !document.querySelector('input[type=password]')", timeout=limite)
    page.wait_for_load_state('domcontentloaded')
    _salvar(ctx)


def sessao(visivel=False, esperar_humano=False):
    """Context manager: devolve (page) ja logada. Refaz login se a sessao expirou."""
    from contextlib import contextmanager
    from playwright.sync_api import sync_playwright

    if not SESSAO.exists():
        credenciais()  # falha rapido, antes de abrir navegador

    @contextmanager
    def _cm():
        with sync_playwright() as p:
            nav, ctx = _abrir(p, visivel)
            page = ctx.new_page()
            try:
                page.goto(URL_BASE, wait_until='domcontentloaded')
                if _na_tela_de_login(page):
                    fazer_login(page, ctx, esperar_humano)
                yield page
                _salvar(ctx)
            finally:
                nav.close()
    return _cm()


# ------------------------------------------------------------------ comandos
def cmd_login():
    with sessao(visivel=True, esperar_humano=True) as page:
        print('Logado. URL:', page.url)
        print('Sessao salva em', SESSAO)


def cmd_testar():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav, ctx = _abrir(p)
        page = ctx.new_page()
        page.goto(URL_BASE, wait_until='domcontentloaded')
        ok = not _na_tela_de_login(page)
        print('LOGADO' if ok else 'SESSAO EXPIRADA (rode: login)', '|', page.url)
        nav.close()
        sys.exit(0 if ok else 1)


def cmd_mapear():
    MAPA.mkdir(parents=True, exist_ok=True)
    with sessao(visivel=True) as page:
        page.screenshot(path=str(MAPA / '00_inicio.png'), full_page=True)
        (MAPA / '00_inicio.txt').write_text(page.url + '\n\n' + page.locator('body').aria_snapshot())
        links = page.eval_on_selector_all(
            'a[href], nav [role=menuitem], aside a',
            "els => [...new Set(els.map(e => (e.innerText.trim().split('\\n')[0] + ' | ' + (e.href || ''))))]")
        (MAPA / 'links.txt').write_text('\n'.join(links))
        print('Mapa salvo em', MAPA)


if __name__ == '__main__':
    acao = (sys.argv[1:] or ['testar'])[0]
    {'login': cmd_login, 'testar': cmd_testar, 'mapear': cmd_mapear}.get(
        acao, lambda: sys.exit(__doc__))()
