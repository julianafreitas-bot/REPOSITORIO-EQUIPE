const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak, BorderStyle, ShadingType, Table, TableRow, TableCell, WidthType, UnderlineType } = require('docx');
const fs = require('fs');

const GOLD = "DDC65F";
const BLACK = "000000";
const DARK = "1A1A1A";
const GRAY = "555555";

function h1(text) {
  return new Paragraph({
    text,
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD } },
    run: { color: DARK, bold: true }
  });
}

function h2(text) {
  return new Paragraph({
    text,
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 150 },
    children: [new TextRun({ text, bold: true, color: "8B6914", size: 26 })]
  });
}

function h3(text) {
  return new Paragraph({
    spacing: { before: 240, after: 100 },
    children: [new TextRun({ text, bold: true, color: DARK, size: 24, underline: { type: UnderlineType.SINGLE } })]
  });
}

function p(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text, color: opts.color || DARK, size: opts.size || 22, bold: opts.bold, italics: opts.italic })]
  });
}

function bullet(text, gold = false) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    indent: { left: 400 },
    children: [
      new TextRun({ text: "✅  ", color: GOLD, size: 22 }),
      new TextRun({ text, color: gold ? "8B6914" : DARK, size: 22 })
    ]
  });
}

function divider() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: GOLD } },
    children: []
  });
}

