# Spec: skill `horas-extra`

> 🔍 **BORRADOR — PENDIENTE DE VISTO BUENO DE JP.** Producida en fase 1 del
> pipeline (ver BACKLOG.md) el 2026-07-07. Citas transcritas por Claude
> directamente de los documentos oficiales descargados esa fecha (detalle en
> "Estado del research"). No construir la skill hasta aprobar esta spec
> contra los PDFs oficiales.

## 1. Resumen ejecutivo

**Qué hace:** clasifica cada hora trabajada más allá de la jornada ordinaria
en su régimen legal correcto (extraordinaria dentro del tope +100 %,
excedente del tope +200 %, o trabajo por siniestro con pago ordinario),
valida los topes semanales del año (calendario 9/9/10/11/12) y la
distribución permitida, y audita que un sistema los aplique bien.

**Por qué importa:** las horas extra son el cálculo más sensible en dinero de
un checador — el pago cambia de +0 % a +100 % o +200 % según la
clasificación. Un tope mal configurado o un porcentaje mal aplicado se
traduce directo en nómina incorrecta y en pérdida de defensa en juicio
(la correlación horas-pagos es la regla R9 de `registro-jornada`).

**Cuándo se activa:** al clasificar tiempo extraordinario, calcular
porcentajes de pago de horas extra, configurar topes semanales, o auditar el
módulo de horas extra de un sistema de asistencia o nómina.

**Frontera con `jornada-laboral`:** aquella define CUÁNDO el tiempo deja de
ser ordinario (sus límites diario/semanal, RD-05 de esa skill); ésta define
qué pasa con ese tiempo DESPUÉS: régimen, topes y porcentajes. Comparten el
techo absoluto de 12 horas diarias (Art. 68, párrafo tercero).

## 2. Fuente legal — texto exacto verificado

**Documentos oficiales usados (descargados el 2026-07-07, los mismos de la
spec de jornada-laboral):**

| Doc | Qué es | URL | Uso |
|-----|--------|-----|-----|
| D1 | LFT consolidada vigente, Cámara de Diputados — portada indica "Última Reforma DOF 14-05-2026" | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf | Texto vigente de los Arts. 65–68 (p. 22 del PDF) |
| D2 | Decreto de reforma en materia de reducción de la jornada laboral, DOF 1 de mayo de 2026, edición vespertina (`LFT_ref52_01may26.pdf`) | https://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_ref52_01may26.pdf | Transitorios Primero y Cuarto — pp. 3–4 de la edición |

### 2.1 Artículos vigentes (D1, p. 22)

| ID | Artículo | Última reforma anotada en la consolidada |
|----|----------|------------------------------------------|
| F-01 | Art. 65 | Sin anotación de reforma |
| F-02 | Art. 66 | Artículo reformado DOF 01-05-2026 |
| F-03 | Art. 67 | Nota: "Reforma DOF 01-05-2026: Derogó del artículo el entonces párrafo segundo" |
| F-04 | Art. 68 | Artículo reformado DOF 01-05-2026 |

**F-01 — Art. 65 (D1, p. 22):**

> "En los casos de siniestro o riesgo inminente en que peligre la vida del
> trabajador, de sus compañeros o del patrón, o la existencia misma de la
> empresa, la jornada de trabajo podrá prolongarse por el tiempo
> estrictamente indispensable para evitar esos males."

**F-02 — Art. 66 (D1, p. 22):**

> "La jornada de trabajo podrá prolongarse por circunstancias
> extraordinarias.
> En estos casos, se abonará como salario por este tiempo un cien por ciento
> más de lo fijado para las horas ordinarias. El trabajo extraordinario no
> excederá de doce horas en una semana, las cuales podrán distribuirse en
> hasta cuatro horas diarias, en un máximo de cuatro días en ese periodo."

**F-03 — Art. 67 (D1, p. 22):**

> "Las horas de trabajo a que se refiere el artículo 65, se retribuirán con
> una cantidad igual a la que corresponda a cada una de las horas de la
> jornada."

**F-04 — Art. 68 (D1, p. 22):**

