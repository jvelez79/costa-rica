#!/usr/bin/env python3
"""
Crea calendario estilo la imagen original de IA
con degradado azul, tarjetas verticales, y decoraciones tropicales
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Configuración
OUTPUT_DIR = Path("docs/assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH = OUTPUT_DIR / "calendar-hero.jpg"

# Dimensiones (16:9 para hero image)
WIDTH = 1920
HEIGHT = 1080

# Colores (esquema azul oceánico)
COLOR_BG_TOP = (35, 67, 126)        # Azul oscuro
COLOR_BG_BOTTOM = (65, 182, 196)    # Cyan/turquesa
COLOR_CARD = (255, 255, 255)        # Blanco
COLOR_TITLE_CYAN = (65, 182, 196)   # Cyan para "COSTA RICA"
COLOR_TITLE_WHITE = (255, 255, 255) # Blanco para "ADVENTURE"
COLOR_SUBTITLE_RED = (231, 76, 60)  # Rojo para fechas
COLOR_TEXT_DARK = (37, 71, 106)     # Azul oscuro para texto tarjetas
COLOR_TEXT_MED = (52, 84, 122)      # Azul medio

# Datos del itinerario
DAYS = [
    {
        "day_num": "1",
        "day_name": "Sun Nov 23",
        "activities": [
            "✈️ Arrival San José",
            "🚗 Airport pick-up",
            "🏨 Hotel Aloft"
        ]
    },
    {
        "day_num": "2",
        "day_name": "Mon Nov 24",
        "activities": [
            "🚗 → La Fortuna",
            "🌋 Arenal Volcano",
            "♨️ Hot Springs"
        ]
    },
    {
        "day_num": "3",
        "day_name": "Tue Nov 25",
        "activities": [
            "🏍️ ATV Adventure",
            "🌊 Whitewater Rafting",
            "💦 Waterfall 70m"
        ]
    },
    {
        "day_num": "4",
        "day_name": "Wed Nov 26",
        "activities": [
            "🚗 → San José",
            "🏛️ City Tour",
            "🎨 Artisan Market"
        ]
    },
    {
        "day_num": "5",
        "day_name": "Thu Nov 27",
        "activities": [
            "🏛️ Cartago",
            "⛪ Basilica",
            "🌋 Irazú Volcano"
        ]
    },
    {
        "day_num": "6",
        "day_name": "Fri Nov 28",
        "activities": [
            "🛍️ Shopping & Relax",
            "☕ Explore SJ",
            "🧳 Trip Preparation"
        ]
    },
    {
        "day_num": "7",
        "day_name": "Sat Nov 29",
        "activities": [
            "⏰ Early Checkout",
            "🚗 Return vehicles",
            "✈️ Return Flight"
        ]
    }
]

def create_gradient_background(width, height, color_top, color_bottom):
    """Crea un fondo con degradado vertical"""
    base = Image.new('RGB', (width, height), color_top)
    draw = ImageDraw.Draw(base)

    for y in range(height):
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return base

def add_simple_decorations(img):
    """Añade decoraciones geométricas simples estilo ilustración"""

    # Convertir a RGBA para transparencias
    img_rgba = img.convert('RGBA')
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    # Colores decorativos (semi-transparentes)
    color_green = (46, 204, 113, 120)      # Verde hoja
    color_red = (231, 76, 60, 140)         # Rojo flor
    color_orange = (230, 126, 34, 130)     # Naranja/amarillo
    color_cyan = (52, 152, 219, 100)       # Cyan

    # Círculos decorativos sutiles (burbujas/luces)
    circles_top = [
        (100, 80, 15), (250, 100, 10), (WIDTH - 200, 90, 12), (WIDTH - 90, 70, 18)
    ]
    circles_bottom = [
        (80, HEIGHT - 100, 20), (200, HEIGHT - 120, 14),
        (WIDTH - 180, HEIGHT - 110, 16), (WIDTH - 70, HEIGHT - 90, 22)
    ]

    for x, y, r in circles_top:
        draw_overlay.ellipse([x-r, y-r, x+r, y+r], fill=color_cyan)

    for x, y, r in circles_bottom:
        draw_overlay.ellipse([x-r, y-r, x+r, y+r], fill=color_green)

    # Círculos más pequeños adicionales
    for i in range(10):
        import random
        if i < 5:
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, 150)
        else:
            x = random.randint(50, WIDTH - 50)
            y = random.randint(HEIGHT - 150, HEIGHT - 50)
        r = random.randint(5, 12)
        color = random.choice([color_green, color_cyan, color_red, color_orange])
        draw_overlay.ellipse([x-r, y-r, x+r, y+r], fill=color)

    # Combinar
    result = Image.alpha_composite(img_rgba, overlay)
    return result.convert('RGB')

def create_calendar():
    """Genera el calendario con estilo de la imagen original"""
    print("🎨 Creando calendario estilo original...")

    # Usar degradado azul limpio (sin tropical-bg complex)
    print("📐 Creando fondo con degradado azul limpio")
    img = create_gradient_background(WIDTH, HEIGHT, COLOR_BG_TOP, COLOR_BG_BOTTOM)

    # Añadir decoraciones simples
    img = add_simple_decorations(img)

    # Cargar fuentes
    try:
        font_title_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_title_med = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_day_num = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        font_day_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        font_activity = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        print("⚠️  Usando fuente por defecto")
        font_title_large = ImageFont.load_default()
        font_title_med = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_day_num = ImageFont.load_default()
        font_day_name = ImageFont.load_default()
        font_activity = ImageFont.load_default()

    draw = ImageDraw.Draw(img)

    # Título: "COSTA RICA ADVENTURE"
    title_y = 50

    # "COSTA RICA" en cyan
    costa_text = "COSTA "
    rica_text = "RICA "
    adv_text = "ADVENTURE"

    # Calcular posiciones para centrar todo el título
    costa_bbox = draw.textbbox((0, 0), costa_text, font=font_title_large)
    rica_bbox = draw.textbbox((0, 0), rica_text, font=font_title_large)
    adv_bbox = draw.textbbox((0, 0), adv_text, font=font_title_large)

    costa_width = costa_bbox[2] - costa_bbox[0]
    rica_width = rica_bbox[2] - rica_bbox[0]
    adv_width = adv_bbox[2] - adv_bbox[0]

    total_width = costa_width + rica_width + adv_width
    start_x = (WIDTH - total_width) // 2

    # Dibujar título
    draw.text((start_x, title_y), costa_text, fill=COLOR_TITLE_CYAN, font=font_title_large)
    draw.text((start_x + costa_width, title_y), rica_text, fill=COLOR_TITLE_CYAN, font=font_title_large)
    draw.text((start_x + costa_width + rica_width, title_y), adv_text, fill=COLOR_TITLE_WHITE, font=font_title_large)

    # Subtítulo: "NOV 23-29, 2025" en rojo
    subtitle1 = "NOV 23-29, 2025"
    sub1_bbox = draw.textbbox((0, 0), subtitle1, font=font_subtitle)
    sub1_width = sub1_bbox[2] - sub1_bbox[0]
    sub1_x = (WIDTH - sub1_width) // 2
    draw.text((sub1_x, title_y + 85), subtitle1, fill=COLOR_SUBTITLE_RED, font=font_subtitle)

    # "7-DAY ITINERARY"
    subtitle2 = "7-DAY ITINERARY"
    sub2_bbox = draw.textbbox((0, 0), subtitle2, font=font_title_med)
    sub2_width = sub2_bbox[2] - sub2_bbox[0]
    sub2_x = (WIDTH - sub2_width) // 2
    draw.text((sub2_x, title_y + 130), subtitle2, fill=COLOR_TITLE_WHITE, font=font_title_med)

    # Tarjetas de días (más altas para mejor espaciado)
    card_width = 230
    card_height = 310
    card_margin = 18
    cards_start_y = 230

    # Calcular espaciado
    total_cards_width = (card_width * 7) + (card_margin * 6)
    cards_start_x = (WIDTH - total_cards_width) // 2

    # Dibujar tarjetas
    for i, day_data in enumerate(DAYS):
        x = cards_start_x + (i * (card_width + card_margin))
        y = cards_start_y

        # Tarjeta con sombra
        shadow_offset = 6
        draw.rounded_rectangle(
            (x + shadow_offset, y + shadow_offset,
             x + card_width + shadow_offset, y + card_height + shadow_offset),
            radius=20,
            fill=(0, 0, 0, 60)
        )

        # Tarjeta blanca
        draw.rounded_rectangle(
            (x, y, x + card_width, y + card_height),
            radius=20,
            fill=COLOR_CARD
        )

        # "DAY X"
        day_text = f"DAY {day_data['day_num']}"
        day_bbox = draw.textbbox((0, 0), day_text, font=font_day_num)
        day_width = day_bbox[2] - day_bbox[0]
        day_x = x + (card_width - day_width) // 2
        draw.text((day_x, y + 20), day_text, fill=COLOR_TEXT_DARK, font=font_day_num)

        # Fecha
        date_text = f"({day_data['day_name']})"
        date_bbox = draw.textbbox((0, 0), date_text, font=font_day_name)
        date_width = date_bbox[2] - date_bbox[0]
        date_x = x + (card_width - date_width) // 2
        draw.text((date_x, y + 70), date_text, fill=COLOR_TEXT_MED, font=font_day_name)

        # Línea divisoria
        draw.line([(x + 20, y + 110), (x + card_width - 20, y + 110)],
                 fill=COLOR_BG_BOTTOM, width=2)

        # Actividades (más espaciadas)
        activity_y = y + 140
        for activity in day_data['activities']:
            act_bbox = draw.textbbox((0, 0), activity, font=font_activity)
            act_width = act_bbox[2] - act_bbox[0]
            act_x = x + (card_width - act_width) // 2

            draw.text((act_x, activity_y), activity,
                     fill=COLOR_TEXT_DARK, font=font_activity)
            activity_y += 45

    # Guardar
    img.save(OUTPUT_PATH, quality=95, optimize=True)
    file_size = OUTPUT_PATH.stat().st_size / 1024

    print(f"✅ Calendario creado: {OUTPUT_PATH}")
    print(f"📏 Tamaño: {file_size:.1f} KB")
    print(f"📐 Dimensiones: {WIDTH}x{HEIGHT}px")

if __name__ == "__main__":
    create_calendar()
