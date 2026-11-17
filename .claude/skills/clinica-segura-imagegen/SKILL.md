---
name: clinica-segura-imagegen
description: Gera imagens de conceito para posts da Clínica Segura usando GPT Image 2 (OpenAI), aplicando automaticamente a identidade visual da marca (dourado sobre preto, estética heráldica/luxuosa, still-life editorial). Use sempre que o usuário pedir para "gerar imagem", "criar post", "imagem para feed", "conceito visual", ou mencionar um tema/gancho para post da Clínica Segura.
---

# Gerador de Imagens — Clínica Segura

Este skill gera imagens usando a API do GPT Image 2 (OpenAI), aplicando
automaticamente a identidade visual de marca da Clínica Segura — para que
Claude Code nunca precise reconstruir o estilo do zero a cada pedido.

## Quando usar

Sempre que o usuário pedir uma imagem de conceito para post, feed ou material
visual da Clínica Segura. Exemplos de gatilho: "gera uma imagem sobre...",
"cria o post visual pra...", "preciso de uma imagem conceito pra...".

## Identidade visual padrão (SEMPRE aplicar, a menos que o usuário peça diferente)

- **Paleta:** dourado sobre preto profundo, alto contraste
- **Estética:** heráldica e luxuosa — brasão, selo, textura de metal escovado
  ou couro, papel de alto gramatura
- **Iluminação:** estúdio dramática, chiaroscuro sutil
- **Composição:** centralizada, equilibrada, formato 1:1 (quadrado), com
  espaço vazio limpo reservado para texto/CTA sobreposto depois
- **Estilo técnico:** fotografia editorial / still life de alto padrão, alta
  definição, sem aparência de banco de imagens genérico
- **Sempre evitar:** rostos reconhecíveis de pessoas reais, texto renderizado
  na imagem, logotipos de terceiros, clichês de estoque (apertos de mão,
  sorrisos forçados), poluição visual

## Como usar

1. Se o usuário não especificou, pergunte: qual o tema do post e qual o
   elemento central da cena.
2. Monte um prompt completo em inglês, combinando:
   - o conceito específico do usuário (tema + elemento central)
   - a identidade visual padrão acima (sempre incluir, a menos que o usuário
     peça um estilo diferente)
   - uma seção de negativos (o que evitar)
3. Rode o script:
   ```
   node generate-image.mjs "<prompt completo>" [nome-do-arquivo.png] [tamanho]
   ```
   - `tamanho` padrão: `1024x1024` (quadrado). Outros válidos: `1536x1024`
     (paisagem), `1024x1536` (retrato).
4. O script salva o PNG na pasta atual e imprime o caminho do arquivo.
5. Mostre a imagem gerada ao usuário (preview inline se o terminal suportar,
   ou informe o caminho do arquivo).
6. Se o usuário pedir ajustes ("mais escuro", "sem os auditores visíveis",
   "mude o ângulo"), gere uma nova versão ajustando o prompt — não tente
   editar o PNG diretamente.

## Setup necessário (uma vez só)

1. Nesta pasta, rode: `npm install`
2. Crie um arquivo `.env` (copie de `.env.example`) com sua chave:
   ```
   OPENAI_API_KEY=sk-...
   ```
3. Copie esta pasta inteira para `~/.claude/skills/clinica-segura-imagegen/`
4. Pronto — a partir daí, basta pedir a imagem em qualquer sessão do Claude
   Code que ele reconhece e usa o skill automaticamente.

## Exemplo

Usuário: "gera uma imagem pro post sobre fiscalização surpresa, com 3
auditores entrando na clínica"

Claude Code deve montar algo como:

```
Editorial still-life photograph, dramatic chiaroscuro studio lighting, deep
black background with gold accents. Three regulatory auditors entering an
aesthetic clinic, holding clipboards and pens, seen from behind/side angle
(no recognizable faces), silhouetted and partially lit. Heraldic luxury
aesthetic: brushed metal textures, leather, embossed paper, subtle metallic
seal/crest motifs. High contrast, centered symmetrical composition, clean
empty space in the lower third for text overlay. Square format, high-end
editorial photography quality, no stock-photo clichés.
Avoid: recognizable faces, rendered text, third-party logos, generic stock
photo look, clutter.
```

...e então rodar o script com esse prompt.
