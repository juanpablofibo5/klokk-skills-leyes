# Guía de auditoría — módulo registro-jornada (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Art. 132 Fr. XXXIV; Art. 994 Fr. IV Bis |
| fuente | DOF 2026-05-01 |

---

## Qué hace este módulo

Audita si el software bajo revisión cumple la obligación de registro
electrónico de jornada del Art. 132 Fr. XXXIV de la LFT, y permite generar
un plan de acción concreto para cerrar las brechas encontradas.

## Por qué importa

Es la obligación laboral de tiempo de trabajo con mayor exposición directa a
multa por trabajador. El incumplimiento expone al empleador a multas de hasta
~$587K MXN por trabajador afectado y —según criterios de tribunales— a perder
cualquier juicio laboral sobre jornada u horas extra, porque la carga de la
prueba recae en el patrón.

**El principio que hace honesta a esta skill:** las disposiciones técnicas de
la STPS (el formato exacto, campos adicionales, excepciones) NO existen
todavía: entran en vigor el 1 de enero de 2027. El módulo nunca inventa un
requisito técnico que la ley aún no publica. Audita contra dos cosas firmes:
(1) lo que el texto de la ley ya exige explícitamente (F-01 a F-06), y (2) lo
que los criterios de tribunales ya establecen sobre valor probatorio. Todo lo
demás se marca como PENDIENTE de 2027.

## Cuándo se activa

Cargar este módulo cuando el software auditado:

- gestiona control de asistencia, fichaje, o registro de entrada/salida;
- lleva tiempos de empleados subordinados (no solo freelancers);
- genera reportes de jornada hacia el patrón, IMSS, o autoridad laboral;
- o cuando el scope de la auditoría incluye tiempo de trabajo o jornada laboral.

## Frontera del módulo

- **Contenido de este módulo:** registro electrónico de jornada (Art. 132
  Fr. XXXIV), sanción (Art. 994 Fr. IV Bis), y calendario de exigibilidad.
- **No cubre:** formato técnico exacto de 2027 (→ RD-10, PENDIENTE STPS);
  cómputo de horas extra (→ módulo horas-extra, lft); teletrabajo SST
  (→ skill nom-037-stps); conservación formal de documentos laborales
  (→ módulo conservacion-y-prueba, lft).
- Registrar jornada de teletrabajadores aplica este módulo con los mismos
  estándares (RD-06); los requisitos SST de teletrabajo son de nom-037-stps.

---

## Aplicabilidad (F1)

### Señales POSITIVAS — el módulo aplica si se encuentra cualquiera de estas

**En el esquema / modelos de datos:**
- Tabla o modelo con nombre del tipo `attendance`, `checkin`, `checkout`,
  `clock_in`, `clock_out`, `registro_jornada`, `asistencia`, `fichaje`,
  `work_log`, `time_entry`, `shift`.
- Campos del tipo `start_time`/`end_time`, `entry`/`exit`, `in_time`/`out_time`
  junto a un identificador de empleado (`employee_id`, `worker_id`, `user_id`).
- Columnas de auditoría en esa tabla: `created_at`, `updated_at`,
  `modified_by`, `deleted_at`.

**En endpoints / rutas:**
- Rutas que incluyan `/checkin`, `/checkout`, `/clock`, `/attendance`,
  `/jornada`, `/registro`, `/time-entry`, `/time-log`.
- Endpoints de exportación o reporte: `/report`, `/export`, `/download` que
  devuelvan datos de asistencia por trabajador.

**En jobs / schedulers:**
- Jobs que calculen horas trabajadas, horas extra, o cierren periodos de
  jornada.
- Schedulers de purga o retención de registros de tiempo.

**En configuración:**
- Variables de entorno o config que mencionen retención de registros
  (`RETENTION_DAYS`, `RECORD_RETENTION`, `HISTORY_MONTHS`).

**Greps sugeridos (correr en el repo target):**
```bash
grep -ri "checkin\|checkout\|clock_in\|clock_out\|registro.*jornada\|time_entry\|attendance" --include="*.py" --include="*.ts" --include="*.js" --include="*.rb" --include="*.go" -l
grep -ri "employee_id\|worker_id" --include="*.sql" --include="*.migration*" -l
grep -ri "/checkin\|/checkout\|/attendance\|/time-entry" --include="*.py" --include="*.ts" --include="*.js" -l
```

### Señales NEGATIVAS — módulo N/A si se cumplen TODAS

- El software no gestiona personas empleadas (clientes, sesiones de usuario,
  inventario, etc.) — no hay ninguna superficie de jornada laboral.
- No hay modelos de datos ni endpoints relacionados con tiempo de trabajo.
- El README o scope del proyecto excluye explícitamente la gestión de
  empleados.

