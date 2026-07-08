# STATUS — estado vivo del repo

**Actualizado:** 2026-07-08

## Ahora mismo

- **Etapa 1 de la Ruta a v1.0 COMPLETADA (2026-07-08):** CI de validación
  activo en cada push (`tools/validar.py` + Action `validacion`, D-17) y
  plantilla v2 publicada. Las 9 skills pasan el validador en verde.
- **Sin loop abierto.** Siguiente al disparar: **Etapa 2** — loop NOM-037
  (→ teletrabajo v2, cierra D-12) y los dos loops P3 (`trabajo-de-menores`,
  `lactancia-y-descansos-especiales`, D-15).

## Estado por skill

| Skill | Fase | Gate pendiente |
|-------|------|----------------|
| `registro-jornada` | ✅ 2 completada | Fase 3 (abogado) |
| `jornada-laboral` | ✅ 2 completada | Fase 3 (abogado) |
| `horas-extra` | ✅ 2 completada | Fase 3 (abogado) |
| `dias-de-descanso` | ✅ 2 completada | Fase 3 (abogado) |
| `dias-festivos` | ✅ 2 completada | Fase 3 (abogado) |
| `vacaciones` | ✅ 2 completada | Fase 3 (abogado) |
| `teletrabajo` | ✅ 2 completada (v1 solo LFT) | NOM-037 → v2 (D-12) + fase 3 |
| `conservacion-y-prueba` | ✅ 2 completada | Fase 3 (abogado) |
| `asistencia-y-faltas` | ✅ 2 completada | Fase 3 (abogado) |

Todas las specs: aprobadas por JP (4 con gate individual, 5 en bloque el
2026-07-08, D-14).

## Decisiones recientes (2026-07-08)

- **P3 entra completo (D-15):** `trabajo-de-menores` y
  `lactancia-y-descansos-especiales` se construyen en la etapa 2 — el
  catálogo final pre-abogado es de **11 skills**.
- **Consumo (D-16):** decisión diferida con dueño — Luis la resuelve al
  integrar la librería en el repo principal.
- **Siguiente loop al disparar:** Etapa 1 de la Ruta a v1.0 (CI de
  validación + plantilla v2).

## Fuentes oficiales ya localizadas (descargadas 2026-07-07)

- LFT consolidada ("Última Reforma DOF 14-05-2026") —
  https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf
  · Rescisión/faltas: pp. 15–16 · Jornada: pp. 21–22 · Descansos: p. 23 ·
  Festivos: pp. 23–24 · Vacaciones: p. 24 · Obligaciones trabajadores:
  p. 39 · Teletrabajo: pp. 95–97 · Carga de la prueba: p. 335 ·
  Conservación: p. 340
- Decreto reducción de jornada, DOF 1-may-2026 vespertina —
  https://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_ref52_01may26.pdf
  · Transitorios: pp. 3–4
- NOM-037-STPS: **PENDIENTE de descarga y transcripción** (D-12, etapa 2 de
  la Ruta a v1.0).
