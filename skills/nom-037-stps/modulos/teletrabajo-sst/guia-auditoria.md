# Guía de auditoría — módulo teletrabajo-sst (nom-037-stps)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-08 |
| ley | NOM-037-STPS-2023 |
| fuente | D3/D4 de FUENTES.md (DOF 08-06-2023) |

---

## Qué hace este módulo

Audita los requisitos de la NOM-037-STPS-2023 (Teletrabajo — Condiciones de
seguridad y salud en el trabajo, vigente desde 05-12-2023) que un sistema de
software puede verificar o alimentar con sus datos: el listado patronal de
teletrabajadores con el porcentaje de tiempo en teletrabajo, el alcance
completo del derecho a la desconexión (extendido por la NOM a horarios no
laborables, vacaciones, permisos, licencias y pausas convenidas), las pausas
y los reposos de lactancia registrables, la documentación del cambio de
modalidad y su reversibilidad, y la conservación de evidencias por al menos
un año.

## Por qué importa

La NOM está VIGENTE desde el 05-12-2023 (180 días naturales tras su
publicación en el DOF el 08-06-2023). Toda organización con teletrabajadores
es inspeccionable contra ella desde esa fecha. El listado del numeral 5.1 con
su campo "tiempo en porcentaje" es exactamente el dato que un sistema de
control de asistencia produce; el PEC admite el listado en archivos
electrónicos y lo compulsa contra nómina — lo que un sistema auditado ya
hace con la correlación horas-pagos (RD-09 del módulo registro-jornada (lft)).

## Cuándo se activa (F1)

Este módulo se activa cuando el repo auditado tiene teletrabajadores
declarados o potenciales. Señales concretas: ver sección "Aplicabilidad (F1)"
abajo.

## Frontera del módulo

Los límites de jornada son del módulo jornada-laboral (lft); el registro
electrónico es del módulo registro-jornada (lft); la retención LFT, del
módulo conservacion-y-prueba (lft). Los reposos de lactancia se auditan aquí
solo en su efecto sobre el registro del sistema (la skill dedicada
`lactancia-y-descansos-especiales` está en el backlog). Las condiciones
físicas y ergonómicas del lugar de trabajo, listas de verificación de SST,
capacitación anual y exámenes médicos son obligaciones de la NOM que NO se
verifican con datos de asistencia: quedan explícitamente fuera de alcance
(ver "Límites del módulo"), nunca como pendientes.

El módulo teletrabajo (lft) cubre la clasificación del teletrabajador (umbral
40 %, RD-01 de teletrabajo (lft)), el registro de jornada remota (RD-02), la
desconexión al término de jornada (RD-03), la supervisión proporcional
(RD-04), la modalidad e historial (RD-05), y los insumos (RD-06). Este
módulo NOM COMPLEMENTA esas reglas: no las duplica.

---

## Aplicabilidad (F1)

### Señales POSITIVAS (el módulo aplica)

Buscar en el repo auditado:

- Tablas o modelos con nombres como `employees`, `workers`, `users`,
  `trabajadores`, `staff` que contengan campos `work_mode`, `modalidad`,
  `remote`, `teletrabajo`, `hybrid`, o similar.
- Tablas de tipo `attendance_records`, `check_ins`, `asistencia`, `jornada`
  con registros de ubicación (`location`, `lugar`, `place_type`).
- Configuraciones o flags como `is_remote`, `remote_percentage`,
  `teletrabajo_pct`, `days_remote`.
- Endpoints o jobs de tipo `/api/employees/list`, `/report/attendance`,
  `generate_report`, `export_workers`.
- Cualquier referencia a "teletrabajo", "home office", "híbrido", "remoto"
  en README, migraciones o configs.

**Greps sugeridos:**

```bash
grep -ri "teletrabajo\|home.office\|remote\|híbrido\|hybrid" \
  --include="*.py" --include="*.ts" --include="*.js" \
  --include="*.rb" --include="*.go" --include="*.java" .

grep -ri "modalidad\|work_mode\|remote_pct\|remote_percentage" \
  --include="*.sql" --include="*.migration*" --include="*.prisma" .
```

