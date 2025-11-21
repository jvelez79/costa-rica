---
description: Genera archivo timeline-dia-X.md con tabla concisa del itinerario
---

# Generate Timeline Command

Genera un archivo `timeline-dia-X.md` para el día especificado por el usuario.

## Instrucciones:

1. **Input del usuario:** El usuario te dará un número de día (ej: "3", "4", "6", etc.)

2. **Leer archivo fuente:**
   - Lee el archivo `/home/juanca/Documents/viaje-costa-rica/docs/itinerario/dia-X.md` (donde X es el número proporcionado)
   - Extrae toda la información del timeline/horarios del día

3. **Crear/Sobrescribir archivo:**
   - Nombre: `/home/juanca/Documents/viaje-costa-rica/docs/itinerario/timeline-dia-X.md`
   - **Si el archivo ya existe:** SOBRESCRIBIRLO completamente (descartar contenido anterior)
   - **NO preguntar confirmación** - siempre reemplazar con contenido nuevo
   - Usar Write tool (sobrescribe automáticamente)
   - Formato: Exactamente como `timeline-dia-2.md` y `timeline-dia-5.md` (usa esos como referencia)

4. **Estructura del archivo timeline (SEGUIR EXACTAMENTE):**

```markdown
# Timeline Día X: [Día de la semana] [Fecha]

**[Descripción breve del día]**

[📋 Ver Itinerario Detallado Completo](dia-X.md)

---

## Timeline del Día

| Hora | Actividad | Ubicación |
|------|-----------|-----------|
| [hora] | [actividad] | [ubicación] |
| ... | ... | ... |

---

## Resumen del Día

- **Duración:** [info]
- **Manejo total:** [info]
- **Actividades principales:** [lista]
- **Comidas:** [info]

---

## Notas Importantes

- [Puntos críticos con emojis]
- [Costos]
- [Clima]
- [Alertas]

---

## ¿Hay espacio para más?

**[SÍ/NO - Análisis del espacio disponible]**

**[Opciones o recomendaciones]**

---

[📋 Ver Itinerario Detallado con Costos, Opciones y Consejos](dia-X.md)
```

5. **Características clave:**
   - Tabla MUY concisa: solo 3 columnas (Hora | Actividad | Ubicación)
   - Extraer TODOS los horarios del día desde inicio hasta fin
   - Incluir sección "¿Hay espacio para más?" que analice si hay tiempo libre
   - Mantener formato limpio y fácil de escanear
   - Links al itinerario detallado (dia-X.md)

6. **NO hacer:**
   - ❌ NO agregar el archivo a `mkdocs.yml` nav
   - ❌ NO hacer commits automáticos
   - ❌ NO modificar otros archivos

7. **Output al usuario:**
   - Confirmar qué archivo se creó
   - Mostrar path completo
   - Resumir cuántas filas tiene la tabla
   - Indicar si hay espacio libre en ese día

---

## Ejemplos de uso:

Usuario: `/timeline 3`
→ Genera `/docs/itinerario/timeline-dia-3.md`

Usuario: `/timeline 6`
→ Genera `/docs/itinerario/timeline-dia-6.md`

---

## Referencias:

Ver archivos existentes como ejemplos:
- `/docs/itinerario/timeline-dia-2.md`
- `/docs/itinerario/timeline-dia-5.md`

Estos muestran el formato exacto a seguir.
