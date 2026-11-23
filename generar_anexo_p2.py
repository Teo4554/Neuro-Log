#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el anexo del Protocolo 2 y copia los archivos descargables.

No modifica los datos originales: solo lee el experimento, el script de
limpieza, el CSV crudo, el XLSX limpio y el informe, y escribe:

    anexo_p2.html
    descargas/

Uso:
    python3 generar_anexo_p2.py
"""

import csv
import html
import importlib.util
import shutil
from pathlib import Path

import openpyxl

BASE = Path(__file__).parent
DATOS = BASE / "datos"
CSV_CRUDO = DATOS / "P2_crudo.csv"
XLSX_LIMPIO = DATOS / "P2_limpio.xlsx"
INFORME = DATOS / "P2_informe_limpieza.txt"
CODIGO_EXPERIMENTO = DATOS / "MODULO2.py"
DISENO_EXPERIMENTO = DATOS / "MODULO2.psyexp"
CODIGO_LIMPIEZA = DATOS / "limpiar_datos_p2.py"
DESTINO = BASE / "descargas"


def leer_texto(ruta):
    return ruta.read_text(encoding="utf-8")


def clasificador_real():
    """Carga la función revisar_fila del script de limpieza original."""
    especificacion = importlib.util.spec_from_file_location(
        "limpiar_datos_p2", CODIGO_LIMPIEZA
    )
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return modulo.revisar_fila, modulo.COL_RT


def tabla_cruda(revisar_fila, columna_rt):
    with CSV_CRUDO.open(encoding="utf-8-sig", newline="") as archivo:
        filas = list(csv.DictReader(archivo))

    salida = []
    for numero, fila in enumerate(filas, start=2):
        accion, motivo, rt_ms = revisar_fila(fila, numero)
        rt_segundos = (fila.get(columna_rt) or "").strip()
        salida.append(
            {
                "fila": numero,
                "tipo": (fila.get("tipo") or "").strip() or "sin tipo",
                "rt_segundos": rt_segundos[:10] if rt_segundos else "sin dato",
                "rt_ms": "{:.1f}".format(rt_ms) if rt_ms is not None else "sin dato",
                "accion": "conservar" if accion == "conservar" else "descartar",
                "motivo": motivo or "cumple el rango de 150 a 1000 ms",
            }
        )
    return salida, len(filas)


def tabla_limpia():
    libro = openpyxl.load_workbook(XLSX_LIMPIO, data_only=True)
    hoja = libro.active
    filas = list(hoja.iter_rows(values_only=True))
    cabecera = filas[0]
    datos = filas[1:]
    return cabecera, datos


def filas_html(filas, clases=""):
    return "\n".join(
        "<tr>{}</tr>".format("".join("<td>{}</td>".format(html.escape(str(c))) for c in fila))
        for fila in filas
    )


def preparar_descargas(datos_limpios):
    DESTINO.mkdir(exist_ok=True)
    copias = [
        (CODIGO_EXPERIMENTO, "experimento_MODULO2.py"),
        (DISENO_EXPERIMENTO, "diseno_MODULO2.psyexp"),
        (CODIGO_LIMPIEZA, "limpieza_datos_p2.py"),
        (CSV_CRUDO, "datos_crudos_P2.csv"),
        (XLSX_LIMPIO, "datos_limpios_P2.xlsx"),
        (INFORME, "informe_limpieza_P2.txt"),
    ]
    for origen, nombre in copias:
        shutil.copy2(origen, DESTINO / nombre)

    ruta_csv_limpio = DESTINO / "datos_limpios_P2.csv"
    with ruta_csv_limpio.open("w", encoding="utf-8-sig", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Ensayo", "Condicion", "RT_ms"])
        for ensayo, condicion, rt in datos_limpios:
            escritor.writerow([int(ensayo), condicion, int(rt)])


def main():
    revisar_fila, columna_rt = clasificador_real()
    crudas, total_crudas = tabla_cruda(revisar_fila, columna_rt)
    cabecera_limpia, datos_limpios = tabla_limpia()
    preparar_descargas(datos_limpios)

    conservadas = sum(1 for f in crudas if f["accion"] == "conservar")
    descartadas = total_crudas - conservadas

    filas_crudas = filas_html(
        [
            (
                f["fila"],
                f["tipo"],
                f["rt_segundos"],
                f["rt_ms"],
                f["accion"],
                f["motivo"],
            )
            for f in crudas
        ]
    )
    filas_limpias = filas_html(datos_limpios)

    pagina = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anexo P2 — Código y tablas — Neurociencias</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="cabecera">
    <p class="institucion">Universidad Bicentenaria de Aragua</p>
    <h1>Anexo del Protocolo 2</h1>
    <p class="subtitulo">Código del experimento, limpieza y tablas comparadas · Actividad Sumativa Nº 4</p>
    <p class="autor">Teofilo Angulo · 22 de noviembre de 2026</p>
    <a class="volver" href="modulo2.html">← Volver al módulo 2</a>
  </header>

  <nav class="nav" aria-label="Navegación del anexo">
    <a href="#experimento">Experimento</a>
    <a href="#limpieza">Limpieza</a>
    <a href="#antes">Tabla previa</a>
    <a href="#despues">Tabla posterior</a>
    <a href="#informe">Informe</a>
    <a href="#descargas">Descargas</a>
  </nav>

  <main class="contenido">

    <section id="intro">
      <h2>Anexo de código y tablas del Protocolo 2</h2>
      <p>Este anexo reúne el código que generó el experimento de tiempos de reacción, el programa que limpió los datos y las tablas antes y después de esa limpieza. Está pensado para leer y comparar el procedimiento completo. Los archivos también se pueden descargar al final de la página.</p>
      <p class="nota">El CSV original se conserva sin modificar en la versión privada. Acá se publica una copia anonimizada: solo cambió el identificador del participante, no los valores de tiempo de reacción. La limpieza conservó __CONSERVADAS__ de __TOTALES__ filas y descartó __DESCARTADAS__. El código se muestra con su sintaxis original, tal como se ejecutó.</p>
    </section>

    <section id="experimento">
      <h2>1. Experimento</h2>
      <p>Archivo <code>MODULO2.py</code>, generado por PsychoPy a partir del diseño <code>MODULO2.psyexp</code>. Es el programa que presentó los estímulos visuales y auditivos y registró las respuestas.</p>
      <details>
        <summary>Ver código del experimento, __LINEAS_EXP__ líneas</summary>
        <div class="codigo"><pre><code>__CODIGO_EXP__</code></pre></div>
      </details>
      <p class="descargas"><a href="descargas/experimento_MODULO2.py" download>Descargar experimento_MODULO2.py</a></p>
      <p class="descargas"><a href="descargas/diseno_MODULO2.psyexp" download>Descargar diseno_MODULO2.psyexp</a></p>
    </section>

    <section id="limpieza">
      <h2>2. Código de limpieza</h2>
      <p>Archivo <code>limpiar_datos_p2.py</code>. Lee el CSV crudo sin modificarlo, separa las filas de inicio y despedida, convierte el tiempo de respuesta a milisegundos y conserva solo los ensayos entre 150 y 1000 ms.</p>
      <details>
        <summary>Ver código de limpieza, __LINEAS_LIMP__ líneas</summary>
        <div class="codigo"><pre><code>__CODIGO_LIMP__</code></pre></div>
      </details>
      <p class="descargas"><a href="descargas/limpieza_datos_p2.py" download>Descargar limpieza_datos_p2.py</a></p>
    </section>

    <section id="antes">
      <h2>3. Tabla previa a la limpieza</h2>
      <p>Filas del CSV original de PsychoPy. Se muestran las columnas necesarias para auditar la decisión. La fila 2 corresponde al inicio y la fila 23 a la despedida.</p>
      <div class="tabla-ancho">
      <table class="datos">
        <caption>CSV crudo, __TOTALES__ filas — decisión del script de limpieza</caption>
        <thead><tr><th>Fila</th><th>Tipo</th><th>RT en segundos</th><th>RT en ms</th><th>Decisión</th><th>Motivo</th></tr></thead>
        <tbody>
__FILAS_CRUdas__
        </tbody>
      </table>
      </div>
      <p class="descargas"><a href="descargas/datos_crudos_P2.csv" download>Descargar datos_crudos_P2.csv</a></p>
    </section>

    <section id="despues">
      <h2>4. Tabla posterior a la limpieza</h2>
      <p>Tabla resultante, con los __CONSERVADAS__ ensayos válidos. Es la que se usó para el gráfico y los resúmenes del módulo 2.</p>
      <div class="tabla-ancho">
      <table class="datos">
        <caption>Tabla limpia, __CONSERVADAS__ ensayos</caption>
        <thead><tr><th>Ensayo</th><th>Condición</th><th>Tiempo de reacción en ms</th></tr></thead>
        <tbody>
__FILAS_LIMPIAS__
        </tbody>
      </table>
      </div>
      <p class="descargas"><a href="descargas/datos_limpios_P2.xlsx" download>Descargar datos_limpios_P2.xlsx</a></p>
      <p class="descargas"><a href="descargas/datos_limpios_P2.csv" download>Descargar datos_limpios_P2.csv</a></p>
    </section>

    <section id="informe">
      <h2>5. Informe de limpieza</h2>
      <p>Texto de auditoría generado por el propio script, con los descartes y los resúmenes con y sin filtro.</p>
      <details>
        <summary>Ver informe de limpieza</summary>
        <div class="codigo"><pre><code>__INFORME__</code></pre></div>
      </details>
      <p class="descargas"><a href="descargas/informe_limpieza_P2.txt" download>Descargar informe_limpieza_P2.txt</a></p>
    </section>

    <section id="descargas">
      <h2>6. Archivos para descargar</h2>
      <ul class="lista-descargas">
        <li><a href="descargas/experimento_MODULO2.py" download>MODULO2.py</a> — código del experimento</li>
        <li><a href="descargas/diseno_MODULO2.psyexp" download>MODULO2.psyexp</a> — diseño de PsychoPy</li>
        <li><a href="descargas/limpieza_datos_p2.py" download>limpiar_datos_p2.py</a> — código de limpieza</li>
        <li><a href="descargas/datos_crudos_P2.csv" download>CSV crudo anonimizado</a></li>
        <li><a href="descargas/datos_limpios_P2.xlsx" download>XLSX limpio anonimizado</a></li>
        <li><a href="descargas/datos_limpios_P2.csv" download>CSV limpio, mismo contenido que el XLSX</a></li>
        <li><a href="descargas/informe_limpieza_P2.txt" download>Informe de limpieza</a></li>
      </ul>
      <p class="nota">El CSV limpio es una conversión del XLSX limpio a texto plano. No agrega ni cambia datos.</p>
    </section>

  </main>

  <footer>
    <p>Actividad Sumativa Nº 4 · Neurociencias · Teofilo Angulo · <a href="modulo2.html">Módulo 2</a> · <a href="index.html">Índice</a></p>
  </footer>

</body>
</html>
"""

    reemplazos = {
        "__CONSERVADAS__": str(conservadas),
        "__TOTALES__": str(total_crudas),
        "__DESCARTADAS__": str(descartadas),
        "__LINEAS_EXP__": str(len(leer_texto(CODIGO_EXPERIMENTO).splitlines())),
        "__LINEAS_LIMP__": str(len(leer_texto(CODIGO_LIMPIEZA).splitlines())),
        "__CODIGO_EXP__": html.escape(leer_texto(CODIGO_EXPERIMENTO)),
        "__CODIGO_LIMP__": html.escape(leer_texto(CODIGO_LIMPIEZA)),
        "__INFORME__": html.escape(leer_texto(INFORME)),
        "__FILAS_CRUdas__": filas_crudas,
        "__FILAS_LIMPIAS__": filas_limpias,
    }
    for clave, valor in reemplazos.items():
        pagina = pagina.replace(clave, valor)

    (BASE / "anexo_p2.html").write_text(pagina, encoding="utf-8")
    print("Anexo generado: anexo_p2.html")
    print("Filas crudas:", total_crudas, "| conservadas:", conservadas, "| descartadas:", descartadas)
    print("Archivos en descargas:", len(list(DESTINO.iterdir())))


if __name__ == "__main__":
    main()
