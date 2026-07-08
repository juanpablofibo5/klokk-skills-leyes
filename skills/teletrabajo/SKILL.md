---
name: teletrabajo
description: Clasifica teletrabajadores (umbral legal >40 % del tiempo en domicilio) y audita sus obligaciones especiales en la LFT mexicana; registro de jornada remota con los mismos máximos, derecho a la desconexión, supervisión proporcional a la intimidad, modalidad e insumos. Usar al auditar plantillas híbridas o remotas. NOM-037 pendiente (v1 solo LFT).
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-07"
  ley: "LFT Arts. 330-A a 330-K (Capítulo XII Bis)"
  fuente: "LFT consolidada (última reforma DOF 2026-05-14), pp. 95-97; NOM-037-STPS PENDIENTE (D-12)"
---

# Skill: teletrabajo

**Qué hace:** determina quién es teletrabajador (umbral legal del 40 % del
tiempo), y audita que el sistema registre su jornada con los mismos límites
que a presenciales, respete el derecho a la desconexión, supervise de forma
proporcional a la intimidad, y registre modalidad, reversibilidad e insumos.

**Por qué importa:** la regla R6 de `registro-jornada` exige registrar
teletrabajadores con los mismos estándares; esta skill define QUIÉN es
teletrabajador y QUÉ obligaciones especiales genera para un checador — el
punto ciego típico de las PyMEs híbridas.

**Cuándo se activa:** al clasificar trabajadores híbridos o remotos, auditar
el registro de jornada remota, configurar alertas de desconexión o revisar
mecanismos de supervisión a distancia.

**Frontera:** los límites de jornada son de `jornada-laboral`; el registro
electrónico es de `registro-jornada`. Aquí vive lo ESPECIAL del teletrabajo.
**Alcance v1 (D-12):** solo el capítulo de la LFT; los requisitos de la
NOM-037-STPS están PENDIENTES y así se reportan siempre.

## Archivos de referencia

- [references/texto-legal.md](references/texto-legal.md) — texto oficial
  verificado: Arts. 330-A a 330-K, extractos relevantes (F-01 a F-07).
- [references/reglas.md](references/reglas.md) — las 7 reglas derivadas
  (RD-01 a RD-07, la última PENDIENTE) y los 4 casos límite (CL-01 a CL-04).
- Plantilla del reporte: se reutiliza la de la librería —
  [../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md).

## Capa interpretativa

Sin criterios citados de memoria. Lecturas operativas del texto:

- **El umbral del 40 % define el régimen (F-01):** más del 40 % del tiempo en
  el domicilio → aplican las obligaciones especiales del capítulo. El texto
  no define la ventana de medición → CL-01.
- **El teletrabajo NO relaja la jornada (F-02):** los horarios pactados no
  pueden exceder los máximos legales — los límites de `jornada-laboral` y el
  registro del Art. 132 Fr. XXXIV aplican íntegros (coherente con R6 de
  registro-jornada).
- **La NOM del 330-J existe como mandato** — su contenido (NOM-037-STPS) se
  transcribirá en un loop dedicado (D-12); hasta entonces sus requisitos
  específicos son PENDIENTE en esta skill.

## Procedimiento de auditoría

1. **Clasificar la plantilla:** calcular el % de tiempo en domicilio por
   trabajador y marcar como teletrabajadores a los que superen 40 % (RD-01,
   anotar CL-01 con la ventana usada).
2. **Auditar el registro de jornada remota:** mismos estándares y máximos que
   presenciales (RD-02); si el sistema exime a remotos del checador, es falla
   inmediata.
3. **Auditar la desconexión:** fin de jornada conocido por el sistema y
   capacidad de detectar actividad posterior (RD-03, anotar CL-02).
4. **Auditar la proporcionalidad de la supervisión:** sin cámaras/micrófonos
   permanentes; minimización de datos (RD-04).
5. **Verificar modalidad e historial** (RD-05) y el registro de insumos
   (RD-06).
6. **Marcar RD-07 como PENDIENTE** (NOM-037) — nunca auditar requisitos de la
   NOM de memoria.
7. **Generar el reporte** con el formato de la sección siguiente.

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Clasifica mal quién es teletrabajador o exime su jornada del registro?
  (RD-01, RD-02)
     SÍ  -> CRÍTICO
     NO  -> siguiente pregunta

  ¿Desconexión sin detección o supervisión desproporcionada? (RD-03, RD-04)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿Modalidad/insumos sin registrar? (RD-05, RD-06)
     SÍ  -> MEDIO

  RD-07 (NOM-037) y CL-01 a CL-04 -> INFORMATIVO / PENDIENTE
```

## Formato de salida

La plantilla de reporte de la librería
([../registro-jornada/assets/plantilla-reporte.md](../registro-jornada/assets/plantilla-reporte.md)),
con encabezado:

```
AUDITORÍA DE COMPLIANCE — Teletrabajo (Arts. 330-A a 330-K LFT)
```

y una sección adicional fija:

```
CLASIFICACIÓN APLICADA: [ventana y método usados para medir el 40 %] — pendiente CL-01
```

## Límites de la skill

- v1 SOLO cubre el capítulo de la LFT; los requisitos de la NOM-037-STPS
  están PENDIENTES (D-12) y así se reportan siempre.
- Los límites de jornada y el registro electrónico son de `jornada-laboral`
  y `registro-jornada`; aquí solo lo especial del teletrabajo.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa al transcribir la NOM-037 (sube a v2), cuando el abogado resuelva
  CL-01–CL-04, o si se reforma el capítulo.

## Estado del contenido

Citas de los Arts. 330-A, 330-B, 330-E, 330-G, 330-I, 330-J y 330-K
transcritas el 2026-07-07 directamente del PDF oficial de la LFT consolidada
(diputados.gob.mx, "Última Reforma DOF 14-05-2026"), pp. 95–97 (capítulo
adicionado DOF 11-01-2021). **La NOM-037-STPS NO fue transcrita (D-12):** sus
requisitos son PENDIENTE (RD-07/CL-03). Spec de origen:
`specs/teletrabajo-spec.md`, **construida en modo batch (D-11): revisión de
JP pendiente en bloque**.

**Pendiente para el abogado (fase 3):** CL-01 (ventana del 40 %) y CL-02
(alcance de la desconexión). **Pendiente de loop dedicado:** NOM-037 → v2.
