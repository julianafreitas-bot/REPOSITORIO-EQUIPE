---
name: "dossie-valor-cliente-jf"
description: "Monta o Dossiê de Atuação de um cliente da JF Advocacia (painel interativo de luxo e deck), valorizando o trabalho diligente. Use em 'dossiê do caso', 'prestação de contas', 'mostrar valor ao cliente'."
---

# Dossiê de Atuação do Cliente – JF Advocacia

Objetivo: mostrar ao cliente, de forma profissional, luxuosa e dinâmica, todo o trabalho diligente do escritório no caso dele, gerando percepção de valor. Usado sobretudo em casos antigos e complexos ou quando há sinal de insatisfação. Público: o próprio cliente (leigo). Tom: elegante, claro, sem juridiquês e sem soar defensivo.

## Regras de ouro (orientações da Dra. Juliana)

1. **Valorizar o trabalho diligente, nunca expor demora.** Não fazer linha do tempo, barras de duração, "para onde foi o tempo" ou sequências de datas que revelem intervalos longos entre atos. Mostrar volume, técnica, estratégia e resultado. Datas só pontuais e quando favorecem (ex.: "a sentença saiu 8 dias depois da nossa previsão").
2. **Profissional, não escolar.** Nada de visual infantil, emojis ou ícones em excesso. Preferir painel interativo (dashboard) com indicadores animados, acordeões, barras e navegação fixa; o deck é secundário.
3. **Não subestimar a complexidade.** Contar TODAS as peças e atos (inicial, emenda, réplicas, especificação de provas, impugnações, embargos, apelações, contrarrazões etc.), não só as "principais". Medir a petição inicial (páginas ≈ palavras/350, número de teses, número de precedentes citados) e destacar a estruturação das teses vencedoras.
4. **Só fatos verificados.** Nunca inventar números, prazos cumpridos ou "0 derrotas". Se um recurso do próprio cliente foi negado, não usar placar tipo "3 × 0"; usar "100% da condenação mantida". Suavizar superlativos sobre adversários ("escritório de referência em Direito Médico", sem nomear).
5. **Honorários: não destacar o êxito em reais.** Em vez de mostrar quanto o escritório ganha de êxito, mostrar **quanto o processo custou por mês ao cliente** durante todo o tempo (entrada + TMP, dividido pelos meses desde o contrato, como teto "menos de R$ X por mês") e que **o escritório assumiu o risco junto com ele**. Ler o contrato de honorários no Drive para os valores reais. Não afirmar que "o restante só existe se vencer" se houver TMP.
6. **Valores = projeção, não garantia.** Toda atualização de valores leva o aviso: "Projeção, não garantia: os valores só poderão ser confirmados após o trânsito em julgado e o cálculo no cumprimento de sentença."
7. **Cuidado além do processo.** Incluir episódios de cuidado humano (ex.: orientação imediata para procurar hospital), com as datas que constarem das peças.
8. **Pesquisa de satisfação é anônima.** Nunca citar a pesquisa nem tentar identificar quem respondeu. O dossiê não confronta o cliente.
9. **Canal de contato:** WhatsApp oficial do escritório.

## Fontes e coleta (antes de desenhar qualquer coisa)

1. **Astrea** (Claude in Chrome; a Dra. Juliana faz o login, nunca digitar senha):
   - Busca pelo nome do cliente → processo → abas Resumo, Atividades e Histórico.
   - Histórico: clicar "Carregar mais andamentos" até o fim (um clique por chamada para não travar); filtrar por instância (1º e 2º grau ficam no mesmo cadastro, coluna INSTÂNCIA). Contar juntadas por tipo e total de registros.
   - Tarefas e comentários: contagem de tarefas concluídas, revisões feitas pela Dra. Juliana, comunicações ao cliente.
   - Publicações: texto da sentença e acórdãos (dispositivo, índices e marcos de juros/correção).
2. **Google Drive:** contrato de honorários, petição inicial (medir), contrarrazões, embargos, manifestações sobre laudo, cálculos.
3. **WhatsApp exportado** (zip no Drive): orientações dadas, previsões acertadas, notícias dadas pessoalmente pela Dra. Juliana. Verificar perguntas do cliente sem resposta e avisar a Dra. Juliana (não colocar no dossiê). Citar mensagens literais, sem acrescentar emojis.
4. **Gmail:** notificações do Astrea como fonte reserva.
5. **STJ/tribunais:** consulta pública se possível; se houver verificação anti-robô, não contornar; informar e indicar conferência manual. Calcular prazo de recurso pendente (15 dias úteis da publicação) e dizer se ainda pode estar correndo.

## Cálculo de atualização (projeção)

- Seguir exatamente os critérios da sentença/acórdão (termo inicial da correção e dos juros por parcela; Súmula 362 para dano moral).
- Índices pelo Banco Central (SGS) via navegador: INPC 188, IPCA 433, Selic mensal 4390. Usar até o último mês publicado.
- Danos materiais: corrigir os valores ORIGINAIS de cada desembolso (se o valor da inicial já vier atualizado, não corrigir de novo para evitar dupla contagem).
- Cenário alternativo Lei 14.905/2024 (a partir de 30/08/2024: IPCA + taxa legal = Selic − IPCA, piso zero) informado à Dra. Juliana, não ao cliente.
- Juros simples pro rata die; registrar escolhas (data de citação usada, data presumida de despesas) e reportá-las à Dra. Juliana.

## Estrutura do painel (artefato HTML interativo)

1. Abertura: nome do cliente, nº do processo, varas/turma, frase-tese (ex.: "Três julgamentos. Três vitórias.") e selos de status.
2. **Panorama em números** (contadores animados): registros de acompanhamento, atos nos autos, páginas da inicial, precedentes, teses, investidas dos réus rebatidas, tarefas da equipe, % do pedido concedido.
3. **Embate:** cada ataque dos réus → nossa resposta → resultado, em acordeão clicável; vitórias numeradas; "100% da condenação mantida".
4. **Volume de trabalho:** barras dos atos por tipo ("todos lidos e respondidos"; deixar claro que incluem atos das outras partes) e destaques do 2º grau.
5. **Estratégia:** a petição inicial como documento (páginas, teses, precedentes) e cards das teses, marcando as que o Tribunal adotou.
6. **Cuidado além do processo.**
7. **Resultado:** projeção atualizada por parcela + aviso de projeção; bloco "Quanto o processo custou a você: menos de R$ X por mês" + "assumimos o risco com você", gratuidade, liminares, sucumbência paga pelos réus.
8. **Próximos passos** sem prazos prometidos (definitiva → cumprimento → cobrança art. 523 → repasse).
9. Rodapé: compromisso de atualização e WhatsApp oficial.

Design: identidade Dourado Noturno (fundo #0E0C09, painéis escuros, dourado #C9A45C/#F1D9A0 em gradiente), Cormorant Garamond nos títulos e Manrope no texto, cantos discretos, animações sutis (respeitar prefers-reduced-motion), responsivo. Assinatura: JF Advocacia Especializada · Dra. Juliana Freitas · OAB/DF 35.929.

Deck (opcional, tipo Slides): mesmos conteúdos e regras, sem slides de linha do tempo ou de demora.

## Entrega

- Publicar como artefato privado; lembrar que o cliente só vê depois que a Dra. Juliana compartilhar.
- Na resposta: o que entrou, as premissas do cálculo a conferir, pendências (prazo de recurso, perguntas sem resposta no WhatsApp, pagamento de TMP incerto) e nada de dados sensíveis desnecessários (CPF, e-mail) no dossiê.