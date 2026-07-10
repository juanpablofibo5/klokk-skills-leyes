---
name: nom-037-stps
description: Audita los requisitos de SST del teletrabajo verificables en código — listado de teletrabajadores con % de tiempo, desconexión de alcance completo (vacaciones/permisos/pausas), pausas y lactancia registrables, documentación de cambio de modalidad y conservación de evidencias ≥ 1 año. Usar al auditar sistemas que gestionan teletrabajadores o trabajo híbrido.
metadata:
  version: "1.0.0"
  owner: "Juan Pablo"
  reviewed_at: "2026-07-08"
  ley: "NOM-037-STPS-2023"
  fuente: "D3/D4 de FUENTES.md (DOF 08-06-2023)"
---

> **AVISO — Construida en modo batch (D-20): la spec de origen
> (`specs/teletrabajo-v2-nom037-spec.md`) sigue PENDIENTE de revisión en
> bloque de JP antes de usarse en producción.**

# Skill: nom-037-stps

Librería de auditoría para la NOM-037-STPS-2023 (Teletrabajo — Condiciones
de seguridad y salud en el trabajo, vigente desde el 05-12-2023). Audita los
requisitos que un sistema de software puede verificar o alimentar con sus
datos; las obligaciones físicas/ergonómicas y de capacitación quedan fuera de
alcance declarado.

## Flujo de auditoría (F0–F5)

El flujo completo está en
[plantillas/flujo-auditoria-codigo.md](../../plantillas/flujo-auditoria-codigo.md).
Esta skill instancia ese flujo para la NOM-037-STPS-2023.

**F0 — Descubrimiento de arquitectura:** leer el repo target sin prejuicios —
README, estructura, esquemas, endpoints, jobs, configs — para mapear dónde
viven los datos que la NOM toca: modalidad de los trabajadores, asistencia
por ubicación, estados de ausencia, historial de cambios de modalidad y
retención.

**F1 — Aplicabilidad de módulos:** por cada módulo de esta skill,
¿aplica al código auditado? Usar las señales de aplicabilidad del
`guia-auditoria.md` del módulo. Un N/A declarado es resultado válido; un
módulo omitido en silencio, no.

**F2 — Mapeo regla → código:** por cada RD-xx de los módulos aplicables,
buscar en el código dónde se cumple o se rompe y clasificar:
IMPLEMENTADA / PARCIAL / AUSENTE / VIOLADA / NO-VERIFICABLE.

**Regla global F2→severidad:** VIOLADA y AUSENTE disparan el árbol de
decisión del módulo tal cual. PARCIAL dispara el árbol y puede atenuar UN
nivel solo si la parte faltante no es el núcleo de la regla (explicar por
qué). NO-VERIFICABLE y CL-xx → INFORMATIVO.

**F3 — Reporte de auditoría:** consolidar F1+F2 en el formato estándar
([plantillas/plantilla-reporte.md](../../plantillas/plantilla-reporte.md)).
La severidad de cada hallazgo la da el árbol del módulo — este flujo no
inventa severidades.

**F4 — Plan de remediación:** por cada hallazgo, propuesta concreta que
respete la arquitectura del repo auditado: qué cambiar, dónde, cómo en los
patrones del propio código, impacto y orden sugerido.

**F5 — Implementación asistida (GATED):** solo con aprobación explícita del
dueño del repo, ítem por ítem. Sin aprobación, el flujo TERMINA en F4.

## Módulos de esta ley

| Módulo | Descripción | Estado |
|--------|-------------|--------|
| [teletrabajo-sst](modulos/teletrabajo-sst/guia-auditoria.md) | Listado NOM, desconexión completa, pausas/lactancia, modalidad y retención verificables con datos de asistencia | en-verificacion |

## Señales de aplicabilidad (resumen)

El módulo `teletrabajo-sst` aplica cuando el repo tiene teletrabajadores
declarados o potenciales. Señales positivas: modelos/tablas con campos de
modalidad de trabajo (`remote`, `teletrabajo`, `work_mode`, `hybrid`),
registros de asistencia con ubicación, configuraciones de porcentaje remoto.
Señales negativas: repo sin empleados ni trabajadores, readme que declara
100 % presencial, ausencia total de campos de modalidad en esquemas.
Ver señales completas y greps en
[modulos/teletrabajo-sst/guia-auditoria.md](modulos/teletrabajo-sst/guia-auditoria.md).

## Formato de reporte

Usar [plantillas/plantilla-reporte.md](../../plantillas/plantilla-reporte.md)
con encabezado:

```
AUDITORÍA DE COMPLIANCE — Teletrabajo SST (NOM-037-STPS-2023) sobre <repo target>
```

Más la sección fija del módulo teletrabajo-sst:

```
CLASIFICACIÓN APLICADA: [ventana y método usados para medir el % de tiempo
en teletrabajo por persona] — pendiente CL-01 del módulo teletrabajo (lft)
```
