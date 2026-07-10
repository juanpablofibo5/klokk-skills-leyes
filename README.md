# skills-leyes-mx

![validacion](https://github.com/juanpablofibo5/skills-leyes-mx/actions/workflows/validacion.yml/badge.svg)

Librería de **skills de compliance legal mexicano para auditar cualquier base
de código**. Cada skill corresponde a una ley o norma; se usa dentro de una
sesión de Claude Code **con acceso al repositorio target**: carga el
conocimiento legal verificado, lee la arquitectura y el código reales,
produce una auditoría con evidencia `archivo:línea`, y propone un plan de
remediación que respeta la codebase existente. Re-ejecutable en cualquier
momento — cada corrida se fecha y se compara con la anterior.

Todo el contenido legal está transcrito de documentos oficiales (DOF /
diputados.gob.mx) descargados y anclados por SHA-256 en
[FUENTES.md](FUENTES.md), con documento y página por cita.

> ⚠️ **Este repositorio no es asesoría legal.** Es una base de conocimiento
> auditada de en qué se basa cada regla. El contenido está `en-verificacion`:
> verificado contra fuentes oficiales y con specs aprobadas, pero la
> validación por abogado laboralista (fase 3) sigue pendiente. Ninguna skill
> debe presentarse como `verificada` antes de eso — el CI lo bloquea.

## Cómo se usa (auditar un repositorio)

1. **Ten la librería junto al target:** clona este repo al lado del repo que
   quieres auditar (el mecanismo definitivo de consumo es una decisión
   abierta con dueño — D-16).
2. **Abre una sesión de Claude Code EN el repo target** (la sesión debe poder
   leer su código; a esta librería se llega por ruta).
3. **Pide la auditoría de una ley:** p. ej. *"ejecuta la skill `lft` de
   ../skills-leyes-mx sobre este repo"*. La skill corre el flujo
   [F0–F5](plantillas/flujo-auditoria-codigo.md): descubrimiento de
   arquitectura → aplicabilidad por módulo (los N/A se declaran, no se
   omiten) → mapeo regla→código con evidencia → reporte → plan de
   remediación. Nada se implementa sin tu aprobación explícita (F5 es gated).
4. **El resultado** es un reporte con el
   [formato estándar](plantillas/plantilla-reporte.md): hallazgos H-xx
   trazables (fuente legal F-xx → regla RD-xx → `archivo:línea`), lo que
   CUMPLE con su evidencia, los casos límite como INFORMATIVO, y el plan
   priorizado por severidad × exposición.

## Las leyes disponibles

| Skill | Cubre | Módulos | Estado |
|-------|-------|---------|--------|
| [lft](skills/lft/SKILL.md) | Ley Federal del Trabajo — tiempo de trabajo y su prueba (incluida la reforma de reducción de jornada, DOF 2026-05-01, con sus calendarios 2026–2030) | registro-jornada · jornada-laboral · horas-extra · dias-de-descanso · dias-festivos · vacaciones · teletrabajo · conservacion-y-prueba · asistencia-y-faltas | en-verificacion |
| [nom-037-stps](skills/nom-037-stps/SKILL.md) | NOM-037-STPS-2023 (teletrabajo — SST): listado, desconexión de alcance completo, pausas y lactancia, cambio de modalidad, conservación | teletrabajo-sst | en-verificacion (spec en revisión de JP, D-20) |

**Próximas (backlog):** módulos LFT de trabajo-de-menores y lactancia (D-15),
y la LFPDPPP (protección de datos personales) como siguiente ley.

## Estructura

```
skills/
  <ley>/
    SKILL.md                  ← la puerta de entrada: qué cubre, el flujo
                                instanciado, la regla F2→severidad y el
                                índice de módulos
    modulos/<tema>/
      texto-legal.md          ← SOLO fuente oficial: citas textuales F-xx
                                con documento y página
      reglas.md               ← reglas RD-xx (riesgo, estado FIRME/FIRME*/
                                PENDIENTE, fuente) + casos límite CL-xx +
                                árbol de severidad
      guia-auditoria.md       ← aplicabilidad (F1, señales + greps),
                                superficies a revisar (F2), guía del módulo,
                                límites y procedencia
plantillas/
  flujo-auditoria-codigo.md   ← el flujo F0–F5 común a todas las leyes
  plantilla-reporte.md        ← formato estándar del reporte
  brief-investigacion-skill.md, plantilla-skill-legal.md  ← pipeline de contenido
specs/                        ← specs verificadas de las que se construyó cada módulo
FUENTES.md                    ← documentos oficiales con SHA-256 (cadena de custodia)
tools/validar.py              ← el CI: estructura, fidelidad de formato, guards
```

## Cómo se produce el contenido (pipeline)

1. **Investigación verificada:** el texto legal se descarga de la fuente
   oficial en la sesión, se transcribe con documento + página y se ancla por
   hash en FUENTES.md. Nada se escribe de memoria; lo ambiguo se registra
   como caso límite (CL-xx), jamás se resuelve inventando.
2. **Spec y gate:** cada módulo nace de una spec aprobada por el dueño de
   la librería (en `specs/`, salvo spec externa documentada — p. ej.
   registro-jornada).
3. **Fase 3 (pendiente):** un abogado laboralista revisará la librería
   completa — los CL-xx priorizados son su paquete de entrada; solo entonces
   los estados suben a `verificada` y se etiqueta v1.0.0.

Proceso completo, decisiones y bitácora: [CLAUDE.md](CLAUDE.md),
[DECISIONES.md](DECISIONES.md), [BITACORA.md](BITACORA.md),
[STATUS.md](STATUS.md), [BACKLOG.md](BACKLOG.md).

## Convenciones

- Español; fechas ISO; IDs estables que no se reciclan: `F-xx` (fuentes),
  `RD-xx` (reglas), `CL-xx` (casos límite), `H-xx` (hallazgos por corrida),
  `D-xx` (decisiones), `M-xx` (mejoras).
- Referencias entre módulos y skills SIEMPRE calificadas: "RD-09 del módulo
  registro-jornada (lft)", "F-02 de la skill nom-037-stps".
- Estados de contenido: `borrador` → `en-verificacion` → `verificada` (solo
  fase 3) → `requiere-actualizacion`.
- La librería es agnóstica del proyecto auditado (D-18): ningún contenido
  asume un producto concreto; el CI lo hace cumplir.
