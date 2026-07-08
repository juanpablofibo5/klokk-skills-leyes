#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de klokk-skills-leyes — hace cumplir en CI las reglas del kernel
(CLAUDE.md). Corre local (`python3 tools/validar.py`) y en GitHub Actions en
cada push.

Qué valida:
  1. Estructura por skill: SKILL.md + references/texto-legal.md + reglas.md.
  2. Frontmatter completo: name (= carpeta), description, version, owner,
     reviewed_at (fecha ISO, no futura), ley, fuente.
  3. Caducidad: reviewed_at más viejo que el umbral -> AVISO (umbral
     provisional, D-17; el formal lo definirá JP/abogado).
  4. texto-legal.md: cero corchetes sin resolver (solo "[...]" de omisión en
     citas); IDs F-xx únicos y consistentes entre tabla y citas.
  5. reglas.md: IDs de regla únicos; cada fila con estado (FIRME/FIRME*/
     PENDIENTE) y riesgo (Crítico/Alto/Medio/—) válidos; "ver CL-xx" apunta a
     un CL existente; F-xx citadas existen en texto-legal.md.
  6. Links internos de SKILL.md resuelven a archivos existentes.
  7. Índices: toda skill aparece en README y BACKLOG; ninguna skill en estado
     `verificada` (BLOQUEADO hasta la fase 3 con abogado — al completarla,
     actualiza este guard junto con la decisión D-xx correspondiente).
  8. Specs: toda skill (salvo las de spec externa) tiene specs/<name>-spec.md
     con banner APROBADA (nunca BORRADOR/🟡 con la skill ya construida).
  9. DECISIONES.md: IDs D-xx únicos y consecutivos.

Salida: exit 0 sin errores (avisos no fallan); exit 1 con errores.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOY = dt.date.today()

# Umbral PROVISIONAL de caducidad (ver D-17): genera AVISO, no error, hasta
# que el umbral formal quede definido (la plantilla lo marca pendiente).
UMBRAL_CADUCIDAD_DIAS = 180

# Skills cuya spec no vive en specs/ (spec externa; documentado en BITACORA).
SKILLS_SIN_SPEC = {"registro-jornada"}

ESTADOS_REGLA = ("FIRME", "PENDIENTE")  # "FIRME*" contiene "FIRME"
RIESGOS = ("Crítico", "Alto", "Medio", "—")

errores: list[str] = []
avisos: list[str] = []


def err(msg: str) -> None:
    errores.append(msg)


def warn(msg: str) -> None:
    avisos.append(msg)


def rel(p: Path) -> str:
    return str(p.relative_to(RAIZ))


def leer(p: Path) -> str:
    return p.read_text(encoding="utf-8")


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
    valores: dict[str, str] = {}
    for campo, patron in campos.items():
        mm = re.search(patron, fm, re.M)
        if not mm:
            err(f"{rel(skill_md)}: frontmatter sin campo obligatorio `{campo}`")
        else:
            valores[campo] = mm.group(1)

    if valores.get("name") and valores["name"] != carpeta:
        err(
            f"{rel(skill_md)}: name `{valores['name']}` no coincide con la "
            f"carpeta `{carpeta}`"
        )
    if valores.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", valores["version"]):
        err(f"{rel(skill_md)}: version `{valores['version']}` no es semver X.Y.Z")
    if valores.get("reviewed_at"):
        fecha = dt.date.fromisoformat(valores["reviewed_at"])
        if fecha > HOY:
            err(f"{rel(skill_md)}: reviewed_at `{fecha}` está en el futuro")
        elif (HOY - fecha).days > UMBRAL_CADUCIDAD_DIAS:
            warn(
                f"{rel(skill_md)}: revisión con {(HOY - fecha).days} días de "
                f"antigüedad (> umbral provisional de {UMBRAL_CADUCIDAD_DIAS}) "
                f"— tratar como requiere-actualizacion"
            )


def validar_texto_legal(path: Path) -> set[str]:
    texto = leer(path)
    for m in re.finditer(r"\[([^\]]*)\]", texto):
        if m.group(1) != "...":
            err(
                f"{rel(path)}: corchetes sin resolver en texto legal: "
                f"`[{m.group(1)[:40]}]` (solo se permite \"[...]\" de omisión)"
            )
    citas = re.findall(r"^\*\*F-(\d{2})", texto, re.M)
    tabla = re.findall(r"^\| F-(\d{2}) \|", texto, re.M)
    dup = {x for x in citas if citas.count(x) > 1}
    if dup:
        err(f"{rel(path)}: IDs F duplicados en citas: {sorted(dup)}")
    # La tabla lista los artículos (D1); los transitorios (D2) se citan sin
    # fila de tabla. Regla: toda fila de tabla debe tener su cita textual.
    sin_cita = set(tabla) - set(citas)
    if sin_cita:
        err(
            f"{rel(path)}: filas de tabla sin cita textual: "
            f"{sorted('F-' + x for x in sin_cita)}"
        )
    return {f"F-{x}" for x in citas}