### Señales NEGATIVAS (el módulo probablemente N/A)

- El repo no tiene ningún concepto de empleados, trabajadores o personas
  físicas: es una biblioteca, un servicio de infraestructura, o un producto
  sin usuarios-empleados.
- El readme o la documentación declara explícitamente que todos los
  trabajadores son presenciales sin excepción.
- No existe ningún campo de ubicación, modalidad o trabajo remoto en
  esquemas ni modelos.

**Declarar N/A con razón explícita** si las señales negativas son concluyentes.
Un N/A declarado es resultado válido; un módulo omitido en silencio, no.

---

## Capa interpretativa

Sin criterios citados de memoria. Lecturas operativas del texto:

- **La NOM ya no es pendiente (F-12):** vigente desde el 05-12-2023. Este
  módulo elimina cualquier reporte de "PENDIENTE NOM-037" y lo sustituye
  por reglas auditables (RD-01 a RD-05); lo no verificable con datos de
  asistencia queda declarado fuera de alcance, no como pendiente.
- **El listado 5.1 es dato de sistema de asistencia (F-04, F-10):** el campo
  f) — "Tiempo (en porcentaje) de la relación laboral que usa para realizar
  Teletrabajo" — se calcula de los registros de asistencia (dónde marca
  cada quien); el PEC admite el listado en "archivos electrónicos de medios
  digitales", lo compulsa contra nómina (la correlación horas-pagos,
  RD-09 del módulo registro-jornada (lft)) y define "actualizado" como
  reflejar altas y bajas de la modalidad. La ventana de medición del %
  sigue sin definirse (CL-01 del módulo teletrabajo (lft)) y el umbral de
  aplicación de la NOM tampoco (CL-03 del módulo teletrabajo (lft)).
- **La desconexión es más ancha que en la LFT (F-02, F-05 e, F-09 e):** la
  LFT la enuncia "al término de la jornada laboral" (RD-03 del módulo
  teletrabajo (lft)); la NOM la define además "en los horarios no
  laborables, vacaciones, permisos y licencias" y, en horarios flexibles,
  "durante las pausas convenidas". Un sistema que solo vigile el fin de
  jornada cubre una fracción del derecho: debe cruzar actividad contra
  TODOS esos periodos — que son exactamente los estados de ausencia/descanso
  que ya registra (`vacaciones`, `dias-de-descanso`, `dias-festivos`). Qué
  actos constituyen violación sigue abierto (CL-01 de este módulo).
- **Pausas y lactancia entran a la jornada registrable (F-05 e, F-06,
  F-09 d):** la política debe incluir pausas para descanso, y la NOM
  aterriza los reposos de lactancia del Art. 170 LFT (2 reposos de media
  hora, o reducción de 1 hora, máximo 6 meses) DENTRO del horario pactado
  de teletrabajo — eventos que el sistema debe poder registrar sin contarlos
  contra la persona. "Adecuadas" no está definido (CL-03 de este módulo).
- **El cambio de modalidad genera papel y calendario (F-07, F-08):** proceso
  documentado presencial↔teletrabajo que incluye "los momentos, condiciones
  o causas" de asistencia al centro (5.6 b) — es decir, el patrón híbrido
  debe poder decir QUÉ días toca centro de trabajo, y el sistema auditado es
  quien evidencia si eso se cumple; refuerza RD-05 del módulo teletrabajo
  (lft) (330-G, reversibilidad).
- **Retención mínima de un año (F-11):** los registros digitales valen como
  evidencia y se conservan "al menos durante un año". Es un PISO de la NOM:
  los registros de jornada tienen plazos LFT mayores (módulo
  conservacion-y-prueba (lft)) — aplica siempre el plazo más largo.

---

## Superficies a revisar (F2)

Dónde buscar cada regla de este módulo en un repo típico:

