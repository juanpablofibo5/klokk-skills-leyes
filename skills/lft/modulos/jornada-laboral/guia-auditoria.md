# Guía de auditoría — módulo jornada-laboral (lft)

## Metadatos del módulo

| Campo | Valor |
|-------|-------|
| version | 1.0.0 |
| reviewed_at | 2026-07-07 |
| ley | LFT Arts. 58-64 y 68; Transitorios Segundo y Séptimo del decreto DOF 2026-05-01 |
| fuente | LFT consolidada (última reforma DOF 2026-05-14) + decreto DOF 2026-05-01 |

## Qué hace este módulo / Por qué importa / Cuándo se activa / Frontera

**Qué hace:** clasifica los tipos de jornada (diurna / nocturna / mixta) y
valida los límites de duración — diario por tipo, semanal por año (calendario
48→40) y el techo absoluto de 12 horas diarias — para que el sistema auditado
calcule y alerte correctamente sobre las jornadas registradas.

**Por qué importa:** es la tabla de límites que da sentido al registro del
Art. 132 Fr. XXXIV. El módulo hermano `registro-jornada` audita CÓMO se
registra; éste define CUÁNTO puede durar lo registrado. Un límite mal
configurado (tipo de turno mal clasificado, o tabla del año equivocado)
corrompe todos los cálculos de cumplimiento y de tiempo extraordinario.

**Cuándo se activa:** al clasificar turnos, validar duraciones de jornada,
determinar cuándo el tiempo pasa a ser extraordinario, o auditar la
configuración de límites de un sistema de control de tiempo.

**Frontera con `horas-extra`:** este módulo define los límites ordinarios y el
umbral donde el tiempo se vuelve extraordinario. El régimen del tiempo
extraordinario (pagos +100 %/+200 %, calendario 9/9/10/11/12, distribución
4h×4 días, siniestros de los Arts. 65 y 67) pertenece al módulo `horas-extra`.
Comparten una regla: el techo de 12 horas diarias (Art. 68, párrafo tercero).

## Capa interpretativa

**Deliberadamente mínima.** No se citan tesis ni criterios jurisprudenciales
de memoria; si el abogado (fase 3) aporta criterios sobre jornada (p. ej.
sobre el cómputo del tiempo a disposición o la distribución por acuerdo), se
agregan aquí con su fuente. Lo que sí es interpretación operativa razonable,
marcada FIRME*, vive en las reglas — con sus dudas registradas como casos
límite.

Dos lecturas operativas que fundamentan reglas:

- **El tiempo a disposición cuenta (F-07):** para un sistema de control de
  asistencia, la comida fichada dentro del centro sin posibilidad de salir es
  tiempo efectivo de jornada. Impacta directamente el conteo de horas del
  sistema auditado.
- **La clasificación de turno es la puerta de todos los límites (F-03):** la
  regla de las 3.5 horas nocturnas decide si un turno vespertino es mixta o
  nocturna, y con ello su límite diario (7.5 vs 7 horas).

## Aplicabilidad (F1)

Señales de que este módulo APLICA al repo auditado:

**Positivas** — el repo contiene alguna de estas superficies:
- Tablas o modelos con nombres como `shifts`, `schedules`, `turnos`,
  `jornadas`, `work_hours`, `time_entries`, `attendance_records`.
- Campos como `start_time` / `end_time` / `duration_minutes` /
  `shift_type` / `turno_tipo` asociados a registros de empleados.
- Lógica que clasifica turnos (diurno/nocturno/mixto) o que compara duraciones
  contra límites configurables.
- Endpoints o jobs que calculan horas trabajadas, generan alertas de jornada o
  exportan datos de asistencia.
- Configuraciones o constantes con valores de horas máximas (8, 7, 7.5, 48,
  40, 12 o similares).
- Greps sugeridos: `grep -ri "shift_type\|turno\|jornada\|max_hours\|weekly_limit"`,
  `grep -ri "diurna\|nocturna\|mixta"`.

**Negativas** — el módulo es N/A si:
- El repo no gestiona tiempo trabajado ni asistencia de personas (p. ej. es
  un servicio de pagos, un CMS, una API pública sin empleados).
- No existe ninguna superficie de registro de entrada/salida o duración de
  jornada en modelos, migraciones ni endpoints.
- Grep de los términos anteriores da cero coincidencias en todo el repo.

