# Spec: skill `dias-de-descanso`

> 🔍 **BORRADOR — PENDIENTE DE VISTO BUENO DE JP.** Producida en fase 1 del
> pipeline (ver BACKLOG.md) el 2026-07-07. Citas transcritas por Claude
> directamente del PDF oficial descargado esa fecha (detalle en "Estado del
> research"). No construir la skill hasta aprobar esta spec contra el PDF
> oficial.

## 1. Resumen ejecutivo

**Qué hace:** audita el descanso semanal: que exista al menos un día de
descanso pagado por cada seis trabajados, que los domingos laborados generen
prima dominical (+25 %), que los descansos trabajados se paguen doble además
del salario del descanso, y que las semanas incompletas acrediten su parte
proporcional.

**Por qué importa:** para un checador, las rachas de días trabajados sin
descanso y los descansos trabajados sin pago correcto son de los
incumplimientos más frecuentes y más caros de una PyME — y los más fáciles
de detectar con un registro de asistencia bien llevado. Es dinero directo
(prima 25 %, pago doble) y exposición en juicio.

**Cuándo se activa:** al auditar patrones de descanso semanal, detectar
rachas de trabajo continuo, calcular prima dominical, o revisar el pago de
descansos trabajados.

**Frontera con `dias-festivos`:** esta skill cubre el descanso SEMANAL
(Arts. 69–73). Los días de descanso obligatorio del calendario (Arts. 74–75:
festivos y su pago) son de la skill `dias-festivos`.

## 2. Fuente legal — texto exacto verificado

**Documento oficial usado (descargado el 2026-07-07, el mismo D1 de las specs
anteriores):**

| Doc | Qué es | URL | Uso |
|-----|--------|-----|-----|
| D1 | LFT consolidada vigente, Cámara de Diputados — portada indica "Última Reforma DOF 14-05-2026" | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf | Texto vigente de los Arts. 69–73, Capítulo III "Días de descanso" (p. 23 del PDF) |

### 2.1 Artículos vigentes (D1, p. 23)

| ID | Artículo | Última reforma anotada en la consolidada |
|----|----------|------------------------------------------|
| F-01 | Art. 69 | Artículo reformado DOF 01-05-2026 |
| F-02 | Art. 70 | Sin anotación de reforma |
| F-03 | Art. 71 | Párrafo segundo reformado DOF 01-05-2026 |
| F-04 | Art. 72 | Sin anotación de reforma |
| F-05 | Art. 73 | Sin anotación de reforma |

**F-01 — Art. 69 (D1, p. 23):**

> "Por cada seis días de trabajo se deberá otorgar, por lo menos, un día de
> descanso con goce de salario íntegro."

**F-02 — Art. 70 (D1, p. 23):**

> "En los trabajos que requieran una labor continua, los trabajadores y el
> patrón fijarán de común acuerdo los días en que los trabajadores deban
> disfrutar de los de descanso semanal."

**F-03 — Art. 71 (D1, p. 23):**

> "En los reglamentos de esta Ley se procurará que el día de descanso semanal
> sea el domingo.
> Las personas que laboren en domingo tendrán derecho a una prima adicional
> de un veinticinco por ciento, por lo menos, sobre el salario de los días
> ordinarios de trabajo."

**F-04 — Art. 72 (D1, p. 23):**

> "Cuando el trabajador no preste sus servicios durante todos los días de
> trabajo de la semana, o cuando en el mismo día o en la misma semana preste
> sus servicios a varios patrones, tendrá derecho a que se le pague la parte
> proporcional del salario de los días de descanso, calculada sobre el
> salario de los días en que hubiese trabajado o sobre el que hubiese
> percibido de cada patrón."

**F-05 — Art. 73 (D1, p. 23):**

> "Los trabajadores no están obligados a prestar servicios en sus días de
> descanso. Si se quebranta esta disposición, el patrón pagará al trabajador,
> independientemente del salario que le corresponda por el descanso, un
> salario doble por el servicio prestado."

## 3. Capa interpretativa

Sin criterios jurisprudenciales citados de memoria; si el abogado (fase 3)
aporta criterios sobre descanso semanal o prima dominical, se agregan con su
fuente. Lecturas operativas desde el propio texto:

- **El piso legal es 1 descanso por cada 6 trabajados (F-01).** "Por lo
  menos" admite más días de descanso (con la transición a 40 horas muchas
  empresas operarán semanas de 5 días); la skill audita el PISO legal, no la
  política interna de la empresa.
- **La prima dominical es por laborar en domingo (F-03).** El texto vigente
  dice "las personas que laboren en domingo" — la marca debe ponerse en toda
  jornada dominical; cómo se acumula con el pago doble del descanso trabajado
  queda abierto (CL-02).
- **El descanso trabajado se paga doble ADEMÁS del salario del descanso
  (F-05).** El sistema debe distinguir el salario del día de descanso (que ya
  se debe) del doble por el servicio prestado — son conceptos separados en el
  texto.

