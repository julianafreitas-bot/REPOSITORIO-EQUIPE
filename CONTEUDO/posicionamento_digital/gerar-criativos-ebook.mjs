import OpenAI from "openai";
import fs from "fs";
import path from "path";
import https from "https";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const client = new OpenAI();

const OUT_DIR = __dirname;

const criativos = [
  {
    arquivo: "Criativo_01_Dor.png",
    label: "01 — Dor/Medo",
    prompt:
      "Photorealistic cinematic scene inside a modern elegant Brazilian aesthetic clinic. A serious official health inspector in dark uniform with government badge stands at the entrance holding a clipboard. Clinic interior: white reclined treatment bed, aesthetic laser equipment, mirrors, soft pink beige walls. A Brazilian woman clinic owner in her 30s, cream blazer, looks shocked and worried in background. Dramatic cinematic lighting, deep dark shadows, warm golden highlights. Wide shot, bottom third of frame darker and emptier for text overlay. Ultra-realistic 4K photography, shallow depth of field, square 1:1 format.",
  },
  {
    arquivo: "Criativo_02_Cena.png",
    label: "02 — Cena Interditada",
    prompt:
      "Photorealistic dramatic close-up of the entrance glass door of a high-end Brazilian aesthetic clinic. Official red government seal sticker INTERDITADO VIGILANCIA SANITARIA affixed to the glass. Yellow and black caution tape stretched across the doorway. Through the glass, luxurious clinic interior softly visible: white reclining treatment bed, skincare products on shelves, beige elegant walls. Modern upscale commercial building exterior. Cinematic deep dramatic shadows, warm golden light. Silent, abandoned, alarming atmosphere. Ultra-realistic 4K photography, square 1:1 format, bottom third darker for text overlay.",
  },
  {
    arquivo: "Criativo_03_Curiosidade.png",
    label: "03 — Curiosidade",
    prompt:
      "Photorealistic flat-lay top-down shot of a modern dark marble desk in an aesthetic clinic office. On the desk: official Brazilian government inspection document auto de infracao sanitaria, fountain pen, business card, smartphone with notification, closed professional notebook. Dramatic warm desk lamp casting golden glow on dark background. Professional and slightly alarming mood, like discovering a serious compliance problem. Ultra-realistic 4K photography, square 1:1 format, bottom third clean and dark for text overlay.",
  },
  {
    arquivo: "Criativo_04_Autoridade.png",
    label: "04 — Autoridade/Transformação",
    prompt:
      "Photorealistic professional portrait of a confident elegant Brazilian businesswoman in her 30s, stylish cream blazer, arms confidently crossed, smiling with authority. Standing inside a luxurious modern Brazilian aesthetic clinic: white treatment bed, organized skincare shelves, warm professional lighting, beige and white elegant interior. Warm cinematic golden tones from above, powerful successful in control energy. She looks like an expert consultant who protects businesses. Ultra-realistic 4K editorial photography, square 1:1 format, bottom third slightly darker for text overlay, shallow depth of field.",
  },
];

async function downloadImage(url, filePath) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(filePath);
    https.get(url, (response) => {
      response.pipe(file);
      file.on("finish", () => {
        file.close();
        resolve();
      });
    }).on("error", reject);
  });
}

async function main() {
  console.log("=".repeat(55));
  console.log("Gerando criativos — Guia Fiscalização Sanitária");
  console.log("Público: Donas de clínicas de estética");
  console.log("=".repeat(55));

  for (const item of criativos) {
    console.log(`\n>>> ${item.label}`);
    console.log("    Gerando... aguarde");

    try {
      const response = await client.images.generate({
        model: "dall-e-3",
        prompt: item.prompt,
        n: 1,
        size: "1024x1024",
        quality: "hd",
      });

      const url = response.data[0].url;
      const filePath = path.join(OUT_DIR, item.arquivo);
      await downloadImage(url, filePath);
      console.log(`    [OK] ${item.arquivo}`);
    } catch (err) {
      console.error(`    [ERRO] ${err.message}`);
    }
  }

  console.log("\n" + "=".repeat(55));
  console.log("Pronto! Abra as imagens no Canva para adicionar textos.");
  console.log("=".repeat(55));
}

main();
