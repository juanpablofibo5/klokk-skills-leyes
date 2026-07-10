# Reglas derivadas — conservación y prueba

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME**,
**FIRME\*** (interpretación con pregunta abierta), **PENDIENTE**.

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | El sistema debe cubrir el catálogo de documentos del 804 que le competen: controles de asistencia (III) como núcleo, y soporte exportable que alimente II y IV (horas que explican pagos de salarios, vacaciones y primas). | Crítico | FIRME | F-02 |
| RD-02 | Plazos de retención (804, último párrafo): contratos (I) mientras dure la relación + 1 año después; nómina, asistencia y comprobantes (II–IV) durante el último año + 1 año tras la extinción de la relación. El sistema NO debe purgar registros de asistencia dentro de esos plazos; lectura operativa segura: todo el histórico de la relación + 1 año → CL-01. | Crítico | FIRME* | F-02; ver CL-01 |
| RD-03 | Exhibición bajo demanda: no presentar los documentos → se presumen ciertos los hechos del trabajador (784 pfo. primero y 805). El sistema debe poder exportar los documentos íntegros por trabajador y periodo en tiempo de juicio o inspección. | Alto | FIRME | F-01, F-03 |
| RD-04 | Cobertura de hechos del 784: el registro debe poder probar al menos las fracciones III (faltas), VIII (jornada ordinaria y extraordinaria), IX (descansos y obligatorios), X (vacaciones) y XI (primas) — con datos, no con dichos. La asimetría de VIII con los topes 2026 → CL-02. | Alto | FIRME | F-01; ver CL-02 |
| RD-05 | Pérdida o destrucción por caso fortuito no releva de probar por otros medios (784, último párrafo): el sistema debe tener respaldo y redundancia documentados de los registros. | Alto | FIRME* | F-01; regla técnica derivada |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿"Durante el último año" (804) permite purgar registros de asistencia de más de 12 meses con relación activa, o el piso práctico es todo el histórico? | El texto fija el mínimo exigible; purgar el histórico anterior es legalmente discutible y probatoriamente riesgoso. | abierta | abogado laboralista |
| CL-02 | 784-VIII pone la carga de la prueba del patrón sobre la jornada extraordinaria "cuando ésta no exceda de nueve horas semanales", pero los topes 2026–2030 suben a 10/11/12. ¿Cómo queda la carga de la prueba entre 9 y el tope del año? | La fracción no fue actualizada por el decreto DOF 2026-05-01 (última reforma: 2019). | abierta | abogado laboralista |
| CL-03 | 804-III dice "controles de asistencia, cuando se lleven en el centro de trabajo" (texto de 1980); el 132-XXXIV hace obligatorio el registro electrónico desde 2026. ¿El registro electrónico queda comprendido en 804-III y sus plazos? | El 804 no fue reformado en 2026; la integración de ambos regímenes no está escrita. | abierta | abogado laboralista |
| CL-04 | Interacción entre la presunción del 805 y la "prueba plena" del registro electrónico acordado (132-XXXIV, párrafo tercero). | Dos reglas probatorias nuevas y viejas sin articulación expresa. | abierta | abogado laboralista |

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Faltan documentos del catálogo o se purga dentro del plazo legal?
  (RD-01, RD-02)
     SÍ  -> CRÍTICO  (presunción en contra: se pierde el juicio por default)
     NO  -> siguiente pregunta

  ¿No puede exhibir, no cubre los hechos del 784, o no tiene respaldo?
  (RD-03, RD-04, RD-05)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  CL-01 a CL-04 y lo pendiente -> INFORMATIVO
```

*(Este módulo no tiene reglas de riesgo MEDIO; el árbol es de dos niveles.)*

La severidad aplica la regla global F2→severidad de lft/SKILL.md: VIOLADA y
AUSENTE disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la
parte faltante no es el núcleo de la regla (y se explica); NO-VERIFICABLE y
CL-xx → INFORMATIVO.
