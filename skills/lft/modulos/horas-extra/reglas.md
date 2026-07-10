# Reglas derivadas — horas extra

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME** (el texto
lo exige hoy), **FIRME\*** (interpretación operativa razonable con pregunta
abierta registrada), **PENDIENTE** (regulación no publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Entrada de la skill: el tiempo candidato a extraordinario viene de exceder los límites ordinarios definidos por `jornada-laboral` (su RD-05). Esta skill no redefine ese umbral. | Alto | FIRME* | F-02; hereda CL-01 de jornada-laboral |
| RD-02 | Tope semanal de trabajo extraordinario según el año, vigente desde el 1 de enero: 2026: 9 · 2027: 9 · 2028: 10 · 2029: 11 · 2030 en adelante: 12. El sistema debe usar la tabla del año auditado. | Crítico | FIRME | F-02, F-05 |
| RD-03 | Distribución del extraordinario: hasta 4 horas por día, en máximo 4 días por semana (texto vigente). Su interacción con los topes de transición (9/10/11) está abierta → CL-02. | Alto | FIRME* | F-02; ver CL-02 |
| RD-04 | Pago del extraordinario dentro del tope: +100 % sobre lo fijado para la hora ordinaria (salario doble por hora extra). | Crítico | FIRME | F-02 |
| RD-05 | Excedente del tope del Art. 66: no puede ser mayor de 4 horas a la semana y se paga +200 % (salario triple por hora). Sobre qué base corre ese tope en años de transición → CL-03. | Alto | FIRME* | F-04; ver CL-03 |
| RD-06 | Techo absoluto: ordinaria + extraordinaria ≤ 12 horas por día, sin excepción. (Regla compartida con `jornada-laboral`, su RD-04.) | Alto | FIRME | F-04 |
| RD-07 | Trabajo por siniestro o riesgo inminente: solo por el tiempo estrictamente indispensable y se paga igual que la hora ordinaria — es un régimen DISTINTO del extraordinario común y debe registrarse aparte. | Medio | FIRME | F-01, F-03 |
| RD-08 | Cada hora no ordinaria debe quedar etiquetada con su régimen (extra +100 % / excedente +200 % / siniestro pago ordinario) de forma exportable, para que la nómina pague bien y la correlación horas-pagos sea verificable. | Alto | FIRME* | F-02, F-03, F-04; interpretación operativa de la correlación (RD-09 del módulo registro-jornada (lft)) |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | (Heredado de `jornada-laboral`) ¿El excedente del límite SEMANAL ordinario sin exceso diario es "tiempo extraordinario" con su régimen de pago? | El Art. 66 habla de "prolongarse" la jornada; el texto no resuelve el excedente puramente semanal. | abierta | abogado laboralista |
| CL-02 | En los años de transición (tope 9, 10 u 11), ¿la distribución "hasta 4 horas diarias en máximo 4 días" aplica tal cual, o se modula con el tope del año? | El Transitorio Cuarto solo gradúa el TOTAL semanal; no dice nada de la distribución diaria/por días. | abierta | abogado laboralista |
| CL-03 | El tope de +4 horas del Art. 68 (pagadas +200 %), ¿corre sobre el tope del año (p. ej. 9+4 en 2027) o sobre las 12 horas del texto del Art. 66? | El Art. 68 remite a "lo establecido en el artículo 66", y el transitorio modifica gradualmente ese valor. | abierta | abogado laboralista |
| CL-04 | La presunción jurisprudencial de "hasta 9 horas extra semanales" a favor del trabajador, ¿se ajusta al tope del año del Transitorio Cuarto? | El criterio citado es previo a la reforma; el tope semanal ahora es variable por año. | abierta | abogado laboralista |

## Árbol de decisión de severidad (hallazgos sobre código)

Aplica la regla global F2→severidad de skills/lft/SKILL.md: VIOLADA y AUSENTE
disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la parte
faltante no es el núcleo de la regla (y se explica); NO-VERIFICABLE y CL-xx
→ INFORMATIVO.

```
Para cada hallazgo sobre el código auditado:

  ¿El código usa un tope de año incorrecto o aplica porcentaje base equivocado?
  (RD-02, RD-04)
     SÍ  -> CRÍTICO  (nómina incorrecta en dinero, por cada trabajador)
     NO  -> siguiente pregunta

  ¿El código clasifica mal regímenes, distribución o techos, o deja horas
  sin etiquetar correctamente? (RD-01, RD-03, RD-05, RD-06, RD-08)
     SÍ  -> ALTO  (horas mal etiquetadas o excesos sin detectar)
     NO  -> siguiente pregunta

  ¿El código maneja mal el régimen especial de siniestro/riesgo inminente?
  (RD-07)
     SÍ  -> MEDIO

  CL-01 a CL-04 y lo pendiente de autoridad -> INFORMATIVO
```