function copyBlock(label, text) {
  return [
    new Paragraph({
      spacing: { before: 160, after: 80 },
      shading: { type: ShadingType.CLEAR, fill: "FDF8EC" },
      children: [new TextRun({ text: `📌 ${label}`, bold: true, color: "8B6914", size: 20 })]
    }),
    new Paragraph({
      spacing: { before: 80, after: 160 },
      shading: { type: ShadingType.CLEAR, fill: "FDF8EC" },
      border: {
        left: { style: BorderStyle.THICK, size: 6, color: GOLD }
      },
      indent: { left: 300 },
      children: [new TextRun({ text, color: DARK, size: 21, italics: true })]
    })
  ];
}

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Calibri", size: 22, color: DARK } }
    }
  },
  sections: [{
    properties: {},
    children: [

      // ── CAPA ──
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 600, after: 200 },
        children: [new TextRun({ text: "📋  CAMPANHA DE LANÇAMENTO", bold: true, color: GRAY, size: 20 })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 100 },
        children: [new TextRun({ text: "Guia Prático para Fiscalização Sanitária", bold: true, color: DARK, size: 44 })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 100 },
        children: [new TextRun({ text: "Dra. Juliana Ramos de Freitas  ·  Direito Sanitário", color: "8B6914", size: 24, italics: true })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 800 },
        children: [new TextRun({ text: "Instagram (impulsionado) + WhatsApp (orgânico)", color: GRAY, size: 22 })]
      }),
      divider(),
      new Paragraph({ children: [new PageBreak()] }),

      // ── ESTRATÉGIA ──
      h1("1. ESTRATÉGIA GERAL"),

      p("O objetivo da campanha é posicionar o ebook como a solução mais completa e acessível para donos de clínicas e estabelecimentos de saúde que têm medo de ser pegos desprevenidos numa fiscalização da Vigilância Sanitária."),
      p(""),
      p("A venda acontece em dois pilares simultâneos:", { bold: true }),
      bullet("Instagram impulsionado: atingir público frio/morno que nunca ouviu falar de você"),
      bullet("WhatsApp orgânico: converter leads quentes — sua base de contatos, grupos e pessoas que já interagiram com você"),
      p(""),
      p("Duração recomendada da campanha ativa: 21 dias (3 semanas)", { bold: true, color: "8B6914" }),
      divider(),

      // ── PÚBLICO ──
      h1("2. PÚBLICO-ALVO"),
      h2("Quem compra esse ebook?"),
      bullet("Donos de clínicas estéticas, odontológicas, médicas e de saúde"),
      bullet("Gestores de SPAs, salões de beleza com procedimentos estéticos"),
      bullet("Veterinários e donos de clínicas veterinárias"),
      bullet("Farmacêuticos e donos de farmácias de manipulação"),
      bullet("Qualquer pessoa que precise de licença sanitária para funcionar"),

      p(""),
      h2("Dores que ativam a compra:"),
      bullet("Medo de ser autuado, multado ou ter o estabelecimento interditado"),
      bullet("Não sabe quais documentos são exigidos pela vigilância sanitária"),
      bullet("Já foi notificado e não sabe como responder"),
      bullet("Quer se regularizar mas não sabe por onde começar"),
      bullet("Quer saber seus direitos durante uma vistoria"),
      divider(),

      // ── SEMANA 1 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("3. SEQUÊNCIA DE 21 DIAS — INSTAGRAM"),
      p("Use o calendário abaixo para publicar 1 conteúdo por dia (ou 1 a cada 2 dias no mínimo). Intercale POSTS no feed com STORIES e REELS."),

      h2("🗓️ SEMANA 1 — DESPERTAR A DOR (Dias 1–7)"),
      p("Objetivo: fazer o público sentir o problema e perceber que precisa de ajuda.", { italic: true }),
      p(""),

      h3("Dia 1 — POST de Pergunta (Enquete nos Stories)"),
      ...copyBlock("Copy para Story com enquete",
        `Sua clínica está pronta para uma fiscalização SURPRESA da Vigilância Sanitária?\n\n` +
        `[ SIM, estou preparada ] ❌\n[ NÃO faço a menor ideia ] 😰\n\n` +
        `Amanhã eu te conto o que os fiscais verificam PRIMEIRO. 👀`),

      h3("Dia 2 — POST Feed (carrossel ou imagem)"),
      ...copyBlock("Copy para legenda do feed",
        `⚠️ 5 erros que levam clínicas a serem AUTUADAS pela Vigilância Sanitária\n\n` +
        `E o pior: a maioria dos donos de clínica não sabe que está cometendo.\n\n` +
        `Erro nº 1: Não ter o Alvará Sanitário atualizado.\n` +
        `Erro nº 2: Descumprir as normas de esterilização.\n` +
        `Erro nº 3: Ausência de registro dos profissionais.\n` +
        `Erro nº 4: Armazenar materiais incorretamente.\n` +
        `Erro nº 5: Não ter protocolo de resíduos documentado.\n\n` +
        `Você está cometendo algum desses? 👇 Me conta nos comentários.\n\n` +
        `#VigilânciaSanitária #ClínicaEstética #DireitoSanitário #FiscalizaçãoSanitária`),

      h3("Dia 3 — REELS (vídeo curto 30–60 seg)"),
      ...copyBlock("Roteiro para Reels",
        `[Cena: você olhando para a câmera, séria]\n` +
        `"Você sabia que a Vigilância Sanitária pode aparecer na sua clínica SEM AVISO PRÉVIO?"\n\n` +
        `[Corte]\n` +
        `"E se isso acontecer amanhã... a sua clínica passaria na inspeção?"\n\n` +
        `[Corte]\n` +
        `"Eu sou a Dra. Juliana, advogada especialista em Direito Sanitário, e criei um guia COMPLETO para você nunca mais ser pega de surpresa."\n\n` +
        `[CTA] "Link na bio. Seu primeiro passo para a blindagem total da sua clínica."`),

      h3("Dia 4 — Story: Bastidor / Autoridade"),
      ...copyBlock("Copy para Story",
        `Passei anos acompanhando clínicas durante fiscalizações da Vigilância Sanitária.\n\n` +
        `Vi donos chorando. Vi clínicas sendo interditadas na hora.\n\n` +
        `Tudo por falta de UMA informação simples.\n\n` +
        `Por isso criei o Guia Prático para Fiscalização Sanitária.\n\n` +
        `👆 Link na bio.`),

      h3("Dias 5 e 6 — Descanso / Conteúdo educativo leve"),
      p("Poste um dado ou curiosidade sobre ANVISA/Vigilância Sanitária. Sem pitch de venda.", { italic: true, color: GRAY }),

      h3("Dia 7 — POST: Lançamento oficial do ebook"),
      ...copyBlock("Copy de lançamento no feed",
        `🚨 CHEGOU O GUIA QUE TODO DONO DE CLÍNICA PRECISAVA!\n\n` +
        `O GUIA PRÁTICO PARA FISCALIZAÇÃO SANITÁRIA é o manual que vai te dar segurança total na hora que a Vigilância Sanitária bater na porta da sua clínica.\n\n` +
        `📌 O que você aprende:\n` +
        `✅ Como se preparar ANTES da fiscalização\n` +
        `✅ Quais documentos ter em mãos\n` +
        `✅ Seus direitos durante a vistoria\n` +
        `✅ Como contestar autos de infração\n` +
        `✅ Blindagem jurídica para seu negócio\n\n` +
        `💰 Acesso imediato após a compra.\n\n` +
        `Link na bio 👆 ou me chama no Direct!\n\n` +
        `#GuiaFiscalizaçãoSanitária #VigilânciaSanitária #DireitoSanitário #ClínicaSegura`),
      divider(),

      // ── SEMANA 2 ──
      new Paragraph({ children: [new PageBreak()] }),
      h2("🗓️ SEMANA 2 — DESEJO E PROVA (Dias 8–14)"),
      p("Objetivo: mostrar transformação, criar desejo e apresentar prova social.", { italic: true }),
      p(""),

      h3("Dia 8 — Story: Antes x Depois (transformação)"),
      ...copyBlock("Copy para Story sequencial",
        `ANTES de ter o guia:\n` +
        `😰 Entrava em pânico só de ouvir "fiscalização"\n` +
        `😰 Não sabia se minha documentação estava ok\n` +
        `😰 Ficava à mercê do que o fiscal quisesse\n\n` +
        `DEPOIS:\n` +
        `✅ Sei exatamente o que preparar\n` +
        `✅ Conheço meus direitos\n` +
        `✅ Fico tranquila quando bate à porta\n\n` +
        `Qual dos dois você quer ser? 👆 Link na bio.`),

      h3("Dia 9 — POST Feed: Objeção #1 — Preco"),
      ...copyBlock("Copy para vencer objeção de preço",
        `Uma multa da Vigilância Sanitária pode custar R$ 2.000 a R$ 75.000.\n\n` +
        `Uma interdição pode custar SEMANAS ou MESES de faturamento.\n\n` +
        `O Guia Prático para Fiscalização Sanitária custa [PREÇO].\n\n` +
        `Qual é o investimento mais inteligente? 🤔\n\n` +
        `Link na bio. 👆`),

      h3('Dia 10 — REELS: 3 coisas que a Vigilância Sanitária verifica PRIMEIRO'),
      ...copyBlock("Roteiro Reels",
        `[Direto ao ponto]\n` +
        `"3 coisas que a Vigilância Sanitária verifica PRIMEIRO na sua clínica:"\n\n` +
        `"Número 1: Alvará Sanitário — ele precisa estar em local visível e atualizado."\n` +
        `"Número 2: Rastreabilidade dos produtos — todo produto precisa ter nota fiscal."\n` +
        `"Número 3: Descarte de resíduos — você tem protocolo documentado?"\n\n` +
        `"Quer o checklist completo? Link na bio. 👆"`),

      h3("Dias 11–12 — Depoimento / Print de feedback"),
      p("Se já vendeu alguma cópia: publique o print do feedback do comprador. Se não: use um depoimento sobre sua assessoria jurídica que mencione confiança e preparo.", { italic: true, color: GRAY }),

      h3("Dia 13 — Story: Urgência leve"),
      ...copyBlock("Copy para urgência",
        `A Vigilância Sanitária não avisa quando vai aparecer.\n\n` +
        `Mas você pode se preparar HOJE.\n\n` +
        `O Guia Prático para Fiscalização Sanitária está disponível agora 👆 Link na bio.`),

      h3("Dia 14 — POST: Autoridade + Credenciais"),
      ...copyBlock("Copy de autoridade",
        `Por que você deveria ouvir o que eu tenho a dizer sobre fiscalização sanitária?\n\n` +
        `Sou a Dra. Juliana Ramos de Freitas.\n` +
        `Advogada especialista em Direito Sanitário.\n` +
        `Já acompanhei dezenas de clínicas em processos com a Vigilância Sanitária.\n` +
        `Já contestei autos de infração, recursos administrativos e muito mais.\n\n` +
        `Esse guia é tudo que aprendi — em formato prático, para você aplicar HOJE.\n\n` +
        `Link na bio 👆`),
      divider(),

      // ── SEMANA 3 ──
      new Paragraph({ children: [new PageBreak()] }),
      h2("🗓️ SEMANA 3 — URGÊNCIA E FECHAMENTO (Dias 15–21)"),
      p("Objetivo: converter os indecisos com urgência real e CTA forte.", { italic: true }),
      p(""),

      h3("Dia 15 — POST: FAQ (perguntas frequentes)"),
      ...copyBlock("Copy para feed",
        `❓ Perguntas que recebo TODA SEMANA sobre fiscalização sanitária:\n\n` +
        `"A vigilância sanitária pode entrar sem autorização?"\n` +
        `→ SIM. E você precisa saber como agir na hora.\n\n` +
        `"Posso recusar a vistoria?"\n` +
        `→ Não da forma que você imagina. Mas há protocolos que te protegem.\n\n` +
        `"Fui autuado. E agora?"\n` +
        `→ Há prazo para contestar. E você PODE ganhar.\n\n` +
        `Todas as respostas no Guia Prático para Fiscalização Sanitária. Link na bio 👆`),

      h3("Dia 17 — Story: Contagem regressiva / Escassez"),
      ...copyBlock("Copy para urgência final",
        `Vou ser honesta com você.\n\n` +
        `Esse guia foi criado para transformar a relação da sua clínica com a Vigilância Sanitária.\n\n` +
        `Mas informação sem ação não muda nada.\n\n` +
        `Se você ainda não garantiu o seu, hoje é o dia. 👆 Link na bio.`),

      h3("Dia 19 — REELS: Depoimento ou estudo de caso"),
      ...copyBlock("Roteiro",
        `[Cena: você relatando um caso real — sem identificar o cliente]\n` +
        `"Uma cliente minha recebeu uma fiscalização surpresa na clínica dela. Sabe o que aconteceu?"\n` +
        `"Ela tinha acabado de ler meu guia. Sabia exatamente o que fazer."\n` +
        `"Resultado? A fiscalização passou, sem autuação, sem multa."\n` +
        `"Quer esse mesmo preparo? Link na bio."`),

      h3("Dia 21 — POST FINAL: CTA direto e emocional"),
      ...copyBlock("Copy de fechamento",
        `Você passou os últimos 21 dias vendo conteúdo sobre fiscalização sanitária.\n\n` +
        `Agora me responde honestamente:\n\n` +
        `Se a Vigilância Sanitária aparecer na sua clínica AMANHÃ... você está pronta?\n\n` +
        `Se a resposta for NÃO — o Guia Prático para Fiscalização Sanitária foi feito para você.\n\n` +
        `Acesso imediato. Link na bio 👆\n\n` +
        `Ou me manda uma mensagem no Direct. Eu respondo pessoalmente. 💛`),
      divider(),

      // ── WHATSAPP ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("4. ESTRATÉGIA WHATSAPP — ORGÂNICO"),

      h2("4.1 Sequência para lista de transmissão (3 mensagens)"),
      p("Envie para sua lista de contatos em dias separados. Nunca as 3 de uma vez."),
      p(""),

      h3("Mensagem 1 — Curiosidade (Dia 1)"),
      ...copyBlock("Mensagem WhatsApp",
        `Oi [nome]! 👋\n\n` +
        `Uma pergunta rápida e importante:\n\n` +
        `Você sabe exatamente o que a Vigilância Sanitária verifica quando faz uma visita surpresa na sua clínica?\n\n` +
        `Me responde aqui — tenho uma novidade importante para te mostrar. 🤫`),

      h3("Mensagem 2 — Apresentação do produto (Dia 3)"),
      ...copyBlock("Mensagem WhatsApp",
        `Oi! 😊 Obrigada pela resposta!\n\n` +
        `Passei os últimos meses reunindo tudo que sei sobre fiscalização sanitária e coloquei em um guia prático.\n\n` +
        `Se você tem uma clínica ou estabelecimento de saúde, esse guia pode te salvar de uma multa ou interdição.\n\n` +
        `📖 *Guia Prático para Fiscalização Sanitária*\n` +
        `✅ Como se preparar antes da fiscalização\n` +
        `✅ Seus direitos durante a vistoria\n` +
        `✅ Como contestar autos de infração\n\n` +
        `👉 [link do produto]\n\n` +
        `Qualquer dúvida, me chama aqui! 💛`),

      h3("Mensagem 3 — Urgência (Dia 7)"),
      ...copyBlock("Mensagem WhatsApp",
        `Olá! Só passando para lembrar 😊\n\n` +
        `O Guia Prático para Fiscalização Sanitária continua disponível.\n\n` +
        `Já tive retornos ótimos de quem adquiriu — o principal: *"eu finalmente sei o que fazer quando baterem na minha porta."*\n\n` +
        `Se tiver interesse: 👉 [link]\n\n` +
        `Qualquer dúvida é só me chamar! 🙏`),

      h2("4.2 Para grupos de WhatsApp"),
      p("Use apenas em grupos dos quais você faz parte naturalmente (associações, grupos de colegas, comunidades de empreendedores de saúde). Nunca envie spam."),
      p(""),
      ...copyBlock("Mensagem para grupo",
        `Oi pessoal! Desculpem a divulgação, mas achei que seria útil para quem tem clínica ou estabelecimento de saúde aqui no grupo.\n\n` +
        `Acabei de lançar o *Guia Prático para Fiscalização Sanitária* — um material completo para te preparar para uma visita da Vigilância Sanitária.\n\n` +
        `Acesso imediato. Quem quiser mais informações, me manda mensagem ou acessa: 👉 [link]\n\n` +
        `Abraços! Dra. Juliana 💛`),
      divider(),

      // ── IMPULSIONAMENTO ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("5. COMO IMPULSIONAR NO INSTAGRAM"),

      h2("Qual post impulsionar?"),
      p("Impulsione os posts com MAIOR ENGAJAMENTO ORGÂNICO. Se um post já teve curtidas e comentários sem pagar, ele tende a performar melhor pago também."),
      p("Priorize na ordem:"),
      bullet("Reels com gancho forte (os de 'erros que levam à autuação')"),
      bullet("Carrossel com os 5 erros ou o FAQ"),
      bullet("Post de lançamento oficial (Dia 7)"),
      p(""),

      h2("Configuração recomendada do impulsionamento:"),
      p(""),

      new Table({
        width: { size: 9000, type: WidthType.DXA },
        rows: [
          new TableRow({
            tableHeader: true,
            children: [
              new TableCell({ width: { size: 3000, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, fill: "8B6914" }, children: [new Paragraph({ children: [new TextRun({ text: "Configuração", bold: true, color: "FFFFFF" })] })] }),
              new TableCell({ width: { size: 6000, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, fill: "8B6914" }, children: [new Paragraph({ children: [new TextRun({ text: "Recomendação", bold: true, color: "FFFFFF" })] })] }),
            ]
          }),
          ...([
            ["Objetivo", "Visitas ao perfil / Mensagens (Direct)"],
            ["Público", "Mulheres 28–55 anos, donos de negócios, área de saúde"],
            ["Localização", "Sua cidade + raio de 50km (ou Brasil inteiro se o ebook é digital)"],
            ["Interesses", "Saúde, clínicas, empreendedorismo, estética, odontologia"],
            ["Duração", "7 dias por post"],
            ["Orçamento sugerido", "R$ 10–20/dia por post (total: R$ 70–140 por post impulsionado)"],
            ["CTA do botão", '"Saiba mais" ou "Enviar mensagem"'],
          ]).map(([col1, col2]) => new TableRow({
            children: [
              new TableCell({ width: { size: 3000, type: WidthType.DXA }, children: [new Paragraph({ children: [new TextRun({ text: col1, bold: true, size: 20 })] })] }),
              new TableCell({ width: { size: 6000, type: WidthType.DXA }, children: [new Paragraph({ children: [new TextRun({ text: col2, size: 20 })] })] }),
            ]
          }))
        ]
      }),
      p(""),

      h2("Hashtags para usar em todos os posts:"),
      p("#VigilânciaSanitária  #FiscalizaçãoSanitária  #DireitoSanitário  #ClínicaEstética  #AnvisaBrasil  #ClínicaSegura  #EmpreendedorismoDaSaúde  #AlvaráSanitário  #DraJulianaFreitas  #GuiaFiscalizaçãoSanitária"),
      divider(),

      // ── MÉTRICAS ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("6. MÉTRICAS PARA ACOMPANHAR"),

      bullet("Alcance dos posts impulsionados (meta: +500 pessoas por post)"),
      bullet("Cliques no link da bio (meta: taxa de 2–5% do alcance)"),
      bullet("Mensagens recebidas no Direct (responda SEMPRE em até 2h)"),
      bullet("Conversas iniciadas no WhatsApp"),
      bullet("Vendas realizadas no Kiwify"),
      p(""),
      p("Dica: Teste dois criativos diferentes impulsionados ao mesmo tempo com R$10/dia cada e mantenha o que performar melhor.", { bold: true, color: "8B6914" }),
      divider(),

      // ── PRÓXIMOS PASSOS ──
      h1("7. PRÓXIMOS PASSOS"),
      bullet("Definir o preço do ebook e configurar no Kiwify"),
      bullet("Colocar o link do produto na bio do Instagram"),
      bullet("Gravar o primeiro Reels (roteiro do Dia 3 acima)"),
      bullet("Preparar lista de transmissão no WhatsApp com sua base de contatos"),
      bullet("Publicar o Story de enquete (Dia 1) para aquecer o público"),
      bullet("Após 7 dias de publicação orgânica, impulsionar o post com mais engajamento"),
      p(""),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 400, after: 200 },
        children: [new TextRun({ text: "💛 Dra. Juliana — você tem tudo para converter muito com esse ebook!", bold: true, color: "8B6914", size: 26 })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/sessions/elegant-gifted-galileo/mnt/POSICIONAMENTO DIGITAL/Campanha_GuiaFiscalizacao.docx', buf);
  console.log('Saved!');
});
