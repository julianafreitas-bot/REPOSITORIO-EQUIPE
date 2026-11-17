---
name: fotos-juliana-imagegen
description: Gera fotografias profissionais e fotorrealistas da própria Dra. Juliana Freitas (JF Advocacia / Clínica Segura) a partir das fotos de referência dela, preservando a identidade facial, para Instagram, LinkedIn, site e campanhas. Use sempre que ela pedir "foto minha", "cria uma imagem minha", "ensaio", "foto profissional", "foto para o feed/stories/LinkedIn em tal cenário" ou descrever um cenário em que ela aparece. Não use para imagens conceituais sem pessoas (essas são da skill clinica-segura-imagegen).
---

# Fotos da Dra. Juliana — geração com identidade preservada

Envia as fotos da pasta `referencias/` à API de imagens da OpenAI (endpoint de edição, com fidelidade alta de entrada) junto com um prompt que trava a identidade facial. O bloco de identidade e o bloco fotográfico já ficam fixos em `prompts/`; a cada pedido você só escreve a CENA.

## Regras

- A foto `referencias/00-atual-referencia-principal.jpg` é a referência principal e mostra a aparência atual, inclusive o nariz atual, mais fino que nas fotos antigas. Ela precisa continuar sendo a primeira da pasta (ordem alfabética). Ao avaliar o resultado, compare o nariz com essa foto, não com as demais.

- Gere imagens apenas da própria Dra. Juliana, a partir das referências dela. Nunca use fotos de outras pessoas como referência.
- Terceiros na cena (clientes, empresárias, equipe) aparecem sempre de costas ou desfocados, sem rosto identificável. Nada que sugira caso ou cliente real.
- Sem texto, logotipo ou marca-d'água na imagem, a menos que ela peça. Títulos e chamadas entram depois, no design.
- Fidelidade do rosto vem antes de embelezamento. Nunca peça para afinar, rejuvenescer ou "melhorar" traços.

## Fluxo

1. Entenda o pedido: cenário, objetivo (feed, stories, LinkedIn, site), roupa e clima. Se faltar o formato, use 4:5. Não faça perguntas se o pedido já der para executar.
2. Escreva a cena em inglês, em um parágrafo, cobrindo: ambiente e paleta; o que ela está fazendo (pose, gesto, atividade); expressão; roupa e acessórios; luz; se houver terceiros, como aparecem. Varie cenário, roupa, pose e enquadramento entre pedidos para formar um acervo diverso.
3. Confira o prompt antes de gastar crédito, se quiser: `node gerar-foto.mjs --cena "..." --seco`
4. Gere:
   ```
   node gerar-foto.mjs --cena "<cena em inglês>" --formato 4:5 --nome <nome-curto> --variacoes 2
   ```
   Formatos: `4:5` feed (padrão), `9:16` stories/reels, `1:1`, `3:2` LinkedIn/site. O script gera, recorta na proporção exata focando o rosto e salva em `saidas/`.
5. Abra as imagens geradas e avalie o rosto contra as referências (nariz conforme a foto 00, olhos, sorriso, formato do rosto, tom de pele) e as mãos. Diga com franqueza à Dra. Juliana o que ficou fiel e o que não ficou.
6. Ajustes: gere de novo alterando apenas a cena. Se o rosto se afastar das referências, reforce na cena "her face must match the reference photos exactly, with the nose exactly as in the first photo"; se o nariz continuar voltando ao formato antigo, rode com menos referências antigas (mova algumas para fora da pasta) e reduza elementos que puxem atenção (muitas pessoas, ângulos extremos, óculos).

## Exemplo

Pedido: "foto minha orientando empresárias de estética, tons off-white e dourado, para o feed"

```
node gerar-foto.mjs --formato 4:5 --nome consultoria-clinicas --variacoes 2 --cena "A contemporary, sophisticated consulting space linked to aesthetic clinic management: off-white boucle armchairs, light oak table, soft beige and nude walls, brushed-gold details, dried pampas in a ceramic vase, elegant binders and an open tablet on the table; softly blurred minimalist clinic reception in the background, no equipment in focus. She sits at the head of the table, mid-conversation, gently gesturing toward a document as she guides two women business owners, who are seen only from behind and out of focus. Warm, attentive, confident expression with a subtle natural smile. Tailored sand-beige blazer over an ivory silk camisole, delicate gold chain necklace, small gold earrings, nude-pink manicure. Soft natural window light from the side with warm fill, 85mm lens, shallow depth of field."
```

## Problemas comuns

- `OPENAI_API_KEY não encontrada`: falta o arquivo `.env` (copie de `.env.example`).
- Erro de modelo inexistente ou sem acesso: em `.env`, troque `OPENAI_IMAGE_MODEL` para `gpt-image-1`. A organização na OpenAI pode precisar de verificação para usar modelos de imagem.
- Rosto pouco fiel: troque ou acrescente referências nítidas (rosto de frente e de 3/4, boa luz, sem texto ou outras pessoas). De 3 a 5 fotos costuma ser o ideal.
