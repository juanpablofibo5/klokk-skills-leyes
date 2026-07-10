# BITÁCORA — registro por sesión

Orden: más reciente arriba. Cada entrada: qué se hizo, qué quedó pendiente.

## 2026-07-09 · S6 — R2+R3 ejecutados con loop de agentes (D-20)

- **Plan revisado antes de ejecutar:** review adversarial por instancia
  Fable independiente encontró 11 problemas (bloqueador de CI por la spec
  NOM en borrador, fuga de cláusulas v2 en la costura teletrabajo/NOM,
  renumeraciones con colisión semántica, secciones sin destino, dependencias
  de olas). Plan v2 los incorporó; D-20 registrado antes de desplegar.
- **Ola 1 (builders Sonnet, 5 paquetes):** el límite de uso del plan tumbó a
  4 de 5 builders y al reviewer de P4 a media respuesta — PERO los 31
  archivos quedaron completos en disco. Recuperación frugal: verificación
  MECÁNICA de fidelidad (script que diffea citas legales old↔new
  bidireccional, barre klokk y refs viejas) en vez de 5 reviewers LLM.
  Resultado inicial: 121 fallas → 1 defecto real (P3 fusionó el contenido
  NOM dentro del módulo LFT, duplicando a P5) + falsos positivos del
  verificador. Correcciones: módulo teletrabajo restaurado a LFT-puro con
  referencias calificadas; cláusulas v2 reubicadas al NOM como notas
  (contacto F-05-d, horario F-05-e) para no dejar citas huérfanas; claim
  falso de aprobación de la spec v2 corregido en la procedencia. Verificador
  final: **0 fallas**.
- **Ola 2 (orquestador, por límite de uso):** lft/SKILL.md (flujo F0–F5
  instanciado, regla global F2→severidad, índice real de los 9 módulos),
  plantillas/plantilla-reporte.md v2 (M-03), tools/validar.py v2 (estructura
  nueva, SPECS_EN_REVISION con D-20, cero-klokk como ERROR, citas huérfanas
  como AVISO) y README completo con "Cómo se usa".
- **Ensamblaje:** estructura vieja retirada (git rm de las 9 skills
  temáticas), registro-jornada normalizado (M-01: F-xx uniformes, páginas
  del decreto restauradas donde ya estaban verificadas), CLAUDE.md formato
  v3, validador **0 errores / 7 avisos** (huérfanas contextuales + páginas
  M-08 documentadas).
- **Review final holístico + SMOKE TEST (instancia Fable fresca):** el
  flujo F0–F3 de `lft/` corrió de punta a punta contra un checador sintético
  usando SOLO la documentación de la librería. Las 2 violaciones sembradas
  cayeron exactas (H-01 conservacion RD-02 CRÍTICO purga@90d; H-02
  horas-extra RD-04 CRÍTICO pago ×1.5) + 38 hallazgos legítimos más, N/A
  declarados con señales, CUMPLE probado (la tabla de vacaciones del fixture
  reproduce exactamente la del módulo). Veredicto de librería:
  REQUIERE-CAMBIOS con 7 problemas → TODOS corregidos: 5 refs CL-03→CL-05 y
  2 refs RD-05→RD-06 en el módulo NOM; RD-07 de registro-jornada alineado a
  la tabla (Crítico) por precedente D-05 → **D-21** (la inconsistencia venía
  del original aprobado); validador ahora RESUELVE referencias calificadas
  entre módulos/skills (y de paso destapó que la tabla 4-columnas legacy de
  registro-jornada no entraba al registro — corregido); secciones homónimas
  del flujo fusionadas; plantilla y README matizados. Fricciones del smoke
  incorporadas: nota APLICA-vs-N/A en lft/SKILL.md, ejemplo resuelto de
  atenuación de PARCIAL y regla de prohibición-sin-superficie
  (NO-VERIFICABLE) en el flujo.
- **Cierre: validador 0 errores / 7 avisos** (citas F de contexto huérfanas
  — informativas — y sin marcadores de página pendientes: los transitorios
  de registro-jornada recuperaron sus páginas verificadas D2 pp. 3–4).
  R2+R3 TERMINADOS. Gates abiertos: revisión en bloque de JP (D-20/D-21) y
  R4 (dogfooding en el repo real del producto).

## 2026-07-08 · S5 (cont.) — PIVOTE: librería agnóstica (D-18/D-19), R0+R1

- **Observaciones de JP y Luis:** el diseño asumía features de Klokk sin
  haber leído su código; lo que se quiere es una librería agnóstica — skills
  por LEY que, en una sesión de Claude Code con acceso al repo target,
  auditen el código REAL y produzcan plan de remediación no-destructivo,
  re-ejecutable. Registrado como D-18. El contenido legal verificado no
  cambia; cambia el empaque.
