---
name: "atualizacao-processual-jf"
description: "Lê os andamentos dos processos no Astrea, classifica a situação real (em andamento, concluso, parado, encerrado) e redige a atualização ao cliente em linguagem leiga, com próximo passo e prazo, no padrão do POP da JF."
---

# Atualização Processual ao Cliente — JF Advocacia Especializada

Use quando pedirem: "revisão mensal dos processos", "atualização dos processos", "andamento do processo X", "mensagem para o cliente sobre o processo", "o que tem de novo no processo", "processos parados" ou "atualização mensal aos clientes".

Referência obrigatória: POP – Acompanhamento Processual e Atualização ao Cliente (v2, Drive > POP JURIDICO) e Código de Cultura (Drive: Codigo_de_Cultura_JF_Advocacia). Regra de ouro: todo cliente com processo ativo recebe notícia ao menos uma vez por mês; silêncio não é resposta.

## Papéis (não inverter)

- Dra. Juliana: lê publicações e intimações, distribui tarefas e encaminha à Andreia, por tarefa, o que deve ser informado ao cliente.
- Andreia (administrativo e suporte ao cliente): revisão mensal de todos os processos, envio das mensagens padrão pré-aprovadas, abertura de alertas/tarefas para a advogada da área, repasse dos textos das advogadas, registro dos envios e cadastro no Astrea. Não interpreta o processo. Usa login próprio no Astrea.
- Advogada da área (Carla: cível, família, processual; Juliana Saggin: saúde e estética): providência em processo parado/concluso e explicação ao cliente em linguagem simples, em até 2 dias úteis da tarefa.

## 1. Confirmar o escopo

Pergunte só se não estiver claro: revisão mensal (todos os ativos), um processo ou um cliente. Por sigilo, trate um cliente por vez ao redigir mensagens.

## 2. Ler os andamentos no Astrea