---

## Superficies a revisar (F2 — dónde buscar cada RD)

| RD | Dónde buscar en el repo |
|----|------------------------|
| RD-01 | Modelo de datos: ¿hay campo de inicio Y fin por registro de empleado individual? Migrations, schema, ORM models. |
| RD-02 | ¿Los timestamps son inmutables tras creación? Buscar endpoints `PATCH`/`PUT` sobre registros de jornada; tablas de auditoría (`audit_log`, `history`). |
| RD-03 | Endpoints o funciones de exportación/reporte por trabajador y periodo. Formatos de salida (CSV, PDF, JSON). |
| RD-04 | ¿Hay flujo de consentimiento del trabajador sobre el mecanismo? Tablas de aceptación, campos `agreed_at`, `consent`, contratos digitales. |
| RD-05 | Jobs de purga o retención: ¿borran registros antes de 12 meses? Config de `RETENTION_DAYS`. Migrations con `DELETE` o `TRUNCATE` sobre asistencia. |
| RD-06 | ¿El sistema diferencia teletrabajadores? ¿Aplica los mismos campos y flujo de registro para ellos? |
| RD-07 | Cruce de identidad: ¿los registros de jornada referencian el mismo empleado que nómina/contrato/IMSS? Integridad referencial. |
| RD-08 | ¿El sistema permite registrar solo algunos días y omitir otros? ¿Hay validación de continuidad o detección de huecos? |
| RD-09 | ¿Las horas registradas alimentan el cálculo de nómina? ¿Hay correlación entre horas extras en jornada y pagos adicionales? |
| RD-10 | PENDIENTE STPS 2027 — marcar INFORMATIVO; no buscar aún formato técnico específico. |

---

## Capa interpretativa

La carga de la prueba recae en el patrón (Arts. 784 y 804 LFT). El argumento
"la STPS no ha publicado" no protege: el principio de primacía de la realidad
obliga a tener un mecanismo de registro desde ahora. Ver sección "Criterios
de tribunales" abajo.

El auditor debe evaluar el **valor probatorio real** del registro que
implementa el software, no solo la existencia de campos. Un registro editable
sin rastro, o con huecos selectivos, o sin correlación con nómina, no es
prueba defendible en juicio.

---

## Guía de auditoría del módulo

Seguir el flujo F0–F5 de lft/SKILL.md. Las fases específicas de este módulo:

**F1 — Aplicabilidad:** usar las señales POSITIVAS y NEGATIVAS de arriba.
Si el software no tiene ninguna superficie de jornada laboral, declarar N/A
con razón explícita. El módulo N/A es un resultado válido.

**F2 — Mapeo RD→código:** por cada RD-01 a RD-10, buscar en las superficies
indicadas arriba. Clasificar: IMPLEMENTADA / PARCIAL / AUSENTE / VIOLADA /
NO-VERIFICABLE. Anclar cada clasificación a `archivo:línea` o a la ausencia
verificada de superficie.

**Pasos concretos:**

1. **RD-01 — captura individual.** Buscar en el esquema/modelos cómo se
   almacenan los eventos de entrada y salida. Falla si son agregados o no
   distinguen por trabajador.
2. **RD-02 y RD-08 — integridad y continuidad.** Revisar si los timestamps
   pueden editarse sin log, y si el sistema permite huecos selectivos. Falla
   si hay edición sin rastro.
3. **RD-03 y RD-05 — exportación e histórico.** Confirmar exportación por
   trabajador/periodo y retención mínima de 12 meses.
4. **RD-04 — evidencia de acuerdo.** Buscar dónde y cómo se registra el
   consentimiento del trabajador sobre el mecanismo.
5. **RD-07 y RD-09 — consistencia y correlación.** Verificar que los datos
   del trabajador crucen con nómina/contrato/CFDI y que las horas expliquen
   los pagos.
6. **RD-10 — marcar INFORMATIVO.** Nunca inventar el formato técnico de 2027.
   Señalar explícitamente que está pendiente de disposiciones STPS.

**F3 — Reporte:** usar formato de ../../../../plantillas/plantilla-reporte.md.
La severidad de cada hallazgo la determina el árbol de decisión en reglas.md.

---

## Secciones fijas del reporte de este módulo

El reporte de este módulo incluye siempre estas secciones adicionales:

**LÍMITES APLICADOS ESTE AÑO:**
Indicar el año auditado y los límites vigentes según F-05 (jornada máxima) y
F-06 (horas extra). Ejemplo: "Año 2026: jornada máxima 48 h/sem (Transitorio
Segundo); horas extra legales 9 h/sem (Transitorio Cuarto)."