| RD | Qué buscar | Superficies típicas |
|----|------------|---------------------|
| RD-01 | Listado de teletrabajadores con campos a)–k) del 5.1 | Modelo/tabla de empleados o teletrabajadores; endpoints de reporte; jobs de exportación |
| RD-01 | Campo "tiempo en porcentaje" (inciso f) calculado de asistencia | Tabla de asistencia con campo de ubicación; queries de cálculo de porcentaje remoto |
| RD-01 | "Actualizado" = refleja altas y bajas de modalidad | Triggers, webhooks, jobs que actualizan el listado; logs de cambio de modalidad |
| RD-01 | Compulsación contra nómina | Integración con sistema de nómina; exportación a CSV/XLSX; campo de número de empleado en nómina |
| RD-02 | Detección de actividad en horarios no laborables | Sistema de alertas; logs de acceso/actividad; estados de ausencia (vacaciones, permisos, licencias) |
| RD-02 | Detección de actividad en pausas convenidas (horario flexible) | Configuración de horario flexible; registro de pausas; tipos de ausencia |
| RD-03 | Tipos de evento de pausa registrables | Catálogo de tipos de marcaje o evento; tipos de ausencia |
| RD-03 | Reposos de lactancia sin computar como incumplimiento | Lógica de cálculo de jornada; tipos de evento especial |
| RD-04 | Proceso de cambio de modalidad documentado | Historial de modalidad; campos de fecha de inicio/fin de teletrabajo; flujo de aprobación |
| RD-04 | Calendario híbrido pactado vs. realidad | Configuración de días de asistencia al centro; comparación registro vs. patrón esperado |
| RD-05 | Política de retención de registros de teletrabajo | Configuración de retención; jobs de purga/archivado; comentarios en código sobre retención |

---

## Guía de auditoría del módulo

1. **Verificar aplicabilidad (F1):** buscar señales positivas de teletrabajo
   en el repo. Si no hay ninguna, declarar N/A con razón y terminar. Anotar
   CL-01 del módulo teletrabajo (lft) con la ventana de medición del 40 %
   usada; anotar CL-03 de ese módulo si hay remotos bajo el umbral.

2. **Auditar el listado NOM (RD-01):** ¿existe un listado actualizado con al
   menos los incisos a) a k) del 5.1? ¿Está en formato digital accesible?
   ¿Refleja cada alta y baja de modalidad? ¿El sistema produce o alimenta
   sus campos operativos: % de tiempo, lugares convenidos, equipo otorgado?
   Anotar CL-02 sobre el historial de versiones del listado.

3. **Auditar la desconexión de alcance completo (RD-02):** ¿el sistema puede
   detectar/alertar actividad laboral no solo al fin de jornada sino también
   en horarios no laborables, vacaciones, permisos y licencias? En horarios
   flexibles, ¿durante las pausas convenidas? Cruzar contra los estados de
   ausencia ya registrados. Anotar CL-01 de este módulo.

4. **Auditar pausas y lactancia (RD-03):** ¿el sistema permite registrar
   pausas dentro del horario pactado sin computarlas como incumplimiento?
   ¿Para madres en lactancia (máx. 6 meses): 2 reposos de 30 min o
   reducción de 1 hora, sin afectar el cómputo de jornada? Anotar CL-03 de
   este módulo.

5. **Verificar modalidad y reversibilidad (RD-04):** ¿existe proceso
   documentado presencial↔teletrabajo? ¿Se registran los momentos/
   condiciones/causas de asistencia al centro (5.6 b)? ¿El historial de
   cambios de modalidad está ligado al de RD-05 del módulo teletrabajo
   (lft)?

6. **Verificar la retención (RD-05):** ¿los registros de teletrabajo se
   conservan al menos 1 año? Si para la jornada el plazo LFT es mayor
   (módulo conservacion-y-prueba (lft)), ¿el sistema aplica el plazo más
   largo?

7. **Generar el reporte** con el formato estándar de la librería
   (../../../../plantillas/plantilla-reporte.md), encabezado:
   `AUDITORÍA DE COMPLIANCE — Teletrabajo SST (NOM-037-STPS-2023)` y la
   sección fija de este módulo (ver abajo).

