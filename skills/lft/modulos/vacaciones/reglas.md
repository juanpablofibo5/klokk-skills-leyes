# Reglas derivadas — vacaciones

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME** (el texto
lo exige hoy), **FIRME\*** (interpretación operativa razonable con pregunta
abierta registrada), **PENDIENTE** (regulación no publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Días de vacaciones por años de servicio cumplidos (tabla derivada de F-01): 1: 12 · 2: 14 · 3: 16 · 4: 18 · 5: 20 · 6–10: 22 · 11–15: 24 · 16–20: 26 · 21–25: 28 · 26–30: 30 (y así sucesivamente, +2 por bloque de 5). Los años 1–5 son literales del texto; los cortes de bloque exactos → CL-01. | Crítico | FIRME* | F-01; ver CL-01 |
| RD-02 | El trabajador tiene derecho a disfrutar al menos 12 días CONTINUOS, y la distribución del periodo es su potestad; el sistema debe permitir registrar la distribución elegida y no forzar fraccionamiento. | Alto | FIRME | F-03 |
| RD-03 | Las vacaciones no se compensan con remuneración durante la relación; el proporcional en dinero solo procede al terminar la relación antes del año. | Medio | FIRME | F-04 |
| RD-04 | Prima vacacional de al menos 25 % sobre los salarios del periodo de vacaciones; el sistema debe etiquetarla para nómina. La base con salario variable → CL-03. | Alto | FIRME | F-05; ver CL-03 |
| RD-05 | Las vacaciones deben concederse dentro de los 6 meses siguientes al aniversario; el sistema debe alertar saldos sin disfrutar cerca del vencimiento y vencidos. Además, constancia anual de antigüedad + días + fecha. | Alto | FIRME | F-06 |
| RD-06 | Trabajadores discontinuos y de temporada: vacaciones proporcionales a los días trabajados en el año. | Medio | FIRME | F-02 |
| RD-07 | Los días de vacaciones se registran en el sistema auditado como ausencia justificada etiquetada (no falta, no día trabajado); su efecto en otros cómputos (rachas, antigüedad) → CL-02. | Alto | FIRME* | F-01, F-06; interpretación operativa; ver CL-02 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | Cortes exactos de los bloques quinquenales del Art. 76 ("a partir del sexto año… por cada cinco"): ¿6–10, 11–15…, u otra lectura? | La redacción admite más de una segmentación; es un debate conocido desde la reforma 2022. | abierta | abogado laboralista |
| CL-02 | ¿Los días de vacaciones cuentan como "días de trabajo" para otros cómputos del sistema auditado (p. ej. la racha 6:1 del descanso semanal, antigüedad, asistencia perfecta)? | La LFT no define el efecto de la ausencia justificada sobre esos cómputos. | abierta | abogado laboralista |
| CL-03 | Base de la prima vacacional con salario variable o por hora ("los salarios que les correspondan durante el período"). | El texto no fija la base para salarios no fijos. | abierta | abogado laboralista |
| CL-04 | Si el trabajador no ejerce su potestad de distribución (F-03) dentro de la ventana de 6 meses (F-06), ¿puede el patrón fijar las fechas para no incumplir el Art. 81? | Tensión entre la potestad del trabajador y el deber del patrón de conceder en la ventana. | abierta | abogado laboralista |

## Árbol de decisión de severidad

Regla global F2→severidad: ver `skills/lft/SKILL.md`. VIOLADA y AUSENTE
disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la parte
faltante no es el núcleo de la regla (explicar); NO-VERIFICABLE y CL-xx →
INFORMATIVO.

```
Para cada hallazgo sobre el código auditado:

  ¿La tabla de días por antigüedad está mal configurada en el código? (RD-01)
     SÍ  -> CRÍTICO  (todos los saldos de todos los trabajadores quedan mal)
     NO  -> siguiente pregunta

  ¿El código bloquea derechos o deja vencimientos/primas sin marcar?
  (RD-02, RD-04, RD-05, RD-07)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿El código permite compensación indebida o no calcula proporcionales?
  (RD-03, RD-06)
     SÍ  -> MEDIO

  CL-01 a CL-04 y hallazgos NO-VERIFICABLE -> INFORMATIVO
```
