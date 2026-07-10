# Reglas derivadas — días festivos (descanso obligatorio)

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME** (el texto
lo exige hoy), **FIRME\*** (interpretación operativa razonable con pregunta
abierta registrada), **PENDIENTE** (regulación no publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | El calendario de festivos del año se genera con las reglas del Art. 74: fijos (1-ene, 1-may, 16-sep, 25-dic), lunes móviles (primer lunes de febrero, tercer lunes de marzo, tercer lunes de noviembre), sexenal (1-oct solo el año de transmisión del Ejecutivo) y electoral (jornada electoral ordinaria, según leyes electorales). Nunca fechas conmemoradas fijas para los móviles. | Crítico | FIRME | F-01 |
| RD-02 | Festivo laborado: se paga salario doble por el servicio, además del salario que ya corresponde por el descanso obligatorio — dos conceptos separados y exportables. | Crítico | FIRME | F-02 |
| RD-03 | La designación de quién trabaja en festivo se determina por convenio (o Tribunal); el sistema debe registrar la asignación pactada antes del festivo. | Medio | FIRME | F-02 |
| RD-04 | Toda jornada registrada en festivo debe quedar etiquetada de forma exportable para nómina (correlación horas-pagos, RD-09 del módulo registro-jornada (lft)). | Alto | FIRME* | F-01, F-02; interpretación operativa de la correlación |
| RD-05 | Los festivos electoral (fracc. IX) y sexenal (fracc. VII) requieren una fuente de calendario externa mantenida (leyes electorales / año de transmisión); el sistema debe declarar de dónde toma esas fechas. | Medio | FIRME* | F-01; ver CL-03 y CL-04 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | Festivo que cae en domingo y se labora: ¿se acumulan el doble del Art. 75 y la prima dominical del Art. 71 (+25 %)? | Son regímenes distintos con supuestos traslapados; el texto no dice si se suman. | abierta | abogado laboralista |
| CL-02 | Festivo que coincide con el día de descanso SEMANAL del trabajador y se labora: ¿aplica el doble del Art. 73, el del Art. 75, o ambos? | Dos fuentes de pago doble para el mismo día; el texto no resuelve el concurso. | abierta | abogado laboralista |
| CL-03 | ¿De qué fuente oficial y con qué anticipación se toma la fecha de la jornada electoral (fracc. IX)? | Depende de leyes electorales federales y locales, externas a la LFT. | abierta | decisión de producto + abogado |
| CL-04 | Confirmación de los años de transmisión del Ejecutivo para la fracc. VII (siguiente aplicable esperado: 2030). | El texto dice "cuando corresponda a la transmisión"; el año concreto debe confirmarse contra calendario oficial, no asumirse. | abierta | abogado / fuente oficial al configurar |

## Árbol de decisión de severidad

Regla global F2→severidad: ver `skills/lft/SKILL.md`. VIOLADA y AUSENTE
disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la parte
faltante no es el núcleo de la regla (explicar); NO-VERIFICABLE y CL-xx →
INFORMATIVO.

```
Para cada hallazgo sobre el código auditado:

  ¿Calendario mal generado o festivo trabajado sin pago doble en el código?
  (RD-01, RD-02)
     SÍ  -> CRÍTICO  (aplica mal el día a todos los trabajadores / dinero directo)
     NO  -> siguiente pregunta

  ¿Festivos laborados sin etiquetar para nómina en el código? (RD-04)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿Asignación sin registrar o fuente externa sin declarar en el código?
  (RD-03, RD-05)
     SÍ  -> MEDIO

  CL-01 a CL-04 y hallazgos NO-VERIFICABLE -> INFORMATIVO
```
