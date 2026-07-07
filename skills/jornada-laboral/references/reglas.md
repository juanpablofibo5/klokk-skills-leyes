# Reglas derivadas — jornada laboral

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME** (el texto
lo exige hoy), **FIRME\*** (interpretación operativa razonable con pregunta
abierta registrada), **PENDIENTE** (regulación no publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Clasificación de turno: DIURNA si cae íntegra entre 06:00–20:00; NOCTURNA si cae íntegra entre 20:00–06:00; si abarca ambas franjas: MIXTA cuando el periodo nocturno es < 3h30m, NOCTURNA cuando es ≥ 3h30m. | Crítico | FIRME | F-03 |
| RD-02 | Límite diario por tipo: diurna 8h, nocturna 7h, mixta 7h30m. | Crítico | FIRME | F-04 |
| RD-03 | Límite semanal de jornada ordinaria según el año, vigente desde el 1 de enero: 2026: 48 · 2027: 46 · 2028: 44 · 2029: 42 · 2030 en adelante: 40. El sistema debe usar la tabla del año auditado, nunca un valor fijo. | Crítico | FIRME | F-02, F-10 |
| RD-04 | Techo absoluto: ordinaria + extraordinaria ≤ 12 horas por día, sin excepción por acuerdo. (Regla compartida con `horas-extra`.) | Alto | FIRME | F-08 |
| RD-05 | Umbral de tiempo extraordinario: el tiempo que excede el límite diario del tipo de turno (RD-02) o el límite semanal vigente (RD-03) deja de ser ordinario y pasa al régimen de `horas-extra`. | Alto | FIRME* | F-02, F-04; ver CL-01 |
| RD-06 | En jornada continua debe existir un descanso de al menos 30 minutos. | Medio | FIRME | F-06 |
| RD-07 | Si el trabajador no puede salir del lugar durante reposo o comidas, ese tiempo se computa como jornada efectiva — el sistema no debe descontarlo. | Alto | FIRME | F-07 |
| RD-08 | La jornada semanal puede distribuirse de común acuerdo entre las partes; el sistema debe poder representar distribuciones pactadas. Los límites de esa distribución están abiertos (CL-02). | Medio | FIRME* | F-01; ver CL-02 |
| RD-09 | La reducción gradual de jornada no puede usarse para disminuir sueldos ni prestaciones; si el sistema detecta recálculo de salario-hora a la baja al cambiar de año de calendario, debe alertarlo. | Medio | FIRME* | F-11 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿El excedente del límite SEMANAL sin exceder ningún límite diario es "tiempo extraordinario" con su régimen de pago? | El Art. 66 habla de "prolongarse" la jornada; el texto no dice explícitamente cómo tratar el excedente puramente semanal. | abierta | abogado laboralista |
| CL-02 | ¿La distribución "de común acuerdo" (Art. 58) permite rebasar los límites diarios del Art. 61 (p. ej. 4×10h)? | El nuevo segundo párrafo del 58 no fija límites propios y el 61 quedó redactado como "la duración de la jornada diaria será…", sin decir "máxima". | abierta | abogado laboralista |
| CL-03 | En turnos que cruzan medianoche, ¿a qué día se imputan las horas para el límite diario y a qué semana para el semanal? | La ley no define el corte; es una decisión operativa con impacto legal. | abierta | decisión de producto + abogado |
| CL-04 | ¿Los 30 minutos de descanso (Art. 63) computan como jornada cuando el trabajador SÍ puede salir? | El Art. 64 solo resuelve el caso "no puede salir"; el caso contrario queda a interpretación. | abierta | abogado laboralista |
