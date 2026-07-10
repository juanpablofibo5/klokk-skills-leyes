# Guía de auditoría — módulo asistencia-y-faltas (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 46, 47 (fracc. X y aviso), 134 fracc. V, 135 fracc. II |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), pp. 15-16 y 39 |

## Qué hace este módulo

Audita la clasificación de ausencias (justificada / injustificada), el
contador de la causal de rescisión por faltas (más de 3 injustificadas en 30
días, Art. 47 fracc. X), el registro de permisos y avisos del trabajador, y
el soporte documental que un despido por faltas exigiría (aviso de rescisión
con fechas exactas).

## Por qué importa

Las faltas son la causal de rescisión más común en PyMEs y la fracción III
del Art. 784 pone su prueba a cargo del patrón. Un sistema auditado que no
distingue falta injustificada de permiso, o que no puede producir las fechas
exactas, deja al cliente sin defensa — o rescindiendo sin causa válida.

## Cuándo se activa

Al clasificar ausencias en el código, configurar alertas de faltas acumuladas,
auditar flujos de permisos, o preparar el soporte de una rescisión por
inasistencias.

## Frontera

Los efectos de las vacaciones (ausencia justificada) son del módulo vacaciones
(lft); la conservación/exhibición del registro es del módulo
conservacion-y-prueba (lft); el "faltar" en remoto cruza con el módulo
teletrabajo (lft).

---

## Aplicabilidad (F1)

### Señales POSITIVAS — el módulo aplica

- El repo tiene modelos de asistencia o registro de presencia (tablas como
  `attendances`, `asistencias`, `time_records`, `checkins`; campos como
  `status`, `absent`, `justificada`, `absence_type`).
- Existe lógica de clasificación de ausencias o alertas de faltas acumuladas
  (tablas como `absences`, `leave_requests`, `faltas`; campos como
  `justified`, `injustificada`, `absence_count`).
- Hay flujo de permisos o autorización de ausencias (tablas como
  `permissions`, `permisos`, `leave_approvals`; campos como `approved_by`,
  `approved_at`, `aviso_trabajador`).
- Greps sugeridos:
  ```
  grep -ri "falta\|absence\|absent\|inasistencia" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "justificad\|injustificad\|permiso\|permission" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "rescision\|termination\|despido\|47.*X\|causal" --include="*.{py,ts,js,rb,go,sql}"
  grep -ri "30.dias\|thirty.days\|absence_count\|contador" --include="*.{py,ts,js,rb,go,sql}"
  ```

### Señales NEGATIVAS — el módulo probablemente N/A

- El repo no gestiona personas trabajadoras ni registros de asistencia.
- Solo es una API de procesamiento sin lógica de presencia/ausencia.

### Superficies a revisar (F2)

| RD | Dónde buscar en el repo |
|----|------------------------|
| RD-01 | Esquema de tipos de ausencia; lógica de clasificación justificada/injustificada; migraciones que definen el campo de tipo |
| RD-02 | Función de contador de faltas en ventana de 30 días; lógica de alerta en la 3ª y marcado en la 4ª; definición de la ventana |
| RD-03 | Flujo de permisos: endpoints de autorización, campos de quién autorizó y cuándo; registro del aviso del trabajador |
| RD-04 | Exportación de fechas exactas de faltas injustificadas; generación de reporte para aviso de rescisión |
| RD-05 | Campos exportables de tipo de ausencia; integración con reportes probatorios |
| RD-06 | Lógica de retardos: ¿existe conversión automática a falta? ¿con qué regla? |

---

## Capa interpretativa

Sin criterios citados de memoria. Lecturas operativas del texto:

- **La falta injustificada tiene dos escapes (F-02, F-05):** permiso del
  patrón O causa justificada. El sistema auditado debe modelar ambos con
  evidencia y fecha — sin ese dato, ninguna falta es defendible (784-III
  pone su prueba a cargo del patrón).
- **"MÁS de tres faltas" = a partir de la cuarta (F-02):** tres faltas
  injustificadas en 30 días NO habilitan la rescisión; la cuarta sí. El
  contador y sus alertas deben reflejar exactamente eso.
- **El despido por faltas vive o muere por las fechas (F-03):** el aviso debe
  referir "la fecha o fechas" exactas; el sistema auditado debe poder
  producirlas.
- **Los retardos no existen en este catálogo:** la LFT leída regula faltas,
  no retardos; su efecto es materia del reglamento interior → CL-02.

---

## Guía de auditoría del módulo

1. **Auditar la clasificación de ausencias en el código** (RD-01): tipos
   disponibles, evidencia y fechas; detectar ausencias sin clasificar.
2. **Auditar el contador del 47-X en el código** (RD-02): umbral en la 4ª
   falta injustificada dentro de 30 días, alerta en la 3ª; verificar la
   ventana usada y anotar CL-01.
3. **Auditar el flujo de permisos y avisos en el código** (RD-03): registro
   de quién autorizó y del aviso del trabajador (134-V).
4. **Probar el soporte de rescisión en el código** (RD-04): exportar las
   fechas exactas de las faltas de un trabajador en un periodo dado.
5. **Verificar el etiquetado exportable** por tipo de ausencia en el código
   (RD-05).
6. **Auditar el manejo de retardos en el código** (RD-06): sin conversión
   automática a falta salvo regla pactada; anotar CL-02.
7. **Generar el reporte** usando la plantilla canónica:
   `../../../../plantillas/plantilla-reporte.md`. Anotar CL-04 si hay
   teletrabajadores.

---

## Secciones fijas del reporte de este módulo

El encabezado del reporte es:

```
AUDITORÍA DE COMPLIANCE — Asistencia y faltas (Arts. 46–47, 134–135 LFT)
```

Sección fija adicional en el reporte:

```
VENTANA DE CÓMPUTO AUDITADA: [método de la ventana de 30 días usado por el sistema] — pendiente CL-01
```

---

## Límites del módulo

- No decide despidos ni valida causales distintas de la fracc. X: produce el
  soporte documental y las alertas.
- Los efectos de vacaciones e incapacidades como ausencias justificadas se
  detallan en sus módulos respectivos; aquí solo su etiquetado.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando el abogado resuelva CL-01–CL-04 o si se reforma el 47.

---

## Procedencia y estado

Citas de los Arts. 46, 47 (fracc. X y párrafos del aviso), 134 fracc. V y
135 fracc. II transcritas el 2026-07-07 directamente del PDF oficial de la
LFT consolidada (diputados.gob.mx, "Última Reforma DOF 14-05-2026"),
pp. 15–16 y 39. Los retardos se trataron como no regulados por las fuentes
leídas (CL-02) — no se inventó su régimen. Spec de origen:
`specs/asistencia-y-faltas-spec.md`, construida en modo batch (D-11) y
**aprobada en bloque por JP el 2026-07-08 (D-14)**.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — CL-01 (ventana de 30
días) define la lógica del contador, la alerta más importante de la skill.
