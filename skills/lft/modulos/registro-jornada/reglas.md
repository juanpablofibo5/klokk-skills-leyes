# Reglas derivadas — para auditar

Lógica sin ambigüedad. Cada regla se marca **FIRME** (ley o tribunales lo
exigen hoy) o **PENDIENTE** (disposiciones STPS 2027).

| #      | Regla que el sistema debe cumplir | Riesgo | Estado |
|--------|-----------------------------------|--------|--------|
| RD-01  | Registrar inicio y fin de jornada por cada trabajador individualmente. | Crítico | FIRME |
| RD-02  | Registro inalterable, o con log de auditoría de cualquier corrección (quién, cuándo, qué). | Alto | FIRME* |
| RD-03  | Exportable por trabajador y periodo, en formato entregable a la autoridad. | Crítico | FIRME |
| RD-04  | Evidencia de que el trabajador acordó el mecanismo (para prueba plena). | Alto | FIRME |
| RD-05  | Conservar histórico (mín. 12 meses; idealmente toda la relación laboral). | Alto | FIRME* |
| RD-06  | Registrar teletrabajadores con los mismos estándares que presenciales. | Medio | FIRME |
| RD-07  | Datos del trabajador consistentes con nómina, contrato, IMSS y CFDI. | Crítico | FIRME |
| RD-08  | Registro continuo y no selectivo (no permitir huecos convenientes). | Alto | FIRME* |
| RD-09  | Correlación verificable entre horas registradas y pagos de nómina. | Alto | FIRME* |
| RD-10  | Formato técnico exacto, campos adicionales y excepciones por sector. | — | PENDIENTE |

\* **FIRME por interpretación / tribunales:** no está en el texto con esas
palabras, pero se deriva del requisito de "prueba plena" o de criterios
judiciales sobre registros confiables. Las disposiciones de 2027 podrían
formalizarlo.

**Precisión 2026-07-07 (verificada contra el Art. 804 LFT, consolidada
p. 340):** el piso estatutario de conservación de controles de asistencia es
"durante el último año y un año después de que se extinga la relación
laboral" (Art. 804, fracc. III y último párrafo). RD-05 ("mín. 12 meses") queda
anclada a esa fuente — y el plazo posterior a la extinción, que RD-05 no
mencionaba, es exigible. El detalle completo vive en el módulo
conservacion-y-prueba (lft).

## Árbol de decisión de severidad

Aplica cuando el mapeo RD→código (F2 del flujo) arroja VIOLADA, AUSENTE o PARCIAL.
Ver también la regla global F2→severidad en skills/lft/SKILL.md.

```
Para cada hallazgo sobre el código auditado:

  ¿El hallazgo impide tener CUALQUIER registro válido? (RD-01, RD-03)
     SÍ  -> CRÍTICO  (expone a multa directa por trabajador; F-01 / F-02)
     NO  -> siguiente pregunta

  ¿El hallazgo DEBILITA el valor probatorio del registro? (RD-02, RD-04, RD-05, RD-07, RD-08, RD-09)
     SÍ  -> ALTO  (pierde defensa en juicio aunque exista registro)
     NO  -> siguiente pregunta

  ¿Es cobertura parcial / buena práctica? (RD-06)
     SÍ  -> MEDIO

  RD-10 y todo lo técnico pendiente de 2027 -> INFORMATIVO (pendiente STPS)
```

## Tabla de mapeo (RD nuevo = R original de la spec de JP)

| ID nuevo | ID original spec | Notas |
|----------|-----------------|-------|
| RD-01    | R1              | Sin cambio de contenido |
| RD-02    | R2              | Sin cambio de contenido |
| RD-03    | R3              | Sin cambio de contenido |
| RD-04    | R4              | Sin cambio de contenido |
| RD-05    | R5              | Sin cambio de contenido |
| RD-06    | R6              | Sin cambio de contenido |
| RD-07    | R7              | Sin cambio de contenido |
| RD-08    | R8              | Sin cambio de contenido |
| RD-09    | R9              | Sin cambio de contenido |
| RD-10    | R10             | Sin cambio de contenido |
