---
name: jornada-laboral
description: Clasifica tipos de jornada (diurna/nocturna/mixta) y valida los límites diarios, semanales por año (48→40, 2026–2030) y el techo de 12 horas de la LFT mexicana. Usar al clasificar turnos, validar duraciones de jornada, configurar límites de asistencia o determinar cuándo empieza el tiempo extraordinario.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Arts. 58-64 y 68; Transitorios Segundo y Séptimo del decreto DOF 2026-05-01"
  fuente: "LFT consolidada (última reforma DOF 2026-05-14) + decreto DOF 2026-05-01"
---

# Skill: jornada-laboral

**Qué hace:** clasifica los tipos de jornada (diurna / nocturna / mixta) y
valida los límites de duración — diario por tipo, semanal por año (calendario
48→40) y el techo absoluto de 12 horas diarias — para que Klokk o un sistema
auditado calcule y alerte correctamente sobre las jornadas registradas.

**Por qué importa:** es la tabla de límites que da sentido al registro del
Art. 132 Fr. XXXIV. La skill hermana `registro-jornada` audita CÓMO se
registra; ésta define CUÁNTO puede durar lo registrado. Un límite mal
configurado (tipo de turno mal clasificado, o tabla del año equivocado)
corrompe todos los cálculos de cumplimiento y de tiempo extraordinario.

**Cuándo se activa:** al clasificar turnos, validar duraciones de jornada,
determinar cuándo el tiempo pasa a ser extraordinario, o auditar la
configuración de límites de un sistema de asistencia.

**Frontera con `horas-extra`:** esta skill define los límites ordinarios y el
umbral donde el tiempo se vuelve extraordinario. El régimen del tiempo
extraordinario (pagos +100 %/+200 %, calendario 9/9/10/11/12, distribución
4h×4 días, siniestros de los Arts. 65 y 67) pertenece a la skill
`horas-extra`. Comparten una regla: el techo de 12 horas diarias (Art. 68,
párrafo tercero).

## Archivos de referencia

Cargar según lo que pida el cálculo o la auditoría:

- [references/texto-legal.md](references/texto-legal.md) — texto oficial
  verificado: Arts. 58–64 y 68 (F-01 a F-08) y transitorios del decreto
  (F-09 a F-11), con documento y página de cada cita.
- [references/reglas.md](references/reglas.md) — las 9 reglas derivadas
  (RD-01 a RD-09) con riesgo y estado, y los 4 casos límite abiertos
  (CL-01 a CL-04).
- Plantilla del reporte: se reutiliza la de la librería —
  [../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md).

## Capa interpretativa

**Deliberadamente mínima.** No se citan tesis ni criterios jurisprudenciales
de memoria; si el abogado (fase 3) aporta criterios sobre jornada (p. ej.
sobre el cómputo del tiempo a disposición o la distribución por acuerdo), se
agregan aquí con su fuente. Lo que sí es interpretación operativa razonable,
marcada FIRME*, vive en las reglas — con sus dudas registradas como casos
límite.

Dos lecturas operativas que fundamentan reglas:

- **El tiempo a disposición cuenta (F-07):** para un checador, la comida
  fichada dentro del centro sin posibilidad de salir es tiempo efectivo de
  jornada. Impacta directamente el conteo de horas de Klokk.
- **La clasificación de turno es la puerta de todos los límites (F-03):** la
  regla de las 3.5 horas nocturnas decide si un turno vespertino es mixta o
  nocturna, y con ello su límite diario (7.5 vs 7 horas).

## Procedimiento de cálculo y auditoría

1. **Determinar el año auditado** y cargar el límite semanal vigente (RD-03).
2. **Clasificar cada turno** con RD-01; en turnos que crucen medianoche,
   aplicar la clasificación y registrar la nota CL-03.
3. **Validar el límite diario** de cada jornada contra su tipo (RD-02).
4. **Acumular la semana** y validar contra el límite del año (RD-03).
5. **Marcar excedentes** diarios o semanales como candidatos a tiempo
   extraordinario y delegar su régimen a `horas-extra` (RD-05).
6. **Verificar el techo absoluto** de 12 horas/día sumando ordinaria +
   extraordinaria (RD-04).
7. **Auditar el cómputo de descansos:** media hora en jornada continua
   (RD-06) y tiempo a disposición contado como efectivo (RD-07).
8. **Verificar la representación de distribuciones pactadas** (RD-08) y la
   alerta de protección salarial (RD-09).
9. **Generar el reporte** con el formato de la sección siguiente, marcando
   los CL abiertos que apliquen.

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Corrompe la clasificación o los límites base? (RD-01, RD-02, RD-03)
     SÍ  -> CRÍTICO  (todos los cálculos posteriores quedan mal)
     NO  -> siguiente pregunta

  ¿Produce horas mal contadas o excesos sin detectar? (RD-04, RD-05, RD-07)
     SÍ  -> ALTO  (el registro existe pero miente sobre la jornada real)
     NO  -> siguiente pregunta

  ¿Es representación incompleta o alerta faltante? (RD-06, RD-08, RD-09)
     SÍ  -> MEDIO

  CL-01 a CL-04 y lo pendiente de autoridad -> INFORMATIVO
```

## Formato de salida

La misma plantilla de reporte de la librería
([../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md)),
con encabezado:

```
AUDITORÍA DE COMPLIANCE — Jornada laboral (Arts. 58–68 LFT)
```

y una sección adicional fija:

```
LÍMITES APLICADOS ESTE AÑO: [tabla del año auditado]
```

## Límites de la skill

- No calcula pagos de tiempo extraordinario — eso es de `horas-extra`.
- No cubre jornadas especiales (personas menores de edad, sectores con
  regulación propia); si el alcance las detecta, lo declara y se detiene.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando cambie el año de calendario (límite semanal nuevo) o
  cuando el abogado resuelva CL-01–CL-04.

## Estado del contenido

Citas de los Arts. 58–68 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), pp. 21–22, y transitorios del decreto oficial
(`LFT_ref52_01may26.pdf`, DOF 1-may-2026 edición vespertina), pp. 3–4. Los
textos del decreto y de la consolidada coinciden entre sí en los artículos
reformados. Spec de origen: `specs/jornada-laboral-spec.md`, aprobada por JP
el 2026-07-07.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME*.
La capa jurisprudencial está deliberadamente vacía: no se citaron criterios
de memoria. Cuando el abogado resuelva los CL o cambie el año de calendario,
esta skill se revisa y sube su `version` y `reviewed_at`.
