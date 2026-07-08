---
name: vacaciones
description: Calcula y audita vacaciones de la LFT mexicana (régimen "vacaciones dignas" 2023); tabla por antigüedad desde 12 días, 12 días continuos a potestad del trabajador, ventana de 6 meses, prima vacacional ≥25 % y registro como ausencia justificada. Usar al calcular saldos, auditar su registro en asistencia o validar primas y constancias.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Arts. 76-81"
  fuente: "LFT consolidada (última reforma DOF 2026-05-14), Capítulo IV, p. 24"
---

# Skill: vacaciones

**Qué hace:** calcula los días de vacaciones que corresponden por antigüedad
(régimen "vacaciones dignas", reforma DOF 27-12-2022), audita la ventana
legal de disfrute (6 meses tras el aniversario), el mínimo de 12 días
continuos a potestad del trabajador, la prima vacacional (≥25 %) y la
constancia anual — y verifica que el checador registre las vacaciones como
ausencia justificada.

**Por qué importa:** para un sistema de asistencia, las vacaciones son la
ausencia justificada más frecuente; si se calculan con la tabla anterior a
2023 (6 días el primer año) o se dejan vencer sin alerta, el cliente
incumple de forma masiva y silenciosa.

**Cuándo se activa:** al calcular saldos de vacaciones, auditar su registro
en el checador, validar la prima vacacional o revisar constancias de
antigüedad.

**Fronteras:** el pago/monto exacto es de nómina (fuera de alcance, D-08);
la interacción de los días de vacaciones con las rachas de descanso semanal
es de `dias-de-descanso` (aquí solo se marca la ausencia como justificada).

## Archivos de referencia

- [references/texto-legal.md](references/texto-legal.md) — texto oficial
  verificado: Arts. 76–81 (F-01 a F-06), con documento y página.
- [references/reglas.md](references/reglas.md) — las 7 reglas derivadas
  (RD-01 a RD-07) y los 4 casos límite (CL-01 a CL-04).
- Plantilla del reporte: se reutiliza la de la librería —
  [../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md).

## Capa interpretativa

Sin criterios jurisprudenciales citados de memoria. Lecturas operativas:

- **La tabla de días por antigüedad se DERIVA del texto de F-01** y su
  segmento quinquenal es la lectura operativa estándar del "a partir del
  sexto año… dos días por cada cinco de servicios". Los cortes exactos de
  los bloques tienen debate conocido → CL-01; la tabla de RD-01 se marca
  FIRME* por eso.
- **Los 12 días continuos son potestad del trabajador (F-03):** el sistema
  no puede forzar fraccionamientos; la distribución la decide la persona
  trabajadora.
- **Las vacaciones no se "pagan en lugar de tomarse" (F-04):** un saldo
  vencido no se liquida con dinero durante la relación; la única
  remuneración proporcional es al terminar la relación.

## Procedimiento de auditoría

1. **Calcular el saldo por antigüedad** de cada trabajador con la tabla de
   RD-01 (años CUMPLIDOS de servicio), anotando CL-01.
2. **Validar la configuración del sistema** contra esa tabla — detectar
   tablas pre-2023 (6/8/10… días) como falla inmediata.
3. **Auditar la distribución:** debe existir la opción de 12 días continuos
   y el registro de la distribución elegida por el trabajador (RD-02).
4. **Auditar la ventana de disfrute:** alertas de saldo próximo a vencer y
   vencido (aniversario + 6 meses), y constancia anual emitida (RD-05).
5. **Verificar el etiquetado:** vacaciones como ausencia justificada
   exportable (RD-07, anotar CL-02) y prima vacacional marcada para nómina
   (RD-04, anotar CL-03 si salario variable).
6. **Verificar que no haya compensación en dinero** de saldos durante la
   relación (RD-03); proporcionales solo al terminar la relación o para
   discontinuos/temporada (RD-06).
7. **Generar el reporte** con el formato de la sección siguiente.

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿La tabla de días por antigüedad está mal? (RD-01)
     SÍ  -> CRÍTICO  (todos los saldos de todos los trabajadores quedan mal)
     NO  -> siguiente pregunta

  ¿Bloquea derechos o deja dinero/vencimientos sin marcar?
  (RD-02, RD-04, RD-05, RD-07)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿Es compensación indebida o proporcional sin calcular? (RD-03, RD-06)
     SÍ  -> MEDIO

  CL-01 a CL-04 y lo pendiente -> INFORMATIVO
```

## Formato de salida

La plantilla de reporte de la librería
([../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md)),
con encabezado:

```
AUDITORÍA DE COMPLIANCE — Vacaciones (Arts. 76–81 LFT)
```

y una sección adicional fija:

```
TABLA DE ANTIGÜEDAD APLICADA: [días por años de servicio usados en la auditoría]
```

## Límites de la skill

- No calcula montos de nómina (salario de vacaciones ni prima en pesos):
  clasifica, etiqueta y valida derechos en días y porcentajes.
- No resuelve el efecto de las vacaciones en otros cómputos (CL-02): lo
  reporta.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si se reforma el
  capítulo de vacaciones.

## Estado del contenido

Citas de los Arts. 76–81 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), p. 24 — Capítulo IV "Vacaciones", con la reforma "vacaciones
dignas" (DOF 27-12-2022) en los Arts. 76 y 78. La tabla de RD-01 es DERIVADA
del texto: los años 1–5 son literales; los bloques quinquenales son lectura
operativa estándar (FIRME* + CL-01). Spec de origen:
`specs/vacaciones-spec.md`, **construida en modo batch (D-11): revisión de JP
pendiente en bloque**.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — en especial CL-01
(cortes de bloque) y CL-04 (potestad del trabajador vs ventana de 6 meses).
Cuando se resuelvan, esta skill se revisa y sube su `version` y `reviewed_at`.
