# STATUS — estado vivo del repo

**Actualizado:** 2026-07-09

## Ahora mismo

- **R2+R3 EJECUTADOS (D-20):** la librería ya es skill-por-ley y agnóstica.
  `skills/lft/` (9 módulos) + `skills/nom-037-stps/` (1 módulo), flujo
  F0–F5, plantilla de reporte v2, validador v2 y README nuevos. Fidelidad
  legal verificada mecánicamente (0 fallas); validador 0 errores.
- **Review final + smoke test: PASADOS (2026-07-09).** Una instancia
  independiente ejecutó F0–F3 de `lft/` sobre un fixture sintético usando
  solo la documentación: las 2 violaciones sembradas detectadas con módulo,
  regla, severidad y archivo:línea correctos (+38 hallazgos legítimos). Sus
  7 problemas de librería quedaron corregidos (refs calificadas del NOM,
  RD-07 por precedente D-05 → D-21, resolver de referencias cruzadas en el
  validador, doc del flujo).
- **Gates abiertos de JP:** (1) revisión en bloque del batch R2/R3 + spec
  NOM (D-20) + D-21; (2) R4 — dogfooding: correr `lft/` en una sesión dentro
  del repo real del producto.

## Estado por ley

| Skill-ley | Módulos | Estado |
|-----------|---------|--------|
| `lft` | registro-jornada · jornada-laboral · horas-extra · dias-de-descanso · dias-festivos · vacaciones · teletrabajo · conservacion-y-prueba · asistencia-y-faltas | en-verificacion — specs aprobadas (D-14 y gates individuales); anotaciones v2 de teletrabajo bajo D-20 |
| `nom-037-stps` | teletrabajo-sst | en-verificacion — spec v2 PENDIENTE de revisión en bloque de JP (D-20) |

## Pendientes ordenados

1. **Revisión en bloque de JP (D-20):** spec NOM
   (`specs/teletrabajo-v2-nom037-spec.md`) + la reestructura R2/R3.
2. **R4 dogfooding** en el repo real del producto (primera corrida del flujo
   F0–F5 de verdad).
3. **Módulos P3 de la LFT** (D-15): trabajo-de-menores y
   lactancia-y-descansos-especiales — pipeline normal.
4. **Blindaje pre-abogado:** pasada independiente de transcripción (M-08,
   incluye las páginas pendientes de los transitorios), matriz de
   consistencia cruzada, paquete del abogado (CL-xx priorizados por dinero).
5. **Fase 3 (abogado laboralista)** → estados a `verificada` → tag v1.0.0.
6. Siguiente ley del catálogo: LFPDPPP (protección de datos).

## Fuentes oficiales (FUENTES.md, SHA-256)

- D1 — LFT consolidada ("Última Reforma DOF 14-05-2026"): jornada pp. 21–22 ·
  descansos p. 23 · festivos pp. 23–24 · vacaciones p. 24 · rescisión/faltas
  pp. 15–16 · obligaciones p. 39 · teletrabajo pp. 95–97 · prueba p. 335 ·
  conservación p. 340
- D2 — Decreto reducción de jornada (DOF 01-05-2026 vespertina): reformas y
  transitorios pp. 3–4
- D3/D4 — NOM-037-STPS-2023 (DOF 08-06-2023): numerales citados con página
  en el módulo teletrabajo-sst