## Superficies a revisar (F2)

Dónde buscar cada RD en un repo típico:

| RD | Dónde buscar en el código |
|----|--------------------------|
| RD-01 | Lógica de clasificación de turno; constantes o enums `SHIFT_TYPE`; funciones que deciden diurno/nocturno/mixto según horario. |
| RD-02 | Constantes de límites diarios (8h, 7h, 7.5h); validaciones al registrar o calcular jornada; tests de duración máxima. |
| RD-03 | Tabla o config de límite semanal; cómo se obtiene el año auditado; si el valor es hardcoded o parametrizable. |
| RD-04 | Validación de techo 12h (suma ordinaria + extraordinaria); alertas de jornada total. |
| RD-05 | Cálculo del umbral de tiempo extraordinario; dónde se traspasa el candidato a horas-extra. |
| RD-06 | Lógica de descanso en jornada continua; si se descuenta o se computa el break de 30 minutos. |
| RD-07 | Config de tiempo de comida; si el sistema permite o fuerza descuento del período de comida. |
| RD-08 | Modelos/formularios que registren distribución pactada de jornada semanal. |
| RD-09 | Lógica de recálculo de salario-hora al cambiar de año de calendario; alertas de protección salarial. |

## Guía de auditoría del módulo

1. **Determinar el año auditado** y cargar el límite semanal vigente (RD-03);
   verificar si el código lo obtiene dinámicamente o tiene un valor hardcoded.
2. **Clasificar cada turno** buscando la lógica de RD-01; en turnos que
   crucen medianoche, registrar el hallazgo de CL-03 sobre el método de
   cómputo.
3. **Validar el límite diario** de cada jornada contra su tipo (RD-02);
   buscar tests o validaciones existentes.
4. **Acumular la semana** y validar contra el límite del año (RD-03); verificar
   si el acumulador reseta correctamente.
5. **Marcar excedentes** diarios o semanales como candidatos a tiempo
   extraordinario y verificar que se delegan al módulo `horas-extra` (RD-05).
6. **Verificar el techo absoluto** de 12 horas/día sumando ordinaria +
   extraordinaria (RD-04).
7. **Auditar el cómputo de descansos:** media hora en jornada continua
   (RD-06) y tiempo a disposición contado como efectivo (RD-07).
8. **Verificar la representación de distribuciones pactadas** (RD-08) y la
   alerta de protección salarial (RD-09).
9. **Generar el reporte** con el formato de
   `../../../../plantillas/plantilla-reporte.md`, marcando los CL abiertos
   que apliquen.

## Secciones fijas del reporte de este módulo

El reporte de auditoría incluye, además de las secciones estándar de la
plantilla, la siguiente sección fija:

```
LÍMITES APLICADOS ESTE AÑO: [tabla del año auditado]
```

Encabezado del reporte:

```
AUDITORÍA DE COMPLIANCE — Jornada laboral (Arts. 58–68 LFT)
```

## Límites del módulo

- No calcula pagos de tiempo extraordinario — eso es del módulo `horas-extra`.
- No cubre jornadas especiales (personas menores de edad, sectores con
  regulación propia); si el alcance las detecta, lo declara y se detiene.
- No resuelve los CL abiertos: los reporta como INFORMATIVO.
- No es asesoría legal formal; lo declara en cada salida.
- Se revisa cuando cambie el año de calendario (límite semanal nuevo) o
  cuando el abogado resuelva CL-01–CL-04.

## Procedencia y estado

Citas de los Arts. 58–68 transcritas el 2026-07-07 directamente del PDF
oficial de la LFT consolidada (diputados.gob.mx, portada: "Última Reforma DOF
14-05-2026"), pp. 21–22, y transitorios del decreto oficial
(`LFT_ref52_01may26.pdf`, DOF 1-may-2026 edición vespertina), pp. 3–4. Los
textos del decreto y de la consolidada coinciden entre sí en los artículos
reformados. Spec de origen: `specs/jornada-laboral-spec.md`, aprobada por JP
el 2026-07-07.

**Pendiente para el abogado (fase 3):** CL-01 a CL-04 y las reglas FIRME*.
La capa jurisprudencial está deliberadamente vacía: no se citaron criterios
de memoria. Cuando el abogado resuelva los CL o cambie el año de calendario,
esta skill se revisa y sube su `version` y `reviewed_at`.
