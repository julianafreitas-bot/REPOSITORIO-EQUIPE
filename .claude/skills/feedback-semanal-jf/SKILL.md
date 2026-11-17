---
name: "feedback-semanal-jf"
description: "Feedback semanal individual das colaboradoras da JF Advocacia Especializada (Dra. Juliana Freitas), no modelo Reconhecer, Corrigir, Combinar. Tem 3 modos. PREPARAR lê as respostas da semana anterior e as fontes do Drive (Análise Semanal, Reuniões de Alinhamento Diário, Descritivos de Função, Código de Cultura) e grava os 4 rascunhos na tela de aprovação. AJUSTAR refaz os rascunhos em que a Dra. Juliana pediu ajuste. PUBLICAR envia os aprovados para a página privada de cada colaboradora. Use quando a Juliana ou uma tarefa agendada pedir \"feedback semanal\", \"feedback das meninas\", \"prepara os feedbacks\", \"ajusta o feedback\", \"publica os feedbacks\" ou \"modo PREPARAR/AJUSTAR/PUBLICAR\"."
---

# Feedback Semanal – JF Advocacia Especializada

O feedback é individual, firme e acolhedor. Ele nasce das fontes da semana, passa pela aprovação da Dra. Juliana e só depois chega à colaboradora. Nesta skill, "Diretora" é a Dra. Juliana Freitas.

## Endereços

Tela de aprovação (só a Dra. Juliana): https://claude.ai/artifact/BiWhedugNuFXV8oUJCJWmc
- `rascunhos/{id}`: um rascunho por colaboradora.
- `resumo/ultimo`: resumo das respostas da semana anterior.
- `notas`: orientações da Dra. Juliana para o agente (pode estar vazia).

Páginas privadas (uma por colaboradora):

| id | nome | ordem | página |
|---|---|---|---|
| juliana-saggin | Juliana Saggin | 1 | https://claude.ai/artifact/4FgS7SPtXXnUhJRXES8Wzy |
| carla | Carla | 2 | https://claude.ai/artifact/DScdtHzyp4YhNVa3ZxdwBD |
| giovanna | Giovanna | 3 | https://claude.ai/artifact/BJRoeTWpYDrfzhWMw3iTPf |
| andreia | Andreia | 4 | https://claude.ai/artifact/1guYcY1DynCqoWHw2ZWjoj |

Cada página privada tem duas coleções:
- `feedbacks/{semana}`: o feedback publicado. Só o agente escreve aqui.
- `respostas/{semana}`: o que a colaboradora respondeu, com os campos `ciente`, `comentario`, `combinadosAceitos` (índices dos combinados) e `respondidoEm`.

Use a ferramenta ArtifactData para ler e gravar. Leia cada documento antes de gravar e passe o `version` lido em `if_version`. Se a gravação for recusada por versão, leia de novo e refaça. Nunca sobrescreva sem ler.

## Formato do rascunho (`rascunhos/{id}`)

```json
{
  "nome": "Carla",
  "ordem": 2,
  "semana": "AAAA-MM-DD",
  "status": "rascunho",
  "mensagem": "Abertura curta: nome, um reconhecimento, o foco da semana.",
  "cobrancaAnterior": [{"texto": "combinado da semana anterior", "status": "cumprido | parcial | nao_cumprido"}],
  "reconhecer": ["fato concreto com data"],
  "corrigir": ["fato + regra do Descritivo ou do Código de Cultura"],
  "combinados": ["ação verificável com prazo"],
  "paraJuliana": ["assunto reservado, só para a Diretora"],
  "notaJuliana": "",
  "fontes": ["Análise Semanal – AAAA-MM-DD", "Transcrições Alinhamento Diário DD/MM a DD/MM", "..."]
}
```

O campo `semana` é a data da segunda-feira seguinte, no formato AAAA-MM-DD. Na página da colaboradora, o status da cobrança "não cumprido" é `nao`. Na tela de aprovação, use `nao_cumprido`. Converta na hora de publicar.

O ciclo de status é: `rascunho` → `aprovado` ou `ajustar` → `publicado`.

---

## Modo PREPARAR

Costuma rodar no domingo à noite.

### 0. Trava de segurança (sempre primeiro)

Liste `rascunhos` na tela de aprovação. Se algum rascunho já tem a `semana` alvo e status `aprovado` ou `publicado`, **não grave nada**. Sobrescrever apagaria a aprovação e as correções da Dra. Juliana. Avise a Diretora e pare. Ela pode pedir explicitamente para refazer.

Se o rascunho está como `rascunho` ou `ajustar` para a semana alvo, ele pode ser reescrito. Prefira o modo AJUSTAR quando houver `notaJuliana`.

### 1. Respostas da semana anterior

Leia `respostas` nas 4 páginas privadas. Grave `resumo/ultimo` na tela de aprovação:

```json
{
  "semana": "segunda da semana anterior",
  "geradoEm": "data de hoje",
  "itens": [{"nome": "Carla", "leu": true, "aceitos": "2 de 3", "comentario": "resumo fiel do que ela escreveu"}],
  "observacao": "opcional"
}
```

Se ela não respondeu, use `leu: false`, `aceitos: "sem registro"` e um comentário dizendo que não há resposta. Um combinado que ela não aceitou deve ser citado com cuidado no novo feedback, sem acusar.

### 2. Fontes da semana (Google Drive e tela de aprovação)

