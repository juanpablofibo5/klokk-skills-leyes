# Flujo de auditoría de código — compliance legal MX (v1)

La metodología compartida que **toda skill-ley de esta librería** ejecuta al
correr dentro de una sesión de Claude Code **con acceso directo al
repositorio target**. La skill aporta el conocimiento legal verificado
(módulos con F-xx, RD-xx, CL-xx); este flujo aporta el CÓMO auditar ese
conocimiento contra el código real y convertirlo en un plan accionable.

**Contrato de entrada:** una sesión con el repo target abierto (cualquier
stack, cualquier arquitectura — no se asume NADA) + una skill-ley cargada.
**Salida:** un reporte de auditoría fechado y trazable + un plan de
remediación que respeta la codebase existente. Re-ejecutable en cualquier
momento.

## Principios (no negociables)

1. **Evidencia real o no es hallazgo.** Toda afirmación sobre el target se
   ancla a `archivo:línea`, configuración, migración, esquema o test del
   repo — nunca a suposiciones sobre cómo "debería" estar hecho.
2. **No romper.** El plan de remediación propone cambios DENTRO de los
   patrones y convenciones del propio código (citando ejemplos análogos de
   la misma codebase), con análisis de impacto y orden incremental.
3. **Auditar ≠ implementar.** El flujo audita y planea; solo toca código en
   F5, con aprobación explícita del dueño del repo, ítem por ítem.
4. **Honestidad estructural.** Lo que no aplica se declara N/A con su razón
   (no se omite en silencio); los casos límite legales (CL-xx) se reportan
   como INFORMATIVO — jamás se resuelven inventando; lo no verificable con
   el código disponible se dice tal cual.
5. **Re-ejecutable y comparable.** Cada reporte registra fecha, commit
   auditado, versión de la librería y hashes de FUENTES.md; una corrida
   posterior calcula el delta contra la anterior.

## Las seis fases

### F0 — Descubrimiento de arquitectura

Leer el repo target sin prejuicios: README y docs, estructura de carpetas,
dependencias/manifiestos, modelos de datos y migraciones, endpoints/rutas,
jobs y schedulers, configuración y variables, flujos de UI relevantes.
**Salida:** MAPA del target — stack, dominios funcionales, y dónde viven los
datos que las leyes tocan (personas, tiempo, ausencias, pagos, retención).
Solo lectura; nada se ejecuta que mute estado.

### F1 — Aplicabilidad de módulos

Por cada módulo legal de la skill-ley: ¿aplica a ESTE código? Con evidencia
(p. ej. "no existe ninguna superficie de teletrabajo → módulo N/A").
**Salida:** tabla de aplicabilidad (APLICA / N/A + razón). Un N/A declarado
es un resultado válido; un módulo omitido sin declarar, no.

### F2 — Mapeo regla → código

Por cada RD-xx de los módulos aplicables, buscar en el código dónde se
cumple o se rompe, y clasificar:

| Estado | Significa |
|--------|-----------|
| IMPLEMENTADA | La regla se cumple; evidencia de dónde |
| PARCIAL | Existe pero incompleta (qué falta, dónde) |
| AUSENTE | No hay rastro de la regla en el código |
| VIOLADA | El código hace activamente lo contrario |
| NO-VERIFICABLE | El código disponible no permite decidir (decirlo) |

Dos precisiones de clasificación:
- **Atenuación de PARCIAL (ejemplo resuelto):** si la regla exige "exportar
  registros por trabajador y periodo" y el código exporta TODO en un CSV sin
  selector, lo faltante (el selector) no es el núcleo (el dato completo y
  exportable) → PARCIAL atenuado un nivel, explicándolo. Si lo faltante ES el
  núcleo (p. ej. la tabla anual de límites en un validador de jornada),
  PARCIAL sin atenuar.
- **Reglas-prohibición sin superficie:** si la regla prohíbe algo y el código
  no tiene NINGUNA superficie relacionada (ni para violarla ni para
  cumplirla), se clasifica NO-VERIFICABLE — no como cumplimiento por
  ausencia.

**Salida:** matriz RD-xx → estado + evidencia `archivo:línea` + nota.

### F3 — Reporte de auditoría

Consolidar F1+F2 en el formato estándar (abajo). La severidad de cada
hallazgo la da el **árbol de decisión del módulo** correspondiente — el
flujo no inventa severidades. Trazabilidad completa: fuente legal (F-xx) →
regla (RD-xx) → evidencia en código.

### F4 — Plan de remediación

Por cada hallazgo, una propuesta concreta que respete la arquitectura:

- **Qué cambiar y dónde** (archivos/módulos concretos del target).
- **Cómo, en los patrones del propio repo** — citar código análogo existente
  como referencia de estilo/estructura.
- **Impacto y riesgo de ruptura** (qué depende de eso; migraciones de datos
  si las hay).
- **Orden sugerido:** quick wins primero, cambios estructurales después,
  cada paso desplegable por sí solo.
- **Prioridad** = severidad legal × exposición práctica (dinero, juicio,
  multa UMA cuando la regla la tenga).

**Salida:** plan priorizado, cada ítem trazable a su RD-xx.

### F5 — Implementación asistida (GATED)

Solo con aprobación explícita del dueño del repo, ítem por ítem del plan:
implementar con tests, sin refactors oportunistas, y re-correr F2 sobre las
reglas afectadas para confirmar el cambio de estado (AUSENTE → IMPLEMENTADA).
Sin aprobación, el flujo TERMINA en F4 — entregar el plan es el default.

## Formato del reporte

```
AUDITORÍA DE COMPLIANCE — <Ley / norma> sobre <repo target>
Fecha: AAAA-MM-DD · Commit auditado: <sha> · Librería: <tag/commit de skills-leyes-mx>
Fuentes legales: <doc + SHA-256, de FUENTES.md> · Corrida anterior: <fecha o "primera">

1. RESUMEN EJECUTIVO — veredicto por módulo + los 3-5 hallazgos que más importan
2. APLICABILIDAD — tabla F1 (APLICA / N/A + razón)
3. HALLAZGOS — por severidad (CRÍTICO → ALTO → MEDIO), cada uno:
   H-xx · [RD-xx del módulo] · estado (PARCIAL/AUSENTE/VIOLADA)
   Evidencia: archivo:línea · Qué exige la ley (F-xx) · Qué hace el código
4. CUMPLE — reglas IMPLEMENTADAS con su evidencia (el cumplimiento también se prueba)
5. INFORMATIVO — CL-xx aplicables (preguntas abiertas para el abogado) y NO-VERIFICABLES
6. PLAN DE REMEDIACIÓN — tabla priorizada (ítem, RD, cambio propuesto, dónde,
   riesgo de ruptura, orden)
7. DELTA — qué cambió vs la corrida anterior (hallazgos nuevos/resueltos), si existe
```

## Qué aporta cada módulo al flujo

Cada módulo legal (p. ej. `lft/modulos/horas-extra/`) alimenta al flujo con:
sus **reglas** (RD-xx con estado FIRME/FIRME*/PENDIENTE y fuente F-xx), su
**árbol de severidad** (qué es CRÍTICO/ALTO/MEDIO al fallar), sus **casos
límite** (CL-xx → sección INFORMATIVO) y sus **señales de aplicabilidad**
(qué buscar en F1 para decidir si el módulo aplica). El flujo es el mismo
para todas las leyes; los módulos son el conocimiento.

*(El formato de arriba está instanciado como plantilla llenable en
[plantilla-reporte.md](plantilla-reporte.md); cada módulo agrega sus
secciones fijas donde su `guia-auditoria.md` lo indique.)*
