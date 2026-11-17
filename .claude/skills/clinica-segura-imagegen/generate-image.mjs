#!/usr/bin/env node
// Gera uma imagem via GPT Image 2 (OpenAI) e salva como PNG local.
//
// Uso:
//   node generate-image.mjs "<prompt completo>" [nome-do-arquivo.png] [tamanho]
//
// Exemplo:
//   node generate-image.mjs "editorial photo of..." fiscalizacao-post.png 1024x1024

import "dotenv/config";
import OpenAI from "openai";
import fs from "fs";
import path from "path";

const [, , promptArg, outputArg, sizeArg] = process.argv;

if (!promptArg) {
  console.error(
    'Uso: node generate-image.mjs "<prompt>" [nome-do-arquivo.png] [tamanho]'
  );
  process.exit(1);
}

if (!process.env.OPENAI_API_KEY) {
  console.error(
    "OPENAI_API_KEY não encontrada. Crie um arquivo .env (veja .env.example) com sua chave da OpenAI."
  );
  process.exit(1);
}

const outputFile = outputArg || `clinica-segura-${Date.now()}.png`;
const size = sizeArg || "1024x1024";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function main() {
  console.log("Gerando imagem com GPT Image 2...");
  console.log(`Tamanho: ${size}`);
  console.log(`Prompt: ${promptArg.slice(0, 120)}${promptArg.length > 120 ? "..." : ""}`);

  const result = await client.images.generate({
    model: "gpt-image-2",
    prompt: promptArg,
    size,
    n: 1,
  });

  const b64 = result.data[0].b64_json;
  const buffer = Buffer.from(b64, "base64");
  const outPath = path.resolve(process.cwd(), outputFile);

  fs.writeFileSync(outPath, buffer);
  console.log(`\n✅ Imagem salva em: ${outPath}`);
}

main().catch((err) => {
  console.error("Erro ao gerar imagem:", err.message || err);
  process.exit(1);
});
