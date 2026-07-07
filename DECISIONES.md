# DECISIONES — log de decisiones del repo

Registro append-only. Cada decisión: qué se decidió, por qué, y quién la tomó.

| ID | Fecha | Decisión | Por qué / contexto |
|----|-------|----------|--------------------|
| D-01 | 2026-07-06 | Nombre oficial del producto: **Klokk** (una sola "c"); repo `klokk-skills-leyes`. | JP lo confirmó al detectarse la discrepancia con "Klockk"; coincide con logos y portafolio. |
| D-02 | 2026-07-06 | Una skill = un tema operativo, no una ley completa. | La LFT entera en un archivo sería inmantenible; la unidad de consumo es la regla operativa. |
| D-03 | 2026-07-06 | No se guardan PDFs del DOF en el repo; se enlaza a la fuente oficial y se cita documento + página. | Evitar peso y duplicación; el DOF es la fuente, git versiona nuestro texto. |
| D-04 | 2026-07-07 | Formato v2 — Agent Skills (carpeta + SKILL.md + references/ + assets/). La anatomía (a)–(e) sobrevive como checklist mapeado. | La spec de registro-jornada lo exigía; es el formato que el repo principal de Klokk consumirá. |
| D-05 | 2026-07-07 | R5 de `registro-jornada` (histórico) clasifica en la rama **ALTO** del árbol de severidad. | La spec traía inconsistencia interna (tabla: Alto; árbol: MEDIO; caso 4: ALTO). JP eligió alinear al riesgo Alto — Arts. 784/804 exigen conservar y exhibir. |
| D-06 | 2026-07-07 | Ninguna skill sube a `verificada` sin abogado; la fase 3 se hace UNA vez, sobre la librería completa. | Secuencia elegida por JP: primero construir todo, luego validación legal única. |
| D-07 | 2026-07-07 | Las specs de fase 1 las produce Claude contra fuente oficial descargada; **gate: visto bueno de JP** antes de construir. | Elegido por JP entre tres modelos de producción; equilibra velocidad y control humano. |
| D-08 | 2026-07-07 | Fuera de alcance del catálogo: aguinaldo, PTU y cálculo de nómina. | Klokk correlaciona horas con nómina (R9) pero no calcula pagos. Se reabre si el producto cambia. |
| D-09 | 2026-07-07 | Calendario de horas extra corregido: gradual 9/9/10/11/12 (2026–2030), NO salto a 12 en 2028. | Contraste con el Transitorio Cuarto del decreto oficial descargado; la síntesis previa era imprecisa. |
| D-10 | 2026-07-07 | Se adopta el sistema de proceso del agent-playbook: CLAUDE.md (kernel), STATUS, DECISIONES, BITACORA + protocolo de loops por fase con checklist y gate. | Pedido por JP: verificación del estado de cada fase y proceso completo versionado en GitHub. |