**CLASIFICACIÓN APLICADA:**
Tabla con los 10 RD y su estado (IMPLEMENTADA / PARCIAL / AUSENTE / VIOLADA /
NO-VERIFICABLE / INFORMATIVO) con evidencia de archivo:línea.

**VENTANA DE CÓMPUTO:**
Periodo auditado (fechas de inicio y fin de los registros analizados).

---

## Ejemplo calibrador

> **[ALTO] RD-02 — Registro alterable sin rastro.**
> **Evidencia:** el endpoint `PATCH /checkins/:id` permite modificar el
> timestamp de un registro sin escribir en la tabla de auditoría; no hay campo
> `modified_by` ni `modified_at`.
> **Acción:** hacer los timestamps de registro de jornada inmutables tras su
> creación; si se requiere corrección, implementarla como un registro nuevo
> que referencia al original, conservando ambos y anotando autor y motivo.
> **Riesgo si no se cierra:** en juicio, un registro editable sin rastro puede
> ser desestimado como prueba, y el tribunal presumiría ciertas las horas que
> alegue el trabajador.

---

## Criterios de tribunales

> **BANNER:** origen: deep research verificado de JP; números de tesis/registro
> digital pendientes del abogado (M-01)

### La carga de la prueba recae en el patrón

Los Arts. 784 y 804 de la LFT obligan al patrón a conservar y exhibir los
registros de asistencia. En juicio, si el patrón no puede probar la jornada,
el tribunal presume ciertos los hechos que alega el trabajador (hasta 9 horas
extra semanales; criterio de la Segunda Sala de la SCJN). Sin registro
confiable, el patrón pierde la defensa.

### El argumento "la STPS no ha publicado" no protege

**Hallazgo jurídico clave para el diseño del módulo:** análisis de abogados
laboralistas (Foro Jurídico) sostiene que, por el principio de primacía de la
realidad, el patrón NO podrá defenderse en juicio diciendo "no tengo registro
porque la STPS aún no define las disposiciones". La obligación de contar con
un mecanismo de registro existe desde la ley; la falta de reglamento técnico
no la suspende.

**Conclusión para la auditoría:** debe evaluarse el valor probatorio del
registro con seriedad AHORA, sin tratar 2027 como excusa para no cumplir hoy.

### Qué hace "confiable" a un registro (criterio de tribunales)

Los jueces no evalúan tecnología, evalúan credibilidad. Un registro es
defendible si tiene:

- **Trazabilidad:** origen, continuidad e integridad de cada registro.
- **Continuidad:** registro continuo y no selectivo — no solo los días que
  convienen.
- **Correlación con nómina:** las horas registradas explican los pagos hechos.
- **Reconstrucción completa:** poder reconstruir semanas enteras con
  ordinarias, extras y descansos.
- **Sin ajustes sin rastro:** un Excel editable o un sistema que sobrescribe
  datos NO es prueba defendible.

---

## Límites del módulo

- **Solo audita y reporta.** No modifica código sin autorización explícita del
  dueño del repo.
- **No es asesoría legal formal.** Identifica brechas contra el texto de la
  ley y criterios de tribunales; no sustituye a un abogado laboralista. Lo
  declara en cada salida.
- **No inventa requisitos técnicos.** Todo lo que dependa de las disposiciones
  STPS 2027 se marca PENDIENTE (RD-10).
- **No confunde al software auditado con el patrón.** La obligación es del
  empleador; el software es la herramienta. El módulo audita si el software
  permite cumplir.
- **Se revisa con la ley.** `reviewed_at` en los metadatos marca la última
  revisión. Cuando salgan las disposiciones de 2027, se actualiza el módulo.

---

## Procedencia y estado

Texto legal verificado palabra por palabra contra fuente oficial
(diputados.gob.mx, DOF 1-may-2026). Criterios jurisprudenciales tomados de
análisis de abogados laboralistas y de la carga de la prueba en la LFT. La
interpretación operativa y las reglas derivadas son un puente al desarrollo y
deben validarse con un abogado laboralista antes de dar la skill por
definitiva — especialmente las reglas FIRME* y todo lo PENDIENTE de 2027.
Cuando la STPS publique sus disposiciones, esta skill se revisa y sube su
`version` y `reviewed_at`.

**Revisión 2026-07-07:** los textos del Art. 132 Fr. XXXIV, del Art. 994
Fr. IV Bis y de los transitorios se contrastaron contra el decreto oficial
descargado de diputados.gob.mx (`LFT_ref52_01may26.pdf`, DOF 1-may-2026
edición vespertina): coinciden palabra por palabra. Se precisó el calendario
de horas extra en `references/texto-legal.md` (Transitorio Cuarto: 9/9/10/11/12
en 2026–2030, no un salto a 12 en 2028).
