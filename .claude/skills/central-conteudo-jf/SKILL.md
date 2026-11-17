---
name: "central-conteudo-jf"
description: "Organiza todo o conteúdo do Instagram da JF (quadros da Maria e da Isis, Giovanna, Wesley) na Central de Conteúdo: inventário, lote de gravação, métricas e pendências, sem editar os quadros delas."
---

# Central de Conteúdo JF

Use quando a Dra. Juliana pedir para organizar o conteúdo do Instagram, "atualizar a central", "o que temos para postar", "montar o lote de gravação", "o que a Isis/Maria mandou", enviar prints de Insights ou fizer a revisão semanal/mensal de conteúdo.

Antes de escrever qualquer coisa para o público, carregue a skill **Cérebro Juliana Freitas** (persona Patrícia, voz, pautas, produtos).

## Regra de ouro (inegociável)

- **Nunca edite, mova, arquive ou crie nada nos quadros da Maria nem da Isis.** Eles são das prestadoras. Só leitura.
- Toda organização acontece **aqui**: na página Central de Conteúdo e na conversa.
- Se algo precisa mudar nos quadros delas, escreva como **pendência para a pessoa responsável** (Maria ou Isis) na Central.
- Nada é excluído em definitivo. Nunca envie mensagens (WhatsApp, e-mail, Instagram) sem confirmação explícita da Dra. Juliana.
- Não automatize consultas ao Instagram pelo navegador (o Instagram bloqueia e pode arriscar a conta). Peça prints dos Insights.

## Quem faz o quê

| Pessoa | Papel |
| --- | --- |
| Dra. Juliana | Aprova pautas (15 min na segunda) e grava em lote 1 manhã por semana. Tem bloqueio em aparecer: priorize gravação em lote, bastidores de trabalho e casos anonimizados. |
| Maria (terceirizada) | 16 posts/mês (4 por semana): roteiriza, edita e agenda os dela. |
| Isis Moreira (mentoria de 1 ano) | Entrega mensal de conteúdo pronto (roteiros de Reels e carrosséis), feito por IA com os dados da Juliana. É **banco**: escolher, não postar tudo. |
| Giovanna (associada) | Tem acesso ao Instagram e ao CapCut. Dirige a gravação em lote, edita vídeos, grava a parte dela nos vídeos (ex.: novelinha) e faz os stories do dia a dia. |
| Wesley (marketing) | Posicionamento digital e nas buscas (Google). Montou o Linktree da bio e acompanha os cliques de cada botão. |

## Fontes

- Quadro da Maria: https://trello.com/b/1r95ULf2/dra-juliana-freitas-advogandonaestetica
- Quadro da Isis: https://trello.com/b/HdoDrpoz/we-dona-juliana-ramos-de-freitas
- Quadro antigo da Juliana (referência de persona e dores): https://trello.com/b/wsStatWw/organizacao-de-conteudo-mensal
- Página Central de Conteúdo: https://claude.ai/artifact/3j6VQ74xaKkJJ8aY4PCZUp

### Como ler os quadros (só leitura)

O conector do Trello **não** enxerga esses dois quadros (estão nas áreas de trabalho da Maria e da Isis). Use, nesta ordem:

1. **Chrome da Juliana via Control Chrome**: abra uma aba do Trello já logada e rode apenas requisições GET (XMLHttpRequest síncrono), por exemplo `/1/boards/<shortLink>/lists?cards=open&card_fields=name,desc,labels,dateLastActivity`. Nunca use PUT, POST ou DELETE nesses quadros. Exige "Permitir JavaScript de eventos da Apple" marcado no Chrome (Visualizar → Desenvolvedor).
2. Se o Chrome não responder: peça a exportação em JSON (Menu ⋯ → Imprimir, exportar e compartilhar → Exportar como JSON) e leia o arquivo anexado.

As etiquetas dos quadros nem sempre refletem a realidade (ex.: um Reels marcado "Gravar" que a Juliana já gravou). Quando a Juliana informar o status, ele prevalece sobre a etiqueta.

## Passo a passo

