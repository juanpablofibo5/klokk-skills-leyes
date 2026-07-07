# klokk-skills-leyes

Base de conocimiento legal versionada para **Klokk** — SaaS de control de
asistencia vía WhatsApp para PyMEs en México.

Cada **skill** es un documento Markdown que convierte una obligación legal
(LFT, NOMs, reglamentos) en reglas operativas que el producto puede
implementar: con su fuente exacta, su interpretación práctica, sus
ambigüedades conocidas y su fecha de última verificación.

> ⚠️ **Este repositorio no es asesoría legal.** Es la documentación interna de
> en qué se basan los cálculos de Klokk. Ninguna skill debe usarse en
> producción si su estado no es `verificada`. Una skill desactualizada se
> considera peligrosa, no solo inútil.

## ¿Por qué un repo separado del producto?

1. **Ritmo de cambio propio.** Las leyes cambian en fechas de publicación del
   DOF, no en sprints. Separado, el conocimiento legal se versiona a su ritmo.
2. **Ownership distinto.** Lo mantiene quien tiene el contexto legal (hoy el
   fundador; eventualmente un abogado laboral), sin tocar el código del
   producto.
3. **Auditable y reutilizable.** Si un cliente o una autoridad pregunta *"¿en
   qué se basa este cálculo?"*, la respuesta es una fuente de verdad
   versionada, con historial de cambios en git.

## Estructura

```
klokk-skills-leyes/
├── README.md                        ← este archivo: propósito, guía de uso e índice
├── plantillas/
│   └── plantilla-skill-legal.md     ← plantilla v1 (documento plano); pendiente su v2 Agent Skills
└── skills/
    └── registro-jornada/            ← una carpeta por skill, en formato Agent Skills
        ├── SKILL.md                 ← frontmatter parseable + instrucciones ejecutables
        ├── references/              ← texto legal, criterios de tribunales, reglas R1–R10
        └── assets/                  ← plantilla del reporte de salida
```

La plantilla vive fuera de `skills/` a propósito: así "consumir las skills"
es simplemente leer `skills/*/SKILL.md`, sin filtrar nada.

## Anatomía de una skill

Toda skill sigue cinco secciones fijas, siempre en este orden:

| Sección | Contenido | Regla de oro |
|---------|-----------|--------------|
| **(a) Fuente legal exacta** | Artículo, fracción, fecha de publicación en el DOF, link oficial y cita textual | Cero interpretación: solo el hecho verificable |
| **(b) Interpretación operativa** | Qué significa en la práctica para una empresa y para Klokk | Lenguaje claro, sin jerga jurídica |
| **(c) Reglas derivadas** | Lógica implementable, numerada (`RD-01`, `RD-02`…) | Cero ambigüedad: unidades, límites y redondeos explícitos |
| **(d) Casos límite y preguntas abiertas** | Dónde la ley es ambigua o falta que la autoridad defina algo (`CL-01`…) | Lo que no se sabe se registra, no se inventa |
| **(e) Estado y última revisión** | Historial de verificaciones contra fuente oficial | Toda revisión se registra, incluso sin cambios |

Además, cada skill abre con **frontmatter YAML** (`id`, `titulo`, `estado`,
`ultima_revision`, `revisado_por`): metadatos legibles por máquina, pensados
para que el repo principal de Klokk pueda consumir las skills
programáticamente sin parsear prosa.

**Trazabilidad:** las fuentes se identifican como `F-xx`, las reglas derivadas
como `RD-xx` y los casos límite como `CL-xx`. Cada RD cita las F que la
respaldan, y el código de Klokk podrá citar `<skill>/RD-xx` en cálculos y
tests. La cadena completa: **artículo → regla → código**.

### Formato v2 — Agent Skills (desde 2026-07-07)

A partir de la primera skill real (`registro-jornada`), las skills adoptan el
formato oficial de **Agent Skills**: una carpeta por skill con `SKILL.md`
(frontmatter `name`/`description`/`metadata` + instrucciones ejecutables),
`references/` para el contenido legal y `assets/` para plantillas de salida.
El punto de entrada programático es `skills/<skill>/SKILL.md`.

