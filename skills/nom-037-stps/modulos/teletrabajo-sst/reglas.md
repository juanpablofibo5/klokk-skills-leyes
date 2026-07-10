# Reglas derivadas — módulo teletrabajo-sst (nom-037-stps)

Lógica sin ambigüedad. Cada regla se ancla a las fuentes de
[texto-legal.md](texto-legal.md) por ID (F-xx). Estados: **FIRME**,
**FIRME\*** (interpretación con pregunta abierta), **PENDIENTE** (fuente o
regulación no transcrita/publicada).

Las reglas RD-01 a RD-05 de este módulo corresponden a las reglas RD-08 a
RD-12 de la spec de origen (`specs/teletrabajo-v2-nom037-spec.md`). Ver
tabla de equivalencia al final.

| ID | Regla | Riesgo | Estado | Fuente |
|----|-------|--------|--------|--------|
| RD-01 | (ex RD-08) Listado de teletrabajadores: el patrón debe contar con un listado actualizado con al menos los incisos a) a k) del 5.1; es válido en archivo electrónico/digital; "actualizado" = refleja cada alta y baja de la modalidad; se compulsa contra nómina. El sistema auditado debe poder producir o alimentar sus campos operativos: quién está en modalidad, % de tiempo en teletrabajo (inciso f, calculado de asistencia), lugares de trabajo convenidos (inciso i, contra el lugar donde se marca) y equipo otorgado (inciso k, vía RD-05 del módulo teletrabajo (lft)); los demás campos (género, estado civil, domicilio, etc.) pueden vivir en otro sistema integrado. Conservación de versiones → CL-02. | Alto | FIRME | F-04, F-10; ver CL-02 |
| RD-02 | (ex RD-09) Desconexión de alcance completo: además del término de la jornada (RD-03 del módulo teletrabajo (lft)), el sistema debe poder detectar/alertar actividad o comunicación laboral en horarios no laborables, vacaciones, permisos y licencias, y — en horarios flexibles — durante las pausas convenidas. Cruza con los estados de ausencia que el sistema de asistencia ya registra. Qué acto constituye violación y qué evidencia guardar → CL-01. | Alto | FIRME* | F-02, F-05 (inciso e), F-09 (inciso e); ver CL-01 |
| RD-03 | (ex RD-10) Pausas y lactancia registrables: la política debe incluir pausas para descanso dentro del horario pactado, y para madres en lactancia (máx. 6 meses) el horario debe determinar 2 reposos extraordinarios de media hora por día O reducción de 1 hora de jornada — el sistema debe poder registrar estos eventos sin computarlos como incumplimiento de jornada. Qué es una pausa "adecuada" → CL-03. | Medio | FIRME* | F-05 (inciso e), F-06, F-09 (inciso d); ver CL-03 |
| RD-04 | (ex RD-11) Cambio de modalidad documentado: proceso de implementación presencial↔teletrabajo documentado, incluyendo los momentos/condiciones/causas de asistencia al centro de trabajo (5.6 b) y los mecanismos de reversibilidad (5.10); el sistema auditado registra el calendario híbrido pactado y evidencia su cumplimiento, ligado al historial de modalidad de RD-05 del módulo teletrabajo (lft). | Medio | FIRME | F-07, F-08 |
| RD-05 | (ex RD-12) Conservación de evidencias NOM: los registros digitales valen como evidencia y se conservan al menos UN AÑO (10.4). Es piso, no techo: para registros de jornada aplican los plazos mayores de la LFT (módulo conservacion-y-prueba (lft)) — el sistema aplica siempre el plazo más largo. | Medio | FIRME | F-11 |

\* FIRME por interpretación operativa: la obligación existe en el texto, pero
su aplicación exacta tiene una pregunta abierta registrada abajo.

**Nota — política de contacto (F-05, inciso d):** los mecanismos y reglas de
contacto de la Política de Teletrabajo deben garantizar el derecho a la
privacidad, no interferir en la relación trabajo-familia y ser proporcionales
a su objetivo. Complementa la supervisión proporcional de RD-04 del módulo
teletrabajo (lft): el sistema auditado que implemente notificaciones o
contacto con teletrabajadores debe respetar estas tres condiciones.

**Nota — horario pactado (F-05, inciso e):** la Política debe establecer la
duración del horario de labores pactado y/o la distribución convenida de los
horarios, sin exceder los máximos legales Y contractuales, incluyendo el
derecho a las pausas para descanso y a la desconexión. Complementa RD-02 del
módulo teletrabajo (lft) (mismos máximos que presenciales) y alimenta RD-02 y
RD-03 de esta skill.

## Casos límite y preguntas abiertas

CL-01 y CL-02 de este módulo son preguntas abiertas propias de la NOM.
CL-03 es nuevo (pausas "adecuadas"). Ver tabla de equivalencia para la
correspondencia con la spec de origen.

| ID | Caso o pregunta | Por qué es ambiguo | Estado | Quién resuelve |
|----|-----------------|--------------------|--------|----------------|
| CL-01 | ¿Qué constituye violación del derecho a la desconexión (mensajes, asignación de tareas, llamadas) y qué evidencia debe guardar el sistema? **Nota v2:** la NOM ya define CUÁNDO aplica (F-02: término de jornada, no laborables, vacaciones, permisos, licencias, pausas convenidas); sigue abierto QUÉ actos la violan. | El alcance temporal quedó definido por la NOM; el alcance material no. | abierta | abogado laboralista |
| CL-02 | ¿El "listado actualizado" (F-04) exige conservar el historial de versiones (altas/bajas con fecha) o solo el estado vigente? | El PEC define actualización como reflejar altas y bajas (F-10) y el 10.4 exige conservar evidencias un año (F-11), pero no dice si las versiones anteriores del listado son "evidencia". | abierta | abogado laboralista |
| CL-03 | ¿Qué son pausas "adecuadas" (F-09, inciso d) — duración, frecuencia — y cómo registrar las pausas convenidas de horarios flexibles sin que ese registro se vuelva supervisión desproporcionada (tensión con RD-04 del módulo teletrabajo (lft))? | La NOM no define "adecuadas" ni el nivel de granularidad exigible del registro de pausas. | abierta | abogado laboralista |

