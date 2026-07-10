#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de skills-leyes-mx (v2 — estructura skill-por-ley, D-18/R2).

Estructura validada:
  skills/<ley>/SKILL.md                 frontmatter completo (name = carpeta)
  skills/<ley>/modulos/<tema>/          texto-legal.md + reglas.md + guia-auditoria.md

Qué valida:
  1. Frontmatter de cada skill-ley: name, description, version (semver),
     owner, reviewed_at (ISO, no futura; caducidad -> AVISO), ley, fuente.
  2. Cada módulo con sus 3 archivos; guia-auditoria.md con la tabla
     "Metadatos del módulo" y las secciones de Aplicabilidad y Procedencia.
  3. texto-legal.md: corchetes solo "[...]"; el marcador
     "(página: pendiente de pasada independiente — M-08)" es AVISO; IDs F-xx
     únicos; toda fila de tabla F con su cita textual.
  4. reglas.md: IDs de regla y CL únicos; estados (FIRME/FIRME*/PENDIENTE) y
     riesgos (Crítico/Alto/Medio/—) válidos; "ver CL-xx" resuelve en el
     archivo; F-xx sin calificar deben existir en el texto-legal del módulo.
  5. AVISO por citas F-xx huérfanas (ninguna regla/nota/guía las cita).
  6. Links internos relativos de SKILL.md y guias resuelven.
  7. ERROR si "klokk" (case-insensitive) aparece bajo skills/ (D-18).
  8. Guard de estados: ninguna skill `verificada` antes de la fase 3.
  9. Specs: cada módulo de lft mapea a specs/<tema>-spec.md APROBADA
     (allowlist SKILLS_SIN_SPEC); las skills en SPECS_EN_REVISION (D-20)
     aceptan banner BORRADOR hasta la revisión en bloque de JP.
 10. DECISIONES.md: IDs D-xx únicos y consecutivos.

Salida: exit 0 sin errores (avisos no fallan); exit 1 con errores.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOY = dt.date.today()

UMBRAL_CADUCIDAD_DIAS = 180  # provisional (D-17)

# Módulos cuya spec no vive en specs/ (spec externa; ver BITACORA).
SKILLS_SIN_SPEC = {"registro-jornada"}

# Skills construidas bajo D-20 cuya spec sigue en revisión en bloque de JP:
# se exige que la spec exista, pero se ACEPTA banner BORRADOR hasta su gate.
SPECS_EN_REVISION = {"nom-037-stps": "teletrabajo-v2-nom037-spec.md"}

MARCADOR_PAGINA = "(página: pendiente de pasada independiente — M-08)"
ESTADOS_REGLA = ("FIRME", "PENDIENTE")  # "FIRME*" contiene "FIRME"
RIESGOS = ("Crítico", "Alto", "Medio", "—")
CALIFICADORES = ("de la skill", "del módulo", "de la misma skill", "de ídem")

errores: list[str] = []
avisos: list[str] = []
# {ley: {módulo: {"F": set, "RD": set, "CL": set}}} — para resolver
# referencias calificadas entre módulos y skills.
REGISTRO: dict[str, dict[str, dict[str, set]]] = {}


def err(m): errores.append(m)
def warn(m): avisos.append(m)
def rel(p: Path) -> str: return str(p.relative_to(RAIZ))
def leer(p: Path) -> str: return p.read_text(encoding="utf-8")