> "Las personas trabajadoras no están obligadas a prestar sus servicios por un
> tiempo mayor del permitido en este capítulo.
> La prolongación del tiempo extraordinario que supere lo establecido en el
> artículo 66 de esta Ley, no podrá ser mayor de cuatro horas a la semana y
> obliga a la persona empleadora a pagar un doscientos por ciento más del
> salario que corresponda a las horas de la jornada ordinaria.
> La suma de las jornadas ordinaria y extraordinaria, en ningún caso podrá ser
> mayor a doce horas diarias."

### 2.2 Transitorios del decreto (D2, pp. 3–4 de la edición del DOF)

**F-05 — Transitorio Cuarto (calendario del tope semanal de horas extra):**

> "La duración de la jornada extraordinaria a que se refiere el artículo 66
> de la Ley Federal del Trabajo se alcanzará de manera gradual, a partir del
> 1 de enero del año correspondiente, conforme a lo siguiente:"

| Año | Horas Extras (tope semanal) |
|-----|------------------------------|
| 2026 | 9 |
| 2027 | 9 |
| 2028 | 10 |
| 2029 | 11 |
| 2030 | 12 |

**F-06 — Transitorio Primero:**

> "El presente Decreto entrará en vigor el día 1 de mayo de 2026."

## 3. Capa interpretativa

Sin criterios nuevos citados de memoria. Dos referencias ya existentes en la
librería (origen: deep research verificado de JP, en
`skills/registro-jornada/references/criterios-tribunales.md`):

- **Carga de la prueba y presunción:** si el patrón no puede probar la
  jornada, el tribunal presume ciertos los hechos del trabajador "hasta 9
  horas extra semanales" (criterio de la Segunda Sala de la SCJN, citado en
  esa referencia). Con los topes nuevos del Transitorio Cuarto, si esa
  presunción se ajusta al tope del año es pregunta abierta → CL-04.
- **Correlación horas-pagos (R9 de registro-jornada):** las horas extra
  registradas deben explicar los pagos de nómina; por eso esta skill exige
  que cada hora quede etiquetada con su régimen (RD-08).

Lectura operativa que fundamenta reglas: la ley distingue DOS regímenes de
prolongación con pagos distintos — el extraordinario común (F-02: +100 %,
con tope y distribución) y el trabajo por siniestro/riesgo inminente
(F-01 + F-03: pago ordinario, "tiempo estrictamente indispensable", sin
tope numérico propio). Un sistema que los mezcla paga mal o audita mal.

## 4. Reglas derivadas

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Entrada de la skill: el tiempo candidato a extraordinario viene de exceder los límites ordinarios definidos por `jornada-laboral` (su RD-05). Esta skill no redefine ese umbral. | Alto | FIRME* | F-02; hereda CL-01 de jornada-laboral |
| RD-02 | Tope semanal de trabajo extraordinario según el año, vigente desde el 1 de enero: 2026: 9 · 2027: 9 · 2028: 10 · 2029: 11 · 2030 en adelante: 12. El sistema debe usar la tabla del año auditado. | Crítico | FIRME | F-02, F-05 |
| RD-03 | Distribución del extraordinario: hasta 4 horas por día, en máximo 4 días por semana (texto vigente). Su interacción con los topes de transición (9/10/11) está abierta → CL-02. | Alto | FIRME* | F-02; ver CL-02 |
| RD-04 | Pago del extraordinario dentro del tope: +100 % sobre lo fijado para la hora ordinaria (salario doble por hora extra). | Crítico | FIRME | F-02 |
| RD-05 | Excedente del tope del Art. 66: no puede ser mayor de 4 horas a la semana y se paga +200 % (salario triple por hora). Sobre qué base corre ese tope en años de transición → CL-03. | Alto | FIRME* | F-04; ver CL-03 |
| RD-06 | Techo absoluto: ordinaria + extraordinaria ≤ 12 horas por día, sin excepción. (Regla compartida con `jornada-laboral`, su RD-04.) | Alto | FIRME | F-04 |
| RD-07 | Trabajo por siniestro o riesgo inminente: solo por el tiempo estrictamente indispensable y se paga igual que la hora ordinaria — es un régimen DISTINTO del extraordinario común y debe registrarse aparte. | Medio | FIRME | F-01, F-03 |
| RD-08 | Cada hora no ordinaria debe quedar etiquetada con su régimen (extra +100 % / excedente +200 % / siniestro pago ordinario) de forma exportable, para que la nómina pague bien y la correlación horas-pagos sea verificable. | Alto | FIRME* | F-02, F-03, F-04; interpretación operativa de la correlación (R9 de registro-jornada) |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

