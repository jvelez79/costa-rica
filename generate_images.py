#!/usr/bin/env python3
"""
Script para generar imágenes hero usando Gemini 2.5 Flash Image (Nano Banana)
"""

import os
import base64
from google import genai
from google.genai import types
from pathlib import Path

# Configuración
API_KEY = "AIzaSyB95sk8qucSwdzbpPxXGZ4Oqs2R2xNkvlY"
OUTPUT_DIR = Path("/home/juanca/Documents/viaje-costa-rica/docs/assets/images")
MODEL = "gemini-2.5-flash-image"

# Crear cliente
client = genai.Client(api_key=API_KEY)

# Definición de todas las imágenes a generar
IMAGES = [
    {
        "filename": "vuelos-hero.jpg",
        "prompt": "Modern airport terminal at sunset, Copa Airlines Boeing 737 on tarmac, tropical vibes, warm golden hour lighting, travelers with luggage walking towards gate, palm trees visible through windows, professional travel photography, cinematic composition, vibrant colors, photorealistic style"
    },
    {
        "filename": "itinerario-hero.jpg",
        "prompt": "Costa Rica adventure collage, split composition showing volcano arenal, lush rainforest, thermal pools, and city streets of San Jose, vibrant tropical colors, golden hour lighting, aerial perspective, professional travel photography, dynamic composition, sense of adventure and exploration, photorealistic style"
    },
    {
        "filename": "alojamientos-hero.jpg",
        "prompt": "Luxury tropical villa in Costa Rica, modern architecture with infinity pool, volcano arenal view in background, lush jungle surroundings, warm sunset lighting, inviting atmosphere, professional real estate photography, high-end vacation rental vibes, photorealistic style"
    },
    {
        "filename": "ropa-hero.jpg",
        "prompt": "Organized travel packing flat lay, adventure clothing for tropical vacation, hiking boots, rain jacket, swimwear, light summer clothes neatly arranged on wooden table, natural daylight, top-down view, minimalist aesthetic, travel preparation concept, photorealistic style"
    },
    {
        "filename": "volcan-arenal-hero.jpg",
        "prompt": "Majestic Arenal Volcano in Costa Rica, perfect cone shape, lush tropical rainforest at base, morning mist, dramatic clouds, professional landscape photography, vibrant greens, sense of scale and grandeur, national geographic style, photorealistic"
    },
    {
        "filename": "aguas-termales-hero.jpg",
        "prompt": "Luxury thermal hot springs in Costa Rica, turquoise natural pools surrounded by tropical jungle, volcanic steam rising, warm ambient lighting at dusk, people relaxing in background, serene spa atmosphere, professional resort photography, inviting and peaceful, photorealistic style"
    },
    {
        "filename": "rafting-hero.jpg",
        "prompt": "Whitewater rafting action shot in Costa Rica, group of adventurers navigating rapids, splashing water, lush jungle river banks, dynamic composition, mid-action freeze frame, vibrant tropical colors, exciting adventure photography, sense of thrill and teamwork, photorealistic style"
    },
    {
        "filename": "restaurantes-la-fortuna-hero.jpg",
        "prompt": "Traditional Costa Rican cuisine plated beautifully, casado dish with rice beans plantains and grilled fish, tropical outdoor restaurant setting with jungle views, natural daylight, vibrant fresh ingredients, professional food photography, warm inviting atmosphere, photorealistic style"
    },
    {
        "filename": "restaurantes-san-jose-hero.jpg",
        "prompt": "Modern upscale restaurant interior in San Jose Costa Rica, stylish urban dining room with tropical touches, beautifully plated fusion cuisine, warm ambient lighting, bustling atmosphere, professional restaurant photography, cosmopolitan vibes, photorealistic style"
    },
    {
        "filename": "cocktails-la-fortuna-hero.jpg",
        "prompt": "Tropical cocktails on rustic wooden bar, colorful drinks with fresh fruit garnishes, jungle rainforest background, tiki bar atmosphere, golden hour lighting, condensation on glasses, professional beverage photography, vacation paradise vibes, photorealistic style"
    },
    {
        "filename": "cocktails-san-jose-hero.jpg",
        "prompt": "Sophisticated speakeasy cocktail bar interior in San Jose, craft cocktails being prepared by bartender, moody atmospheric lighting, vintage modern decor with tropical accents, premium spirits display, intimate urban nightlife vibe, professional bar photography, photorealistic style"
    },
    {
        "filename": "panama-tips-hero.jpg",
        "prompt": "Panama City skyline with modern skyscrapers and waterfront, Tocumen International Airport visible, tropical urban landscape, blue hour lighting, sense of transit and connection, professional travel photography, vibrant metropolitan atmosphere, photorealistic style"
    },
    {
        "filename": "panama-metro-hero.jpg",
        "prompt": "Modern Panama Metro station interior, clean efficient public transportation, travelers with luggage, contemporary architecture, bright natural lighting, sense of movement and connectivity, professional urban photography, photorealistic style"
    },
    {
        "filename": "panama-restaurantes-hero.jpg",
        "prompt": "Albrook Mall food court and restaurants in Panama City, diverse dining options, modern shopping center interior, travelers and locals eating, vibrant atmosphere, professional architectural photography, sense of variety and convenience, photorealistic style"
    }
]

def generate_image(prompt: str, filename: str, aspect_ratio: str = "16:9"):
    """Genera una imagen usando Gemini 2.5 Flash Image"""
    print(f"\n🎨 Generando: {filename}")
    print(f"   Prompt: {prompt[:80]}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["Image"],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio
                )
            )
        )

        # Extraer la imagen de la respuesta
        if response.candidates and len(response.candidates) > 0:
            candidate = response.candidates[0]
            if candidate.content and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        # Guardar la imagen
                        image_data = part.inline_data.data
                        output_path = OUTPUT_DIR / filename

                        with open(output_path, 'wb') as f:
                            f.write(image_data)

                        print(f"   ✅ Guardada en: {output_path}")
                        return True

        print(f"   ❌ Error: No se pudo extraer la imagen de la respuesta")
        return False

    except Exception as e:
        print(f"   ❌ Error al generar: {str(e)}")
        return False

def main():
    """Función principal"""
    print("=" * 70)
    print("🍌 GENERADOR DE IMÁGENES - Nano Banana (Gemini 2.5 Flash Image)")
    print("=" * 70)
    print(f"\nDirectorio de salida: {OUTPUT_DIR}")
    print(f"Total de imágenes a generar: {len(IMAGES)}")
    print(f"Costo estimado: ${len(IMAGES) * 0.039:.2f} USD")

    # Confirmar que el directorio existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Generar cada imagen
    successful = 0
    failed = 0

    for i, image_config in enumerate(IMAGES, 1):
        print(f"\n[{i}/{len(IMAGES)}]", end=" ")

        success = generate_image(
            prompt=image_config["prompt"],
            filename=image_config["filename"]
        )

        if success:
            successful += 1
        else:
            failed += 1

    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE GENERACIÓN")
    print("=" * 70)
    print(f"✅ Exitosas: {successful}")
    print(f"❌ Fallidas: {failed}")
    print(f"📁 Ubicación: {OUTPUT_DIR}")
    print("\n¡Proceso completado!")

if __name__ == "__main__":
    main()
