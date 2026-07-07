# CLAUDE.md — kernel de trabajo de klokk-skills-leyes

Base de conocimiento legal de Klokk (control de asistencia vía WhatsApp).
Contexto completo en [README.md](README.md); catálogo y pipeline en
[BACKLOG.md](BACKLOG.md).

## Reglas duras (no negociables)

1. **Cero contenido legal sin fuente oficial descargada.** Toda cita legal se
   transcribe de un documento oficial (diputados.gob.mx / DOF) descargado en
   la sesión, y se cita con documento + página. Nunca de memoria, nunca
   parafraseado.
2. **Lo que no se sabe se registra como caso límite (CL-xx)** — jamás se
   resuelve inventando. Los CL los cierra el abogado o la autoridad.
3. **Placeholders siempre `[entre corchetes]`**; ninguno sobrevive en una
   skill `verificada`.
4. **Estados:** ninguna skill sube a `verificada` sin la fase 3 (abogado
   laboralista, sobre la librería completa). Hasta entonces: `en-verificacion`.
5. **Todo cambio queda en GitHub:** commits ordenados y descriptivos por paso,
   push al cerrar cada loop.
6. **Toda decisión** (de formato, alcance, lógica de severidad, proceso) se
   registra en [DECISIONES.md](DECISIONES.md). **Toda sesión** deja entrada en
   [BITACORA.md](BITACORA.md). El estado vivo está en [STATUS.md](STATUS.md).

## Protocolo de loop por fase

Cada fase del pipeline se trabaja como un loop auditable:

```
EJECUTAR la fase
  → VERIFICAR contra el checklist de la fase (abajo)
  → DOCUMENTAR: STATUS.md + BITACORA.md (+ DECISIONES.md si hubo decisión)
  → COMMIT + PUSH
  → GATE: no se avanza de fase sin cumplir el gate
```

**Checklist fase 1 (investigación → spec):**
- [ ] Citas íntegras con documento oficial + página por cada F-xx
- [ ] Los 9 requisitos de `plantillas/brief-investigacion-skill.md` cumplidos
- [ ] Consistencia árbol / tabla de riesgos / casos de prueba verificada
- [ ] Casos límite (CL-xx) registrados, nunca resueltos inventando
- [ ] Spec con banner BORRADOR → **gate: visto bueno de JP**

**Checklist fase 2 (construcción):**
- [ ] Estructura EXACTA de la sección 8 de la spec aprobada
- [ ] Solo contenido de la spec — nada inventado
- [ ] Casos de prueba corridos mentalmente y reportados → **gate: N/N ✓**
- [ ] Índices actualizados: README, BACKLOG, STATUS, BITACORA

**Checklist fase 3 (validación legal):**
- [ ] Revisión del abogado sobre la librería completa (reglas FIRME* y CL-xx
      primero)
- [ ] Estados a `verificada` + DECISIONES.md actualizado con lo resuelto

## Formato de skills

Formato v2 — Agent Skills: carpeta por skill con `SKILL.md` + `references/`
(+ `assets/` solo si tiene plantillas propias). Detalle y mapeo con la
anatomía (a)–(e) en el README. La skill de referencia es
`skills/jornada-laboral/`.
