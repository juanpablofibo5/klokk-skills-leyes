---
name: registro-jornada
description: Audita si un sistema cumple el registro electrónico de jornada del Art. 132 Fr. XXXIV de la LFT (México) y genera un plan de compliance. Usar al revisar control de asistencia, registro de jornada, fichaje de empleados o cumplimiento laboral mexicano de tiempo de trabajo.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Art. 132 Fr. XXXIV; Art. 994 Fr. IV Bis"
  fuente: "DOF 2026-05-01"
---

# Skill: registro-jornada

**Qué hace:** audita si un sistema de software (Klokk, o el sistema de un
cliente) cumple la obligación de registro electrónico de jornada del
Art. 132 Fr. XXXIV de la LFT, y genera un plan de acción concreto para cerrar
las brechas encontradas.

**Por qué importa:** es la ley ancla de Klokk. El incumplimiento expone al
cliente a multas de hasta ~$587K MXN por trabajador y —según criterios de
tribunales— a perder cualquier juicio laboral sobre jornada u horas extra,
porque la carga de la prueba recae en el patrón.

**El principio que hace honesta a esta skill:** las disposiciones técnicas de
la STPS (el formato exacto, campos adicionales, excepciones) NO existen
todavía: entran en vigor el 1 de enero de 2027. La skill nunca inventa un
requisito técnico que la ley aún no publica. Audita contra dos cosas firmes:
(1) lo que el texto de la ley ya exige explícitamente, y (2) lo que los
criterios de tribunales ya establecen sobre valor probatorio. Todo lo demás se
marca como PENDIENTE de 2027.

## Archivos de referencia

Cargar según lo que pida la auditoría:

- [references/texto-legal.md](references/texto-legal.md) — texto oficial
  verificado: la obligación, la sanción y las fechas.
- [references/criterios-tribunales.md](references/criterios-tribunales.md) —
  carga de la prueba y qué hace confiable a un registro.
- [references/reglas.md](references/reglas.md) — las 10 reglas de auditoría
  (R1–R10) con su riesgo y su estado FIRME / PENDIENTE.
- [assets/plantilla-reporte.md](assets/plantilla-reporte.md) — plantilla del
  reporte de salida.

## Procedimiento de auditoría

1. **Identificar el alcance.** Determinar qué sistema se audita y si el
   cliente tiene teletrabajadores (activa R6).
2. **Auditar R1 — captura individual.** Buscar en el código/esquema cómo se
   guardan los eventos de entrada y salida. Falla si son agregados o no
   distinguen por trabajador.
3. **Auditar R2 y R8 — integridad y continuidad.** Revisar si los timestamps
   pueden editarse sin log, y si el sistema permite huecos selectivos. Falla
   si hay edición sin rastro.
4. **Auditar R3 y R5 — exportación e histórico.** Confirmar exportación por
   trabajador/periodo y retención mínima de 12 meses.
5. **Auditar R4 — evidencia de acuerdo.** Buscar dónde y cómo se registra el
   consentimiento del trabajador sobre el mecanismo.
6. **Auditar R7 y R9 — consistencia y correlación.** Verificar que los datos
   del trabajador crucen con nómina/contrato/CFDI y que las horas expliquen
   los pagos.
7. **Marcar R10 como pendiente.** Nunca inventar el formato técnico de 2027.
   Señalar explícitamente que está pendiente.
8. **Generar el plan.** Producir la salida con el formato de la sección
   siguiente.

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿La falla impide tener CUALQUIER registro válido? (R1, R3)
     SÍ  -> CRÍTICO  (expone a multa directa por trabajador)
     NO  -> siguiente pregunta

  ¿La falla DEBILITA el valor probatorio? (R2, R4, R7, R8, R9)
     SÍ  -> ALTO  (pierde defensa en juicio, aunque exista registro)
     NO  -> siguiente pregunta

  ¿Es buena práctica / cobertura parcial? (R5, R6)
     SÍ  -> MEDIO

  R10 y todo lo técnico de 2027 -> INFORMATIVO (pendiente STPS)
```

## Formato del plan de compliance (la salida)

La skill produce siempre la estructura de
[assets/plantilla-reporte.md](assets/plantilla-reporte.md): estado general,
incumplimientos detectados por severidad (con evidencia y acción por cada
uno), lo pendiente de disposiciones STPS 2027, y la nota de que no sustituye
asesoría legal profesional.

### Ejemplo de un hallazgo real (para calibrar el tono)

> **[ALTO] R2 — Registro alterable sin rastro.**
> **Evidencia:** el endpoint `PATCH /checkins/:id` permite modificar el
> timestamp de un fichaje sin escribir en la tabla de auditoría; no hay campo
> `modified_by` ni `modified_at`.
> **Acción:** hacer los timestamps de fichaje inmutables tras su creación; si
> se requiere corrección, implementarla como un registro nuevo que referencia
> al original, conservando ambos y anotando autor y motivo.
> **Riesgo si no se cierra:** en juicio, un registro editable sin rastro puede
> ser desestimado como prueba, y el tribunal presumiría ciertas las horas que
> alegue el trabajador.

## Límites de la skill

- **Solo audita y reporta.** No modifica código sin autorización explícita del
  usuario.
- **No es asesoría legal formal.** Identifica brechas contra el texto de la
  ley y criterios de tribunales; no sustituye a un abogado laboralista. Lo
  declara en cada salida.
- **No inventa requisitos técnicos.** Todo lo que dependa de las disposiciones
  STPS 2027 se marca PENDIENTE.
- **No confunde a Klokk con el patrón.** La obligación es del empleador; Klokk
  es la herramienta. La skill audita si la herramienta permite cumplir.
- **Se revisa con la ley.** `reviewed_at` en el frontmatter marca la última
  revisión. Cuando salgan las disposiciones de 2027, se actualiza la skill.

## Estado del contenido

Texto legal verificado palabra por palabra contra fuente oficial
(diputados.gob.mx, DOF 1-may-2026). Criterios jurisprudenciales tomados de
análisis de abogados laboralistas y de la carga de la prueba en la LFT. La
interpretación operativa y las reglas derivadas son un puente al desarrollo y
deben validarse con un abogado laboralista antes de dar la skill por
definitiva — especialmente las reglas FIRME* y todo lo PENDIENTE de 2027.
Cuando la STPS publique sus disposiciones, esta skill se revisa y sube su
`version` y `reviewed_at`.
