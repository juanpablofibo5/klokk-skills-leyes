# Guía de auditoría — módulo vacaciones (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 76-81 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), Capítulo IV, p. 24 |

## Qué hace este módulo

Calcula los días de vacaciones que corresponden por antigüedad (régimen
"vacaciones dignas", reforma DOF 27-12-2022), audita la ventana legal de
disfrute (6 meses tras el aniversario), el mínimo de 12 días continuos a
potestad del trabajador, la prima vacacional (≥25 %) y la constancia anual —
y verifica que el sistema auditado registre las vacaciones como ausencia
justificada.

## Por qué importa

Para un sistema de asistencia, las vacaciones son la ausencia justificada más
frecuente; si se calculan con la tabla anterior a 2023 (6 días el primer año)
o se dejan vencer sin alerta, el software incumple de forma masiva y
silenciosa.

## Cuándo se activa

Al calcular saldos de vacaciones, auditar su registro en el sistema auditado,
validar la prima vacacional o revisar constancias de antigüedad.

## Fronteras

El pago/monto exacto es de nómina (fuera de alcance, D-08); la interacción
de los días de vacaciones con las rachas de descanso semanal es del módulo
dias-de-descanso (lft) — aquí solo se marca la ausencia como justificada.

---

## Aplicabilidad (F1)

### Señales POSITIVAS — el módulo aplica

- El repo tiene modelos de empleado con campo de antigüedad o fecha de ingreso
  (tablas como `employees`, `trabajadores`, `staff`; campos como
  `hire_date`, `fecha_ingreso`, `start_date`).
- Existe lógica de cálculo de saldo de vacaciones o acumulación de días
  (tablas como `vacation_balances`, `leave_balances`, `saldo_vacaciones`;
  endpoints como `/vacations/balance`, `/leave/entitlement`).
- Hay registro de ausencias o solicitudes de vacaciones (tablas como
  `absences`, `leave_requests`, `time_off`; campos como `leave_type`,
  `vacation_days`).
- Greps sugeridos:
  ```
  grep -ri "vacation\|vacacion\|leave.balance\|saldo.vacac" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "hire_date\|fecha_ingreso\|antiguedad\|years_of_service" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "prima.vacac\|vacation.premium\|25.*percent\|25.*por.ciento" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "6.meses\|six.months\|expir\|venc" --include="*.{py,ts,js,rb,go,sql}"
  ```

### Señales NEGATIVAS — el módulo probablemente N/A

- El repo no gestiona empleados ni tiempo de trabajo.
- La gestión de vacaciones es completamente externa (HRIS integrado) y el
  repo no almacena ni valida saldos ni fechas.

### Superficies a revisar (F2)

| RD | Dónde buscar en el repo |
|----|------------------------|
| RD-01 | Función/método de cálculo de días por antigüedad; constantes o tablas de configuración con los días por año; seeds o fixtures de la tabla |
| RD-02 | Lógica de distribución de periodo vacacional; validación de 12 días continuos mínimos; campo de potestad del trabajador |
| RD-03 | Cualquier lógica de compensación en dinero de saldo durante la relación activa |
| RD-04 | Cálculo y etiquetado de prima vacacional (≥25 %); integración con nómina |
| RD-05 | Alertas de vencimiento (aniversario + 6 meses); generación de constancia anual |
| RD-06 | Tratamiento de trabajadores discontinuos o de temporada: cálculo proporcional |
| RD-07 | Etiquetado de días de vacaciones como ausencia justificada en el sistema; campos exportables de tipo de ausencia |

---

## Capa interpretativa

Sin criterios jurisprudenciales citados de memoria. Lecturas operativas:

- **La tabla de días por antigüedad se DERIVA del texto de F-01** y su
  segmento quinquenal es la lectura operativa estándar del "a partir del
  sexto año… dos días por cada cinco de servicios". Los cortes exactos de
  los bloques tienen debate conocido → CL-01; la tabla de RD-01 se marca
  FIRME* por eso.
- **Los 12 días continuos son potestad del trabajador (F-03):** el sistema
  auditado no puede forzar fraccionamientos; la distribución la decide la
  persona trabajadora.
- **Las vacaciones no se "pagan en lugar de tomarse" (F-04):** un saldo
  vencido no se liquida con dinero durante la relación; la única
  remuneración proporcional es al terminar la relación.

---

## Guía de auditoría del módulo

1. **Calcular el saldo por antigüedad** de cada trabajador con la tabla de
   RD-01 (años CUMPLIDOS de servicio), anotando CL-01. Buscar en el código
   la función de cálculo y comparar contra la tabla.
2. **Validar la configuración del sistema** contra esa tabla — detectar en el
   código tablas pre-2023 (6/8/10… días) como falla inmediata.
3. **Auditar la distribución en el código:** debe existir la opción de 12
   días continuos y el registro de la distribución elegida por el trabajador
   (RD-02).
4. **Auditar la ventana de disfrute en el código:** alertas de saldo próximo
   a vencer y vencido (aniversario + 6 meses), y constancia anual emitida
   (RD-05).
5. **Verificar el etiquetado en el código:** vacaciones como ausencia
   justificada exportable (RD-07, anotar CL-02) y prima vacacional marcada
   para nómina (RD-04, anotar CL-03 si salario variable).
6. **Verificar que no haya compensación en dinero** de saldos durante la
   relación en el código (RD-03); proporcionales solo al terminar la relación
   o para discontinuos/temporada (RD-06).
7. **Generar el reporte** usando la plantilla canónica:
   `../../../../plantillas/plantilla-reporte.md`.

---

## Secciones fijas del reporte de este módulo

El encabezado del reporte es:

```
AUDITORÍA DE COMPLIANCE — Vacaciones (Arts. 76–81 LFT)
```

Sección fija adicional en el reporte:

```
TABLA DE ANTIGÜEDAD APLICADA: [días por años de servicio usados en la auditoría]
```

---

## Límites del módulo

- No calcula montos de nómina (salario de vacaciones ni prima en pesos):
  clasifica, etiqueta y valida derechos en días y porcentajes.
- No resuelve el efecto de las vacaciones en otros cómputos (CL-02): lo
  reporta.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si se reforma el
  capítulo de vacaciones.

---

## Procedencia y estado

Citas de los Arts. 76–81 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), p. 24 — Capítulo IV "Vacaciones", con la reforma "vacaciones
dignas" (DOF 27-12-2022) en los Arts. 76 y 78. La tabla de RD-01 es DERIVADA
del texto: los años 1–5 son literales; los bloques quinquenales son lectura
operativa estándar (FIRME* + CL-01). Spec de origen:
`specs/vacaciones-spec.md`, construida en modo batch (D-11) y **aprobada en
bloque por JP el 2026-07-08 (D-14)**.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — en especial CL-01
(cortes de bloque) y CL-04 (potestad del trabajador vs ventana de 6 meses).
Cuando se resuelvan, esta skill se revisa y sube su `version` y `reviewed_at`.
