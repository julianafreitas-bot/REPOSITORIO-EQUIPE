#!/usr/bin/env node
// Gera fotografias profissionais da Dra. Juliana Freitas preservando a identidade facial,
// enviando as fotos da pasta referencias/ para a API de imagens da OpenAI (endpoint de edição).
//
// Uso:
//   node gerar-foto.mjs --cena "<descrição da cena em inglês>" [opções]
//
// Opções:
//   --cena "..."        Cenário, roupa, pose e expressão (obrigatório, salvo com --prompt)
//   --prompt "..."      Prompt completo, substitui o modelo padrão (uso avançado)
//   --formato 4:5       4:5 (feed, padrão) | 9:16 (stories/reels) | 1:1 | 3:2 (paisagem/LinkedIn)
//   --nome arquivo      Nome base do arquivo de saída (sem extensão)
//   --variacoes 1       Quantas versões gerar na mesma chamada (1 a 4)
//   --qualidade high    high (padrão) | medium | low
//   --refs pasta        Pasta das fotos de referência (padrão: ./referencias)
//   --seco              Só mostra o prompt montado, sem chamar a API

import "dotenv/config";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import sharp from "sharp";

const DIR = path.dirname(fileURLToPath(import.meta.url));

// ---------- argumentos ----------
const args = {};
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (!a.startsWith("--")) continue;
  const key = a.slice(2);
  const next = argv[i + 1];
  if (next === undefined || next.startsWith("--")) args[key] = true;
  else { args[key] = next; i++; }
}

const FORMATOS = {
  "4:5":  { size: "1024x1536", ratio: 4 / 5 },
  "9:16": { size: "1024x1536", ratio: 9 / 16 },
  "1:1":  { size: "1024x1024", ratio: 1 },
  "3:2":  { size: "1536x1024", ratio: 3 / 2 },
};

const formato = String(args.formato || "4:5");
if (!FORMATOS[formato]) sair(`Formato inválido: ${formato}. Use 4:5, 9:16, 1:1 ou 3:2.`);
if (!args.cena && !args.prompt) sair('Informe a cena. Ex.: node gerar-foto.mjs --cena "seated in a modern office..."');

const variacoes = Math.min(Math.max(parseInt(args.variacoes || "1", 10) || 1, 1), 4);
const qualidade = String(args.qualidade || "high");
const pastaRefs = path.resolve(DIR, String(args.refs || "referencias"));
const pastaSaida = path.resolve(DIR, "saidas");
const nomeBase = slug(String(args.nome || `juliana-${formato.replace(":", "x")}-${carimbo()}`));

// ---------- prompt ----------
const IDENTIDADE = fs.readFileSync(path.join(DIR, "prompts", "identidade.txt"), "utf8").trim();
const FOTOGRAFIA = fs.readFileSync(path.join(DIR, "prompts", "fotografia.txt"), "utf8").trim();

const prompt = args.prompt
  ? String(args.prompt)
  : [
      IDENTIDADE,
      `SCENE AND STYLING:\n${String(args.cena).trim()}`,
      FOTOGRAFIA.replace("{FORMATO}", formato),
    ].join("\n\n");

// ---------- referências ----------
const refs = fs.existsSync(pastaRefs)
  ? fs.readdirSync(pastaRefs)
      .filter((f) => /\.(jpe?g|png|webp)$/i.test(f))
      .sort()
      .map((f) => path.join(pastaRefs, f))
  : [];

if (args.seco) {
  console.log("=== PROMPT MONTADO ===\n");
  console.log(prompt);
  console.log(`\n=== ${refs.length} referência(s) ===`);
  refs.forEach((r) => console.log(" -", path.basename(r)));
  console.log(`\nFormato ${formato} | gera ${FORMATOS[formato].size} | ${variacoes} variação(ões) | qualidade ${qualidade}`);
  process.exit(0);
}

if (!process.env.OPENAI_API_KEY) sair("OPENAI_API_KEY não encontrada. Crie o arquivo .env (copie de .env.example) com sua chave.");
if (refs.length === 0) sair(`Nenhuma foto de referência em ${pastaRefs}. Coloque de 2 a 6 fotos nítidas do rosto.`);

const MODELO = process.env.OPENAI_IMAGE_MODEL || "gpt-image-2";

// ---------- chamada à API ----------
async function chamarAPI(comFidelidade) {
  const form = new FormData();
  form.append("model", MODELO);
  form.append("prompt", prompt);
  form.append("size", FORMATOS[formato].size);
  form.append("quality", qualidade);
  form.append("n", String(variacoes));
  if (comFidelidade) form.append("input_fidelity", "high");

  for (const r of refs.slice(0, 6)) {
    // Normaliza cada referência para JPEG de até 2048px (evita arquivos pesados ou HEIC renomeado)
    const buf = await sharp(r).rotate().resize({ width: 2048, height: 2048, fit: "inside", withoutEnlargement: true }).jpeg({ quality: 92 }).toBuffer();
    form.append("image[]", new Blob([buf], { type: "image/jpeg" }), path.basename(r).replace(/\.\w+$/, ".jpg"));
  }

  const resp = await fetch("https://api.openai.com/v1/images/edits", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
    body: form,
  });
  const json = await resp.json().catch(() => ({}));
  if (!resp.ok) {
    const msg = json?.error?.message || `HTTP ${resp.status}`;
    const err = new Error(msg);
    err.fidelidade = /input_fidelity/i.test(msg);
    throw err;
  }
  return json;
}

async function main() {
  console.log(`Gerando ${variacoes} imagem(ns) | modelo ${MODELO} | formato ${formato} | ${refs.length} referência(s)...`);
  let json;
  try {
    json = await chamarAPI(true);
  } catch (e) {
    if (!e.fidelidade) throw e;
    console.log("O modelo não aceita o ajuste de fidelidade; repetindo sem ele...");
    json = await chamarAPI(false);
  }

  fs.mkdirSync(pastaSaida, { recursive: true });
  const salvos = [];
  for (let i = 0; i < json.data.length; i++) {
    const original = Buffer.from(json.data[i].b64_json, "base64");
    const sufixo = json.data.length > 1 ? `-v${i + 1}` : "";
    const final = await recortar(original, FORMATOS[formato].ratio);
    const arq = path.join(pastaSaida, `${nomeBase}${sufixo}.png`);
    fs.writeFileSync(arq, final);
    salvos.push(arq);
  }
  console.log("\n✅ Imagem(ns) salva(s):");
  salvos.forEach((s) => console.log("  " + s));
  console.log("\nConfira o rosto antes de publicar. Se não estiver fiel, gere de novo ou ajuste as referências.");
}

// Recorta para a proporção exata, priorizando a região de maior interesse (rosto)
async function recortar(buf, ratio) {
  const img = sharp(buf);
  const { width, height } = await img.metadata();
  const atual = width / height;
  if (Math.abs(atual - ratio) < 0.01) return img.png().toBuffer();
  let w = width, h = height;
  if (atual > ratio) w = Math.round(height * ratio);
  else h = Math.round(width / ratio);
  return sharp(buf).resize(w, h, { fit: "cover", position: sharp.strategy.attention }).png().toBuffer();
}

function slug(s) { return s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^\w-]+/g, "-").toLowerCase(); }
function carimbo() { const d = new Date(); return d.toISOString().slice(0, 16).replace(/[-:T]/g, ""); }
function sair(msg) { console.error("❌ " + msg); process.exit(1); }

main().catch((e) => sair("Erro ao gerar imagem: " + (e.message || e)));
