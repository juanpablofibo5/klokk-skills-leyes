# Guía de auditoría — módulo dias-festivos (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 74-75 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), pp. 23-24 |

## Qué hace este módulo

Genera el calendario de días de descanso obligatorio del año (fijos, de lunes
móvil, sexenal y electoral), audita que los festivos laborados se paguen con
salario doble además del salario del descanso obligatorio, y que la
designación de quién trabaja en festivo quede registrada.

## Por qué importa

Los festivos de lunes móvil (febrero, marzo, noviembre) son un error clásico
de configuración — un sistema que celebra el 5 de febrero en fecha fija aplica
mal el descanso y el pago de ese día para todos los trabajadores. Y el festivo
laborado sin pago doble es incumplimiento directo, por trabajador.

## Cuándo se activa

Al configurar o auditar calendarios laborales, validar el pago de festivos
trabajados, o clasificar jornadas registradas en días de descanso obligatorio.

## Frontera

Este módulo cubre los descansos OBLIGATORIOS del calendario (Arts. 74-75). El
descanso SEMANAL (Arts. 69-73) pertenece al módulo dias-de-descanso (lft).
Cuando un festivo coincide con domingo o con el descanso semanal del
trabajador, los regímenes se traslapan: ver CL-01 y CL-02 de este módulo.

---

## Aplicabilidad (F1)

### Señales POSITIVAS — el módulo aplica

- El repo maneja calendarios laborales (tablas como `holidays`, `public_holidays`,
  `calendar_days`, `festivos`; campos como `is_holiday`, `holiday_type`,
  `mandatory_rest`).
- Existen modelos o endpoints relacionados con nómina/pago de días especiales
  (tablas como `payroll_items`, `day_types`, `jornadas`; campos como
  `double_pay`, `holiday_pay`, `descanso_obligatorio`).
- Hay lógica de turnos o asignación de quién trabaja en días especiales
  (tablas como `shift_assignments`, `trabajadores_festivo`, `holiday_workers`).
- Greps sugeridos:
  ```
  grep -ri "holiday\|festivo\|descanso.obligatorio\|día.de.descanso" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "doble\|double_pay\|holiday_pay" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "lunes.movil\|primer.lunes\|tercer.lunes" --include="*.{py,ts,js,rb,go,sql}"
  ```

### Señales NEGATIVAS — el módulo probablemente N/A

- El repo no tiene ningún modelo de persona trabajadora ni calendario laboral.
- Es una API pura de procesamiento de datos sin lógica de tiempo de trabajo.
- La gestión de calendarios es 100% delegada a un servicio externo y el repo
  no almacena ni valida las fechas festivas.

### Superficies a revisar (F2)

| RD | Dónde buscar en el repo |
|----|------------------------|
| RD-01 | Lógica de generación de calendario: funciones de cómputo de lunes móviles; seeds o fixtures de fechas festivas; constantes de días fijos |
| RD-02 | Cálculo de pago por festivo laborado: modelos de nómina/conceptos de pago; campos de importe doble; tests de cálculo |
| RD-03 | Asignación de turno en festivo: tablas de convenio/asignación; endpoints de confirmación previa al festivo |
| RD-04 | Etiquetado de jornadas en festivo: campos de tipo de jornada exportables; integración con nómina o reportes |
| RD-05 | Fuente de festivos electorales y sexenales: configuración externa; parámetros de año de transmisión; documentación interna |

---

## Capa interpretativa

Sin criterios jurisprudenciales citados de memoria. Lecturas operativas del
propio texto:

- **Tres tipos de festivo (F-01):** de fecha fija (I, IV, V, VIII), de lunes
  móvil (II, III, VI — se celebran el lunes, no la fecha conmemorada),
  sexenal (VII — solo el año de transmisión del Ejecutivo) y electoral (IX —
  depende de las leyes electorales, fuente externa a la LFT).
- **El festivo trabajado se paga doble ADEMÁS del salario del descanso
  (F-02)** — misma estructura de dos conceptos separados que el Art. 73 del
  descanso semanal.
- **Trabajar en festivo es por convenio (F-02):** requiere determinación
  previa de quiénes prestan servicios; el sistema auditado debe poder
  registrarla.

---

## Guía de auditoría del módulo

1. **Generar o validar el calendario del año auditado** con RD-01 (fijos +
   lunes móviles computados + sexenal si aplica + electoral si hay fuente),
   anotando CL-03/CL-04 para las fracciones IX y VII. Buscar en el código
   la lógica de cómputo de lunes móviles y los valores usados.
2. **Cruzar las jornadas registradas contra el calendario en el código:**
   toda jornada en festivo debe marcarse (RD-04). Verificar existencia de
   campos exportables de tipo de jornada.
3. **Verificar la asignación pactada** de quienes trabajan el festivo en el
   código auditado (RD-03): ¿existe flujo de registro de convenio o
   asignación previa?
4. **Verificar el cálculo de pago** en el código: salario doble por el
   servicio + salario del descanso obligatorio como conceptos separados y
   exportables (RD-02).
5. **Detectar traslapes** festivo-domingo (anotar CL-01) y festivo-descanso
   semanal (anotar CL-02); reportarlos como INFORMATIVO.
6. **Verificar fuente de festivos electorales y sexenales** en la
   configuración del sistema auditado (RD-05).
7. **Generar el reporte** usando la plantilla canónica:
   `../../../../plantillas/plantilla-reporte.md`.

---

## Secciones fijas del reporte de este módulo

El encabezado del reporte es:

```
AUDITORÍA DE COMPLIANCE — Días de descanso obligatorio (Arts. 74–75 LFT)
```

Sección fija adicional en el reporte:

```
CALENDARIO DEL AÑO AUDITADO: [festivos computados con su fracción de origen]
```

---

## Límites del módulo

- No cubre el descanso semanal ni la prima dominical — eso es del módulo
  dias-de-descanso (lft).
- No calcula montos de nómina: marca, clasifica y verifica conceptos.
- No determina la fecha electoral ni los años de transmisión: exige que el
  sistema auditado declare su fuente (RD-05) y lo reporta.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa si se reforma el Art. 74 (nuevas fracciones) o cuando el abogado
  resuelva CL-01–CL-04.

---

## Procedencia y estado

Citas de los Arts. 74–75 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), pp. 23–24; la fracc. VII refleja la reforma DOF 30-09-2024.
Spec de origen: `specs/dias-festivos-spec.md`, construida en modo batch
(D-11) y **aprobada en bloque por JP el 2026-07-08 (D-14)**.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — en especial los
concursos de pago doble (CL-01, CL-02). Cuando se resuelvan, esta skill se
revisa y sube su `version` y `reviewed_at`.
