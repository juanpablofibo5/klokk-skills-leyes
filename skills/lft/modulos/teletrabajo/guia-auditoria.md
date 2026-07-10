# Guía de auditoría — módulo teletrabajo (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 2.0.0 |
| reviewed_at | 2026-07-08 |
| ley | LFT Arts. 330-A a 330-K (Capítulo XII Bis) |
| fuente | LFT consolidada (última reforma DOF 2026-05-14), pp. 95–97 — D1 de FUENTES.md |

---

**Qué hace:** determina quién es teletrabajador (umbral legal del 40 % del
tiempo) y audita que el sistema registre su jornada con los mismos límites
que a presenciales, respete el derecho a la desconexión al término de la
jornada, supervise de forma proporcional a la intimidad, y registre
modalidad, reversibilidad e insumos.

**Por qué importa:** la regla RD-06 del módulo registro-jornada (lft) exige
registrar teletrabajadores con los mismos estándares; este módulo define
QUIÉN es teletrabajador y QUÉ obligaciones especiales genera — el punto
ciego típico de las PyMEs híbridas.

**Cuándo se activa:** al clasificar trabajadores híbridos o remotos, auditar
el registro de jornada remota, configurar alertas de desconexión o revisar
mecanismos de supervisión a distancia.

**Frontera:** los límites de jornada son del módulo jornada-laboral (lft); el
registro electrónico es del módulo registro-jornada (lft). TODO lo relativo a
la NOM-037-STPS-2023 (listado de teletrabajadores, desconexión de alcance
completo, pausas y lactancia, cambio de modalidad documentado, conservación
de evidencias, y su fuera-de-alcance declarado) vive en la skill
**nom-037-stps** — si este módulo aplica, esa skill se corre también.

---

## Aplicabilidad (F1)

### Señales POSITIVAS (el módulo aplica)

- El sistema tiene un campo o estado "modalidad" (remote/presencial/híbrido)
  por trabajador o registro.
- Existen tablas, modelos o campos con nombres como `modalidad`, `remote`,
  `teletrabajo`, `home_office`, `work_location`, `lugar_trabajo`.
- Hay endpoints, formularios o configuraciones que permiten registrar o
  consultar días/horas trabajados en domicilio.
- El sistema controla o registra el fin de jornada de empleados remotos
  o tiene lógica de "desconexión".
- Hay un listado de empleados etiquetados como remotos, híbridos o
  teletrabajadores.

**Greps sugeridos:**
```
grep -ri "modal\|remote\|teletrabaj\|home_office\|work_location" --include="*.py,*.ts,*.js,*.rb,*.go,*.java,*.sql" .
grep -ri "desconex\|disconnect\|end_of_day\|fin_jornada" --include="*.py,*.ts,*.js" .
```

### Señales NEGATIVAS (módulo N/A)

- El sistema solo registra empleados presenciales sin ningún campo de
  modalidad o ubicación.
- No hay ninguna lógica o dato que distinga entre presencial y remoto.
- El README o documentación indica que el sistema es exclusivo para
  operaciones físicas (fábrica, punto de venta, etc.).

**Si el módulo APLICA:** ejecutar también la skill `nom-037-stps` (sus
obligaciones son adicionales a las de este módulo).

## Superficies a revisar (F2)

| RD | Dónde buscar en el código |
|----|--------------------------|
| RD-01 | Lógica de clasificación de modalidad; campo `porcentaje_remoto` o cálculo equivalente; condición que activa obligaciones especiales |
| RD-02 | Validaciones de límites de jornada aplicadas a registros de tipo remoto vs. presencial; ¿el mismo tope? |
| RD-03 | Detección de actividad después del fin de jornada pactado para teletrabajadores; alertas de desconexión |
| RD-04 | Configuración de herramientas de monitoreo; permisos de cámara/micrófono; política de datos |
| RD-05 | Campo o historial de `modalidad` por trabajador; registro de fecha de cambio y acuerdo escrito |
| RD-06 | Registro o integración de insumos/equipo entregado por trabajador |
| RD-07 | (Meta-regla) Si hay teletrabajo, el reporte debe incluir la corrida de la skill nom-037-stps |

---

## Capa interpretativa

Sin criterios citados de memoria. Lecturas operativas del texto:

- **El umbral del 40 % define el régimen (F-01):** más del 40 % del tiempo en
  el domicilio → aplican las obligaciones especiales del capítulo. El texto
  no define la ventana de medición → CL-01; si la NOM aplica bajo el umbral
  → CL-05.