def validar_frontmatter(skill_md: Path, carpeta: str) -> None:
    texto = leer(skill_md)
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        err(f"{rel(skill_md)}: sin frontmatter YAML al inicio")
        return
    fm = m.group(1)
    campos = {
        "name": r"^name:\s*(\S+)\s*$",
        "description": r"^description:\s*(\S.+)$",
        "version": r'^\s+version:\s*"([^"]+)"',
        "owner": r'^\s+owner:\s*"([^"]+)"',
        "reviewed_at": r'^\s+reviewed_at:\s*"(\d{4}-\d{2}-\d{2})"',
        "ley": r'^\s+ley:\s*"([^"]+)"',
        "fuente": r'^\s+fuente:\s*"([^"]+)"',
    }
    v: dict[str, str] = {}
    for campo, patron in campos.items():
        mm = re.search(patron, fm, re.M)
        if not mm:
            err(f"{rel(skill_md)}: frontmatter sin campo obligatorio `{campo}`")
        else:
            v[campo] = mm.group(1)
    if v.get("name") and v["name"] != carpeta:
        err(f"{rel(skill_md)}: name `{v['name']}` ≠ carpeta `{carpeta}`")
    if v.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", v["version"]):
        err(f"{rel(skill_md)}: version `{v['version']}` no es semver")
    if v.get("reviewed_at"):
        fecha = dt.date.fromisoformat(v["reviewed_at"])
        if fecha > HOY:
            err(f"{rel(skill_md)}: reviewed_at `{fecha}` en el futuro")
        elif (HOY - fecha).days > UMBRAL_CADUCIDAD_DIAS:
            warn(f"{rel(skill_md)}: revisión de hace {(HOY - fecha).days} días "
                 f"(> {UMBRAL_CADUCIDAD_DIAS}) — tratar como requiere-actualizacion")


def validar_texto_legal(path: Path) -> set[str]:
    texto = leer(path)
    if MARCADOR_PAGINA in texto:
        warn(f"{rel(path)}: páginas pendientes de pasada independiente (M-08)")
    for m in re.finditer(r"\[([^\]]*)\]", texto):
        if m.group(1) != "..." and not (path.parent / m.group(1)).exists():
            err(f"{rel(path)}: corchetes sin resolver: `[{m.group(1)[:40]}]`")
    citas = re.findall(r"^\*\*F-(\d{2})", texto, re.M)
    tabla = re.findall(r"^\|\s*F-(\d{2})\s*\|", texto, re.M)
    dup = {x for x in citas if citas.count(x) > 1}
    if dup:
        err(f"{rel(path)}: IDs F duplicados en citas: {sorted(dup)}")
    sin_cita = set(tabla) - set(citas)
    if sin_cita:
        err(f"{rel(path)}: filas de tabla sin cita textual: {sorted('F-' + x for x in sin_cita)}")
    return {f"F-{x}" for x in citas}


def ref_calificada(texto: str, fin: int) -> bool:
    return any(c in texto[fin:fin + 40] for c in CALIFICADORES)


EQUIVALENCIA = re.compile(r"^\|\s*(?:F|RD|CL)-\d{2}\s*\|\s*(?:F|RD|CL)-\d{2}\s*\|")


def es_fila_regla(linea: str) -> bool:
    # Fila de regla/CL: tabla de >= 4 columnas cuya segunda celda es prosa.
    # Las tablas de equivalencia (segunda celda = solo otro ID) se excluyen;
    # el formato de registro-jornada (4 columnas, sin Fuente) se acepta.
    return linea.count("|") >= 5 and not EQUIVALENCIA.match(linea)


def validar_reglas(path: Path, fuentes: set[str], guia_texto: str) -> None:
    texto = leer(path)
    lineas = texto.splitlines()
    filas = [m.group(1) for l in lineas if es_fila_regla(l)
             for m in [re.match(r"^\|\s*(RD-\d{2})\s*\|", l)] if m]
    dup = {x for x in filas if filas.count(x) > 1}
    if dup:
        err(f"{rel(path)}: IDs de regla duplicados: {sorted(dup)}")
    cls = set()
    for linea in lineas:
        if not es_fila_regla(linea):
            continue
        if re.match(r"^\|\s*RD-\d{2}\s*\|", linea):
            if not any(e in linea for e in ESTADOS_REGLA):
                err(f"{rel(path)}: fila de regla sin estado válido: `{linea[:70]}…`")
            if not any(r in linea for r in RIESGOS):
                err(f"{rel(path)}: fila de regla sin riesgo válido: `{linea[:70]}…`")
        m = re.match(r"^\|\s*(CL-\d{2})\s*\|", linea)
        if m:
            cls.add(m.group(1))
            if not ("abierta" in linea or "resuelta" in linea):
                err(f"{rel(path)}: fila de CL sin estado abierta/resuelta: `{linea[:70]}…`")
    for linea in lineas:
        # filas de equivalencia (ID | ID | …) documentan numeración de la
        # spec: no se validan como citas del módulo
        if re.match(r"^\| (?:F|RD|CL)-\d{2} \| (?:F|RD|CL)-\d{2} \|", linea):
            continue
        for m in re.finditer(r"F-\d{2}", linea):
            if fuentes and m.group(0) not in fuentes and not ref_calificada(linea, m.end()):
                err(f"{rel(path)}: cita {m.group(0)} sin calificar y no existe en texto-legal.md")
        for m in re.finditer(r"ver (CL-\d{2})", linea):
            if m.group(1) not in cls and not ref_calificada(linea, m.end()):
                err(f"{rel(path)}: `ver {m.group(1)}` sin CL correspondiente en el archivo")
    citadas = set(re.findall(r"F-\d{2}", texto)) | set(re.findall(r"F-\d{2}", guia_texto))
    for f in sorted(fuentes - citadas):
        warn(f"{rel(path.parent / 'texto-legal.md')}: cita {f} huérfana (ninguna regla/guía la usa)")
    return ({f"RD-{x}" for x in re.findall(r"^\|\s*RD-(\d{2})\s*\|", texto, re.M)
             if any(es_fila_regla(l) and re.match(rf"^\|\s*RD-{x}\s*\|", l) for l in lineas)},
            cls)


