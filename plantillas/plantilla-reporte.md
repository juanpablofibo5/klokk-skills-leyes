# Plantilla de reporte de auditoría — v2 (formato del flujo F0–F5)

Formato estándar de salida de toda skill-ley de esta librería. Sustituye a la
plantilla v1 (que vivía en la skill registro-jornada; M-03). Los campos
`[entre corchetes]` se llenan en cada corrida; las secciones fijas propias de
cada módulo se agregan donde su guía lo indique.

---

```
AUDITORÍA DE COMPLIANCE — [Ley / norma y módulos corridos] sobre [repo target]

Fecha: [AAAA-MM-DD] · Commit auditado: [sha corto del repo target]
Librería: skills-leyes-mx [tag o commit] · Fuentes legales: [D-xx de FUENTES.md, con SHA-256]
Corrida anterior: [fecha del reporte previo, o "primera corrida"]

════════════════════════════════════════════════════════════════════

1. RESUMEN EJECUTIVO

   Veredicto por módulo: [módulo → CUMPLE / HALLAZGOS (n) / N-A]
   Los 3–5 hallazgos que más importan ahora:
   - [H-xx — una línea: qué, dónde, por qué duele]

2. APLICABILIDAD (F1)

   | Módulo | ¿Aplica? | Evidencia / razón |
   |--------|----------|-------------------|
   | [módulo] | APLICA / N-A | [señal encontrada o ausente, con ruta] |

3. HALLAZGOS (F2+F3) — por severidad: CRÍTICO → ALTO → MEDIO

   H-[nn] · [CRÍTICO|ALTO|MEDIO] · [RD-xx del módulo <tema>] · [PARCIAL|AUSENTE|VIOLADA]
   Qué exige la ley: [síntesis de la regla, con su F-xx]
   Qué hace el código: [comportamiento real observado]
   Evidencia: [archivo:línea, config, migración o test]
   [Si PARCIAL atenuado: qué parte falta y por qué no es el núcleo]

4. CUMPLE — el cumplimiento también se prueba

   | RD | Módulo | Evidencia de implementación |
   |----|--------|------------------------------|

5. INFORMATIVO

   - Casos límite aplicables: [CL-xx del módulo <tema> — pregunta abierta, quién la resuelve]
   - NO-VERIFICABLE: [reglas que el código disponible no permite decidir, y qué faltó]
   - Fuera de alcance declarado: [lo que la skill excluye por diseño]

6. PLAN DE REMEDIACIÓN (F4) — prioridad = severidad × exposición

   | # | H-xx | RD | Cambio propuesto | Dónde (en los patrones del repo) | Riesgo de ruptura | Orden |
   |---|------|----|------------------|----------------------------------|-------------------|-------|

   Notas de no-ruptura: [dependencias, migraciones de datos, qué se despliega solo]

7. DELTA vs corrida anterior

   Resueltos: [H-xx…] · Nuevos: [H-xx…] · Persistentes: [H-xx…]
   [O: "primera corrida — sin delta"]

════════════════════════════════════════════════════════════════════
Este reporte no es asesoría legal. Contenido legal en estado
en-verificacion (fase 3 con abogado laboralista pendiente); los CL-xx son
preguntas abiertas. Trazabilidad completa: F-xx → RD-xx → evidencia.
```

---

**Reglas de uso:** los H-xx se numeran por corrida y no se reciclan dentro de
ella; todo hallazgo cita su RD y su evidencia o no es hallazgo; las secciones
fijas por módulo (p. ej. "LÍMITES APLICADOS ESTE AÑO", "CLASIFICACIÓN
APLICADA") se insertan al final de la sección 3; la severidad sale del árbol
del módulo bajo la regla global F2→severidad (SKILL.md de la ley corrida); F5 solo procede
con aprobación explícita del dueño del repo.
