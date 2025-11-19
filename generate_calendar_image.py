#!/usr/bin/env python3
"""
Script para generar imagen de calendario del viaje a Costa Rica
usando Gemini 2.5 Flash Image (Nano Banana)

Uso:
    python3 generate_calendar_image.py YOUR_API_KEY
    O configura GOOGLE_AI_API_KEY como variable de entorno
"""

from google import genai
from google.genai import types
from pathlib import Path
import os
import sys

# Configuración
API_KEY = os.getenv('GOOGLE_API_KEY') or os.getenv('GOOGLE_AI_API_KEY') or (sys.argv[1] if len(sys.argv) > 1 else None)
if not API_KEY:
    print("❌ Error: Se requiere API Key")
    print("Uso: python3 generate_calendar_image.py YOUR_API_KEY")
    print("O configura: export GOOGLE_API_KEY=your_key")
    sys.exit(1)

OUTPUT_DIR = Path("docs/assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL = "gemini-2.5-flash-image"

# Prompt para background decorativo tropical (SIN TEXTO)
CALENDAR_PROMPT = """
Tropical Costa Rica themed decorative background for a travel website hero image.
Lush tropical rainforest elements: monstera leaves, palm fronds, banana leaves,
vibrant red and orange hibiscus flowers, colorful toucan birds, blue morpho butterflies,
tropical paradise atmosphere. Rich emerald greens, ocean blues, sunset oranges,
vibrant reds from flowers. Professional nature photography aesthetic, photorealistic style.

IMPORTANT - NO TEXT ELEMENTS:
- NO words, NO letters, NO numbers, NO text of any kind
- NO calendar cards, NO date boxes, NO information panels
- NO title, NO labels, NO captions
- PURE decorative natural background ONLY

Composition: Frame the decorative elements around the edges (top corners, bottom corners),
leaving the center area relatively clear for overlay content. Tropical foliage and flowers
should feel natural and organic, not artificial. Lighting: bright, vibrant, tropical sunlight.

Style: National Geographic nature photography, professional travel brochure background,
photorealistic, high quality, 16:9 aspect ratio
"""

def generate_calendar():
    """Genera el background tropical decorativo usando Gemini 2.5 Flash Image"""

    print(f"🎨 Generando background tropical decorativo con {MODEL}...")
    print(f"💰 Costo estimado: ~$0.039 USD\n")

    # Crear cliente
    client = genai.Client(api_key=API_KEY)

    try:
        # Generar imagen
        response = client.models.generate_content(
            model=MODEL,
            contents=[CALENDAR_PROMPT],
            config=types.GenerateContentConfig(
                response_modalities=["Image"],
                image_config=types.ImageConfig(
                    aspect_ratio="16:9"  # Horizontal para calendario
                )
            )
        )

        # Extraer y guardar imagen
        output_path = OUTPUT_DIR / "tropical-bg.jpg"

        if response.candidates:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'inline_data'):
                    with open(output_path, 'wb') as f:
                        f.write(part.inline_data.data)

                    print(f"✅ Imagen guardada en: {output_path}")
                    print(f"📏 Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
                    print(f"\n📝 Para insertar en markdown:")
                    print(f"![Calendario del Viaje](assets/images/calendar-hero.jpg)")
                    return True

        print("❌ No se pudo extraer la imagen de la respuesta")
        return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    generate_calendar()