def validar_guia(path: Path) -> None:
    texto = leer(path)
    if "Metadatos del módulo" not in texto:
        err(f"{rel(path)}: sin tabla 'Metadatos del módulo'")
    else:
        for campo in ("version", "reviewed_at", "ley", "fuente"):
            if not re.search(rf"^\| {campo} \|", texto, re.M):
                err(f"{rel(path)}: Metadatos sin fila `{campo}`")
    for seccion in ("Aplicabilidad", "Procedencia"):
        if seccion.lower() not in texto.lower():
            err(f"{rel(path)}: sin sección '{seccion}'")


def validar_links(path: Path) -> None:
    texto = leer(path)
    for destino in re.findall(r"\]\((?!https?://)([^)#\s]+)\)", texto):
        if not (path.parent / destino).resolve().exists():
            err(f"{rel(path)}: link interno roto -> `{destino}`")


def validar_ley(carpeta: Path) -> list[str]:
    nombre = carpeta.name
    skill_md = carpeta / "SKILL.md"
    if not skill_md.exists():
        err(f"skills/{nombre}: falta SKILL.md")
        return []
    validar_frontmatter(skill_md, nombre)
    validar_links(skill_md)
    modulos_dir = carpeta / "modulos"
    if not modulos_dir.is_dir():
        err(f"skills/{nombre}: falta el directorio modulos/")
        return []
    modulos = []
    skill_texto = leer(skill_md)
    for mod in sorted(p for p in modulos_dir.iterdir() if p.is_dir()):
        modulos.append(mod.name)
        tl, rg, ga = mod / "texto-legal.md", mod / "reglas.md", mod / "guia-auditoria.md"
        for f in (tl, rg, ga):
            if not f.exists():
                err(f"{rel(mod)}: falta {f.name}")
        fuentes = validar_texto_legal(tl) if tl.exists() else set()
        guia_texto = leer(ga) if ga.exists() else ""
        rds, cls = (set(), set())
        if rg.exists():
            rds, cls = validar_reglas(rg, fuentes, guia_texto)
        REGISTRO.setdefault(nombre, {})[mod.name] = {"F": fuentes, "RD": rds, "CL": cls}
        if ga.exists():
            validar_guia(ga)
            validar_links(ga)
        if mod.name not in skill_texto:
            err(f"skills/{nombre}/SKILL.md: el módulo `{mod.name}` no está indexado")
    return modulos


PATRON_DESTINO = re.compile(
    r"de(?:l\s+módulo|\s+la\s+skill)\s+([a-z0-9][a-z0-9-]*)(?:\s*\(([a-z0-9-]+)\))?")


def conjuntos_destino(nombre: str, ley_suf: str | None):
    if ley_suf and nombre in REGISTRO.get(ley_suf, {}):
        return REGISTRO[ley_suf][nombre]
    for mods in REGISTRO.values():
        if nombre in mods:
            return mods[nombre]
    if nombre in REGISTRO:  # skill-ley completa: unión de sus módulos
        u = {"F": set(), "RD": set(), "CL": set()}
        for s in REGISTRO[nombre].values():
            for k in u:
                u[k] |= s[k]
        return u
    return None