Leia tudo antes de escrever:
1. **Análise Semanal mais recente.** Busque o título "Análise Semanal" e pegue a mais nova. Use também a anterior para checar reincidências e combinados.
2. **"REUNIÃO ALINHAMENTO DIÁRIO" dos últimos 7 dias.** São as transcrições do Gemini. Busque pelo título com `modifiedTime` dos últimos 7 dias.
3. **Descritivos de Função**, na pasta `1P0J-VPjv7mtpdlpixEnJePz7VkVkmxcR`. Use para dizer o que é e o que não é função de cada uma.
4. **Código de Cultura.** Está nos arquivos do Project "Gestão De Pessoas" (`Codigo_de_Cultura_JF_Advocacia.pdf`) ou no Drive.
5. **Coleção `notas`** da tela de aprovação. São orientações da Dra. Juliana e têm prioridade.
6. **Rascunhos da semana anterior.** Os `combinados` deles são a base da `cobrancaAnterior`.

Se uma fonte não abrir, siga com as outras e registre a falta em `paraJuliana` do primeiro rascunho e no aviso final.

### 3. Escrita (Reconhecer, Corrigir, Combinar)

- **mensagem:** de 2 a 4 frases, com o apelido de costume (Ju, Gi). Traga um reconhecimento verdadeiro e o foco da semana. Se a segunda for feriado, diga em que dia começa.
- **cobrancaAnterior:** um item por combinado da semana anterior, com status `cumprido`, `parcial` ou `nao_cumprido`. Baseie o status em evidência das fontes. Sem evidência de cumprimento, o status é `nao_cumprido`, e você menciona no `corrigir` só se for relevante.
- **reconhecer:** de 3 a 5 fatos concretos, com data e, quando couber, o valor do Código de Cultura que o fato mostra (Excelência, Colaboração etc.). Use citação curta entre aspas quando ajudar.
- **corrigir:** de 2 a 5 itens. Cada um tem o fato e a regra que ele fere (Descritivo de Função ou Código de Cultura). Indique reincidência ("3ª ocorrência desde DD/MM") quando a Análise Semanal mostrar. Seja firme e não humilhe.
- **combinados:** de 3 a 6 ações verificáveis, cada uma com prazo (dia da semana e data). Inclua a regra permanente quando ela nascer de um erro ("Vale a partir de terça, 13/10").
- **Tom:** firme e acolhedor. Frases curtas, voz ativa, sem jargão de RH.

### 4. Regras que não se negociam

- **Só fatos das fontes.** Nunca invente fato, data, citação, número ou elogio. Na dúvida, deixe de fora.
- **Assuntos reservados vão só em `paraJuliana`, nunca no texto da colaboradora:** remuneração, salário, pró-labore, contrato, pagamento, RPA, desligamento, saúde, sobrecarga, vida pessoal, questões éticas que pedem decisão da Diretora e registro formal ou advertência (escada de reincidência). Em `paraJuliana`, sugira como tratar (no One-on-One, no Minuto de Padrão etc.).
- Um tema que é da equipe toda (exemplo: linguagem sobre clientes) vai em `paraJuliana`, com a sugestão de tratar no Minuto de Padrão, e não no feedback individual.
- **No modo PREPARAR, nunca grave nas páginas das colaboradoras.**

### 5. Gravar

Grave os 4 documentos `rascunhos/{id}` com `status: "rascunho"` e `notaJuliana: ""`. Use um único `batch` com `if_version` em cada entrada que já existe.

### 6. Aviso final

Termine com até 3 linhas para a Dra. Juliana. Em execução agendada, mande também um PushNotification:
```
Feedbacks prontos para aprovação.
https://claude.ai/artifact/BiWhedugNuFXV8oUJCJWmc
N assuntos reservados para você.
```
N é a soma dos itens de `paraJuliana` dos 4 rascunhos.

---

## Modo AJUSTAR

Liste `rascunhos`. Para cada um com `status: "ajustar"`:
1. Leia `notaJuliana` e os campos que a Dra. Juliana já editou. As edições dela valem mais que o texto original: preserve-as.
2. Refaça só o que a nota pede, com as mesmas regras do PREPARAR. Se precisar, volte às fontes.
3. Grave com `status: "rascunho"` e `if_version`. Mantenha `notaJuliana` para histórico e acrescente "Correções da Dra. Juliana (DD/MM)" em `fontes`.

Aviso: "Ajustes feitos em X feedbacks. Aguardando sua aprovação." e o link.

---

## Modo PUBLICAR

Costuma rodar na segunda de manhã, ou no primeiro dia útil.

1. Liste `rascunhos`. Publique **só** os que têm `status: "aprovado"` e a `semana` alvo. Não publique `rascunho` nem `ajustar`. Liste os pendentes no aviso.
2. Para cada aprovado, leia `feedbacks/{semana}` na página da colaboradora. Grave com `set` (com `if_version` se o documento já existir):
   ```json
   {"semana": "...", "mensagem": "...", "cobrancaAnterior": [{"texto": "...", "status": "cumprido|parcial|nao"}],
    "reconhecer": [...], "corrigir": [...], "combinados": [...], "publicadoEm": "ISO"}
   ```
   **Nunca** copie `paraJuliana`, `notaJuliana`, `fontes` nem `decididoEm` para a página da colaboradora.
3. Depois de publicar, atualize o rascunho na tela de aprovação para `status: "publicado"` (`update` com `if_version`).
4. Aviso: "X feedbacks publicados." e quais ficaram pendentes.

---

## Checklist antes de gravar

- [ ] A trava de segurança foi checada (nenhum aprovado ou publicado da semana alvo será sobrescrito).
- [ ] Todo fato tem fonte e data.
- [ ] Nenhum assunto reservado aparece em `mensagem`, `reconhecer`, `corrigir` ou `combinados`.
- [ ] Todo combinado tem prazo.
- [ ] A `cobrancaAnterior` cobre todos os combinados da semana anterior.
- [ ] `semana` é a próxima segunda, no formato AAAA-MM-DD.
- [ ] Toda gravação em documento existente usou `if_version`.