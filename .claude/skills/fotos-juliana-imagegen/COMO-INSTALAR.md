# Como instalar e usar (uma vez só)

## 1. Pré-requisitos
- Node.js 20 ou superior. No terminal: `node --version`. Se não tiver, instale em nodejs.org (versão LTS).
- Claude Code instalado (`claude` no terminal).
- Uma chave da OpenAI com crédito: platform.openai.com > API keys > Create new secret key.

## 2. Instalar a skill
No Mac, com o arquivo .zip baixado na pasta Downloads:

```
mkdir -p ~/.claude/skills
cd ~/.claude/skills
unzip ~/Downloads/fotos-juliana-imagegen.zip
cd fotos-juliana-imagegen
npm install
cp .env.example .env
open -e .env
```

No arquivo `.env` que abrir, cole sua chave no lugar de `sk-...` e salve.

## 3. Testar
Ainda na pasta da skill, confira o prompt sem gastar crédito:

```
node gerar-foto.mjs --cena "portrait in a modern office" --seco
```

## 4. Usar no dia a dia
Abra o Claude Code (`claude`) e peça normalmente, por exemplo:
"Cria uma foto minha em uma sala de reuniões liderando uma reunião estratégica, para stories."

O Claude escreve a cena, roda o script e mostra o resultado. As imagens ficam em
`~/.claude/skills/fotos-juliana-imagegen/saidas/`.

## 5. Trocar as fotos de referência
Substitua as fotos da pasta `referencias/` (2 a 6 fotos nítidas do rosto). Quanto melhores as referências, mais fiel o resultado.

## Custos e segurança
- Cada imagem em qualidade alta consome crédito da OpenAI. Use `--variacoes 1` para economizar e `--qualidade medium` para testes.
- Nunca envie o arquivo `.env` a ninguém: ele contém sua chave.
