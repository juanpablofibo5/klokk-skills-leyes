# Spec: skill `jornada-laboral`

> ✅ **APROBADA POR JP — 2026-07-07.** Producida en fase 1 del pipeline (ver
> BACKLOG.md) el 2026-07-07; citas transcritas por Claude directamente de los
> documentos oficiales descargados esa fecha (detalle en "Estado del
> research", al final). La skill se construyó en fase 2 a partir de esta spec:
> `skills/jornada-laboral/`.

## 1. Resumen ejecutivo

**Qué hace:** clasifica los tipos de jornada (diurna / nocturna / mixta) y
valida los límites de duración — diario por tipo, semanal por año (calendario
48→40), y el techo absoluto de 12 horas diarias — para que Klokk o un sistema
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

## 2. Fuente legal — texto exacto verificado

**Documentos oficiales usados (descargados el 2026-07-07):**

| Doc | Qué es | URL | Uso |
|-----|--------|-----|-----|
| D1 | LFT consolidada vigente, Cámara de Diputados — portada indica "Última Reforma DOF 14-05-2026" | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf | Texto vigente de los Arts. 58–68 (pp. 21–22 del PDF) |
| D2 | Decreto de reforma en materia de reducción de la jornada laboral, DOF 1 de mayo de 2026, edición vespertina (`LFT_ref52_01may26.pdf`) | https://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_ref52_01may26.pdf | Transitorios (calendarios graduales) — pp. 3–4 de la edición |

### 2.1 Artículos vigentes (D1, pp. 21–22)

| ID | Artículo | Última reforma anotada en la consolidada |
|----|----------|------------------------------------------|
| F-01 | Art. 58 | Párrafo segundo adicionado DOF 01-05-2026 |
| F-02 | Art. 59 | Artículo reformado DOF 01-05-2026 |
| F-03 | Art. 60 | Sin anotación de reforma (texto original) |
| F-04 | Art. 61 | Artículo reformado DOF 01-05-2026 |
| F-05 | Art. 62 | Sin anotación de reforma |
| F-06 | Art. 63 | Sin anotación de reforma |
| F-07 | Art. 64 | Sin anotación de reforma |
| F-08 | Art. 68 | Artículo reformado DOF 01-05-2026 |

**F-01 — Art. 58 (D1, pp. 21–22):**

> "Jornada de trabajo es el tiempo durante el cual el trabajador está a
> disposición del patrón para prestar su trabajo.
> Esta podrá ser distribuida de común acuerdo por las personas empleadoras y
> trabajadoras."

**F-02 — Art. 59 (D1, p. 22):**

> "La duración máxima de la jornada ordinaria de trabajo será de cuarenta
> horas semanales."

**F-03 — Art. 60 (D1, p. 22):**

> "Jornada diurna es la comprendida entre las seis y las veinte horas.
> Jornada nocturna es la comprendida entre las veinte y las seis horas.
> Jornada mixta es la que comprende períodos de tiempo de las jornadas diurna
> y nocturna, siempre que el período nocturno sea menor de tres horas y media,
> pues si comprende tres y media o más, se reputará jornada nocturna."

**F-04 — Art. 61 (D1, p. 22):**

> "La duración de la jornada diaria será de ocho horas la diurna, siete la
> nocturna y siete horas y media la mixta."

**F-05 — Art. 62 (D1, p. 22):**

> "Para fijar la jornada de trabajo se observará lo dispuesto en el artículo
> 5o., fracción III."

**F-06 — Art. 63 (D1, p. 22):**

> "Durante la jornada continua de trabajo se concederá al trabajador un
> descanso de media hora, por lo menos."

**F-07 — Art. 64 (D1, p. 22):**

> "Cuando el trabajador no pueda salir del lugar donde presta sus servicios
> durante las horas de reposo o de comidas, el tiempo correspondiente le será
> computado como tiempo efectivo de la jornada de trabajo."

**F-08 — Art. 68 (D1, p. 22):**

> "Las personas trabajadoras no están obligadas a prestar sus servicios por un
> tiempo mayor del permitido en este capítulo.
> La prolongación del tiempo extraordinario que supere lo establecido en el
> artículo 66 de esta Ley, no podrá ser mayor de cuatro horas a la semana y
> obliga a la persona empleadora a pagar un doscientos por ciento más del
> salario que corresponda a las horas de la jornada ordinaria.
> La suma de las jornadas ordinaria y extraordinaria, en ningún caso podrá ser
> mayor a doce horas diarias."

### 2.2 Transitorios del decreto (D2, pp. 3–4 de la edición del DOF)

**F-09 — Transitorio Primero:**

> "El presente Decreto entrará en vigor el día 1 de mayo de 2026."

**F-10 — Transitorio Segundo (calendario de jornada semanal):**

> "La duración de la jornada laboral a que se refiere el artículo 59 de la Ley
> Federal del Trabajo se alcanzará de manera gradual, a partir del 1 de enero
> del año que corresponda, conforme a lo siguiente:"

| Año | Jornada Laboral (horas semanales) |
|-----|-----------------------------------|
| 2026 | 48 |
| 2027 | 46 |
| 2028 | 44 |
| 2029 | 42 |
| 2030 | 40 |

**F-11 — Transitorio Séptimo:**

> "En ningún caso la reducción de la jornada laboral implicará la disminución
> de sueldos, salarios o prestaciones de las personas trabajadoras."

*(El Transitorio Cuarto — calendario de horas extra 9/9/10/11/12 — se cita en
la spec de `horas-extra`; aquí solo se referencia.)*

## 3. Capa interpretativa

**Deliberadamente mínima en esta spec.** No se citan tesis ni criterios
jurisprudenciales de memoria; si el abogado (fase 3) aporta criterios sobre
jornada (p. ej. sobre el cómputo del tiempo a disposición o la distribución
por acuerdo), se agregan aquí con su fuente. Lo que sí es interpretación
operativa razonable, marcada FIRME*, vive en las reglas — con sus dudas
registradas como casos límite (sección 4.1).

Dos lecturas operativas que fundamentan reglas:

- **El tiempo a disposición cuenta (F-07):** para un checador, la comida
  fichada dentro del centro sin posibilidad de salir es tiempo efectivo de
  jornada. Impacta directamente el conteo de horas de Klokk.
- **La clasificación de turno es la puerta de todos los límites (F-03):** la
  regla de las 3.5 horas nocturnas decide si un turno vespertino es mixta o
  nocturna, y con ello su límite diario (7.5 vs 7 horas).

## 4. Reglas derivadas

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Clasificación de turno: DIURNA si cae íntegra entre 06:00–20:00; NOCTURNA si cae íntegra entre 20:00–06:00; si abarca ambas franjas: MIXTA cuando el periodo nocturno es < 3h30m, NOCTURNA cuando es ≥ 3h30m. | Crítico | FIRME | F-03 |
| RD-02 | Límite diario por tipo: diurna 8h, nocturna 7h, mixta 7h30m. | Crítico | FIRME | F-04 |
| RD-03 | Límite semanal de jornada ordinaria según el año, vigente desde el 1 de enero: 2026: 48 · 2027: 46 · 2028: 44 · 2029: 42 · 2030 en adelante: 40. El sistema debe usar la tabla del año auditado, nunca un valor fijo. | Crítico | FIRME | F-02, F-10 |
| RD-04 | Techo absoluto: ordinaria + extraordinaria ≤ 12 horas por día, sin excepción por acuerdo. (Regla compartida con `horas-extra`.) | Alto | FIRME | F-08 |
| RD-05 | Umbral de tiempo extraordinario: el tiempo que excede el límite diario del tipo de turno (RD-02) o el límite semanal vigente (RD-03) deja de ser ordinario y pasa al régimen de `horas-extra`. | Alto | FIRME* | F-02, F-04; ver CL-01 |
| RD-06 | En jornada continua debe existir un descanso de al menos 30 minutos. | Medio | FIRME | F-06 |
| RD-07 | Si el trabajador no puede salir del lugar durante reposo o comidas, ese tiempo se computa como jornada efectiva — el sistema no debe descontarlo. | Alto | FIRME | F-07 |
| RD-08 | La jornada semanal puede distribuirse de común acuerdo entre las partes; el sistema debe poder representar distribuciones pactadas. Los límites de esa distribución están abiertos (CL-02). | Medio | FIRME* | F-01; ver CL-02 |
| RD-09 | La reducción gradual de jornada no puede usarse para disminuir sueldos ni prestaciones; si el sistema detecta recálculo de salario-hora a la baja al cambiar de año de calendario, debe alertarlo. | Medio | FIRME* | F-11 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada en 4.1.

### 4.1 Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿El excedente del límite SEMANAL sin exceder ningún límite diario es "tiempo extraordinario" con su régimen de pago? | El Art. 66 habla de "prolongarse" la jornada; el texto no dice explícitamente cómo tratar el excedente puramente semanal. | abierta | abogado laboralista |
| CL-02 | ¿La distribución "de común acuerdo" (Art. 58) permite rebasar los límites diarios del Art. 61 (p. ej. 4×10h)? | El nuevo segundo párrafo del 58 no fija límites propios y el 61 quedó redactado como "la duración de la jornada diaria será…", sin decir "máxima". | abierta | abogado laboralista |
| CL-03 | En turnos que cruzan medianoche, ¿a qué día se imputan las horas para el límite diario y a qué semana para el semanal? | La ley no define el corte; es una decisión operativa con impacto legal. | abierta | decisión de producto + abogado |
| CL-04 | ¿Los 30 minutos de descanso (Art. 63) computan como jornada cuando el trabajador SÍ puede salir? | El Art. 64 solo resuelve el caso "no puede salir"; el caso contrario queda a interpretación. | abierta | abogado laboralista |

## 5. Instrucciones de cálculo y auditoría (cuerpo del SKILL.md)

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
9. **Generar el reporte** con el formato de la sección 6, marcando los CL
   abiertos que apliquen.

### 5.1 Árbol de decisión de severidad

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

**Checklist de consistencia (requisito 5 del brief):** RD-01/02/03 = Crítico
en tabla y árbol ✓ · RD-04/05/07 = Alto en tabla y árbol ✓ · RD-06/08/09 =
Medio en tabla y árbol ✓ · casos de prueba abajo alineados ✓.

## 6. Formato de salida

La misma plantilla de reporte de la librería (ver
`skills/registro-jornada/assets/plantilla-reporte.md`), con encabezado:
`AUDITORÍA DE COMPLIANCE — Jornada laboral (Arts. 58–68 LFT)` y una sección
adicional fija: `LÍMITES APLICADOS ESTE AÑO: [tabla del año auditado]`.

## 7. Límites de la skill

- No calcula pagos de tiempo extraordinario — eso es de `horas-extra`.
- No cubre jornadas especiales (personas menores de edad, sectores con
  regulación propia); si el alcance las detecta, lo declara y se detiene.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando cambie el año de calendario (límite semanal nuevo) o
  cuando el abogado resuelva CL-01–CL-04.

## 8. Estructura de archivos

```
skills/jornada-laboral/
  SKILL.md                 <- frontmatter + secciones 3, 5, 6, 7 de esta spec
  references/
    texto-legal.md         <- sección 2 (F-01 a F-11, con doc y página)
    reglas.md              <- sección 4 (RD-01 a RD-09 + CL-01 a CL-04)
  assets/
    (sin plantilla propia: reutiliza la plantilla de reporte de la librería)
```

### 8.1 Frontmatter del SKILL.md

```yaml
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
```

## 9. Casos de prueba

| # | Entrada | Debe detectar | Severidad esperada |
|---|---------|---------------|--------------------|
| 1 | Turno 21:00–05:00 (8h, íntegro en franja nocturna) que el sistema acepta sin marcar | Clasificación NOCTURNA con límite 7h; hay 1h de exceso diario sin detectar (RD-02) | CRÍTICO |
| 2 | Turno 14:00–22:30 (periodo nocturno 2h30m) que el sistema clasifica como diurna | Es MIXTA (< 3h30m nocturnas), límite 7h30m; clasificación errónea (RD-01) | CRÍTICO |
| 3 | Turno 17:00–01:00 (periodo nocturno 5h ≥ 3h30m) | Se reputa NOCTURNA, no mixta (RD-01); cruza medianoche → anotar CL-03 | CRÍTICO si clasifica mixta; nota INFORMATIVA por CL-03 |
| 4 | Año 2027: semana de 6×8h = 48h; el sistema valida contra 48 | El límite vigente 2027 es 46 (RD-03): 2h de exceso semanal sin detectar; anotar CL-01 sobre su régimen | CRÍTICO (tabla del año mal aplicada) |
| 5 | Sistema que clasifica los 3 tipos con la regla de 3h30m, aplica 8/7/7.5 diario, usa la tabla anual vigente desde el 1 de enero, marca excedentes como candidatos a extra y computa comidas sin salida como efectivas | Ninguna falla firme; solo INFORMATIVO por CL abiertos | CUMPLE |
| 6 | Empleado ficha 30 min de comida dentro de la planta sin poder salir; el sistema descuenta ese tiempo de las horas efectivas | Falla RD-07 (Art. 64): ese tiempo computa como jornada efectiva | ALTO |

## 10. Kickoff prompt (para la fase 2)

> Construye la skill `jornada-laboral` en el repo klokk-skills-leyes a partir
> de `specs/jornada-laboral-spec.md` (ya aprobada por JP). Sigue EXACTAMENTE
> la estructura de la sección 8. No inventes contenido legal: usa solo lo que
> está en la spec. Al terminar, corre mentalmente los 6 casos de prueba de la
> sección 9 y reporta si cada uno da lo esperado. Commits ordenados.

---

## Estado del research

Citas de los Arts. 58–68 transcritas por Claude el 2026-07-07 directamente del
PDF oficial de la LFT consolidada (D1, descargado de diputados.gob.mx esa
fecha; portada: "Última Reforma DOF 14-05-2026"), pp. 21–22. Transitorios
transcritos del decreto oficial (D2, `LFT_ref52_01may26.pdf`, DOF 1-may-2026
edición vespertina), pp. 3–4. Los textos del decreto y de la consolidada
coinciden entre sí en los artículos reformados.

**Pendiente para el visto bueno de JP (gate de fase 1):** contrastar las citas
F-01 a F-11 contra esos dos PDFs (páginas indicadas en cada cita).
**Pendiente para el abogado (fase 3):** CL-01 a CL-04, y las reglas FIRME*.
La capa jurisprudencial está deliberadamente vacía: no se citaron criterios de
memoria.
