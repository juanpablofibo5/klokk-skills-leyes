# Reglas derivadas — teletrabajo

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME**,
**FIRME\*** (interpretación con pregunta abierta), **PENDIENTE** (fuente o
regulación no transcrita/publicada).

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | Clasificación: si la relación se desarrolla más del 40 % del tiempo en el domicilio del trabajador (o el que eligió), es teletrabajo y aplican las obligaciones del capítulo; lo ocasional o esporádico NO es teletrabajo. La ventana de medición del 40 % → CL-01. | Crítico | FIRME* | F-01; ver CL-01 |
| RD-02 | La jornada del teletrabajador se pacta y registra con los MISMOS máximos legales que presenciales (duración y distribución de horarios en el contrato); el checador la registra con los mismos estándares. | Crítico | FIRME | F-02 |
| RD-03 | Derecho a la desconexión al término de la jornada: el sistema debe conocer el fin de jornada de cada teletrabajador y poder detectar/alertar actividad laboral posterior. Qué constituye violación exactamente → CL-02. | Alto | FIRME* | F-03 (fracc. VI); ver CL-02 |
| RD-04 | Supervisión proporcional: los mecanismos de monitoreo (incluido el checador) deben ser proporcionales, respetar intimidad y datos personales; cámaras y micrófonos solo de manera extraordinaria o por la naturaleza de las funciones. | Alto | FIRME | F-05 |
| RD-05 | Modalidad e historial: el cambio a teletrabajo es voluntario y por escrito, con derecho de reversibilidad; el sistema debe registrar la modalidad vigente de cada trabajador y su historial de cambios. | Medio | FIRME | F-04 |
| RD-06 | Registro de insumos entregados al teletrabajador (obligación patronal): el sistema debe poder registrarlo o integrarse con quien lo haga. | Medio | FIRME | F-03 (fracc. IV) |
| RD-07 | Requisitos específicos de seguridad y salud del teletrabajo (NOM del 330-J / NOM-037-STPS): NO auditar hasta transcribir la NOM contra su texto oficial (D-12). | — | PENDIENTE | F-06; ver CL-03 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

## Casos límite y preguntas abiertas

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿Sobre qué ventana se mide el "más del cuarenta por ciento del tiempo" (semana, mes, contrato)? ¿Y cómo se mide: días, horas? | El texto no define periodo ni unidad de medición. | abierta | abogado laboralista |
| CL-02 | ¿Qué constituye violación del derecho a la desconexión (mensajes, asignación de tareas, llamadas) y qué evidencia debe guardar el sistema? | La LFT enuncia el derecho sin definir su alcance operativo. | abierta | abogado laboralista |
| CL-03 | Requisitos específicos de la NOM-037-STPS (seguridad y salud en teletrabajo): pendientes de transcripción contra el texto oficial de la NOM. | Fuente aún no transcrita al repo (D-12); no se audita de memoria. | abierta | loop dedicado + abogado |
| CL-04 | Registro de jornada remota entre husos horarios distintos al del centro de trabajo. | Cross-ref: es el CL-03 de `jornada-laboral`; aplica con más frecuencia en teletrabajo. | abierta | decisión de producto + abogado |
