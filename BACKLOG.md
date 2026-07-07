# BACKLOG — Catálogo de skills legales

El tablero de producción de la librería. El índice del README lista lo ya
construido; aquí vive lo que falta y en qué fase va cada skill.

**Meta:** todas las skills del catálogo construidas y consistentes
(`en-verificacion`), para pasarlas JUNTAS con un abogado laboralista y
subirlas a `verificada`.

## Pipeline de producción (por skill)

| Fase | Qué pasa | Gate para avanzar |
|------|----------|-------------------|
| 1. Investigación verificada | Se produce la spec con el texto legal contrastado contra fuente oficial (DOF / diputados.gob.mx), cumpliendo `plantillas/brief-investigacion-skill.md` | La spec cumple el brief y JP la aprueba |
| 2. Construcción | Claude Code transcribe la spec al formato Agent Skills y corre sus casos de prueba | Todos los casos pasan; árbol, tabla de riesgos y casos consistentes |
| 3. Validación legal | Un abogado laboralista revisa la librería completa | El estado sube a `verificada` |

**Definición de "lista" (antes del abogado):** construida + citas textuales
tomadas de documento oficial (con fecha y link) + reglas FIRME/PENDIENTE
consistentes + casos de prueba pasando + estado `en-verificacion`. Ninguna
skill se declara "perfecta" antes de la fase 3 — ese candado protege al
negocio.

## P1 — Núcleo: tiempo de trabajo (la propuesta de valor del Art. 132)

| Skill | Pregunta operativa | Fuentes a investigar* | Fase |
|-------|--------------------|-----------------------|------|
| `registro-jornada` | ¿El sistema cumple el registro electrónico del Art. 132 Fr. XXXIV? | Decreto DOF 2026-05-01 (ya citado en el repo) | ✅ 2 completada — espera fase 3 |
| `jornada-laboral` | ¿Cuánto puede durar la jornada por tipo de turno y por año (calendario 48→40, 2026–2030)? | LFT consolidada pp. 21–22 (Arts. 58–68) + decreto DOF 2026-05-01 | 🔍 1 — spec en visto bueno (`specs/jornada-laboral-spec.md`) |
| `horas-extra` | ¿Cuándo una hora es extra, cuántas caben por semana (9/9/10/11/12 en 2026–2030) y cómo se pagan? | LFT consolidada p. 22 (Arts. 65–68) + Transitorio Cuarto del decreto 2026 | pendiente |
| `dias-de-descanso` | ¿Qué descanso semanal corresponde, qué prima aplica y qué pasa si se trabaja? | LFT consolidada p. 23 (Arts. 69–73, localizados 2026-07-07) | pendiente |
| `dias-festivos` | ¿Qué días son descanso obligatorio y cómo se paga trabajarlos? | LFT consolidada pp. 23–24 (Arts. 74–75, localizados 2026-07-07) | pendiente |

## P2 — Lo que el registro debe poder probar o cubrir

| Skill | Pregunta operativa | Fuentes a investigar* | Fase |
|-------|--------------------|-----------------------|------|
| `vacaciones` | ¿Cuántos días tocan por antigüedad y cómo se registran como ausencia justificada? | LFT consolidada p. 24 (Arts. 76–81, localizados 2026-07-07; reforma "vacaciones dignas" DOF 27-12-2022) | pendiente |
| `teletrabajo` | ¿Qué obliga el teletrabajo en registro de jornada y desconexión? | LFT, capítulo de teletrabajo + NOM-037-STPS | pendiente |
| `conservacion-y-prueba` | ¿Qué documentos conservar, cuánto tiempo, y qué pasa en juicio si faltan? | LFT Arts. 784 y 804 (ya citados en el repo) + plazos de conservación | pendiente |
| `asistencia-y-faltas` | ¿Qué efectos legales tienen faltas y retardos, y qué debe quedar registrado? | LFT, causales y obligaciones relacionadas con asistencia | pendiente |

## P3 — Perímetro (decidir si entran)

- `trabajo-de-menores` — jornadas reducidas y prohibiciones (PyMEs con
  trabajadores de 15–17 años).
- `lactancia-y-descansos-especiales` — pausas que el checador debería
  reconocer.

## Fuera de alcance (decidido 2026-07-07)

Aguinaldo, PTU y cálculo de nómina: Klokk correlaciona horas con nómina
(regla R9 de registro-jornada) pero no calcula pagos. Si el producto cambia,
se reabre.

---

\* Las referencias de este backlog son **objetivos de investigación, no
contenido verificado**. El artículo exacto, su texto vigente y su fecha de
reforma se confirman en la fase 1 — nunca se citan de memoria.