La anatomía (a)–(e) sigue siendo el checklist de contenido y se mapea así:
(a) → `references/texto-legal.md` · (b) → `SKILL.md` y
`references/criterios-tribunales.md` · (c) → `references/reglas.md` (con su
estado FIRME / PENDIENTE por regla) · (d) → reglas `FIRME*` y marcas
`PENDIENTE` · (e) → `metadata.reviewed_at` y la sección "Estado del contenido"
del `SKILL.md`. La plantilla v1 (`plantillas/plantilla-skill-legal.md`) queda
como referencia del formato documento hasta que exista su versión v2.

## Ciclo de vida de una skill

```
borrador ──→ en-verificacion ──→ verificada
                  ↑                   │ (reforma en el DOF, o revisión vencida)
                  │                   ↓
                  └──── requiere-actualizacion
```

- **borrador** — en redacción; puede contener `[corchetes]` sin resolver.
- **en-verificacion** — completa, pendiente de contraste contra el DOF.
- **verificada** — contrastada contra fuente oficial; la única apta para consumo.
- **requiere-actualizacion** — se publicó una reforma que la afecta, o su última revisión ya venció.

## Cómo leer y usar una skill

1. Mira el frontmatter: si `estado` no es `verificada`, detente ahí.
2. La sección (b) te dice qué significa; la (c) te da las reglas exactas para implementar.
3. Antes de implementar una RD, revisa la (d): puede haber un caso límite abierto que la afecte.
4. Ante cualquier duda de vigencia: la (a) tiene el link a la fuente oficial y la (e) el historial de revisiones.

## Cómo crear una skill nueva

1. Crea `skills/<tema>/` (kebab-case) siguiendo la estructura de
   `registro-jornada` — SKILL.md + references/ + assets/; mientras no exista
   la plantilla v2, esa skill es la referencia del formato. Una skill = un
   tema operativo (jornada, horas extra, aguinaldo…), no una ley completa.
2. Llénala siguiendo las instrucciones incluidas en la propia plantilla.
3. Toda afirmación legal se contrasta contra el DOF **antes** de marcar la
   skill como `verificada`.
4. Agrega su fila al índice de abajo y haz commits descriptivos: el historial
   de git es parte del valor auditable de este repo.

## Índice de skills

| Skill | Qué cubre | Estado | Última revisión |
|-------|-----------|--------|-----------------|
| [registro-jornada](skills/registro-jornada/SKILL.md) | Auditoría del registro electrónico de jornada — Art. 132 Fr. XXXIV LFT (DOF 2026-05-01) | en-verificacion | 2026-07-07 |
| [jornada-laboral](skills/jornada-laboral/SKILL.md) | Tipos de jornada y límites diario/semanal por año — Arts. 58–68 LFT + calendario 48→40 (2026–2030) | en-verificacion | 2026-07-07 |

<!-- Al agregar o revisar una skill, actualiza su fila. Este índice es el
     tablero de auditoría del repo. -->

## Consumo desde el repo principal de Klokk (futuro)

Decisión abierta. Opciones sobre la mesa:

- **Submódulo de git** — el repo del producto fija una versión exacta de las
  skills; cada build es auditable por commit.
- **Copia versionada por release** — un script sincroniza `skills/` hacia el
  repo principal y registra el commit de origen.
- **Lectura directa de metadatos** — tooling del producto (o un agente) lee
  `skills/*/SKILL.md` y usa el frontmatter para validar vigencia antes de
  confiar en una regla.

Las tres dependen de lo mismo, y por eso el formato importa más que el
mecanismo: frontmatter parseable, secciones fijas e IDs estables.

## Convenciones

- Español; fechas en formato ISO (`AAAA-MM-DD`); archivos en `kebab-case`.
- Una skill = un tema operativo, no una ley completa.
- No se guardan PDFs del DOF en el repo: se enlaza a la fuente oficial.
- IDs estables que nunca se reciclan: `F-xx`, `RD-xx`, `CL-xx`.
- Placeholders siempre `[entre corchetes]`; ninguno sobrevive en una skill `verificada`.
