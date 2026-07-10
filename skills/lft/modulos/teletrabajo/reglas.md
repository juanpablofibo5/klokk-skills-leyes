# Reglas derivadas — teletrabajo

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME**,
**FIRME\*** (interpretación con pregunta abierta), **PENDIENTE** (fuente o
regulación no transcrita/publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Clasificación: si la relación se desarrolla más del 40 % del tiempo en el domicilio del trabajador (o el que eligió), es teletrabajo y aplican las obligaciones del capítulo; lo ocasional o esporádico NO es teletrabajo. La ventana de medición del 40 % → CL-01. **v2:** si la NOM aplica también bajo el umbral → CL-05. | Crítico | FIRME* | F-01; ver CL-01, ver CL-05 |
| RD-02 | La jornada del teletrabajador se pacta y registra con los MISMOS máximos legales que presenciales (duración y distribución de horarios en el contrato); el sistema auditado la registra con los mismos estándares. | Crítico | FIRME | F-02 |
| RD-03 | Derecho a la desconexión al término de la jornada: el sistema debe conocer el fin de jornada de cada teletrabajador y poder detectar/alertar actividad laboral posterior. Qué constituye violación exactamente → CL-02. | Alto | FIRME* | F-03 (fracc. VI); ver CL-02 |
| RD-04 | Supervisión proporcional: los mecanismos de monitoreo (incluido el sistema auditado) deben ser proporcionales, respetar intimidad y datos personales; cámaras y micrófonos solo de manera extraordinaria o por la naturaleza de las funciones. | Alto | FIRME | F-05 |
| RD-05 | Modalidad e historial: el cambio a teletrabajo es voluntario y por escrito, con derecho de reversibilidad; el sistema debe registrar la modalidad vigente de cada trabajador y su historial de cambios. | Medio | FIRME | F-04 |
| RD-06 | Registro de insumos entregados al teletrabajador (obligación patronal): el sistema debe poder registrarlo o integrarse con quien lo haga. | Medio | FIRME | F-03 (fracc. IV) |
| RD-07 | Requisitos de SST del teletrabajo: NOM-037-STPS-2023, vigente desde 05-12-2023 → ver la skill nom-037-stps. Sus obligaciones de SST física/ergonómica, capacitación y exámenes médicos quedan fuera de alcance declarado de este módulo (no son verificables con datos de asistencia). | — | FIRME | F-06; F-01 y F-12 de la skill nom-037-stps |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

Las obligaciones auditables de la NOM-037 (listado de teletrabajadores,
desconexión de alcance completo, pausas y lactancia, cambio de modalidad
documentado, conservación de evidencias) viven como RD-01 a RD-05 de la
skill **nom-037-stps** — si este módulo aplica, esa skill se corre también.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿Sobre qué ventana se mide el "más del cuarenta por ciento del tiempo" (semana, mes, contrato)? ¿Y cómo se mide: días, horas? **v2:** la NOM obliga a declarar el % en el listado (F-04, inciso f, de la skill nom-037-stps) pero tampoco define ventana ni método. | Ni la LFT ni la NOM definen periodo ni unidad de medición. | abierta | abogado laboralista |
| CL-02 | ¿Qué constituye violación del derecho a la desconexión (mensajes, asignación de tareas, llamadas) y qué evidencia debe guardar el sistema? **v2:** la NOM ya define CUÁNDO aplica (F-02 de la skill nom-037-stps: término de jornada, no laborables, vacaciones, permisos, licencias, pausas convenidas); sigue abierto QUÉ actos la violan. | El alcance temporal quedó definido por la NOM; el alcance material no. | abierta | abogado laboralista |
| CL-03 | Requisitos específicos de la NOM-037-STPS: pendientes de transcripción contra el texto oficial. **Resuelta 2026-07-08:** NOM transcrita y verificada contra el DOF 08-06-2023 (D3/D4, FUENTES.md); los requisitos aplicables al sistema de asistencia son RD-01 a RD-05 de la skill nom-037-stps y el resto quedó fuera de alcance declarado. | — | resuelta | loop NOM-037 (spec v2) |
| CL-04 | Registro de jornada remota entre husos horarios distintos al del centro de trabajo. | Cross-ref: es el CL-03 del módulo jornada-laboral (lft); aplica con más frecuencia en teletrabajo. | abierta | decisión de producto + abogado |
| CL-05 | ¿La NOM-037 aplica a trabajadores remotos que NO superan el 40 % del tiempo (p. ej. híbridos de 1–2 días)? El campo de aplicación (F-01 de la skill nom-037-stps) y la definición 4.20 (F-03 de la misma skill) hablan de "personas trabajadoras bajo la modalidad de Teletrabajo" sin repetir el umbral del 330-A. | Lectura conservadora: la NOM sigue al régimen LFT (>40 %); lectura literal: aplica a toda persona en la modalidad. La diferencia decide a quién exigir el listado y la política. | abierta | abogado laboralista |

## Árbol de decisión de severidad

```
Para cada regla que FALLA:

  ¿Clasifica mal quién es teletrabajador o exime su jornada del registro?
  (RD-01, RD-02)
     SÍ  -> CRÍTICO
     NO  -> siguiente pregunta

  ¿Desconexión sin detección o supervisión desproporcionada? (RD-03, RD-04)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿Modalidad/insumos sin registrar? (RD-05, RD-06)
     SÍ  -> MEDIO

  RD-07 (meta-regla: remite a nom-037-stps) y CL-01 a CL-05 -> INFORMATIVO
```

La severidad aplica la regla global F2→severidad de lft/SKILL.md: VIOLADA y
AUSENTE disparan el árbol tal cual; PARCIAL puede atenuar UN nivel solo si la
parte faltante no es el núcleo de la regla (y se explica); NO-VERIFICABLE y
CL-xx → INFORMATIVO.
