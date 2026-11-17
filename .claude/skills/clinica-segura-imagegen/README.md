# Clínica Segura — Gerador de Imagens (skill do Claude Code)

Skill que dá ao Claude Code a capacidade de gerar imagens de post prontas no
padrão visual da Clínica Segura (dourado sobre preto, estética heráldica
editorial), usando a API do GPT Image 2 (OpenAI).

## Instalação (uma vez só)

1. **Tenha uma chave de API da OpenAI.**
   Se ainda não tem: crie uma conta em https://platform.openai.com, vá em
   "API keys" e gere uma nova chave. É uma cobrança separada do ChatGPT
   Plus — paga por uso (poucos centavos por imagem).

2. **Copie esta pasta para dentro da pasta de skills do Claude Code no seu Mac:**
   ```
   cp -r clinica-segura-imagegen ~/.claude/skills/
   cd ~/.claude/skills/clinica-segura-imagegen
   ```

3. **Instale as dependências:**
   ```
   npm install
   ```

4. **Configure sua chave:**
   ```
   cp .env.example .env
   ```
   Depois abra o `.env` e cole sua chave no lugar de `sk-cole-sua-chave-aqui`.

5. Pronto. Abra o Claude Code normalmente (no terminal, dentro de qualquer
   pasta) e peça algo como:
   > "gera uma imagem de post sobre fiscalização surpresa na clínica"

   O Claude Code vai reconhecer o pedido, aplicar automaticamente a
   identidade visual da marca (definida em `SKILL.md`) e gerar o arquivo PNG.

## Testar sem o Claude Code (opcional)

Você também pode rodar o script direto pelo terminal, sem passar pelo Claude:

```
node generate-image.mjs "seu prompt aqui" nome-do-arquivo.png 1024x1024
```

## Custos aproximados

A API do GPT Image 2 cobra por imagem gerada (não por assinatura). Vale
checar o preço atualizado em https://platform.openai.com/pricing antes de
gerar em volume.

## Ajustando a identidade visual

Se a marca evoluir (nova paleta, novo elemento visual padrão), edite o
`SKILL.md` — é o único lugar que precisa mudar. O script `generate-image.mjs`
não precisa ser tocado.
