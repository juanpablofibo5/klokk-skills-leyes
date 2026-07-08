# BITÁCORA — registro por sesión

Orden: más reciente arriba. Cada entrada: qué se hizo, qué quedó pendiente.

## 2026-07-08 · S5 — Aprobación del batch y Ruta a v1.0

- JP revisó y aprobó EN BLOQUE las 5 specs del modo batch (D-14): banners
  🟡 → ✅ en specs y SKILL.md; README, BACKLOG y STATUS actualizados.
- Corrección de conteo del cierre de anoche: eran 5 specs batch, no 6.
- Verificación de integridad tras errores de reporte de anoche: los 3
  archivos de `vacaciones` existen, están en git y el texto legal llega
  íntegro hasta el Art. 81 (6/6 fuentes) — los Writes aplicaron aunque el
  mensaje de resultado se perdió.
- Se agrega la **Ruta a v1.0** al BACKLOG: etapas de profesionalización
  hasta la fase 3 y el tag v1.0.0.
- Decisiones de JP del día: P3 entra completo (D-15, catálogo final = 11
  skills) y el mecanismo de consumo queda diferido con dueño — Luis (D-16).
- **Etapa 1 de la Ruta a v1.0 COMPLETADA** (aclaración previa de JP:
  "barato" = esfuerzo, no calidad — se construyó al estándar completo):
  - `tools/validar.py` + GitHub Action `validacion` en cada push (D-17).
    Primera corrida: 2 falsos positivos del propio validador (transitorios
    citados sin fila de tabla) → check calibrado → 9 skills en verde.
    Prueba negativa: estado `verificada` y link roto inyectados → detectados
    → restaurado. El validador truena cuando debe.
  - Plantilla v2: `plantillas/plantilla-skill-legal.md` reescrita al formato
    real (Agent Skills), con mapeo (a)–(e) → v2 y pipeline de origen.
    Cierra la deuda de S2.
  - CLAUDE.md: el protocolo de loop ahora incluye el paso VALIDAR; README
    con badge del CI.

## 2026-07-07 · S4 — Adopción del proceso + fase 1 de horas-extra

- Se adopta el sistema del agent-playbook: CLAUDE.md (kernel de reglas),
  STATUS.md, DECISIONES.md (D-01 a D-10 capturadas retroactivamente) y esta
  bitácora. Protocolo de loops por fase con checklist y gate (D-10).
- Loop fase 1 de `horas-extra` CERRADO: spec producida
  (`specs/horas-extra-spec.md`) con F-01–F-06 (Arts. 65–68 de D1 p. 22 +
  Transitorios Primero y Cuarto de D2 pp. 3–4), RD-01–RD-08, CL-01–CL-04
  (dos nuevos de dinero: base del tope +4h en transición, distribución
  4h×4 días vs topes graduales), 6 casos de prueba y checklist del brief
  verificado (9/9). Gate: visto bueno de JP → APROBADA.
- Loop fase 2 de `horas-extra` CERRADO: skill construida
  (`skills/horas-extra/`, estructura exacta de la sección 8), casos de
  prueba 6/6 ✓, checklist de fase 2 completo (estructura, solo-spec, casos
  reportados, índices README/BACKLOG/STATUS/BITACORA actualizados).
  3 skills construidas; siguiente: `dias-de-descanso`.
- Loop fase 1 de `dias-de-descanso` CERRADO: spec producida
  (`specs/dias-de-descanso-spec.md`) con F-01–F-05 (Arts. 69–73 de D1
  p. 23; Arts. 74–75 excluidos → van en `dias-festivos`), RD-01–RD-06,
  CL-01–CL-04 (dos que definen la lógica del checador: cómputo de rachas
  por ventana móvil vs semana calendario, y naturaleza del segundo día
  libre en semanas de 5 días por la transición a 40h), 6 casos de prueba
  y checklist del brief verificado (9/9 — el requisito de calendarios
  graduales no aplica: el capítulo no tiene transitorios propios).
  Gate: visto bueno de JP → APROBADA.
- Loop fase 2 de `dias-de-descanso` CERRADO: skill construida
  (`skills/dias-de-descanso/`, estructura exacta de la sección 8), casos de
  prueba 6/6 ✓, checklist de fase 2 completo. 4 skills construidas;
  siguiente: `dias-festivos` (Arts. 74–75, pp. 23–24 ya leídos).