### 4.1 Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | (Heredado de `jornada-laboral`) ¿El excedente del límite SEMANAL ordinario sin exceso diario es "tiempo extraordinario" con su régimen de pago? | El Art. 66 habla de "prolongarse" la jornada; el texto no resuelve el excedente puramente semanal. | abierta | abogado laboralista |
| CL-02 | En los años de transición (tope 9, 10 u 11), ¿la distribución "hasta 4 horas diarias en máximo 4 días" aplica tal cual, o se modula con el tope del año? | El Transitorio Cuarto solo gradúa el TOTAL semanal; no dice nada de la distribución diaria/por días. | abierta | abogado laboralista |
| CL-03 | El tope de +4 horas del Art. 68 (pagadas +200 %), ¿corre sobre el tope del año (p. ej. 9+4 en 2027) o sobre las 12 horas del texto del Art. 66? | El Art. 68 remite a "lo establecido en el artículo 66", y el transitorio modifica gradualmente ese valor. | abierta | abogado laboralista |
| CL-04 | La presunción jurisprudencial de "hasta 9 horas extra semanales" a favor del trabajador, ¿se ajusta al tope del año del Transitorio Cuarto? | El criterio citado es previo a la reforma; el tope semanal ahora es variable por año. | abierta | abogado laboralista |

## 5. Instrucciones de auditoría y clasificación (cuerpo del SKILL.md)

1. **Recibir los candidatos a extraordinario** desde `jornada-laboral`
   (excedentes de límites diario/semanal ordinarios) — RD-01.
2. **Determinar el año auditado** y cargar el tope semanal vigente (RD-02).
3. **Separar el trabajo por siniestro** (RD-07): si el registro está marcado
   como siniestro/riesgo inminente, su régimen es pago ordinario y tiempo
   estrictamente indispensable; auditarlo aparte y no contarlo contra el tope
   del extraordinario común sin resolver antes su clasificación.
4. **Clasificar cada hora extraordinaria común:** dentro del tope semanal del
   año → régimen +100 % (RD-04); por encima del tope → excedente, máximo 4
   horas por semana, régimen +200 % (RD-05), anotando CL-03.
5. **Validar la distribución** del extraordinario: hasta 4 h/día y máximo 4
   días por semana (RD-03), anotando CL-02 en años de transición.
6. **Verificar el techo absoluto** de 12 horas por día sumando ordinaria +
   extraordinaria (RD-06).
7. **Auditar el etiquetado por régimen** y su exportabilidad para nómina
   (RD-08).
8. **Generar el reporte** con el formato de la sección 6, marcando los CL
   abiertos que apliquen.

### 5.1 Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Corrompe el tope del año o el porcentaje de pago base? (RD-02, RD-04)
     SÍ  -> CRÍTICO  (nómina incorrecta en dinero, por cada trabajador)
     NO  -> siguiente pregunta

  ¿Clasifica mal regímenes, distribución o techos? (RD-01, RD-03, RD-05, RD-06, RD-08)
     SÍ  -> ALTO  (horas mal etiquetadas o excesos sin detectar)
     NO  -> siguiente pregunta

  ¿Es un régimen especial mal registrado? (RD-07)
     SÍ  -> MEDIO

  CL-01 a CL-04 y lo pendiente de autoridad -> INFORMATIVO
```

**Checklist de consistencia (requisito 5 del brief):** RD-02/04 = Crítico en
tabla y árbol ✓ · RD-01/03/05/06/08 = Alto en tabla y árbol ✓ · RD-07 =
Medio en tabla y árbol ✓ · casos de prueba abajo alineados ✓.

## 6. Formato de salida

La plantilla de reporte de la librería
(`skills/registro-jornada/assets/plantilla-reporte.md`), con encabezado:
`AUDITORÍA DE COMPLIANCE — Tiempo extraordinario (Arts. 65–68 LFT)` y una
sección adicional fija: `TOPES APLICADOS ESTE AÑO: [tope semanal del año +
distribución vigente]`.

## 7. Límites de la skill

- No calcula montos de nómina: clasifica horas y valida porcentajes y topes;
  el cálculo monetario (salario base, integraciones) es del sistema de
  nómina.
- No redefine cuándo el tiempo deja de ser ordinario — eso es de
  `jornada-laboral`.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando cambie el año de calendario (tope nuevo), cuando el
  abogado resuelva CL-01–CL-04, o si la STPS publica disposiciones que
  toquen el registro del tiempo extraordinario.

## 8. Estructura de archivos

```
skills/horas-extra/
  SKILL.md                 <- frontmatter + secciones 3, 5, 6, 7 de esta spec
  references/
    texto-legal.md         <- sección 2 (F-01 a F-06, con doc y página)
    reglas.md              <- sección 4 (RD-01 a RD-08 + CL-01 a CL-04)
  assets/
    (sin plantilla propia: reutiliza la plantilla de reporte de la librería)
