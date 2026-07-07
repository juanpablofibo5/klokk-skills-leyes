---
id: "ejemplo-jornada-laboral"
titulo: "EJEMPLO — Jornada laboral (plantilla con placeholders)"
estado: borrador   # borrador | en-verificacion | verificada | requiere-actualizacion
ultima_revision: "2026-07-06"
revisado_por: "nadie — archivo de demostración, sin verificación legal"
---

> ⚠️ **ARCHIVO DE EJEMPLO — TODOS LOS DATOS SON FICTICIOS.**
> Este archivo existe solo para mostrar cómo se llena
> [la plantilla](../plantillas/plantilla-skill-legal.md). Ningún artículo,
> número, fecha o cita de aquí es información legal real ni verificada.
> **No usar para ningún cálculo ni decisión.** Se elimina cuando exista la
> primera skill real.

# [EJEMPLO] Jornada laboral

> **Pregunta operativa que responde:** ¿cuántas horas puede durar la jornada
> según el tipo de turno, y a partir de qué momento el tiempo trabajado se
> clasifica distinto?

---

## (a) Fuente legal exacta

| ID   | Instrumento                 | Artículo / fracción | Última reforma en DOF | Link oficial |
|------|-----------------------------|---------------------|-----------------------|--------------|
| F-01 | [Ley Federal del Trabajo]   | [Art. NN]           | [AAAA-MM-DD]          | [https://dof.gob.mx/...] |
| F-02 | [Ley Federal del Trabajo]   | [Art. MM]           | [AAAA-MM-DD]          | [https://dof.gob.mx/...] |

### Texto citado

**F-01 — [Art. NN, Ley Federal del Trabajo]:**

> "[Aquí va la cita textual del artículo, copiada del texto vigente publicado
> en el DOF, sin parafrasear. Por ejemplo, la definición de los tipos de
> jornada y su duración máxima.]"

**F-02 — [Art. MM, Ley Federal del Trabajo]:**

> "[Cita textual del artículo que regula qué pasa con el tiempo trabajado más
> allá del límite de la jornada.]"

---

## (b) Interpretación operativa

**Para una empresa (el empleador):**

[En la práctica, esto significa que la empresa debe conocer el tipo de turno
de cada trabajador y vigilar que la jornada registrada no exceda el máximo de
[N] horas que corresponde a ese tipo. Si lo excede, ese tiempo tiene un
tratamiento distinto (pago, límites, autorización).]

**Para Klokk (el producto):**

[Klokk registra entradas y salidas por WhatsApp, así que debe: (1) conocer el
tipo de turno de cada empleado, (2) calcular la duración efectiva de la
jornada a partir de los registros, y (3) clasificar y alertar el tiempo que
exceda el máximo aplicable.]

---

## (c) Reglas derivadas

### RD-01 — Duración máxima por tipo de turno

- **Aplica cuando:** se calcula la duración de la jornada de un empleado con
  turno de tipo [diurno / nocturno / mixto].
- **Regla:** la jornada de tipo [X] tiene un máximo de [N] horas; todo minuto
  posterior al minuto [N × 60] se clasifica como [categoría — p. ej. tiempo
  extraordinario].
- **Fuente:** F-01, F-02
- **Notas de implementación:** [la granularidad del conteo está pendiente de
  definir — ver CL-01. Definir también la zona horaria de referencia del
  centro de trabajo — ver CL-02.]

### RD-02 — Clasificación del tipo de turno según el horario

- **Aplica cuando:** se da de alta o se modifica el horario de un empleado.
- **Regla:** si el horario cae completamente dentro de la franja [HH:MM–HH:MM],
  el turno es [tipo A]; si cae dentro de [HH:MM–HH:MM], es [tipo B]; si abarca
  partes de ambas franjas, es [tipo C].
- **Fuente:** F-01

---

## (d) Casos límite y preguntas abiertas

| ID    | Caso o pregunta | Por qué es ambiguo | Estado  | Quién lo resuelve |
|-------|-----------------|--------------------|---------|-------------------|
| CL-01 | [¿El tiempo que excede la jornada se cuenta minuto a minuto o por bloques?] | [La fuente fija el límite en horas pero no define la granularidad del conteo.] | abierta | [abogado laboral] |
| CL-02 | [¿Qué zona horaria rige cuando el empleado registra desde un estado distinto al del centro de trabajo?] | [La fuente no contempla registros remotos; es una situación operativa nueva.] | abierta | [decisión de producto + abogado laboral] |

---

## (e) Estado y última revisión

**Regla de caducidad:** si `ultima_revision` tiene más de [N meses — umbral
por definir], esta skill se trata como `requiere-actualizacion` aunque el
frontmatter diga otra cosa.

| Fecha      | Revisó      | Qué se verificó o cambió | Fuente contrastada |
|------------|-------------|--------------------------|--------------------|
| 2026-07-06 | Juan Pablo  | Creación del archivo de ejemplo con placeholders; sin verificación legal | ninguna |
