# Spec: skill `vacaciones`

> 🟡 **CONSTRUIDA EN MODO BATCH (D-11) — 2026-07-07.** Producida y construida
> de corrido con autorización de JP. PENDIENTE: revisión de JP en bloque
> contra el PDF oficial, y fase 3 con abogado. Citas transcritas por Claude
> del PDF oficial descargado el 2026-07-07 (detalle en "Estado del research").

## 1. Resumen ejecutivo

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

## 2. Fuente legal — texto exacto verificado

**Documento oficial usado (descargado el 2026-07-07):**

| Doc | Qué es | URL | Uso |
|-----|--------|-----|-----|
| D1 | LFT consolidada vigente, Cámara de Diputados — portada indica "Última Reforma DOF 14-05-2026" | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf | Texto vigente de los Arts. 76–81, Capítulo IV "Vacaciones" (p. 24 del PDF) |

### 2.1 Artículos vigentes (D1, p. 24)

| ID | Artículo | Última reforma anotada en la consolidada |
|----|----------|------------------------------------------|
| F-01 | Art. 76 | Artículo reformado DOF 27-12-2022 |
| F-02 | Art. 77 | Sin anotación de reforma |
| F-03 | Art. 78 | Artículo reformado DOF 27-12-2022 |
| F-04 | Art. 79 | Sin anotación de reforma |
| F-05 | Art. 80 | Sin anotación de reforma |
| F-06 | Art. 81 | Sin anotación de reforma |

**F-01 — Art. 76 (D1, p. 24):**

> "Las personas trabajadoras que tengan más de un año de servicios
> disfrutarán de un periodo anual de vacaciones pagadas, que en ningún caso
> podrá ser inferior a doce días laborables, y que aumentará en dos días
> laborables, hasta llegar a veinte, por cada año subsecuente de servicios.
> A partir del sexto año, el periodo de vacaciones aumentará en dos días por
> cada cinco de servicios."

**F-02 — Art. 77 (D1, p. 24):**

> "Los trabajadores que presten servicios discontinuos y los de temporada
> tendrán derecho a un período anual de vacaciones, en proporción al número
> de días de trabajos en el año."

**F-03 — Art. 78 (D1, p. 24):**

> "Del total del periodo que le corresponda conforme a lo previsto en el
> artículo 76 de esta Ley, la persona trabajadora disfrutará de doce días de
> vacaciones continuos, por lo menos. Dicho periodo, a potestad de la persona
> trabajadora podrá ser distribuido en la forma y tiempo que así lo
> requiera."

**F-04 — Art. 79 (D1, p. 24):**

> "Las vacaciones no podrán compensarse con una remuneración.
> Si la relación de trabajo termina antes de que se cumpla el año de
> servicios, el trabajador tendrá derecho a una remuneración proporcionada al
> tiempo de servicios prestados."

**F-05 — Art. 80 (D1, p. 24):**

> "Los trabajadores tendrán derecho a una prima no menor de veinticinco por
> ciento sobre los salarios que les correspondan durante el período de
> vacaciones."

**F-06 — Art. 81 (D1, p. 24):**

> "Las vacaciones deberán concederse a los trabajadores dentro de los seis
> meses siguientes al cumplimiento del año de servicios. Los patrones
> entregarán anualmente a sus trabajadores una constancia que contenga su
> antigüedad y de acuerdo con ella el período de vacaciones que les
> corresponda y la fecha en que deberán disfrutarlo."

## 3. Capa interpretativa

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

## 4. Reglas derivadas

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Días de vacaciones por años de servicio cumplidos (tabla derivada de F-01): 1: 12 · 2: 14 · 3: 16 · 4: 18 · 5: 20 · 6–10: 22 · 11–15: 24 · 16–20: 26 · 21–25: 28 · 26–30: 30 (y así sucesivamente, +2 por bloque de 5). Los cortes de bloque exactos → CL-01. | Crítico | FIRME* | F-01; ver CL-01 |
| RD-02 | El trabajador tiene derecho a disfrutar al menos 12 días CONTINUOS, y la distribución del periodo es su potestad; el sistema debe permitir registrar la distribución elegida y no forzar fraccionamiento. | Alto | FIRME | F-03 |
| RD-03 | Las vacaciones no se compensan con remuneración durante la relación; el proporcional en dinero solo procede al terminar la relación antes del año. | Medio | FIRME | F-04 |
| RD-04 | Prima vacacional de al menos 25 % sobre los salarios del periodo de vacaciones; el sistema debe etiquetarla para nómina. La base con salario variable → CL-03. | Alto | FIRME | F-05; ver CL-03 |
| RD-05 | Las vacaciones deben concederse dentro de los 6 meses siguientes al aniversario; el sistema debe alertar saldos sin disfrutar cerca del vencimiento y vencidos. Además, constancia anual de antigüedad + días + fecha. | Alto | FIRME | F-06 |
| RD-06 | Trabajadores discontinuos y de temporada: vacaciones proporcionales a los días trabajados en el año. | Medio | FIRME | F-02 |
| RD-07 | Los días de vacaciones se registran en el checador como ausencia justificada etiquetada (no falta, no día trabajado); su efecto en otros cómputos (rachas, antigüedad) → CL-02. | Alto | FIRME* | F-01, F-06; interpretación operativa; ver CL-02 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

