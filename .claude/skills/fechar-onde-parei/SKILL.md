---
name: "fechar-onde-parei"
description: "Use quando a Dra. Juliana disser \"fechar\", \"fecha\", \"fechar o dia\" ou \"atualiza onde parei\": registra no Painel Onde Parei onde cada frente parou, a próxima ação e os links de onde a tarefa está."
---

# Fechar — Painel Onde Parei (JF Advocacia)

## Objetivo
Ao final de uma conversa ou de um bloco de trabalho, registrar no **Painel Onde Parei** tudo o que avançou, onde cada frente parou, a **próxima ação concreta** e **onde a tarefa está** (links), para a Dra. Juliana retomar qualquer frente com um clique no botão "Continuar".

Painel: https://claude.ai/artifact/RdcCnRLZzBseRyxzR9byQW (fixado na barra lateral do claude.ai).

## Onde ficam os dados
- O painel lê e grava no banco do próprio artifact, coleção **`frentes`**.
- Use a ferramenta `ArtifactData` com a `url` do painel. **Não republique o HTML** para atualizar frentes.
- Campos de cada frente:
  - `titulo` — o que é a frente (até 120 caracteres)
  - `setor` — exatamente um destes: "Estratégia & Gestão", "Financeiro", "Marketing & Conteúdo", "Comercial", "Pessoas & Cultura", "Jurídico", "Operação & Organização", "Pessoal"
  - `status` — "andamento" | "aguardando" (com a equipe, cliente ou terceiro) | "travado" | "concluido"
  - `prazo` — "AAAA-MM-DD" ou ""
  - `ondeParei` — o que foi feito e em que ponto ficou (fatos, nomes, datas)
  - `proximaAcao` — **uma única ação**, concreta, começando com verbo (até 200 caracteres)
  - `links` — lista de até 8 objetos `{ "rotulo": "...", "url": "https://..." }`. **O primeiro link é o lugar exato onde a próxima ação acontece** (vira o botão "Continuar"): o documento no Drive/Docs, a tarefa ou área no Astrea, o e-mail no Gmail, a pasta do cliente. Os demais são apoio (pasta do processo, contrato, conversa do Claude). Só URLs https reais, vistas na conversa; nunca inventar.
  - `foco` — true/false (no máximo **3** frentes ativas com foco)
  - `criadoEm`, `atualizadoEm` — ISO 8601 (UTC)

## Passo a passo
1. **Ler o painel**: `ArtifactData` action `list`, collection `frentes`. Guarde o `version` de cada documento.
2. **Mapear a conversa**: tudo o que foi trabalhado — tarefas, peças, análises, decisões da Dra. Juliana, o que foi delegado, o que ficou bloqueado — e **os links** de cada item (Drive, Docs, Astrea, Gmail, pastas). Se a sessão tem link próprio (ex.: claude.ai/code/session_…), inclua como "Conversa no Claude".
3. **Casar com as frentes existentes**: assunto já existente → `update` com `if_version`; assunto novo → `set` (sem `if_version`) com `doc_id` curto em kebab-case.
4. **Escrever bem cada frente**:
   - `ondeParei`: concluído + pendente, com responsável e data (ex.: "Devolvido à Carla no Astrea com prazo 16/10").
   - `proximaAcao`: executável e específica ("Revisar a versão ajustada da Carla em 16/10"), nunca vaga.
   - `links`: o primeiro tem de levar direto ao lugar dessa próxima ação. Toda frente ativa deve ter pelo menos um link.
   - `status` "aguardando" quando a bola está com outra pessoa; "travado" quando depende de decisão, permissão ou documento.
   - Marque `concluido` (e `foco: false`) o que terminou.
5. **Foco**: no máximo 3 frentes ativas com `foco: true`, priorizando prazos processuais e o que trava a equipe. Respeite o foco que a Dra. Juliana escolheu; se precisar mudar, avise na resposta.
6. **Gravar em lote** com `batch`, com `if_version` em toda frente existente. Se der conflito de versão, releia e refaça só o que mudou.
7. **Responder curto** (português do Brasil): frentes criadas/atualizadas/concluídas, o que está no foco e qualquer mudança de foco.

## Regras
- Não inventar status, prazos nem links: registrar só o que aconteceu na conversa ou foi decidido pela Dra. Juliana.
- Não expor dados sensíveis de clientes além do necessário para retomar o trabalho (sem CPF, sem dados de saúde de pacientes).
- Não apagar frentes sem pedido expresso.
- Se o painel não carregar ou a gravação falhar, mostrar no chat o resumo de onde parou, as próximas ações e os links.