1. Abra o Astrea no navegador do Claude (https://astrea.net.br). Se pedir login, peça à pessoa que entre com o próprio usuário; nunca digite senha.
2. Leia pela API da própria sessão (economiza uso, não abra processo por processo):
   - Capture o header `Authorization: Bearer …` interceptando um `fetch` da página (ex.: navegar para `#/main/folders/[,,]` com `window.fetch` envolvido).
   - Lista de processos ativos: `POST https://app.astrea.net.br/api/v2/case/query` com o corpo capturado da tela de processos (`status:'Active'`, `limit:100`, paginar por `queryCursor`/`cursor`). Use só `type === 'CTE_LAWSUIT'`.
   - Movimentações de cada processo: `GET https://app.astrea.net.br/api/v2/historical/{id}/resume?limit=12` (tipos: AUTOMATIC_LAWSUIT = tribunal; CLIPPING = publicação; DONE_TASK = tarefa da equipe).
   - Tarefas e comentários de uma tarefa: abrir a tarefa e ler o texto do modal.
3. Processe no navegador e devolva só o resumo (número | última data | 3 a 5 eventos relevantes), descartando trâmite: disponibilização no DJe, expedição de certidão/intimação, decurso de prazo, confirmação de intimação.
4. Movimentação genérica ("Outras decisões", "Despacho", publicação sem teor) NÃO basta para redigir: marque "tarefa para a advogada esclarecer" e não invente o conteúdo.

## 3. Classificar a situação real

- Em andamento: ato relevante nos últimos 30 dias.
- Sem novidade: sem ato relevante no mês, dentro do normal → mensagem padrão pré-aprovada.
- Concluso ou sem ato há mais de 30 dias → alerta: tarefa para a advogada da área (prioridade/impulso + texto ao cliente), prazo 2 dias úteis.
- Concluso há mais de 60 dias após pedido de prioridade → despacho com gabinete (advogada; Dra. Juliana nos casos estratégicos).
- Suspenso: anotar o motivo; execução frustrada → tarefa para a advogada indicar novas medidas; prescrição intercorrente → tarefa no mesmo dia para a advogada e a Dra. Juliana.
- Encerrado: arquivamento definitivo, baixa, trânsito com arquivamento, precatório quitado → roteiro de encerramento: conferir valores/honorários, mensagem de encerramento pré-aprovada, inativar no Astrea.
- Sem sincronização: sem movimentações no Astrea → corrigir número/cadastro e ativar monitoramento.
- Sinalize também: cadastro duplicado, campo cliente com a parte contrária, processo de família/próprio da Dra. Juliana (não enviar), última comunicação ao cliente há mais de 30 dias, tarefas abertas há mais de 15 dias.

## 4. Mensagens

### 4.1 Modo Andreia (revisão mensal) — só modelos pré-aprovados

Use apenas os 3 modelos pré-aprovados do POP (seção 6): sem novidade no mês, aguardando decisão do juiz, encerrado. Preencha [Nome], [assunto], [último ato em linguagem simples], [data] e [próximo passo] a partir das movimentações. Se o último ato não puder ser traduzido com segurança, não redija: gere a tarefa para a advogada esclarecer. Cliente com vários processos = uma mensagem organizada por processo.

### 4.2 Modo advogada — texto explicativo

Cinco partes, nesta ordem, no máximo 6 linhas por processo:

1. O que aconteceu — uma frase, sem termo técnico.
2. O que isso significa para o cliente — bom, neutro ou atenção; sem alarmismo, sem prometer resultado.
3. Próximo passo — o que acontece agora e quem faz (nós, o juiz, a outra parte).
4. Prazo — até quando esse passo será concluído. Ato nosso: data certa (prazo fatal menos 2 dias úteis). Ato do juiz/outra parte: prazo legal ou estimativa honesta + o que faremos se não ocorrer até a data.
5. O que precisamos do cliente — com data; ou "por ora, nada é necessário da sua parte".

Regras: traduza termos (concluso = com o juiz para decidir; contrarrazões = nossa resposta ao recurso; embargos de declaração = pedido para o juiz esclarecer; trânsito em julgado = decisão definitiva). Só o relevante: sem IDs, nomes de servidores, trâmite de cartório ou lista de argumentos da outra parte. Notícia ruim sempre com estratégia e próximo passo, e passa pela Dra. Juliana. Use os modelos da seção 6 do POP para a advogada (defesa/recurso da outra parte, decisão favorável, desfavorável, audiência/perícia, processo parado após providência). Prazo não definido: deixe [DATA] e aponte.

## 5. Registrar e entregar

- Planilha "Atualização Processos Ativos" (Drive): preencher Situação real, Última movimentação relevante, Ação necessária, Responsável (Andreia ou advogada da área), Mensagem ao cliente e Status.
- Listar as tarefas a abrir no Astrea (processo, advogada, motivo, prazo de 2 dias úteis). Criar tarefas, comentar ou alterar cadastros no Astrea só com confirmação de quem pediu.
- Nunca enviar mensagem ao cliente pelo Claude: o envio é feito pela Andreia, que registra no histórico do processo no Astrea (data, canal e texto).

## 6. Resposta final

1. Resumo em números (em andamento, sem novidade, alertas, suspensos, encerrados, sem sincronização, duplicados).
2. Alertas para as advogadas, com o motivo em uma linha cada.
3. Mensagens padrão prontas por cliente (ou link da planilha).
4. Pontos de atenção: teor não conferido, prazos a definir, riscos (prescrição, prazos fatais).

## Nunca

- Inventar teor de decisão, prazo, valor ou número de processo.
- Usar, no modo Andreia, mensagem fora dos modelos pré-aprovados.
- Misturar dados de clientes diferentes numa mensagem.
- Mandar mensagem a cliente em processo próprio ou de familiares da Dra. Juliana.
- Usar termo técnico sem tradução ou passar de 6 linhas por processo.