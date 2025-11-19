#!/usr/bin/env python3
"""
Crea imagen de calendario visual para el viaje a Costa Rica
usando Pillow con texto perfectamente controlado
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

# Colores (esquema tropical Costa Rica)
COLOR_BG_TOP = (41, 128, 185)      # Azul oceano
COLOR_BG_BOTTOM = (39, 174, 96)    # Verde tropical
COLOR_CARD = (255, 255, 255)       # Blanco
COLOR_TEXT_DARK = (44, 62, 80)     # Gris oscuro
COLOR_TEXT_LIGHT = (127, 140, 141) # Gris claro
COLOR_ACCENT = (231, 76, 60)       # Rojo acento

# Datos del itinerario
DAYS = [
    {
        "day": "DÍA 1",
        "date": "Dom 23 Nov",
        "activities": [
            "✈️ Llegada SJO",
            "🚗 Pickup vehículos",
            "🏨 Hotel Aloft"
        ]
    },
    {
        "day": "DÍA 2",
        "date": "Lun 24 Nov",
        "activities": [
            "🚗 → La Fortuna",
            "🌋 Volcán Arenal",
            "♨️ Aguas Termales"
        ]
    },
    {
        "day": "DÍA 3",
        "date": "Mar 25 Nov",
        "activities": [
            "🏍️ ATV Tour",
            "🌊 Rafting Rápidos",
            "💦 Cascada 70m"
        ]
    },
    {
        "day": "DÍA 4",
        "date": "Mié 26 Nov",
        "activities": [
            "🚗 → San José",
            "🏛️ City Tour",
            "🎨 Mercado Arte"
        ]
    },
    {
        "day": "DÍA 5",
        "date": "Jue 27 Nov",
        "activities": [
            "🏛️ Cartago",
            "⛪ La Negrita",
            "🌋 Volcán Irazú"
        ]
    },
    {
        "day": "DÍA 6",
        "date": "Vie 28 Nov",
        "activities": [
            "🛍️ Compras",
            "☕ Explorar SJ",
            "🧳 Preparar viaje"
        ]
    },
    {
        "day": "DÍA 7",
        "date": "Sáb 29 Nov",
        "activities": [
            "⏰ Salida 6:00 AM",
            "🚗 Devolver autos",
            "✈️ Vuelo regreso"
        ]
    }
]

def create_gradient_background(width, height, color_top, color_bottom):
    """Crea un fondo con degradado vertical"""
    base = Image.new('RGB', (width, height), color_top)
    draw = ImageDraw.Draw(base)

    for y in range(height):
        # Interpolación lineal entre colores
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return base

def draw_rounded_rectangle(draw, xy, radius, fill):
    """Dibuja un rectángulo con esquinas redondeadas"""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

def create_calendar():
    """Genera la imagen del calendario"""
    print("🎨 Creando calendario visual...")

    # Intentar cargar imagen IA como fondo (si existe)
    ai_bg_path = OUTPUT_DIR / "tropical-bg.jpg"

    if ai_bg_path.exists():
        print("🌴 Usando fondo tropical generado por IA...")
        img = Image.open(ai_bg_path)

        # Redimensionar a las dimensiones deseadas si es necesario
        if img.size != (WIDTH, HEIGHT):
            img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

        # Convertir a RGB si es necesario
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Añadir overlay semi-transparente SUTIL para mejor legibilidad
        # (menos opaco que antes para preservar la belleza del fondo)
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 40))
        img_rgba = img.convert('RGBA')
        img = Image.alpha_composite(img_rgba, overlay).convert('RGB')
    else:
        print("📐 Usando degradado programático...")
        # Crear imagen base con degradado (fallback)
        img = create_gradient_background(WIDTH, HEIGHT, COLOR_BG_TOP, COLOR_BG_BOTTOM)

    draw = ImageDraw.Draw(img)

    # Intentar cargar fuentes del sistema (fallback a default si no existen)
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        font_day = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_date = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_activity = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except:
        print("⚠️  Usando fuente por defecto (instala DejaVu fonts para mejor resultado)")
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_day = ImageFont.load_default()
        font_date = ImageFont.load_default()
        font_activity = ImageFont.load_default()

    # Título principal
    title = "COSTA RICA ADVENTURE"
    subtitle = "Noviembre 23-29, 2025 • 7 Días"

    # Centrar título
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2

    draw.text((title_x, 40), title, fill=(255, 255, 255), font=font_title)

    # Centrar subtítulo
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2

    draw.text((subtitle_x, 110), subtitle, fill=(255, 255, 255), font=font_subtitle)

    # Configuración de las tarjetas
    card_width = 240
    card_height = 260
    card_margin = 20
    cards_start_y = 180

    # Calcular espaciado para centrar las 7 tarjetas
    total_cards_width = (card_width * 7) + (card_margin * 6)
    cards_start_x = (WIDTH - total_cards_width) // 2

    # Dibujar tarjetas de cada día
    for i, day_data in enumerate(DAYS):
        # Posición de la tarjeta
        x = cards_start_x + (i * (card_width + card_margin))
        y = cards_start_y

        # Dibujar tarjeta con sombra
        shadow_offset = 4
        draw_rounded_rectangle(
            draw,
            (x + shadow_offset, y + shadow_offset,
             x + card_width + shadow_offset, y + card_height + shadow_offset),
            radius=15,
            fill=(0, 0, 0, 50)  # Sombra semi-transparente
        )

        # Dibujar tarjeta principal
        draw_rounded_rectangle(
            draw,
            (x, y, x + card_width, y + card_height),
            radius=15,
            fill=COLOR_CARD
        )

        # Header de la tarjeta con color acento
        draw_rounded_rectangle(
            draw,
            (x, y, x + card_width, y + 60),
            radius=15,
            fill=COLOR_ACCENT
        )
        draw.rectangle((x, y + 45, x + card_width, y + 60), fill=COLOR_ACCENT)

        # Día número
        day_text = day_data["day"]
        day_bbox = draw.textbbox((0, 0), day_text, font=font_day)
        day_width = day_bbox[2] - day_bbox[0]
        day_x = x + (card_width - day_width) // 2
        draw.text((day_x, y + 12), day_text, fill=(255, 255, 255), font=font_day)

        # Fecha
        date_text = day_data["date"]
        date_bbox = draw.textbbox((0, 0), date_text, font=font_date)
        date_width = date_bbox[2] - date_bbox[0]
        date_x = x + (card_width - date_width) // 2
        draw.text((date_x, y + 75), date_text, fill=COLOR_TEXT_DARK, font=font_date)

        # Actividades
        activity_y = y + 115
        for activity in day_data["activities"]:
            # Centrar actividad
            act_bbox = draw.textbbox((0, 0), activity, font=font_activity)
            act_width = act_bbox[2] - act_bbox[0]
            act_x = x + (card_width - act_width) // 2

            draw.text((act_x, activity_y), activity,
                     fill=COLOR_TEXT_DARK, font=font_activity)
            activity_y += 35

    # Footer
    footer_text = "10 Adultos • 2 Vehículos • Naturaleza + Aventura + Cultura"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=font_subtitle)
    footer_width = footer_bbox[2] - footer_bbox[0]
    footer_x = (WIDTH - footer_width) // 2
    draw.text((footer_x, HEIGHT - 80), footer_text,
             fill=(255, 255, 255), font=font_subtitle)

    # Guardar imagen
    img.save(OUTPUT_PATH, quality=95, optimize=True)
    file_size = OUTPUT_PATH.stat().st_size / 1024

    print(f"✅ Calendario creado: {OUTPUT_PATH}")
    print(f"📏 Tamaño: {file_size:.1f} KB")
    print(f"📐 Dimensiones: {WIDTH}x{HEIGHT}px")

    return OUTPUT_PATH

if __name__ == "__main__":
    create_calendar()
