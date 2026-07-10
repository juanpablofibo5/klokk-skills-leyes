---
name: lft
description: Audita cualquier base de código contra la Ley Federal del Trabajo mexicana (módulos de tiempo de trabajo y su prueba; reforma de reducción de jornada DOF 2026-05-01 incluida). Corre dentro de una sesión con acceso al repo target; ejecuta el flujo F0–F5 (descubrimiento de arquitectura, aplicabilidad, mapeo regla→código con evidencia archivo:línea, reporte trazable, plan de remediación no destructivo). Usar para pre-auditorías de compliance laboral en software que registre asistencia, jornadas, ausencias, vacaciones, descansos, teletrabajo o retención de registros.
metadata:
  version: "2.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-08"
  ley: "LFT — módulos de tiempo de trabajo y su prueba (Arts. 46-47, 58-81, 132 fr. XXXIV, 134-135, 330-A a 330-K, 784, 804-805, 994 fr. IV Bis y transitorios del decreto DOF 2026-05-01)"
  fuente: "D1 y D2 de FUENTES.md (LFT consolidada, última reforma DOF 2026-05-14 + decreto DOF 2026-05-01), SHA-256 anclados"
---

# Skill: lft — auditoría de compliance laboral sobre código

**Qué hace:** audita el código real de un repositorio contra la Ley Federal
del Trabajo — la ley completa NO: sus **módulos de tiempo de trabajo y su
prueba** (los que un sistema que toque asistencia, jornadas o ausencias puede
violar). Produce un reporte trazable (fuente legal → regla → evidencia
`archivo:línea`) y un plan de remediación que respeta la arquitectura del
repo auditado.

**Cómo se usa:** en una sesión de Claude Code abierta EN el repo target, con
esta librería accesible. Se ejecuta el flujo
[flujo-auditoria-codigo.md](../../plantillas/flujo-auditoria-codigo.md)
(F0–F5) con los módulos de abajo. Re-ejecutable: cada corrida se fecha y se
compara con la anterior.

## Los 9 módulos

| Módulo | Pregunta que audita | Aplica típicamente cuando el código… |
|--------|--------------------|--------------------------------------|
| [registro-jornada](modulos/registro-jornada/) | ¿El registro electrónico de jornada cumple el Art. 132 fr. XXXIV (obligatorio desde 2026)? | registra entradas/salidas o jornadas de trabajadores |
| [jornada-laboral](modulos/jornada-laboral/) | ¿Tipos de turno y límites diarios/semanales correctos (calendario 48→40, 2026–2030)? | clasifica turnos o valida duraciones de jornada |
| [horas-extra](modulos/horas-extra/) | ¿El tiempo extraordinario se clasifica y paga por régimen (+100 %/+200 %/siniestro) con topes por año? | calcula, marca o exporta horas extra |
| [dias-de-descanso](modulos/dias-de-descanso/) | ¿Descanso semanal 6:1, prima dominical y pago doble del descanso trabajado? | maneja calendarios de descanso o rachas de días trabajados |
| [dias-festivos](modulos/dias-festivos/) | ¿Calendario de descansos obligatorios (lunes móviles incluidos) y doble pago del festivo laborado? | genera calendarios laborales o marca festivos |
| [vacaciones](modulos/vacaciones/) | ¿Tabla "vacaciones dignas", 12 días continuos, ventana de 6 meses, prima ≥25 %? | administra saldos o solicitudes de vacaciones |
| [teletrabajo](modulos/teletrabajo/) | ¿Umbral del 40 %, misma jornada para remotos, desconexión, supervisión proporcional? | distingue modalidad presencial/remota (si aplica → correr también la skill nom-037-stps) |
| [conservacion-y-prueba](modulos/conservacion-y-prueba/) | ¿Retención legal de registros, exhibición bajo demanda y cobertura de los hechos del Art. 784? | almacena o purga registros laborales |
| [asistencia-y-faltas](modulos/asistencia-y-faltas/) | ¿Clasificación de ausencias, contador de la causal 47-X (4ª falta en 30 días) y soporte del despido? | registra ausencias, permisos o faltas |

