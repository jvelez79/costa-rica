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

# Prompt para calendario del viaje
CALENDAR_PROMPT = """
Create a beautiful, modern travel calendar infographic for a 7-day trip to Costa Rica
(November 23-29, 2025). The calendar should be visually appealing with a tropical,
vibrant Costa Rican aesthetic.

Layout should show 7 days horizontally or in a clean grid, with each day containing:

DAY 1 (Sun Nov 23):
- Arrival San José ✈️
- Airport pickup 🚗
- Hotel check-in 🏨

DAY 2 (Mon Nov 24):
- Drive to La Fortuna 🚗
- Arenal Volcano 🌋
- Hot Springs ♨️

DAY 3 (Tue Nov 25):
- ATV Adventure 🏍️
- Whitewater Rafting 🌊
- La Fortuna Waterfall 💦

DAY 4 (Wed Nov 26):
- Return to San José 🚗
- City Tour 🏛️
- Artisan Market 🎨

DAY 5 (Thu Nov 27):
- Cartago Visit 🏛️
- Basilica ⛪
- Irazú Volcano 🌋❄️

DAY 6 (Fri Nov 28):
- Free Day San José 🛍️
- Shopping & Relax ☕
- Trip Preparation 🧳

DAY 7 (Sat Nov 29):
- Early Checkout ⏰
- Return Flight ✈️
- Back Home 🏠

Style: Modern, colorful, tropical vibes with Costa Rican colors (blue, white, red accents),
clean typography, icons for each activity, professional travel brochure aesthetic,
infographic style, vibrant but organized layout, each day clearly separated
"""

def generate_calendar():
    """Genera la imagen del calendario usando Gemini 2.5 Flash Image"""

    print(f"🎨 Generando imagen de calendario con {MODEL}...")
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
        output_path = OUTPUT_DIR / "calendar-hero.jpg"

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
