# Guía de auditoría — módulo dias-de-descanso (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 69-73 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), Capítulo III, p. 23 |

## Qué hace este módulo / Por qué importa / Cuándo se activa / Frontera

**Qué hace:** audita el descanso semanal: que exista al menos un día de
descanso pagado por cada seis trabajados, que los domingos laborados generen
prima dominical (+25 %), que los descansos trabajados se paguen doble además
del salario del descanso, y que las semanas incompletas acrediten su parte
proporcional.

**Por qué importa:** las rachas de días trabajados sin descanso y los descansos
trabajados sin pago correcto son de los incumplimientos más frecuentes y más
caros en un sistema de asistencia — y los más fáciles de detectar con un
registro bien llevado. Es dinero directo (prima 25 %, pago doble) y exposición
en juicio.

**Cuándo se activa:** al auditar patrones de descanso semanal, detectar rachas
de trabajo continuo, calcular prima dominical, o revisar el pago de descansos
trabajados en el código del sistema auditado.

**Frontera con `dias-festivos`:** este módulo cubre el descanso SEMANAL
(Arts. 69–73). Los días de descanso obligatorio del calendario (Arts. 74–75:
festivos y su pago) son del módulo `dias-festivos`.

## Capa interpretativa

Sin criterios jurisprudenciales citados de memoria; si el abogado (fase 3)
aporta criterios sobre descanso semanal o prima dominical, se agregan con su
fuente. Lecturas operativas desde el propio texto:

- **El piso legal es 1 descanso por cada 6 trabajados (F-01).** "Por lo
  menos" admite más días de descanso (con la transición a 40 horas muchas
  empresas operarán semanas de 5 días); el módulo audita el PISO legal, no
  la política interna de la empresa.
- **La prima dominical es por laborar en domingo (F-03).** El texto vigente
  dice "las personas que laboren en domingo" — la marca debe ponerse en toda
  jornada dominical; cómo se acumula con el pago doble del descanso trabajado
  queda abierto (CL-02).
- **El descanso trabajado se paga doble ADEMÁS del salario del descanso
  (F-05).** El sistema debe distinguir el salario del día de descanso (que ya
  se debe) del doble por el servicio prestado — son conceptos separados en el
  texto.

## Aplicabilidad (F1)

Señales de que este módulo APLICA al repo auditado:

**Positivas** — el repo contiene alguna de estas superficies:
- Tablas o modelos con nombres como `attendance`, `asistencia`, `work_days`,
  `dias_trabajados`, `rest_days`, `descanso`, `schedules`, `turnos`.
- Campos como `is_rest_day`, `dia_descanso`, `worked_on_rest`, `is_sunday`,
  `prima_dominical`, `descanso_trabajado`.
- Lógica que cuenta días trabajados consecutivos, detecta domingos laborados
  o identifica descansos trabajados.
- Jobs o endpoints que calculan o exportan conceptos de nómina dominical o de
  descanso trabajado.
- Configuraciones que registran el patrón de descanso pactado por trabajador
  o grupo.
- Greps sugeridos: `grep -ri "rest_day\|descanso\|sunday\|domingo\|prima_dominical"`,
  `grep -ri "consecutive\|racha\|worked_rest\|descanso_trabajado"`.

**Negativas** — el módulo es N/A si:
- El repo no gestiona asistencia ni días trabajados de personas.
- No existe lógica de patrones de descanso, domingos ni nómina dominical.
- Grep de los términos anteriores da cero coincidencias relevantes.

## Superficies a revisar (F2)

Dónde buscar cada RD en un repo típico:

| RD | Dónde buscar en el código |
|----|--------------------------|
| RD-01 | Lógica de detección de rachas de días consecutivos trabajados; alertas de 7+ días sin descanso; método de cómputo (calendario vs ventana móvil). |
| RD-02 | Modelos o campos que registren el día de descanso pactado por trabajador; si este dato existe y es accesible para la auditoría. |
| RD-03 | Detección de domingos laborados; cálculo o marcado de prima +25 %; exportación del concepto para nómina. |
| RD-04 | Detección de descansos trabajados; marcado de pago doble como concepto separado del salario del descanso. |
| RD-05 | Cálculo proporcional de descanso para semana incompleta o varios patrones; base de cálculo con salario variable. |
| RD-06 | Etiquetado exportable de domingos laborados y descansos trabajados; campo de tipo de concepto para nómina. |

## Guía de auditoría del módulo

1. **Cargar el patrón de descansos** pactado por trabajador (RD-02); si el
   sistema no lo registra, reportar como hallazgo inmediato (no se puede
   auditar RD-04 sin saber qué día es descanso).
2. **Barrer rachas de días trabajados** consecutivos; verificar si el código
   alerta ante 7 o más sin descanso (RD-01), anotando CL-01 sobre el método
   de cómputo.
3. **Marcar domingos laborados** → verificar que el código genera prima +25 %
   para nómina (RD-03); si el domingo era además el descanso del trabajador,
   aplicar también el paso 4 y anotar CL-02.
4. **Detectar descansos trabajados** → verificar que el código detecta pago
   doble además del salario del descanso, como conceptos separados (RD-04).
5. **Calcular proporcionales** de semana incompleta o multi-patrón (RD-05),
   anotando CL-03 si el salario es variable.
6. **Auditar el etiquetado exportable** de domingos y descansos trabajados
   (RD-06).
7. **Generar el reporte** con el formato de
   `../../../../plantillas/plantilla-reporte.md`, marcando los CL abiertos
   que apliquen (incluido CL-04 si la empresa opera semana de 5 días).

## Secciones fijas del reporte de este módulo

El reporte de auditoría incluye, además de las secciones estándar de la
plantilla, la siguiente sección fija:

```
PATRÓN DE DESCANSOS AUDITADO: [día(s) de descanso pactados por trabajador o grupo]
```

Encabezado del reporte:

```
AUDITORÍA DE COMPLIANCE — Días de descanso (Arts. 69–73 LFT)
```

## Límites del módulo

- No cubre los días de descanso obligatorio del calendario (festivos,
  Arts. 74–75) — eso es del módulo `dias-festivos`.
- No calcula montos de nómina: marca, clasifica y verifica conceptos; el
  cálculo monetario es del sistema de nómina.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si la transición a 40
  horas genera criterios o reglamentos nuevos sobre el descanso semanal.

## Procedencia y estado

Citas de los Arts. 69–73 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), p. 23 — Capítulo III "Días de descanso". Los Arts. 74–75 se
excluyeron deliberadamente: pertenecen al módulo `dias-festivos`. No se
citaron criterios jurisprudenciales de memoria. Spec de origen:
`specs/dias-de-descanso-spec.md`, aprobada por JP el 2026-07-07.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME* —
en especial CL-01 (método de cómputo de rachas) y CL-04 (naturaleza del
segundo día libre en semanas de 5 días). Cuando se resuelvan, esta skill se
revisa y sube su `version` y `reviewed_at`.