```

### 8.1 Frontmatter del SKILL.md

```yaml
---
name: horas-extra
description: Clasifica el tiempo extraordinario de la LFT mexicana en su régimen correcto (+100 % dentro del tope, +200 % el excedente, pago ordinario por siniestro), valida los topes semanales por año (9/9/10/11/12 en 2026–2030), la distribución 4h×4 días y el techo de 12 horas diarias. Usar al calcular o auditar horas extra, configurar topes o revisar módulos de tiempo extraordinario.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Arts. 65-68; Transitorios Primero y Cuarto del decreto DOF 2026-05-01"
  fuente: "LFT consolidada (última reforma DOF 2026-05-14) + decreto DOF 2026-05-01"
---
```

## 9. Casos de prueba

| # | Entrada | Debe detectar | Severidad esperada |
|---|---------|---------------|--------------------|
| 1 | Año 2027: trabajador acumula 11h extra en la semana y el sistema valida contra 12 | El tope vigente 2027 es 9 (RD-02): 2h clasificadas como extra común que ya son excedente | CRÍTICO (tabla del año mal aplicada) |
| 2 | Sistema paga la hora extra común con +50 % | Falla RD-04: el pago legal es +100 % sobre la hora ordinaria | CRÍTICO |
| 3 | Año 2030: 2h extra diarias en 5 días (10h totales) | Total 10 ≤ 12 ✓, pero 5 días > máximo de 4 días (RD-03) | ALTO |
| 4 | La hora que excede el tope semanal se paga +100 % en vez de +200 % | Falla RD-05: el excedente del tope (máx. 4h/semana) se paga +200 %; anotar CL-03 | ALTO |
| 5 | Día con 8h ordinarias + 5h extra = 13h sin alerta | Falla RD-06: techo absoluto de 12h/día | ALTO |
| 6 | Sistema que usa la tabla del año, paga +100 %/+200 % según tope, valida 4h×4 días y techo de 12h, y etiqueta el siniestro aparte con pago ordinario | Ninguna falla firme; solo INFORMATIVO por CL abiertos | CUMPLE |

## 10. Kickoff prompt (para la fase 2)

> Construye la skill `horas-extra` en el repo klokk-skills-leyes a partir de
> `specs/horas-extra-spec.md` (ya aprobada por JP). Sigue EXACTAMENTE la
> estructura de la sección 8. No inventes contenido legal: usa solo lo que
> está en la spec. Al terminar, corre mentalmente los 6 casos de prueba de la
> sección 9 y reporta si cada uno da lo esperado. Cierra el loop de fase 2
> según CLAUDE.md: checklist, STATUS, BITACORA, commits ordenados y push.

---

## Estado del research

Citas de los Arts. 65–68 transcritas por Claude el 2026-07-07 del PDF oficial
de la LFT consolidada (D1, descargado de diputados.gob.mx esa fecha; portada:
"Última Reforma DOF 14-05-2026"), p. 22. Transitorios Primero y Cuarto
transcritos del decreto oficial (D2, `LFT_ref52_01may26.pdf`, DOF 1-may-2026
edición vespertina), pp. 3–4. Los textos del decreto y de la consolidada
coinciden entre sí en los artículos reformados. La capa interpretativa solo
referencia criterios YA presentes en la librería (deep research verificado de
JP en registro-jornada); no se citaron criterios nuevos de memoria.

**Pendiente para el visto bueno de JP (gate de fase 1):** contrastar F-01 a
F-06 contra los dos PDFs (páginas indicadas en cada cita).
**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME* —
en especial CL-03 (base del tope de +4h en transición), que impacta dinero.