### 4.1 Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | Cortes exactos de los bloques quinquenales del Art. 76 ("a partir del sexto año… por cada cinco"): ¿6–10, 11–15…, u otra lectura? | La redacción admite más de una segmentación; es un debate conocido desde la reforma 2022. | abierta | abogado laboralista |
| CL-02 | ¿Los días de vacaciones cuentan como "días de trabajo" para otros cómputos del checador (p. ej. la racha 6:1 del descanso semanal, antigüedad, asistencia perfecta)? | La LFT no define el efecto de la ausencia justificada sobre esos cómputos. | abierta | abogado laboralista |
| CL-03 | Base de la prima vacacional con salario variable o por hora ("los salarios que les correspondan durante el período"). | El texto no fija la base para salarios no fijos. | abierta | abogado laboralista |
| CL-04 | Si el trabajador no ejerce su potestad de distribución (F-03) dentro de la ventana de 6 meses (F-06), ¿puede el patrón fijar las fechas para no incumplir el Art. 81? | Tensión entre la potestad del trabajador y el deber del patrón de conceder en la ventana. | abierta | abogado laboralista |

## 5. Instrucciones de auditoría (cuerpo del SKILL.md)

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
7. **Generar el reporte** con el formato de la sección 6.

### 5.1 Árbol de decisión de severidad

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

**Checklist de consistencia (requisito 5 del brief):** RD-01 = Crítico en
tabla y árbol ✓ · RD-02/04/05/07 = Alto ✓ · RD-03/06 = Medio ✓ · casos
alineados ✓.

## 6. Formato de salida

La plantilla de reporte de la librería, con encabezado:
`AUDITORÍA DE COMPLIANCE — Vacaciones (Arts. 76–81 LFT)` y una sección
adicional fija: `TABLA DE ANTIGÜEDAD APLICADA: [días por años de servicio
usados en la auditoría]`.

## 7. Límites de la skill

- No calcula montos de nómina (salario de vacaciones ni prima en pesos):
  clasifica, etiqueta y valida derechos en días y porcentajes.
- No resuelve el efecto de las vacaciones en otros cómputos (CL-02): lo
  reporta.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si se reforma el
  capítulo de vacaciones.

## 8. Estructura de archivos

```
skills/vacaciones/
  SKILL.md                 <- frontmatter + secciones 3, 5, 6, 7 de esta spec
  references/
    texto-legal.md         <- sección 2 (F-01 a F-06, con doc y página)
    reglas.md              <- sección 4 (RD-01 a RD-07 + CL-01 a CL-04)
  assets/
    (sin plantilla propia: reutiliza la plantilla de reporte de la librería)
```

### 8.1 Frontmatter del SKILL.md

```yaml
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
```

## 9. Casos de prueba

| # | Entrada | Debe detectar | Severidad esperada |
|---|---------|---------------|--------------------|
| 1 | Sistema que otorga 6 días el primer año (tabla anterior a 2023) | Falla RD-01: mínimo legal 12 días desde el primer año cumplido | CRÍTICO |
| 2 | Trabajador con 7 años de servicio al que el sistema da 20 días | Falla RD-01: por la tabla derivada le corresponden 22 (bloque 6–10); anotar CL-01 | CRÍTICO |
| 3 | Sistema que solo permite tomar vacaciones en bloques máximos de 5 días | Falla RD-02: debe existir la opción de 12 días continuos a potestad del trabajador | ALTO |
| 4 | Aniversario + 7 meses con saldo íntegro y sin ninguna alerta | Falla RD-05: ventana de 6 meses vencida sin detección | ALTO |
| 5 | Sistema que ofrece "pagar" al trabajador los días no tomados en su aniversario, siguiendo la relación activa | Falla RD-03: las vacaciones no se compensan con remuneración durante la relación | MEDIO |
| 6 | Sistema con tabla 2023 correcta, 12 continuos disponibles, alertas de vencimiento, prima etiquetada, constancia anual y vacaciones como ausencia justificada | Ninguna falla firme; solo INFORMATIVO por CL abiertos | CUMPLE |

## 10. Kickoff prompt (para la fase 2)

> Construye la skill `vacaciones` en el repo klokk-skills-leyes a partir de
> `specs/vacaciones-spec.md`. Sigue EXACTAMENTE la estructura de la sección
> 8. No inventes contenido legal: usa solo lo que está en la spec. Corre los
> 6 casos de prueba y reporta. Cierra el loop según CLAUDE.md.

---

## Estado del research

Citas de los Arts. 76–81 transcritas por Claude el 2026-07-07 directamente
del PDF oficial de la LFT consolidada (D1, descargado de diputados.gob.mx esa
fecha; portada: "Última Reforma DOF 14-05-2026"), p. 24 — Capítulo IV
"Vacaciones", con la reforma "vacaciones dignas" (DOF 27-12-2022) reflejada
en los Arts. 76 y 78. La tabla de RD-01 es DERIVADA del texto (los años 1–5
son literales; los bloques quinquenales son la lectura operativa estándar,
marcada FIRME* con CL-01). No se citaron criterios de memoria.

**Pendiente para la revisión en bloque de JP:** contrastar F-01 a F-06 contra
la p. 24 del PDF oficial.
**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — en especial CL-01
(cortes de bloque, afecta saldos de todos) y CL-04 (potestad vs ventana).