## 4. Reglas derivadas

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Por cada seis días de trabajo debe existir al menos un día de descanso con goce de salario íntegro. El sistema debe detectar rachas de 7+ días trabajados consecutivos sin descanso. El método de cómputo (semana calendario vs ventana móvil) está abierto → CL-01. | Crítico | FIRME* | F-01; ver CL-01 |
| RD-02 | El descanso semanal se procura en domingo; en labor continua, los días de descanso se fijan de común acuerdo. El sistema debe registrar el día (o días) de descanso pactado de cada trabajador — sin ese dato no puede auditarse F-05. | Medio | FIRME | F-02, F-03 |
| RD-03 | Toda jornada laborada en domingo genera prima adicional de al menos +25 % sobre el salario de los días ordinarios; el sistema debe marcarla para nómina. | Alto | FIRME | F-03 |
| RD-04 | Trabajar el día de descanso no es obligatorio; si ocurre, el patrón paga salario doble por el servicio, además del salario que ya corresponde por el descanso. El sistema debe detectar todo descanso trabajado y marcar ambos conceptos. | Crítico | FIRME | F-05 |
| RD-05 | Semana incompleta o varios patrones: se acredita la parte proporcional del salario de los días de descanso, calculada sobre los días trabajados. La base con salario variable → CL-03. | Medio | FIRME | F-04; ver CL-03 |
| RD-06 | Cada domingo laborado y cada descanso trabajado deben quedar etiquetados de forma exportable, para que la nómina pague bien y la correlación horas-pagos sea verificable (R9 de registro-jornada). | Alto | FIRME* | F-03, F-05; interpretación operativa de la correlación |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

### 4.1 Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿El "por cada seis días de trabajo" se computa por semana calendario o por ventana móvil de días consecutivos? (P. ej.: 8 días seguidos repartidos entre dos semanas calendario, cada una con ≤ 6 trabajados.) | El texto no define el periodo de cómputo; para un checador cambia qué rachas disparan alerta. | abierta | abogado laboralista |
| CL-02 | Cuando el día de descanso del trabajador ES domingo y lo labora, ¿se acumulan la prima dominical (+25 %) y el pago doble del Art. 73? | Son artículos distintos con supuestos que se traslapan; el texto no dice si se suman. | abierta | abogado laboralista |
| CL-03 | ¿Cómo se calcula el "salario íntegro" del descanso y su proporcional con salario variable o por hora? | F-04 da la proporcionalidad por días, pero no la base para salarios variables. | abierta | abogado laboralista |
| CL-04 | Con la transición a 40 horas (semanas de 5 días), ¿el segundo día no trabajado es "descanso" con las protecciones del Art. 73 (pago doble si se labora) o día no laborable contractual? | La reforma redujo horas semanales sin tocar el esquema 6:1 del Art. 69; la naturaleza del día extra no está definida. | abierta | abogado laboralista |

## 5. Instrucciones de auditoría (cuerpo del SKILL.md)

1. **Cargar el patrón de descansos** pactado por trabajador (RD-02); si el
   sistema no lo registra, es hallazgo inmediato (no se puede auditar F-05
   sin saber qué día es descanso).
2. **Barrer rachas de días trabajados** consecutivos; alertar 7 o más sin
   descanso (RD-01), anotando CL-01 sobre el método de cómputo.
3. **Marcar domingos laborados** → prima +25 % para nómina (RD-03); si el
   domingo era además el descanso del trabajador, aplicar también el paso 4 y
   anotar CL-02.
4. **Detectar descansos trabajados** → verificar pago doble además del
   salario del descanso, como conceptos separados (RD-04).
5. **Calcular proporcionales** de semana incompleta o multi-patrón (RD-05),
   anotando CL-03 si el salario es variable.
6. **Auditar el etiquetado exportable** de domingos y descansos trabajados
   (RD-06).
7. **Generar el reporte** con el formato de la sección 6, marcando los CL
   abiertos que apliquen (incluido CL-04 si la empresa opera semana de 5
   días).

### 5.1 Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Deja rachas sin descanso o descansos trabajados sin detectar/pagar?
  (RD-01, RD-04)
     SÍ  -> CRÍTICO  (incumplimiento directo y caro, por trabajador)
     NO  -> siguiente pregunta

  ¿Deja dinero dominical sin marcar o sin exportar? (RD-03, RD-06)
     SÍ  -> ALTO  (nómina incompleta; correlación horas-pagos rota)
     NO  -> siguiente pregunta

  ¿Es registro de patrón de descansos o proporcionales incompletos?
  (RD-02, RD-05)
     SÍ  -> MEDIO

  CL-01 a CL-04 y lo pendiente de autoridad -> INFORMATIVO
