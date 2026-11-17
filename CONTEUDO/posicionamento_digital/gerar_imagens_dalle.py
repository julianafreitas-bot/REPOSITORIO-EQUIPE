"""
Gerador de criativos via DALL-E 3
Campanha: Guia Prático para Fiscalização Sanitária
Público: Donas de clínicas de estética

USO:
    export OPENAI_API_KEY="sua-chave-aqui"
    python gerar_imagens_dalle.py
"""

import os
import urllib.request
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

criativos = [
    {
        "arquivo": "Criativo_01_Dor.png",
        "descricao": "Criativo 01 — Dor/Medo",
        "prompt": (
            "Photorealistic cinematic scene inside a modern, elegant Brazilian aesthetic clinic (clínica de estética). "
            "A serious official health inspector in a dark uniform with a government badge stands at the entrance holding a clipboard. "
            "The clinic interior: white reclined treatment bed, aesthetic laser equipment, mirrors, soft pink and beige walls. "
            "A Brazilian woman clinic owner in her 30s, professional cream blazer, looks shocked and worried in the background. "
            "Dramatic cinematic lighting, deep dark shadows, warm golden highlights on the decor. "
            "Wide shot composition, bottom third of frame darker and emptier for text overlay. "
            "Ultra-realistic 4K photography, shallow depth of field, square 1:1 format."
        ),
    },
    {
        "arquivo": "Criativo_02_Cena.png",
        "descricao": "Criativo 02 — Cena Interditada",
        "prompt": (
            "Photorealistic dramatic close-up of the entrance glass door of a high-end Brazilian aesthetic clinic. "
            "An official red government seal sticker 'INTERDITADO - VIGILÂNCIA SANITÁRIA' is affixed to the glass. "
            "Yellow and black caution tape is stretched across the doorway. "
            "Through the glass, the luxurious clinic interior is softly visible: white reclining treatment bed, skincare products on shelves, beige elegant walls. "
            "The exterior is a modern upscale commercial building. "
            "Cinematic lighting with deep dramatic shadows and warm golden light. "
            "The scene feels silent, abandoned, alarming. "
            "Ultra-realistic 4K photography, square 1:1 format, bottom third darker for text overlay."
        ),
    },
    {
        "arquivo": "Criativo_03_Curiosidade.png",
        "descricao": "Criativo 03 — Curiosidade",
        "prompt": (
            "Photorealistic flat-lay top-down shot of a modern dark marble desk in an aesthetic clinic office. "
            "On the desk: an official Brazilian government inspection document (auto de infração sanitária), a fountain pen, a business card, "
            "a smartphone showing a notification, a closed professional notebook with gold pen. "
            "Dramatic warm desk lamp light casting golden glow. "
            "Dark background with rich warm gold tones. "
            "The mood is professional and slightly alarming — like discovering a serious compliance problem. "
            "Ultra-realistic 4K photography, square 1:1 format, bottom third of frame clean and dark for text overlay."
        ),
    },
    {
        "arquivo": "Criativo_04_Autoridade.png",
        "descricao": "Criativo 04 — Autoridade/Transformação",
        "prompt": (
            "Photorealistic professional portrait of a confident, elegant Brazilian businesswoman in her 30s, "
            "wearing a stylish cream blazer, arms confidently crossed, smiling with authority. "
            "She stands inside a luxurious modern Brazilian aesthetic clinic (clínica de estética): "
            "white treatment bed, organized skincare product shelves, soft professional warm lighting, beige and white elegant interior. "
            "The lighting is warm and cinematic with golden tones from above — powerful, successful, in control. "
            "She looks like an expert and protector — a lawyer or consultant who solves problems. "
            "Ultra-realistic 4K editorial photography, square 1:1 format, bottom third slightly darker for text overlay, "
            "shallow depth of field."
        ),
    },
]


def baixar_imagem(url, caminho):
    urllib.request.urlretrieve(url, caminho)


def gerar():
    print("=" * 60)
    print("Gerando criativos via DALL-E 3...")
    print(f"Salvando em: {OUT_DIR}")
    print("=" * 60)

    for item in criativos:
        print(f"\n>>> {item['descricao']}")
        print("    Gerando... (pode levar 15-30 segundos)")

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=item["prompt"],
                n=1,
                size="1024x1024",
                quality="hd",
            )

            url = response.data[0].url
            caminho = os.path.join(OUT_DIR, item["arquivo"])
            baixar_imagem(url, caminho)
            print(f"    [OK] Salvo: {item['arquivo']}")

        except Exception as e:
            print(f"    [ERRO] {e}")

    print("\n" + "=" * 60)
    print("Pronto! Abra as imagens no Canva para adicionar os textos.")
    print("=" * 60)


if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERRO: Defina a variável OPENAI_API_KEY antes de rodar.")
        print('  export OPENAI_API_KEY="sk-..."')
        exit(1)
    gerar()