1. **Ler** os dois quadros por completo (lists, cards, etiquetas, data da última atividade, descrição).
2. **Inventariar** por fonte e formato: roteiros de Reels, carrosséis, estáticos, stories, Reels pendentes de gravação. Para cada grupo: quantidade, situação (Pronto · Gravado · Parado · Vazio · Conferir · Referência) e o que fazer.
3. **Detectar problemas**, sempre nesta lista:
   - Reels com etiqueta Gravar/Editar vídeo há mais de 2 semanas, ou parados na coluna Postados sem terem sido gravados (confirmar com a Juliana antes de afirmar);
   - cards vazios (só título ou só a frase de CTA);
   - listas duplicadas;
   - palavra-chave que não combina com o objetivo do post (ex.: "comente GUIA" num post que não leva ao e-book, ou palavra que ainda não está configurada no ManyChat);
   - legendas institucionais sem gancho de medo nem chamada para ação.
4. **Montar o lote de gravação**: 8 roteiros por semana, escolhidos do banco da Isis (e roteiros pendentes da Maria). Prioridade: o medo da Patrícia (fiscalização sanitária, interdição, paciente que processa ou cobra, publicidade/antes e depois, quem pode fazer o procedimento). Para cada um: título curto, tema, Gancho, Corpo, Fecho e status (a gravar · gravado · em edição · agendado · postado). Não repetir roteiros de lotes anteriores.
5. **Atualizar a Central de Conteúdo** (publicar no mesmo artifact, URL acima): diagnóstico, linha de base e metas, "Quem faz o quê", tabela de inventário, lote da semana com texto completo e botão copiar, rotina semanal, pendências com responsável.
6. **Responder em poucas linhas**: o que mudou desde a última versão, o número de Reels prontos x gravados x postados, e a próxima ação concreta da Juliana.

## Regras de conteúdo

- A palavra-chave depende do **objetivo** de cada conteúdo:
  - **GUIA** = somente para vender o e-book Guia Prático — Fiscalização Sanitária (já configurada no ManyChat).
  - **SEGURA** = proposta para o Programa Clínica Segura (convite para o diagnóstico com a equipe). Só usar depois de configurada no ManyChat; até lá, pendência.
  - Outro objetivo usa outra palavra-chave. Se ela ainda não estiver definida e configurada no ManyChat, não invente: registre como pendência da Dra. Juliana.
  - Todo conteúdo tem um objetivo (alcance, autoridade ou conversão) e uma chamada para ação coerente com ele.
- Todo conteúdo começa pelo medo que a dona de clínica já sente e só depois mostra a solução.
- Bio do Instagram: Linktree do Wesley, com o Guia como primeiro botão.
- Ética OAB (Provimento 205/2021): sem promessa de resultado, sem captação indevida, sem valores de honorários em publicidade, nunca expor caso ou cliente identificável; post com cliente só com autorização por escrito; impulsionamento só de conteúdo informativo.
- Lista de licenciamento do DF não vale para outros estados.
- Português do Brasil, voz elegante, segura e acessível.

## Rotina semanal sugerida

- Segunda: Juliana aprova o lote e os posts (15 min).
- Dia de gravação combinado com a Giovanna: gravação em lote (6 a 8 vídeos).
- Quinta e sexta: Maria edita e agenda os 4 posts da semana seguinte (Meta Business Suite), entre 12h e 15h.
- Todos os dias: stories pela Giovanna (bastidor, caso anonimizado, uma enquete); 20 min respondendo comentários e directs.

## Métricas (toda sexta)

Linha de base em 14/10/2026 (Insights, últimos 30 dias): 3.441 contas alcançadas, 21.836 visualizações (46% de não seguidores), 213 visitas ao perfil, 7 toques no link, 1.310 seguidores, 1.034 interações (78% de seguidores).
Metas em 90 dias: 6.000 contas alcançadas, 500 visitas ao perfil, 80 toques no link/mês, 1.700 seguidores.
Comparar sempre com esses números, mais: comentários de cada palavra-chave no ManyChat e cliques do Linktree (vindos do Wesley).
Aprendizados: fiscalização sanitária traz alcance; posts da Juliana com pessoas (parceiras, eventos, entregas) trazem mais interação; seguidores mais ativos entre 12h e 15h.

## Economia

A Juliana quer economia de uso: leia os quadros uma vez por execução, filtre em script e só abra a descrição completa dos cards que entram no lote.