Cada módulo tiene tres archivos: `texto-legal.md` (citas oficiales verbatim
con documento y página), `reglas.md` (reglas RD-xx con riesgo y estado +
casos límite CL-xx + árbol de severidad) y `guia-auditoria.md` (aplicabilidad
F1, superficies F2, guía de auditoría y procedencia).

**Nota de aplicabilidad:** la columna "aplica típicamente cuando…" es
orientativa; deciden las señales F1 de cada guía. En particular, un sistema
que registre asistencia APLICA a `dias-de-descanso` y `asistencia-y-faltas`
aunque no tenga ninguna lógica de descansos o faltas — la ausencia de esa
lógica es justamente el hallazgo (reglas en estado AUSENTE), no un N/A.

## Ejecución del flujo para esta ley

1. **F0 — Descubrimiento:** mapear el repo target (stack, modelos de datos,
   endpoints, jobs, configs) SIN suposiciones. Dónde viven personas, tiempo,
   ausencias, pagos y retención.
2. **F1 — Aplicabilidad:** por cada módulo, decidir APLICA / N/A con la
   sección "Aplicabilidad (F1)" de su guía (señales positivas/negativas y
   greps). Un N/A se declara con razón; nunca se omite en silencio.
3. **F2 — Mapeo regla→código:** por cada RD-xx de los módulos aplicables,
   clasificar IMPLEMENTADA / PARCIAL / AUSENTE / VIOLADA / NO-VERIFICABLE
   con evidencia `archivo:línea`, usando "Superficies a revisar (F2)".
4. **F3 — Reporte:** con la
   [plantilla estándar](../../plantillas/plantilla-reporte.md) y las
   secciones fijas que cada módulo declare. La severidad la da el árbol del
   módulo bajo la **regla global** de abajo.
5. **F4 — Plan de remediación:** propuestas dentro de los patrones del propio
   repo, con impacto, orden incremental y prioridad = severidad × exposición
   (los módulos con multas UMA o pagos la explicitan).
6. **F5 — Implementación asistida:** SOLO con aprobación del dueño del repo,
   ítem por ítem, con tests; re-correr F2 sobre las reglas afectadas.

## Regla global F2 → severidad

- **VIOLADA** y **AUSENTE** disparan el árbol de severidad del módulo tal
  cual.
- **PARCIAL** dispara el árbol y puede atenuar UN nivel solo si la parte
  faltante no es el núcleo de la regla — y el reporte lo explica.
- **NO-VERIFICABLE** y los casos límite **CL-xx** van a INFORMATIVO: se
  reportan, no se califican.

## Límites de esta skill

- Cubre los módulos listados, no la LFT completa (contratos, sindicatos,
  PTU, salarios mínimos, etc. quedan fuera y el reporte lo declara).
- El contenido legal está `en-verificacion`: verificado contra fuentes
  oficiales (FUENTES.md, SHA-256) y con specs aprobadas por el dueño de la
  librería, PERO la validación de abogado laboralista (fase 3) sigue
  pendiente — ninguna regla es asesoría legal.
- Los casos límite (CL-xx) son preguntas abiertas para el abogado: el flujo
  los reporta como INFORMATIVO, jamás los resuelve.
- Si el target tiene teletrabajo, esta skill NO cubre la NOM-037-STPS-2023:
  correr también la skill `nom-037-stps`.

## Procedencia

Módulos construidos desde specs verificadas contra los documentos oficiales
D1/D2 de [FUENTES.md](../../FUENTES.md) (hashes SHA-256; auditoría de
transcripción M-08: 0 discrepancias). Specs aprobadas por JP (D-14); las
anotaciones v2 de teletrabajo provienen de la spec NOM (D-20, revisión en
bloque pendiente). Reestructura R2/R3 ejecutada con loop de agentes
(builders + reviewers) el 2026-07-08 bajo D-20.