---

## Secciones fijas del reporte de este módulo

Todo reporte de este módulo incluye obligatoriamente la sección:

```
CLASIFICACIÓN APLICADA: [ventana y método usados para medir el % de tiempo
en teletrabajo por persona] — pendiente CL-01 del módulo teletrabajo (lft)
```

Si hay teletrabajadores bajo el umbral del 40 % a quienes se aplica la NOM,
agregar:

```
NOTA CL-03 (teletrabajo-lft): se aplicó la NOM a trabajadores con [X %] de
tiempo en teletrabajo — umbral de aplicación abierto, pendiente del abogado.
```

---

## Límites del módulo

- Cubre SOLO los numerales de la NOM-037-STPS verificables con datos de
  asistencia (RD-01 a RD-05 de este módulo; ver tabla de equivalencia en
  reglas.md). **Fuera de alcance
  declarado** (se listan en el reporte como "no auditado — fuera del dominio
  del sistema de asistencia", nunca como pendiente): condiciones físicas y
  ergonómicas del lugar de trabajo (numerales 7.1, 7.2 y 7.3 incisos a–c),
  listas de verificación de SST y su validación por la Comisión de Seguridad
  e Higiene (5.3, 5.4, 5.5, 5.5.1, 5.12), entrega de silla/insumos
  ergonómicos (5.7, salvo su registro vía RD-05 del módulo teletrabajo
  (lft)), mantenimiento de equipos (5.8), capacitación anual (5.9 y numeral
  8), exámenes médicos y avisos de accidente (5.11), violencia familiar
  (5.13, salvo su efecto de reversibilidad vía RD-04 de este módulo),
  participación en comisiones (5.14), obligaciones del trabajador (numeral
  6), organismos y dictámenes de evaluación de la conformidad (numerales 9,
  10.1 y 10.2) y apéndices informativos 1–5.
- No resuelve los CL abiertos (CL-01 a CL-03 de este módulo, ni CL-01 y
  CL-04 del módulo teletrabajo (lft)): los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa si se modifica la NOM-037-STPS (los hashes de D3/D4 en
  FUENTES.md detectan el cambio), o cuando el abogado resuelva los CL
  (fase 3).

---

## Procedencia y estado

Citas F-01 a F-12 transcritas por Claude el 2026-07-08 del texto íntegro de
la NOM-037-STPS-2023 descargado de dof.gob.mx en la misma sesión: nota
5691672 en HTML (`nom037_dof.html`, D4) y PDF oficial de la edición
vespertina del 08-06-2023 (`dof_ves_08062023.pdf`, D3, 61 pp.; la NOM en
pp. 3–50). Verificación cruzada palabra por palabra entre ambos documentos
en las pp. 5–26 de D3 (numerales 1–10.4 y Transitorio). Integridad: SHA-256
idéntico en doble descarga de cada archivo, registrado en FUENTES.md.
Búsqueda web del 2026-07-08: sin modificaciones ni aclaraciones posteriores
de la NOM en el DOF. Calendarios graduales: no aplica — el único transitorio
es la entrada en vigor (F-12; 08-06-2023 + 180 días naturales = 05-12-2023).
Columna "Riesgo" de la tabla del PEC (10.3): viene VACÍA en la edición
oficial (verificado en D3 pp. 14–25); por eso ninguna regla cita severidades
del PEC. No se citaron criterios de memoria.

Spec de origen: `specs/teletrabajo-v2-nom037-spec.md`, construida en modo
batch (D-20). **PENDIENTE de revisión en bloque de JP** (ver banner en
SKILL.md de la ley).

**Pendiente para el visto bueno de JP:** contrastar F-01 a F-12 (= F-08 a
F-19 de la spec) contra las páginas citadas de D3 (o D4); decidir si el
alcance auditado (sección "Límites del módulo") es el correcto.
**Pendiente para el abogado (fase 3):** CL-01 de este módulo (actos que
violan la desconexión), CL-02 (historial del listado), CL-03 (pausas
"adecuadas" vs. supervisión proporcional).