- **R0 cerrado:** repo renombrado a `skills-leyes-mx` (D-19, GitHub
  redirige; remote y carpeta local actualizados), visión reescrita en
  README y CLAUDE.md, kickoff pendiente de teletrabajo v2 actualizado.
  Menciones históricas del nombre viejo se conservan.
- **R1 cerrado:** publicado `plantillas/flujo-auditoria-codigo.md` — el
  flujo compartido F0–F5 (descubrimiento → aplicabilidad → mapeo
  regla→código con evidencia archivo:línea → reporte trazable → plan de
  remediación → implementación gated) + formato de reporte con delta entre
  corridas. **Gate abierto: revisión de JP/Luis del flujo antes de R2.**
- Nota operativa: dos cortes de internet interrumpieron turnos; en ambos se
  verificó el estado (git/validador/tareas) antes de continuar — sin
  pérdidas. La estructura del pivote (R0–R4) quedó en BACKLOG.

## 2026-07-08 · S5 (cont.) — Fase 1 NOM-037 cerrada: spec teletrabajo v2 en visto bueno

- **Loop NOM-037 (etapa 2 de la Ruta, cierra D-12) — fase 1 CERRADA.**
  Fuente oficial localizada y descargada de dof.gob.mx en la sesión:
  PDF de la edición vespertina del 08-06-2023 (D3, 61 pp.; la NOM en
  pp. 3–50) y texto íntegro HTML de la nota 5691672 (D4). Integridad:
  SHA-256 idéntico en doble descarga de cada archivo → filas D3/D4 nuevas
  en FUENTES.md. Verificación cruzada palabra por palabra HTML↔PDF en las
  pp. 5–26. Búsqueda web: sin modificaciones posteriores de la NOM en el
  DOF.
- Spec BORRADOR producida: `specs/teletrabajo-v2-nom037-spec.md` — F-08 a
  F-19 (numerales 1–2, 4.11, 4.20, 5.1, 5.2 d/e/h, 5.6, 5.10, 7.3 d/e,
  PEC 10.3 obs. del listado, 10.4, Transitorio PRIMERO; cita = numeral +
  página de D3), RD-07 redefinida (PENDIENTE → FIRME: NOM vigente desde
  05-12-2023) + RD-08 a RD-12 nuevas (listado NOM, desconexión de alcance
  completo, pausas/lactancia, cambio de modalidad documentado, conservación
  ≥1 año), CL-03 resuelta + CL-05/06/07 nuevos, árbol de severidad v2
  consistente con tabla y 7 casos de prueba (1 CUMPLE, 1 límite del 40.0 %).
  Alcance quirúrgico: solo numerales verificables con datos de asistencia;
  SST física/capacitación/exámenes → fuera de alcance declarado.
- Hallazgo de transcripción: la columna "Riesgo" de la tabla del PEC (10.3)
  viene VACÍA en la edición oficial (D3 pp. 14–25) — ninguna regla cita
  severidades del PEC. Y el Transitorio PRIMERO dice "entrará a los 180
  días" (sic, sin "en vigor").
- Checklist de fase 1 verificado (brief 9/9; calendarios graduales: no
  aplica — único transitorio = entrada en vigor). Validador en verde.
- **Gate ABIERTO: visto bueno de JP a la spec v2.** La skill NO se tocó
  (fase 2 solo tras el gate).

## 2026-07-08 · S5 (cont.) — Auditoría de citas cerrada (M-08)

- El agente en background de la auditoría se colgó (10 min sin progreso) →
  se reemplazó por auditoría directa en sesión: ~45 citas F-xx de las 9
  skills contra las páginas oficiales de D1/D2 (integridad SHA-256
  confirmada contra FUENTES.md): **0 discrepancias**. M-08 cerrado; la
  pasada 100 % independiente queda como escalón opcional pre-fase 3.
- Loop siguiente disparado en background: fase 1 de NOM-037-STPS →
  `teletrabajo` v2 (etapa 2 de la Ruta, cierra D-12).

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
- **Revisión integral por orden de JP** ("double check de todas las
  skills"): validador 9/9 en verde; matriz de secciones 9/9 salvo
  `registro-jornada` (formato pre-convención → M-01); disclaimer de
  no-asesoría 9/9. Hallazgos M-01 a M-08 marcados en BACKLOG. FUENTES.md
  creado con SHA-256 de los dos PDFs oficiales (M-02). Auditoría de
  transcripción independiente lanzada en background (M-08) — un agente
  fresco contrasta cada cita contra los PDFs re-leídos.

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
