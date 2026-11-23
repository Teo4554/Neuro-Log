#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inserta en las páginas el texto que escribiste en CONTENIDO.md.

No genera contenido: solo reemplaza lo que está entre marcadores
<!-- INICIO_TEXTO:clave --> ... <!-- FIN_TEXTO:clave -->.

Uso:
    python3 insertar_contenido.py
"""

import html
import re
from pathlib import Path

BASE = Path(__file__).parent
FUENTE = BASE / "CONTENIDO.md"

ARCHIVOS = {
    "modulo1.html": [
        "m1_fundamentos", "m1_metodo", "m1_foto", "m1_discusion",
    ],
    "modulo2.html": [
        "m2_fundamentos", "m2_metodo", "m2_foto", "m2_discusion",
    ],
    "modulo3.html": [
        "m3_fundamentos", "m3_metodo", "m3_foto", "m3_discusion",
    ],
    "conclusiones.html": ["conclusiones"],
}


def markdown_a_html(texto):
    """Convierte lo mínimo: párrafos, **negrita** y enlaces http(s)."""
    seguro = html.escape(texto.strip())
    seguro = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", seguro)
    seguro = re.sub(
        r"\[([^\]]+)\]\((https?://[^\s)]+)\)",
        r'<a href="\2">\1</a>',
        seguro,
    )
    parrafos = [p.strip() for p in re.split(r"\n\s*\n", seguro) if p.strip()]
    return "\n".join("<p>{}</p>".format(p.replace("\n", "<br>")) for p in parrafos)


def main():
    contenido = FUENTE.read_text(encoding="utf-8")
    secciones = {}
    for coincidencia in re.finditer(
        r"^##\s+(\w+)\s*\n(.*?)(?=^##\s|\Z)", contenido, re.M | re.S
    ):
        clave, texto = coincidencia.group(1), coincidencia.group(2).strip()
        if texto and not texto.startswith("["):
            secciones[clave] = texto

    total = 0
    for nombre, claves in ARCHIVOS.items():
        ruta = BASE / nombre
        pagina = ruta.read_text(encoding="utf-8")
        insertados = 0
        for clave in claves:
            if clave not in secciones:
                continue
            patron = r"(<!-- INICIO_TEXTO:{0} -->).*?(<!-- FIN_TEXTO:{0} -->)".format(
                re.escape(clave)
            )
            reemplazo = r"\1\n" + markdown_a_html(secciones[clave]) + r"\n\2"
            pagina, n = re.subn(patron, reemplazo, pagina, flags=re.S)
            if n:
                insertados += n
            else:
                print("Aviso: no encontré el marcador", clave, "en", nombre)
        ruta.write_text(pagina, encoding="utf-8")
        print("{}: {} bloque(s)".format(nombre, insertados))
        total += insertados

    print("Total insertado:", total)


if __name__ == "__main__":
    main()
