# Guía de auditoría — módulo horas-extra (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 65-68; Transitorios Primero y Cuarto del decreto DOF 2026-05-01 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14) + decreto DOF 2026-05-01 |

## Qué hace este módulo / Por qué importa / Cuándo se activa / Frontera

**Qué hace:** clasifica cada hora trabajada más allá de la jornada ordinaria
en su régimen legal correcto (extraordinaria dentro del tope +100 %,
excedente del tope +200 %, o trabajo por siniestro con pago ordinario),
valida los topes semanales del año (calendario 9/9/10/11/12) y la
distribución permitida, y audita que el sistema auditado los aplique bien.

**Por qué importa:** las horas extra son el cálculo más sensible en dinero de
un sistema de asistencia o nómina — el pago cambia de +0 % a +100 % o +200 %
según la clasificación. Un tope mal configurado o un porcentaje mal aplicado
se traduce directo en nómina incorrecta y en pérdida de defensa en juicio
(la correlación horas-pagos es RD-09 del módulo registro-jornada (lft)).

**Cuándo se activa:** al clasificar tiempo extraordinario, calcular
porcentajes de pago de horas extra, configurar topes semanales, o auditar el
módulo de horas extra de un sistema de asistencia o nómina.

**Frontera con `jornada-laboral`:** aquel módulo define CUÁNDO el tiempo deja
de ser ordinario (sus límites diario/semanal, RD-05 del módulo jornada-laboral
(lft)); éste define qué pasa con ese tiempo DESPUÉS: régimen, topes y
porcentajes. Comparten el techo absoluto de 12 horas diarias (Art. 68,
párrafo tercero).

## Capa interpretativa

Sin criterios nuevos citados de memoria. Dos referencias ya existentes en la
librería (origen: deep research verificado de JP, en guia-auditoria.md del
módulo `registro-jornada` de esta misma skill):

- **Carga de la prueba y presunción:** si el patrón no puede probar la
  jornada, el tribunal presume ciertos los hechos del trabajador "hasta 9
  horas extra semanales" (criterio de la Segunda Sala de la SCJN, citado en
  esa referencia). Con los topes nuevos del Transitorio Cuarto, si esa
  presunción se ajusta al tope del año es pregunta abierta → CL-04.
- **Correlación horas-pagos (RD-09 del módulo registro-jornada (lft)):** las
  horas extra registradas deben explicar los pagos de nómina; por eso este
  módulo exige que cada hora quede etiquetada con su régimen (RD-08).

Lectura operativa que fundamenta reglas: la ley distingue DOS regímenes de
prolongación con pagos distintos — el extraordinario común (F-02: +100 %,
con tope y distribución) y el trabajo por siniestro/riesgo inminente
(F-01 + F-03: pago ordinario, "tiempo estrictamente indispensable", sin
tope numérico propio). Un sistema que los mezcla paga mal o audita mal.

## Aplicabilidad (F1)

Señales de que este módulo APLICA al repo auditado:

**Positivas** — el repo contiene alguna de estas superficies:
- Tablas o modelos con nombres como `overtime`, `horas_extra`, `extra_hours`,
  `time_entries`, `payroll_concepts`, `nomina_conceptos`.
- Campos como `overtime_type`, `overtime_hours`, `overtime_rate`,
  `tipo_extra`, `regimen_extra`, `pago_porcentaje`.
- Lógica que compara horas trabajadas contra un tope semanal y aplica
  porcentajes de pago diferenciados (+100 %, +200 %).
- Configuraciones o constantes con topes semanales de horas extra (9, 10, 11,
  12 o "overtime_weekly_limit").
- Jobs o endpoints que calculan nómina de horas extra, clasifican régimen o
  exportan conceptos de tiempo extraordinario.
- Greps sugeridos: `grep -ri "overtime\|horas_extra\|extra_hours\|overtime_limit"`,
  `grep -ri "100\|200\|siniestro\|riesgo_inminente"`.

**Negativas** — el módulo es N/A si:
- El repo no gestiona tiempo trabajado ni nómina de personas.
- No existe lógica de clasificación o pago de tiempo extraordinario.
- Grep de los términos anteriores da cero coincidencias relevantes.