def validar_refs_calificadas() -> None:
    """Resuelve refs tipo 'RD-09 del módulo registro-jornada (lft)' o
    'F-02 de la skill nom-037-stps' en todo skills/. Las contextuales
    ('de ese módulo', 'de la misma skill') no se resuelven estáticamente."""
    for p in sorted((RAIZ / "skills").rglob("*.md")):
        texto = leer(p)
        for m in re.finditer(r"\b(F|RD|CL)-(\d{2})\b", texto):
            cola = re.sub(r"\s+", " ", texto[m.end():m.end() + 80])
            d = PATRON_DESTINO.search(cola[:60])
            if not d or d.start() > 20:
                continue
            tid = f"{m.group(1)}-{m.group(2)}"
            destino = conjuntos_destino(d.group(1), d.group(2))
            if destino is None:
                err(f"{rel(p)}: referencia `{tid} … {d.group(0).strip()}` a un "
                    f"destino inexistente")
            elif tid not in destino[m.group(1)]:
                err(f"{rel(p)}: `{tid} {d.group(0).strip()}` — ese ID no existe "
                    f"en el destino")


def validar_globales(leyes: dict[str, list[str]]) -> None:
    for p in sorted((RAIZ / "skills").rglob("*.md")):
        if re.search(r"klokk", leer(p), re.I):
            err(f"{rel(p)}: contiene 'Klokk' — la librería es agnóstica (D-18)")
    readme = leer(RAIZ / "README.md")
    if re.search(r"\|\s*verificada\s*\|", readme):
        err("README.md: estado `verificada` — BLOQUEADO hasta la fase 3 "
            "(si la fase 3 ya ocurrió, actualiza este guard con su D-xx)")
    for ley in leyes:
        if f"skills/{ley}/" not in readme and f"skills/{ley})" not in readme:
            err(f"README.md: la skill-ley `{ley}` no está indexada")
    for ley, spec in SPECS_EN_REVISION.items():
        s = RAIZ / "specs" / spec
        if ley in leyes and not s.exists():
            err(f"specs/: falta {spec} (SPECS_EN_REVISION, D-20)")
    for mod in leyes.get("lft", []):
        if mod in SKILLS_SIN_SPEC:
            continue
        s = RAIZ / "specs" / f"{mod}-spec.md"
        if not s.exists():
            err(f"specs/: falta {mod}-spec.md para el módulo construido")
        elif "APROBADA" not in leer(s):
            err(f"{rel(s)}: módulo construido con spec sin APROBADA")
    texto = leer(RAIZ / "DECISIONES.md")
    ids = [int(x) for x in re.findall(r"^\| D-(\d{2}) \|", texto, re.M)]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        err(f"DECISIONES.md: IDs duplicados: {sorted('D-%02d' % x for x in dup)}")
    if ids and ids != list(range(1, len(ids) + 1)):
        err("DECISIONES.md: los IDs D-xx no son consecutivos desde D-01")


def main() -> int:
    for archivo in ("CLAUDE.md", "README.md", "BACKLOG.md", "STATUS.md",
                    "DECISIONES.md", "BITACORA.md", "FUENTES.md",
                    "plantillas/flujo-auditoria-codigo.md",
                    "plantillas/plantilla-reporte.md"):
        if not (RAIZ / archivo).exists():
            err(f"falta el archivo {archivo}")

    leyes: dict[str, list[str]] = {}
    for carpeta in sorted(p for p in (RAIZ / "skills").iterdir() if p.is_dir()):
        leyes[carpeta.name] = validar_ley(carpeta)
    validar_refs_calificadas()
    validar_globales(leyes)

    total_mod = sum(len(m) for m in leyes.values())
    print(f"Validadas {len(leyes)} skills-ley ({', '.join(leyes)}) con {total_mod} módulos\n")
    for a in avisos:
        print(f"  AVISO  {a}")
    for e in errores:
        print(f"  ERROR  {e}")
    print(f"\nResultado: {len(errores)} errores, {len(avisos)} avisos.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