## Notas de fundamento (F no citadas en reglas)

Las siguientes F de texto-legal.md fundamentan el módulo pero no generan
reglas auditables directas en código:

- **F-01** (Numerales 1 y 2 — objetivo y campo de aplicación): La NOM rige
  en toda la República Mexicana y aplica a todos los centros de trabajo con
  personas en modalidad de Teletrabajo. Define el alcance normativo que
  justifica este módulo; la aplicabilidad concreta al software auditado la
  determina F1 del flujo. Sin F-01 el módulo no tiene campo de aplicación.
- **F-03** (Numeral 4.20 — definición de persona teletrabajadora): "Persona
  trabajadora que presta su servicio personal, remunerado y subordinado en
  lugar(es) fijo(s), distinto(s) al centro de trabajo, y utiliza las
  tecnologías de la información y la comunicación." Base para decidir quién
  cuenta en el listado NOM (RD-01) y cuándo la desconexión aplica (RD-02).
  La diferencia entre esta definición y el umbral del 40 % del Art. 330-A
  LFT es la esencia de CL-03 del módulo teletrabajo (lft).
- **F-12** (Transitorio PRIMERO — entrada en vigor): La NOM entró en vigor el
  05-12-2023 (publicación 08-06-2023 + 180 días naturales). Toda auditoría
  desde esa fecha puede reportar fallas como exigibles; antes de esa fecha
  no eran auditables. Cada reporte debe registrar la fecha auditada.

## Árbol de decisión de severidad

Aplica la regla global F2→severidad de skills/nom-037-stps/SKILL.md
(VIOLADA/AUSENTE → árbol tal cual; PARCIAL → árbol con posible atenuación de
un nivel si la parte faltante no es el núcleo; NO-VERIFICABLE/CL-xx →
INFORMATIVO).

```
Para cada regla del módulo teletrabajo-sst que FALLA (estado VIOLADA o AUSENTE):

  ¿Sin listado NOM o desactualizado, o desconexión sin cubrir todos sus
  periodos? (RD-01, RD-02)
     SÍ  -> ALTO
     NO  -> siguiente pregunta

  ¿Pausas/lactancia, modalidad/calendario híbrido o retención de evidencias
  sin registrar o sin documentar? (RD-03, RD-04, RD-05)
     SÍ  -> MEDIO

  CL-01 a CL-03 -> INFORMATIVO
```

Checklist de consistencia: RD-01, RD-02 = Alto ✓ · RD-03, RD-04, RD-05 =
Medio ✓ · CL-01 a CL-03 = Informativo ✓.

## Tabla de equivalencia con la spec de origen

La spec `specs/teletrabajo-v2-nom037-spec.md` numeraba las reglas NOM como
extensión de la skill teletrabajo (lft). Este módulo las renumera desde RD-01.
Las F de texto-legal.md también se renumeran respecto a la spec.

| ID en este módulo | ID en la spec (teletrabajo-v2-nom037-spec.md) | Notas |
|-------------------|----------------------------------------------|-------|
| RD-01 | RD-08 | Listado de teletrabajadores |
| RD-02 | RD-09 | Desconexión de alcance completo |
| RD-03 | RD-10 | Pausas y lactancia registrables |
| RD-04 | RD-11 | Cambio de modalidad documentado |
| RD-05 | RD-12 | Conservación de evidencias NOM |
| CL-01 | CL-02 | Qué actos violan la desconexión |
| CL-02 | CL-06 | Historial de versiones del listado |
| CL-03 | CL-07 | Pausas "adecuadas" y supervisión proporcional |

### F renumeradas (texto-legal.md de este módulo vs. spec)

| F en este módulo | F en la spec | Numeral NOM | D3 página |
|------------------|-------------|-------------|-----------|
| F-01 | F-08 | Numerales 1 y 2 (objetivo y campo de aplicación) | p. 5 |
| F-02 | F-09 | 4.11 Definición Desconexión | p. 6 |
| F-03 | F-10 | 4.20 Definición Persona teletrabajadora | p. 6 |
| F-04 | F-11 | 5.1 Listado de teletrabajadores | p. 7 |
| F-05 | F-12 | 5.2 Política de Teletrabajo (incisos d y e) | p. 8 |
| F-06 | F-13 | 5.2 inciso h) lactancia | p. 8 |
| F-07 | F-14 | 5.6 Proceso de implementación | p. 9 |
| F-08 | F-15 | 5.10 Reversibilidad | p. 10 |
| F-09 | F-16 | 7.3 Factores psicosociales (incisos d y e) | p. 12 |
| F-10 | F-17 | 10.3 PEC, fila 5.1, observaciones | p. 14 |
| F-11 | F-18 | 10.4 Conservación de evidencias | p. 26 |
| F-12 | F-19 | Transitorio PRIMERO | p. 26 |

Nota: Las reglas RD-01 a RD-07 de la spec permanecen en el módulo teletrabajo
(lft) sin renumerar. Las CL-01, CL-04 y CL-05 de la spec tampoco se
trasladan aquí: CL-01 (ventana del 40 %) y CL-04 (husos horarios) son
propias del módulo teletrabajo (lft); CL-05 (umbral de aplicación NOM) se
mantiene en teletrabajo (lft) como nota cruzada de RD-01 de ese módulo.
