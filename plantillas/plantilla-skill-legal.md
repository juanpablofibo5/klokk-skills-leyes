# Plantilla de skill legal — v2 (formato Agent Skills)

> **v2 — 2026-07-08.** Documenta el formato real de la librería: carpeta por
> skill con `SKILL.md` + `references/`. La v1 (anatomía (a)–(e) en un solo
> archivo) vive en el historial de git; su anatomía sobrevive aquí como
> mapeo. El validador (`tools/validar.py`) hace cumplir esta plantilla en CI
> en cada push.

## Cómo nace una skill (no se llena esta plantilla directamente)

Las skills NO se escriben desde cero sobre esta plantilla: se **construyen
desde una spec aprobada**, siguiendo el pipeline del BACKLOG:

1. **Fase 1 — investigación verificada:** se produce
   `specs/<nombre>-spec.md` cumpliendo
   [brief-investigacion-skill.md](brief-investigacion-skill.md), con citas
   transcritas de documentos oficiales descargados en la sesión (documento +
   página por cita). Gate: aprobación de JP.
2. **Fase 2 — construcción:** se transcribe la spec a la estructura de abajo
   — sin inventar nada que no esté en la spec — y se corren sus casos de
   prueba. Gate: casos N/N ✓ + validador en verde.
3. **Fase 3 — validación legal:** el abogado revisa la librería completa;
   solo entonces una skill puede subir a `verificada`.

Esta plantilla define el **formato destino** de la fase 2.

## Estructura de carpeta

```
skills/<nombre-en-kebab-case>/
  SKILL.md                 <- puerta de entrada: qué hace, procedimiento,
                              severidad, formato de salida, límites, estado
  references/
    texto-legal.md         <- SOLO fuente verificada: citas textuales F-xx
                              con documento oficial y página
    reglas.md              <- lógica implementable: RD-xx + casos límite CL-xx
  assets/                  <- solo si la skill tiene plantillas propias
    plantilla-reporte.md      (si no, se reutiliza la de la librería y NO se
                               crea la carpeta)
```

## SKILL.md

Frontmatter obligatorio (el validador lo exige):

```yaml
---
name: <idéntico al nombre de la carpeta>
description: <qué hace + cuándo usarla, en una descripción rica en términos de búsqueda>
metadata:
  version: "X.Y.Z"          # semver; sube con cada revisión de contenido
  owner: "<responsable>"
  reviewed_at: "AAAA-MM-DD" # última verificación contra fuente oficial
  ley: "<artículos que cubre>"
  fuente: "<documento(s) oficial(es) y su versión/fecha>"
---
```

Secciones del cuerpo, en este orden:

1. **Qué hace / Por qué importa / Cuándo se activa / Frontera** con las
   skills vecinas (de la sección 1 de la spec).
2. **Archivos de referencia** — links a `references/` y a la plantilla de
   reporte que use.
3. **Capa interpretativa** — lecturas operativas del texto y criterios CON
   fuente; se declara vacía si no hay criterios verificados. Nunca de
   memoria.
4. **Procedimiento** de auditoría o cálculo — pasos numerados que citan
   RD-xx y anotan CL-xx.
5. **Árbol de decisión de severidad** — consistente con la columna Riesgo de
   reglas.md y con los casos de prueba de la spec (checklist del brief).
6. **Formato de salida** — plantilla de reporte + secciones fijas propias.
7. **Límites de la skill** — qué NO hace, qué es de otras skills, y el
   disclaimer de no-asesoría-legal.
8. **Estado del contenido** — de dónde salieron las citas (documento, fecha,
   páginas), spec de origen y su aprobación, y qué queda pendiente para el
   abogado (fase 3).

## references/texto-legal.md

- Tabla de **documentos oficiales** usados (qué es, URL, uso), descargados en
  la sesión de investigación.
- Tabla de **artículos** con su última reforma anotada en la consolidada.
- **Citas textuales** F-01, F-02… copiadas sin parafrasear, cada una con
  documento y página: `**F-01 — Art. NN (D1, p. NN):**` + blockquote.
- Cero interpretación. Cero corchetes: el único permitido es `[...]` para
  marcar omisión deliberada dentro de una cita.

## references/reglas.md

- Tabla de **reglas derivadas** con columnas: `ID | Regla | Riesgo | Estado |
  Fuente`.
  - IDs `RD-xx` estables, nunca reciclados.
  - Riesgo: `Crítico | Alto | Medio | —`.
  - Estado: `FIRME` (el texto lo exige) · `FIRME*` (interpretación operativa
    con pregunta abierta registrada) · `PENDIENTE` (fuente o regulación no
    publicada/transcrita).
  - Fuente: las F-xx que la respaldan (deben existir en texto-legal.md).
- Tabla de **casos límite** `CL-xx`: caso, por qué es ambiguo, estado
  (`abierta`/`resuelta`), quién resuelve. Lo que no se sabe se registra
  aquí — jamás se resuelve inventando.

## Mapeo con la anatomía v1 (a)–(e)

| Anatomía v1 | Dónde vive en v2 |
|-------------|------------------|
| (a) Fuente legal exacta | `references/texto-legal.md` |
| (b) Interpretación operativa | SKILL.md: qué hace/por qué + capa interpretativa |
| (c) Reglas derivadas | `references/reglas.md` (RD-xx) + procedimiento del SKILL.md |
| (d) Casos límite y preguntas abiertas | `references/reglas.md` (CL-xx) |
| (e) Estado y última revisión | frontmatter (`reviewed_at`, `version`) + "Estado del contenido" |

## Reglas no negociables (resumen del kernel)

- Cero contenido legal sin documento oficial descargado y citado con página.
- Toda ambigüedad → CL-xx; nunca se resuelve inventando.
- `verificada` solo existe después de la fase 3 (el CI lo bloquea).
- Toda revisión (aunque no cambie nada) sube `reviewed_at` y se registra en
  el "Estado del contenido" y la BITACORA.
- Antes de cada push: `python3 tools/validar.py` en verde.