def validar_reglas(path: Path, fuentes: set[str]) -> None:
    texto = leer(path)
    filas_rd = re.findall(r"^\| ((?:RD-\d{2}|R\d{1,2})) \|.*$", texto, re.M)
    dup = {x for x in filas_rd if filas_rd.count(x) > 1}
    if dup:
        err(f"{rel(path)}: IDs de regla duplicados: {sorted(dup)}")
    for linea in texto.splitlines():
        if re.match(r"^\| (?:RD-\d{2}|R\d{1,2}) \|", linea):
            if not any(e in linea for e in ESTADOS_REGLA):
                err(f"{rel(path)}: fila de regla sin estado válido: `{linea[:70]}…`")
            if not any(r in linea for r in RIESGOS):
                err(f"{rel(path)}: fila de regla sin riesgo válido: `{linea[:70]}…`")
            for f_ref in re.findall(r"F-\d{2}", linea):
                if fuentes and f_ref not in fuentes:
                    err(f"{rel(path)}: la regla cita {f_ref}, que no existe en texto-legal.md")
    cls = set(re.findall(r"^\| (CL-\d{2}) \|", texto, re.M))
    for ref in re.findall(r"ver (CL-\d{2})", texto):
        if ref not in cls:
            err(f"{rel(path)}: referencia `ver {ref}` sin CL correspondiente en el archivo")
    for linea in texto.splitlines():
        if re.match(r"^\| CL-\d{2} \|", linea):
            if not ("abierta" in linea or "resuelta" in linea):
                err(f"{rel(path)}: fila de CL sin estado abierta/resuelta: `{linea[:70]}…`")


def validar_links(skill_md: Path) -> None:
    texto = leer(skill_md)
    for destino in re.findall(r"\]\((?!https?://)([^)#\s]+)\)", texto):
        if not (skill_md.parent / destino).resolve().exists():
            err(f"{rel(skill_md)}: link interno roto -> `{destino}`")


def validar_skill(carpeta: Path) -> None:
    nombre = carpeta.name
    skill_md = carpeta / "SKILL.md"
    texto_legal = carpeta / "references" / "texto-legal.md"
    reglas = carpeta / "references" / "reglas.md"
    for obligatorio in (skill_md, texto_legal, reglas):
        if not obligatorio.exists():
            err(f"skills/{nombre}: falta {obligatorio.name}")
    if not skill_md.exists():
        return
    validar_frontmatter(skill_md, nombre)
    validar_links(skill_md)
    fuentes = validar_texto_legal(texto_legal) if texto_legal.exists() else set()
    if reglas.exists():
        validar_reglas(reglas, fuentes)


def validar_indices(nombres: list[str]) -> None:
    readme = leer(RAIZ / "README.md")
    backlog = leer(RAIZ / "BACKLOG.md")
    for nombre in nombres:
        if f"skills/{nombre}/SKILL.md" not in readme:
            err(f"README.md: la skill `{nombre}` no está en el índice")
        if nombre not in backlog:
            err(f"BACKLOG.md: la skill `{nombre}` no aparece")
    if re.search(r"\|\s*verificada\s*\|", readme):
        err(
            "README.md: hay una skill en estado `verificada` — BLOQUEADO hasta "
            "la fase 3 con abogado (si la fase 3 ya ocurrió, actualiza este "
            "guard junto con su decisión D-xx)"
        )


def validar_specs(nombres: list[str]) -> None:
    for nombre in nombres:
        if nombre in SKILLS_SIN_SPEC:
            continue
        spec = RAIZ / "specs" / f"{nombre}-spec.md"
        if not spec.exists():
            err(f"specs/: falta {nombre}-spec.md para una skill construida")
            continue
        texto = leer(spec)
        if "APROBADA" not in texto:
            err(f"{rel(spec)}: la skill está construida pero la spec no dice APROBADA")
        if "BORRADOR" in texto or "🟡" in texto:
            err(f"{rel(spec)}: banner BORRADOR/🟡 con la skill ya construida")


def validar_decisiones() -> None:
    texto = leer(RAIZ / "DECISIONES.md")
    ids = [int(x) for x in re.findall(r"^\| D-(\d{2}) \|", texto, re.M)]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        err(f"DECISIONES.md: IDs duplicados: {sorted('D-%02d' % x for x in dup)}")
    if ids and ids != list(range(1, len(ids) + 1)):
        err("DECISIONES.md: los IDs D-xx no son consecutivos desde D-01")


def main() -> int:
    for archivo in ("CLAUDE.md", "README.md", "BACKLOG.md", "STATUS.md",
                    "DECISIONES.md", "BITACORA.md"):
        if not (RAIZ / archivo).exists():
            err(f"falta el archivo de proceso {archivo}")

    carpetas = sorted(p for p in (RAIZ / "skills").iterdir() if p.is_dir())
    for carpeta in carpetas:
        validar_skill(carpeta)
    nombres = [c.name for c in carpetas]
    validar_indices(nombres)
    validar_specs(nombres)
    validar_decisiones()

    print(f"Validadas {len(nombres)} skills: {', '.join(nombres)}\n")
    for a in avisos:
        print(f"  AVISO  {a}")
    for e in errores:
        print(f"  ERROR  {e}")
    print(f"\nResultado: {len(errores)} errores, {len(avisos)} avisos.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