- **El teletrabajo NO relaja la jornada (F-02):** los horarios pactados no
  pueden exceder los máximos legales — los límites del módulo jornada-laboral
  (lft) y el registro del Art. 132 Fr. XXXIV aplican íntegros (coherente con
  RD-06 del módulo registro-jornada (lft)).
- **La NOM dejó de ser pendiente:** la NOM-037-STPS-2023 está vigente desde
  el 05-12-2023 y sus obligaciones auditables con datos de asistencia viven
  como RD-01 a RD-05 de la skill nom-037-stps (transcrita y verificada contra
  el DOF, D3/D4 de FUENTES.md). Este módulo ya no reporta "PENDIENTE
  NOM-037": remite a esa skill.

---

## Guía de auditoría del módulo

1. **Clasificar la plantilla (RD-01):** calcular el % de tiempo en domicilio
   por trabajador y marcar como teletrabajadores a quienes superen 40 %;
   anotar CL-01 con la ventana usada y CL-05 si hay remotos bajo el umbral.
   Si el sistema no tiene campo de modalidad o % de tiempo: hallazgo RD-01
   sobre el código.
2. **Auditar el registro de jornada remota (RD-02):** verificar que los mismos
   límites y validaciones de jornada aplican a registros de empleados remotos
   que a presenciales; si el sistema exime a remotos del registro, es falla
   inmediata.
3. **Auditar la desconexión (RD-03):** fin de jornada conocido por el sistema
   y capacidad de detectar/alertar actividad posterior; anotar CL-02. (El
   alcance completo de la desconexión NOM — no laborables, vacaciones,
   permisos, licencias, pausas — se audita en la skill nom-037-stps.)
4. **Auditar la proporcionalidad de la supervisión (RD-04):** sin
   cámaras/micrófonos permanentes configurados; minimización de datos.
5. **Verificar modalidad e historial (RD-05)** y el registro de insumos
   (RD-06).
6. **Ejecutar la skill nom-037-stps (RD-07)** si el módulo aplicó, y anexar
   su resultado al reporte.
7. **Generar el reporte** con el formato estándar
   (../../../../plantillas/plantilla-reporte.md), encabezado:
   `AUDITORÍA DE COMPLIANCE — Teletrabajo (Arts. 330-A a 330-K LFT)`.

---

## Secciones fijas del reporte de este módulo

Además de las secciones estándar del flujo (ver plantilla-reporte.md), el
reporte de este módulo incluye siempre:

```
CLASIFICACIÓN APLICADA: [ventana y método usados para medir el 40 % de tiempo en domicilio] — pendiente CL-01
```

---

## Límites del módulo

- Cubre el capítulo LFT completo (Arts. 330-A a 330-K). Todo lo relativo a
  la NOM-037-STPS-2023 — sus obligaciones auditables Y su fuera-de-alcance
  declarado (SST física, capacitación, exámenes, comisiones, apéndices) —
  vive en la skill nom-037-stps.
- Los límites de jornada son del módulo jornada-laboral (lft); el registro
  electrónico, del módulo registro-jornada (lft); la retención, del módulo
  conservacion-y-prueba (lft).
- No resuelve los CL abiertos (CL-01, CL-02, CL-04, CL-05): los reporta como
  INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa si se reforma el Capítulo XII Bis de la LFT, o cuando el abogado
  resuelva los CL (fase 3).

---

## Procedencia y estado

Citas de los Arts. 330-A, 330-B, 330-E, 330-G, 330-I, 330-J y 330-K
transcritas el 2026-07-07 directamente del PDF oficial de la LFT consolidada
(diputados.gob.mx, "Última Reforma DOF 14-05-2026"), pp. 95–97 (capítulo
adicionado DOF 11-01-2021). Spec de origen: `specs/teletrabajo-spec.md` (v1),
construida en modo batch (D-11) y **aprobada en bloque por JP el 2026-07-08
(D-14)**. Las anotaciones **v2** de este módulo (refinamientos de CL-01 y
CL-02, CL-05, y la redefinición de RD-07) provienen de
`specs/teletrabajo-v2-nom037-spec.md`, construida en modo batch (D-20) —
**esa spec sigue PENDIENTE de revisión en bloque de JP**; el contenido NOM
completo vive en la skill nom-037-stps con la misma marca D-20.

**Pendiente para el abogado (fase 3):** CL-01 (ventana del 40 %), CL-02
(actos que violan la desconexión), CL-05 (umbral de aplicación de la NOM).
**Pendiente para la revisión en bloque de JP (D-20):** las anotaciones v2 de
este módulo y la skill nom-037-stps completa.