```

**Checklist de consistencia (requisito 5 del brief):** RD-01/04 = Crítico en
tabla y árbol ✓ · RD-03/06 = Alto en tabla y árbol ✓ · RD-02/05 = Medio en
tabla y árbol ✓ · casos de prueba abajo alineados ✓.

## 6. Formato de salida

La plantilla de reporte de la librería
(`skills/registro-jornada/assets/plantilla-reporte.md`), con encabezado:
`AUDITORÍA DE COMPLIANCE — Días de descanso (Arts. 69–73 LFT)` y una sección
adicional fija: `PATRÓN DE DESCANSOS AUDITADO: [día(s) de descanso pactados
por trabajador o grupo]`.

## 7. Límites de la skill

- No cubre los días de descanso obligatorio del calendario (festivos,
  Arts. 74–75) — eso es de `dias-festivos`.
- No calcula montos de nómina: marca, clasifica y verifica conceptos; el
  cálculo monetario es del sistema de nómina.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si la transición a 40
  horas genera criterios o reglamentos nuevos sobre el descanso semanal.

## 8. Estructura de archivos

```
skills/dias-de-descanso/
  SKILL.md                 <- frontmatter + secciones 3, 5, 6, 7 de esta spec
  references/
    texto-legal.md         <- sección 2 (F-01 a F-05, con doc y página)
    reglas.md              <- sección 4 (RD-01 a RD-06 + CL-01 a CL-04)
  assets/
    (sin plantilla propia: reutiliza la plantilla de reporte de la librería)
```

### 8.1 Frontmatter del SKILL.md

```yaml
---
name: dias-de-descanso
description: Audita el descanso semanal de la LFT mexicana; al menos un día pagado por cada seis trabajados, prima dominical (+25 %), pago doble del descanso trabajado y proporcionales de semana incompleta. Usar al auditar patrones de descanso, detectar rachas de trabajo continuo o revisar pagos de domingos y descansos laborados.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Arts. 69-73"
  fuente: "LFT consolidada (última reforma DOF 2026-05-14), Capítulo III, p. 23"
---
```

## 9. Casos de prueba

| # | Entrada | Debe detectar | Severidad esperada |
|---|---------|---------------|--------------------|
| 1 | Trabajador con 8 días consecutivos laborados repartidos entre dos semanas calendario; el sistema no alerta porque "cada semana tuvo ≤ 6 días" | Racha de 7+ días sin descanso (RD-01); anotar CL-01 sobre el método de cómputo | CRÍTICO |
| 2 | Empleado labora su día de descanso y el sistema paga solo salario normal | Falla RD-04: corresponde salario doble por el servicio, además del salario del descanso | CRÍTICO |
| 3 | Empleado con descanso en martes labora un domingo y el sistema no marca nada | Falla RD-03: prima dominical +25 % sin marcar para nómina | ALTO |
| 4 | Empleado trabajó 3 días de la semana; el sistema no acredita la parte proporcional del descanso | Falla RD-05: proporcional del Art. 72 sin calcular | MEDIO |
| 5 | Sistema que registra el día de descanso pactado, detecta rachas por ventana móvil, marca domingos con prima y descansos trabajados con doble, calcula proporcionales y exporta etiquetas | Ninguna falla firme; solo INFORMATIVO por CL abiertos | CUMPLE |
| 6 | Trabajador cuyo descanso ES domingo lo labora; el sistema aplica el pago doble pero no evalúa la prima | RD-04 cumplida (doble presente); la acumulación con la prima es CL-02 → se reporta como pregunta abierta, no como hallazgo firme | INFORMATIVO (CL-02) |

## 10. Kickoff prompt (para la fase 2)

> Construye la skill `dias-de-descanso` en el repo klokk-skills-leyes a
> partir de `specs/dias-de-descanso-spec.md` (ya aprobada por JP). Sigue
> EXACTAMENTE la estructura de la sección 8. No inventes contenido legal:
> usa solo lo que está en la spec. Al terminar, corre mentalmente los 6
> casos de prueba de la sección 9 y reporta si cada uno da lo esperado.
> Cierra el loop de fase 2 según CLAUDE.md: checklist, STATUS, BITACORA,
> commits ordenados y push.

---

## Estado del research

Citas de los Arts. 69–73 transcritas por Claude el 2026-07-07 directamente
del PDF oficial de la LFT consolidada (D1, descargado de diputados.gob.mx esa
fecha; portada: "Última Reforma DOF 14-05-2026"), p. 23 — Capítulo III "Días
de descanso". Los Arts. 74–75 (descansos obligatorios del calendario) se
excluyeron deliberadamente: pertenecen a la skill `dias-festivos`. No se
citaron criterios jurisprudenciales de memoria; la capa interpretativa se
limita a lecturas del propio texto.

**Pendiente para el visto bueno de JP (gate de fase 1):** contrastar F-01 a
F-05 contra la p. 23 del PDF oficial.
**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME* —
en especial CL-01 (método de cómputo de rachas) y CL-04 (naturaleza del
segundo día libre en semanas de 5 días), que definen la lógica central del
checador.
