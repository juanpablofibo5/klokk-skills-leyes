# Reglas derivadas — asistencia y faltas

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME**,
**FIRME\*** (interpretación con pregunta abierta), **PENDIENTE**.

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Toda ausencia se clasifica como justificada (permiso del patrón o causa justificada, con evidencia y fecha del aviso del trabajador) o injustificada. Sin clasificación, el registro no sirve para la causal ni para el 784-III. | Crítico | FIRME | F-02, F-04, F-05 |
| RD-02 | Contador de la causal: MÁS de tres faltas injustificadas (la 4ª) en un período de 30 días habilita rescisión sin responsabilidad. El sistema alerta en la 3ª y marca la 4ª. La naturaleza de la ventana (días naturales/laborables, móvil/fija) → CL-01. | Crítico | FIRME* | F-02; ver CL-01 |
| RD-03 | Flujo de permisos con registro: quién autorizó, cuándo, y el aviso del trabajador (134-V) con su fecha. Permisos verbales sin registro dejan la ausencia en ambigüedad probatoria. | Alto | FIRME | F-04, F-05 |
| RD-04 | Soporte del despido por faltas: el sistema debe poder producir las fechas exactas de las faltas injustificadas del periodo, aptas para el aviso escrito del 47 (sin aviso → presunción de separación injustificada). | Alto | FIRME | F-03 |
| RD-05 | Etiquetado exportable de ausencias por tipo (injustificada / permiso / causa justificada / vacaciones / incapacidad) para su uso probatorio (784-III, 804-III). | Alto | FIRME* | F-02, F-04; interpretación operativa de la correlación probatoria |
| RD-06 | Retardos: se registran como hechos, pero el sistema NO debe convertirlos automáticamente en "faltas" sin una regla pactada en el reglamento interior — la LFT no los regula como falta. | Medio | FIRME* | Interpretación operativa; ver CL-02 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | La ventana de "un período de treinta días" del 47-X: ¿días naturales o laborables? ¿ventana móvil o periodos fijos? | El texto no lo define; cambia qué secuencias de faltas activan la causal. | abierta | abogado laboralista |
| CL-02 | ¿Pueden los retardos acumulados pactarse como falta en el reglamento interior, y con qué límites? | La LFT leída no regula retardos; es materia de reglamento interior y criterios. | abierta | abogado laboralista |
| CL-03 | ¿Qué evidencia basta para "causa justificada" (incapacidades, caso fortuito del 134-V) y quién la califica? | El texto exige la causa pero no define el estándar probatorio del trabajador. | abierta | abogado laboralista |
| CL-04 | ¿Qué constituye "faltar" en teletrabajo (sin centro de trabajo físico): no conectarse, no fichar, no entregar? | Cruce del 47-X con el capítulo de teletrabajo; sin definición legal. | abierta | abogado laboralista + decisión de producto |

## Árbol de decisión de severidad

Regla global F2→severidad: ver `skills/lft/SKILL.md`. VIOLADA y AUSENTE
disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la parte
faltante no es el núcleo de la regla (explicar); NO-VERIFICABLE y CL-xx →
INFORMATIVO.

```
Para cada hallazgo sobre el código auditado:

  ¿Ausencias sin clasificar o contador de la causal mal calibrado en el código?
  (RD-01, RD-02)
     SÍ  -> CRÍTICO  (rescisiones inválidas o faltas indefendibles)
     NO  -> siguiente pregunta

  ¿El código carece de registro de permisos, soporte de fechas o etiquetado
  exportable? (RD-03, RD-04, RD-05)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿El código convierte retardos en faltas sin regla pactada? (RD-06)
     SÍ  -> MEDIO

  CL-01 a CL-04 y hallazgos NO-VERIFICABLE -> INFORMATIVO
```