- **MODO BATCH (D-11):** JP autorizó correr los loops de corrido para
  completar P1+P2 mientras se ausenta. Regla de marcado: specs batch = 🟡
  revisión de JP pendiente en bloque; nada se marca "aprobada" sin su gate.
  Alcance quirúrgico: `teletrabajo` v1 solo LFT (D-12); P3 (menores,
  lactancia) NO se construye — sigue siendo decisión abierta de JP.
- Loops de `dias-festivos` CERRADOS (batch): spec + skill construida, casos
  6/6 ✓. CL nuevos de dinero: concursos de pago doble festivo-domingo
  (CL-01) y festivo-descanso semanal (CL-02); fuentes externas para las
  fracc. VII y IX (CL-03/04). **P1 completo: 5/5.**
- Loops de `vacaciones` CERRADOS (batch): spec + skill construida, casos
  6/6 ✓. La tabla por antigüedad se marcó FIRME* — años 1–5 literales del
  Art. 76, bloques quinquenales como lectura estándar con CL-01 (cortes de
  bloque) para el abogado. CL-04: tensión potestad del trabajador (78) vs
  ventana de 6 meses (81).
- Fuentes localizadas para las 3 restantes (sondeos por página en D1):
  Art. 47 + aviso de rescisión (pp. 15–16), Arts. 134-V/135-II (p. 39),
  teletrabajo 330-A–330-K (pp. 95–97), Art. 784 (p. 335), Arts. 804–805
  (p. 340). Hallazgo: 784-VIII sigue diciendo "nueve horas semanales" —
  NO fue actualizado por el decreto 2026 → CL para el abogado.
- Loops de `teletrabajo` CERRADOS (batch, v1 solo LFT por D-12): spec +
  skill construida, casos 6/6 ✓. RD-07 = PENDIENTE (NOM-037); CL-01
  (ventana del 40 %), CL-02 (alcance de la desconexión).
- Loops de `conservacion-y-prueba` CERRADOS (batch): spec + skill, casos
  6/6 ✓. Dos hallazgos mayores: (1) el 804-III ancla estatutariamente la
  R5 de registro-jornada → precisión aplicada a sus reglas (D-13); (2) el
  784-VIII conserva "nueve horas semanales" sin armonizar con los topes
  2026 → CL-02, prioridad para el abogado.
- Loops de `asistencia-y-faltas` CERRADOS (batch): spec + skill, casos
  6/6 ✓. Regla fina: la causal 47-X se activa en la 4ª falta ("más de
  tres"), alerta en la 3ª; retardos NO se convierten en faltas sin regla
  pactada (CL-02).
- **CIERRE DEL MODO BATCH:** librería P1+P2 completa — 9/9 skills
  construidas, 54/54 casos de prueba ✓, todo pusheado. Incidente menor:
  un push se colgó por red y se recuperó verificando estado antes de
  reintentar (sin commits perdidos). Pendientes ordenados en STATUS.md:
  revisión en bloque de JP (6 specs 🟡), NOM-037 (D-12), decisión P3,
  fase 3 con abogado.

## 2026-07-07 · S3 — Sistema de producción + jornada-laboral completa

- BACKLOG.md (catálogo de 10 skills, 3 fases) y brief de investigación
  (plantilla de fase 1, con el checklist de consistencia aprendido de D-05).
- Fuentes oficiales descargadas de diputados.gob.mx: LFT consolidada
  ("Última Reforma DOF 14-05-2026", 457 pp.) y decreto DOF 1-may-2026.
- Cross-check de `registro-jornada` contra el decreto: coincide palabra por
  palabra. Corrección aplicada al calendario de horas extra (D-09).
- `jornada-laboral`: fase 1 (spec con F-01–F-11, RD-01–RD-09, CL-01–CL-04)
  → visto bueno de JP → fase 2 construida → 6/6 casos de prueba ✓.

## 2026-07-07 · S2 — Primera skill real: registro-jornada

- JP adjuntó la spec verificada (docx de deep research). Se construyó
  `skills/registro-jornada/` en formato Agent Skills (D-04); se eliminó la
  skill de ejemplo; README actualizado al formato v2.
- Corrida de casos de prueba destapó la inconsistencia de R5 → D-05 → 6/6 ✓.

## 2026-07-06 · S1 — Fundación del repo

- Estructura inicial: plantilla v1 con anatomía (a)–(e), skill de ejemplo con
  placeholders, README, .gitignore. Git inicializado y conectado a
  github.com/juanpablofibo5/klokk-skills-leyes (D-01, D-02, D-03).
