# Guía de auditoría — módulo conservacion-y-prueba (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 784, 804 y 805 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), pp. 335 y 340 |

---

**Qué hace:** audita que el sistema conserve y pueda exhibir los documentos
que la ley obliga al patrón a presentar en juicio (contratos, nómina,
controles de asistencia, comprobantes de vacaciones y primas), con los plazos
legales de retención, y que el registro cubra los hechos cuya carga de la
prueba recae en el patrón.

**Por qué importa:** es la columna probatoria de toda la librería. Si el
patrón no exhibe estos documentos, se presumen ciertos los hechos que alegue
el trabajador (Arts. 784 y 805) — el registro perfecto que no se puede
exhibir a tiempo vale lo mismo que no tener registro.

**Cuándo se activa:** al auditar políticas de retención y purga de datos,
capacidad de exportación para juicio o inspección, o la cobertura probatoria
del registro (¿qué hechos puede probar el sistema?).

**Frontera:** el CÓMO registrar es del módulo registro-jornada (lft); aquí
vive el CONSERVAR, EXHIBIR y QUÉ HECHOS probar.

---

## Aplicabilidad (F1)

### Señales POSITIVAS (el módulo aplica)

- El sistema genera o almacena registros de asistencia, listas de nómina,
  comprobantes de vacaciones, permisos o primas.
- Hay modelos, tablas o entidades con nombres como `attendance_record`,
  `asistencia`, `registro_jornada`, `nomina`, `payroll`, `vacaciones`,
  `comprobante`.
- El sistema tiene lógica de retención, purga o archivado de datos históricos
  (jobs de limpieza, policies de retención, configuración de TTL).
- Existe funcionalidad de exportación o reporte por trabajador y periodo.

**Greps sugeridos:**
```
grep -ri "reten\|purge\|archive\|delete.*record\|cleanup.*attend\|ttl\|expir" --include="*.py,*.ts,*.js,*.rb,*.go,*.java,*.sql" .
grep -ri "export\|exhib\|juicio\|download.*record" --include="*.py,*.ts,*.js" .
```

### Señales NEGATIVAS (módulo N/A)

- El sistema no guarda datos históricos — opera solo en tiempo real sin
  persistencia.
- No existe ninguna función de exportación o reporte de registros históricos.

## Superficies a revisar (F2)

| RD | Dónde buscar en el código |
|----|--------------------------|
| RD-01 | Entidades/tablas de controles de asistencia, nómina/pagos y comprobantes de vacaciones/primas; ¿el sistema produce o puede exportar todos los tipos del catálogo 804? |
| RD-02 | Jobs de purga, políticas de retención, configuraciones de TTL o `delete_at`; ¿se purga asistencia dentro del plazo legal? |
| RD-03 | Endpoints o funciones de exportación por trabajador y periodo; ¿incluye extrabajadores dentro del año posterior a la extinción? |
| RD-04 | ¿Los datos de asistencia pueden probar faltas (III), jornada ordinaria y extraordinaria (VIII), descansos (IX), vacaciones (X) y primas (XI)? |
| RD-05 | Configuración de backups, redundancia documentada, plan de recuperación ante pérdida de datos |

---

## Capa interpretativa

Sin criterios citados de memoria. Lecturas operativas del texto:

- **El catálogo probatorio de F-01 es el mapa de cobertura del software
  auditado:** de las 14 fracciones del 784, el registro de asistencia
  alimenta directamente III (faltas), VIII (jornada ordinaria y
  extraordinaria), IX (descansos y obligatorios), X (vacaciones) y XI
  (primas). Es la justificación estatutaria de la correlación horas-pagos
  (RD-09 del módulo registro-jornada (lft)).
- **El hallazgo 784-VIII:** la fracción habla de jornada extraordinaria
  "cuando ésta no exceda de nueve horas semanales" y su última reforma es de
  2019 — el decreto del 2026-05-01 NO la actualizó, aunque los topes de
  horas extra suben gradualmente a 12. La asimetría es CL-02.
- **Los plazos del 804 son el piso de retención:** controles de asistencia
  (fracc. III): "durante el último año y un año después de que se extinga la
  relación laboral". Lectura operativa segura para un sistema SaaS: conservar
  TODO el histórico mientras dure la relación + 1 año tras la extinción (el
  "último año" es lo mínimo exigible en cualquier momento; purgar antes es
  riesgo directo) → detalle en CL-01.

---

## Guía de auditoría del módulo

1. **Mapear la cobertura documental (RD-01):** identificar en el código las
   entidades o tablas que corresponden a controles de asistencia (III), listas
   de nómina/pagos (II) y comprobantes de vacaciones/primas (IV); verificar
   que el sistema puede exportarlos o producirlos.
2. **Auditar la política de retención y purga (RD-02):** buscar jobs,
   políticas de TTL o condiciones de borrado de registros de asistencia;
   verificar que ningún registro se purga dentro de los plazos del 804;
   recomendar histórico completo + 1 año tras extinción; anotar CL-01.
3. **Probar la exhibición (RD-03):** verificar que existe exportación íntegra
   por trabajador y periodo, incluyendo extrabajadores dentro del año
   posterior a la extinción de la relación.
4. **Verificar la cobertura de hechos del 784 (RD-04):** comprobar que el
   sistema puede producir evidencia de faltas (III), jornada (VIII),
   descansos (IX), vacaciones (X) y primas (XI) con datos, no con dichos;
   anotar CL-02.
5. **Verificar respaldo y redundancia documentados (RD-05):** revisar
   configuración de backups y plan de recuperación; si no existe o no está
   documentado, hallazgo.
6. **Generar el reporte** con el formato estándar
   (../../../../plantillas/plantilla-reporte.md), encabezado:
   `AUDITORÍA DE COMPLIANCE — Conservación y prueba (Arts. 784, 804 y 805 LFT)`
   y sección adicional fija:
   `POLÍTICA DE RETENCIÓN AUDITADA: [plazos de retención y purga configurados en el sistema]`

---

## Secciones fijas del reporte de este módulo

Además de las secciones estándar del flujo (ver plantilla-reporte.md), el
reporte de este módulo incluye siempre:

```
POLÍTICA DE RETENCIÓN AUDITADA: [plazos de retención y purga configurados en el sistema]
```

---

## Límites del módulo

- No audita el CÓMO se registra (eso es el módulo registro-jornada (lft)):
  audita conservación, exhibición y cobertura probatoria.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa si se reforman los Arts. 784/804/805 (en particular si una
  reforma armoniza 784-VIII con los topes 2026) o cuando el abogado resuelva
  CL-01–CL-04.

---

## Procedencia y estado

Citas de los Arts. 784, 804 y 805 transcritas el 2026-07-07 directamente del
PDF oficial de la LFT consolidada (diputados.gob.mx, "Última Reforma DOF
14-05-2026"), pp. 335 y 340. Hallazgos de esta investigación: (1) el 804-III
da ancla estatutaria exacta a la RD-05 del módulo registro-jornada (lft);
(2) el 784-VIII conserva "nueve horas semanales" sin armonizar con los topes
2026 → CL-02. Spec de origen: `specs/conservacion-y-prueba-spec.md`,
construida en modo batch (D-11) y **aprobada en bloque por JP el 2026-07-08
(D-14)**.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 — CL-02 y CL-03 son
de máximo interés para el sistema auditado (carga de la prueba del
extraordinario y estatus probatorio del registro electrónico).