## Superficies a revisar (F2)

Dónde buscar cada RD en un repo típico:

| RD | Dónde buscar en el código |
|----|--------------------------|
| RD-01 | Punto de entrada del módulo: ¿recibe candidatos desde jornada-laboral o redefine el umbral internamente? |
| RD-02 | Constante o config del tope semanal de horas extra; si es hardcoded o parametrizable por año. |
| RD-03 | Validaciones de distribución (4h/día, 4 días máx); lógica de distribución semanal del extraordinario. |
| RD-04 | Cálculo del pago +100 %; fórmula o factor aplicado a la hora ordinaria. |
| RD-05 | Lógica del excedente del tope; pago +200 % y límite de 4h adicionales; CL-03 si hay duda sobre la base. |
| RD-06 | Validación del techo absoluto de 12h; suma ordinaria + extraordinaria por día. |
| RD-07 | Tabla o campo para registrar siniestro/riesgo inminente; separación del régimen de pago ordinario. |
| RD-08 | Etiquetado de régimen por hora; exportabilidad para nómina; campo exportable con tipo de hora. |

## Guía de auditoría del módulo

1. **Recibir los candidatos a extraordinario** desde `jornada-laboral`
   (excedentes de límites diario/semanal ordinarios) — RD-01; verificar que
   el código no redefine internamente el umbral.
2. **Determinar el año auditado** y cargar el tope semanal vigente (RD-02);
   verificar si el valor está hardcoded o se obtiene dinámicamente.
3. **Separar el trabajo por siniestro** (RD-07): verificar si el código
   registra este régimen aparte y aplica pago ordinario.
4. **Clasificar cada hora extraordinaria común:** dentro del tope semanal del
   año → verificar régimen +100 % (RD-04); por encima del tope → verificar
   excedente, máximo 4 horas por semana, régimen +200 % (RD-05), anotando
   CL-03.
5. **Validar la distribución** del extraordinario: hasta 4 h/día y máximo 4
   días por semana (RD-03), anotando CL-02 en años de transición.
6. **Verificar el techo absoluto** de 12 horas por día sumando ordinaria +
   extraordinaria (RD-06).
7. **Auditar el etiquetado por régimen** y su exportabilidad para nómina
   (RD-08).
8. **Generar el reporte** con el formato de
   `../../../../plantillas/plantilla-reporte.md`, marcando los CL abiertos
   que apliquen.

## Secciones fijas del reporte de este módulo

El reporte de auditoría incluye, además de las secciones estándar de la
plantilla, la siguiente sección fija:

```
TOPES APLICADOS ESTE AÑO: [tope semanal del año + distribución vigente]
```

Encabezado del reporte:

```
AUDITORÍA DE COMPLIANCE — Tiempo extraordinario (Arts. 65–68 LFT)
```

## Límites del módulo

- No calcula montos de nómina: clasifica horas y valida porcentajes y topes;
  el cálculo monetario (salario base, integraciones) es del sistema de nómina.
- No redefine cuándo el tiempo deja de ser ordinario — eso es del módulo
  `jornada-laboral`.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando cambie el año de calendario (tope nuevo), cuando el
  abogado resuelva CL-01–CL-04, o si la STPS publica disposiciones que
  toquen el registro del tiempo extraordinario.

## Procedencia y estado

Citas de los Arts. 65–68 transcritas el 2026-07-07 del PDF oficial de la LFT
consolidada (diputados.gob.mx, portada: "Última Reforma DOF 14-05-2026"),
p. 22, y Transitorios Primero y Cuarto del decreto oficial
(`LFT_ref52_01may26.pdf`, DOF 1-may-2026 edición vespertina), pp. 3–4. Los
textos del decreto y de la consolidada coinciden entre sí en los artículos
reformados. La capa interpretativa solo referencia criterios ya presentes en
la librería; no se citaron criterios nuevos de memoria. Spec de origen:
`specs/horas-extra-spec.md`, aprobada por JP el 2026-07-07.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME* —
en especial CL-03 (base del tope de +4h en transición), que impacta dinero.
Cuando el abogado los resuelva o cambie el año de calendario, esta skill se
revisa y sube su `version` y `reviewed_at`.
