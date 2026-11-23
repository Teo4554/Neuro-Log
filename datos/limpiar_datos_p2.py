#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LIMPIEZA DE DATOS — PROTOCOLO 2 (tiempos de reacción)
=====================================================

¿Qué hace?
----------
1. Lee el CSV CRUDO que generó PsychoPy (NO lo modifica).
2. Separa tres tipos de filas:
   a) filas de bienvenida / despedida (no son ensayos) -> se descartan;
   b) ensayos reales con RT fuera de 150-1000 ms -> se descartan;
   c) ensayos reales con RT válido -> se conservan.
3. Escribe DOS archivos nuevos al lado del original:
   - "..._LIMPIO.csv"           -> tabla corta lista para graficar: ensayo, tipo, RT_ms
   - "..._INFORME_LIMPIEZA.txt" -> auditoría: qué se descartó y por qué, más los resúmenes

¿Por qué no hace falta pandas?
------------------------------
`csv` lee filas como diccionarios y `statistics` calcula media/mediana/desviación.
Con 20 ensayos eso es todo lo que necesitamos. Además, así se ve exactamente
qué pasa con cada fila, que es lo que se quiere mostrar en el portafolio.

¿Cómo se usa?
-------------
    python3 limpiar_datos_p2.py

O, si quieres limpiar otro CSV:

    python3 limpiar_datos_p2.py "/ruta/al/otro_archivo.csv"

Requisitos: solo Python 3. No instalar nada.
"""

import csv          # viene con Python: lee y escribe archivos CSV
import statistics  # viene con Python: mean(), median(), stdev()
import sys          # para leer la ruta opcional que pases por terminal
from pathlib import Path  # para armar rutas sin pelearnos con barras ni espacios

# --- Configuración: cambiar solo si el experimento cambia ---
ARCHIVO_POR_DEFECTO = Path(
    "datos/"
    "P2_crudo.csv"
)
COL_TIPO = "tipo"                 # dice si el ensayo fue "audio" o "texto"
COL_RT = "RESPUESTASEÑAL.rt"      # RT en segundos (ojo: lleva ñ)
CONDICIONES = ("audio", "texto")  # todo lo demás no es un ensayo
RT_MIN_MS = 150.0                 # umbral inferior acordado
RT_MAX_MS = 1000.0                # umbral superior acordado


def leer_csv(ruta):
    """Devuelve (cabecera, filas). utf-8-sig quita el BOM y respeta la ñ."""
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        cabecera = lector.fieldnames or []
        filas = list(lector)
    return cabecera, filas


def revisar_fila(fila, numero_linea):
    """
    Clasifica una fila. Devuelve (accion, motivo, rt_ms).

    'accion' es "conservar" o "descartar". El número de línea es el del
    archivo original (la cabecera es la línea 1), para poder auditar.
    """
    tipo = (fila.get(COL_TIPO) or "").strip()

    # 1) La fila de WELCOME y la de DESPEDIDA tienen 'tipo' vacío.
    #    Aunque la despedida tenga un RT, NO es un ensayo: se va.
    if tipo not in CONDICIONES:
        return "descartar", "fila de inicio/despedida (no es ensayo)", None

    # 2) Ensayo sin respuesta registrada.
    texto_rt = (fila.get(COL_RT) or "").strip()
    if not texto_rt:
        return "descartar", "ensayo sin respuesta registrada", None

    # 3) PsychoPy guarda el RT en segundos; lo pasamos a milisegundos.
    try:
        rt_ms = float(texto_rt) * 1000.0
    except ValueError:
        return "descartar", "RT no numérico: {!r}".format(texto_rt), None

    # 4) Regla de limpieza acordada: 150 ms <= RT <= 1000 ms.
    if not (RT_MIN_MS <= rt_ms <= RT_MAX_MS):
        lado = "menor a 150 ms" if rt_ms < RT_MIN_MS else "mayor a 1000 ms"
        return "descartar", "RT {:.1f} ms ({})".format(rt_ms, lado), rt_ms

    return "conservar", "", rt_ms


def resumen(valores):
    """Devuelve una frase con n, media, mediana y DE, o un aviso si está vacío."""
    if not valores:
        return "sin datos"
    frase = "n={}, media={:.1f} ms, mediana={:.1f} ms".format(
        len(valores), statistics.mean(valores), statistics.median(valores)
    )
    if len(valores) >= 2:
        frase += ", DE={:.1f} ms".format(statistics.stdev(valores))
    return frase


def main():
    # La ruta puede venir como argumento; si no, usamos la de arriba.
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else ARCHIVO_POR_DEFECTO
    if not ruta.exists():
        print("ERROR: no encontré el archivo:", ruta)
        return

    cabecera, filas = leer_csv(ruta)

    # Si el experimento cambia de nombre de columnas, avisamos en vez de fallar en silencio.
    faltan = [c for c in (COL_TIPO, COL_RT) if c not in cabecera]
    if faltan:
        print("ERROR: faltan columnas en el CSV:", ", ".join(faltan))
        return

    conservadas, descartes = [], []
    for numero_linea, fila in enumerate(filas, start=2):  # 1 es la cabecera
        accion, motivo, rt_ms = revisar_fila(fila, numero_linea)
        if accion == "conservar":
            conservadas.append((fila[COL_TIPO].strip(), rt_ms))
        else:
            descartes.append((numero_linea, motivo))

    ruta_limpia = ruta.with_name(ruta.stem + "_LIMPIO.csv")
    ruta_informe = ruta.with_name(ruta.stem + "_INFORME_LIMPIEZA.txt")

    # Escribimos la tabla corta.csv (solo 3 columnas, lista para graficar).
    with ruta_limpia.open("w", encoding="utf-8-sig", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ensayo", "condicion", "RT_ms"])
        for i, (tipo, rt_ms) in enumerate(conservadas, start=1):
            escritor.writerow([i, tipo, round(rt_ms)])

    # Armamos el informe en texto plano con todo lo que pasó.
    lineas = []
    lineas.append("INFORME DE LIMPIEZA - PROTOCOLO 2 (tiempos de reaccion)")
    lineas.append("=" * 60)
    lineas.append("Archivo original (NO modificado): {}".format(ruta))
    lineas.append("Archivo limpio generado:          {}".format(ruta_limpia))
    lineas.append("")
    lineas.append("CRITERIO: conservar solo ensayos audio/texto con 150 <= RT <= 1000 ms.")
    lineas.append("")
    lineas.append("FILAS DEL ARCHIVO ORIGINAL: {}".format(len(filas)))
    lineas.append("  Ensayos conservados: {}".format(len(conservadas)))
    lineas.append("  Filas descartadas:   {}".format(len(descartes)))
    lineas.append("")
    lineas.append("DESCARTES (numero de linea del CSV original):")
    for numero_linea, motivo in descartes:
        lineas.append("  linea {}: {}".format(numero_linea, motivo))
    if not descartes:
        lineas.append("  (ninguno)")
    lineas.append("")
    lineas.append("TABLA LISTA PARA PEGAR EN EL PORTAFOLIO")
    lineas.append("  ensayo | condicion | RT (ms)")
    for i, (tipo, rt_ms) in enumerate(conservadas, start=1):
        lineas.append("  {:>6} | {:>9} | {:>6.0f}".format(i, tipo, rt_ms))
    lineas.append("")

    # Resumen final: primero con filtro (el que se informa) y luego sin filtro
    # (solo como referencia, para mostrar que no escondemos nada).
    lineas.append("RESUMEN CON LA LIMPIEZA APLICADA (usar este en el informe):")
    for cond in CONDICIONES:
        vals = [rt for tipo, rt in conservadas if tipo == cond]
        lineas.append("  {}: {}".format(cond, resumen(vals)))
    lineas.append("")
    lineas.append("RESUMEN SIN FILTRAR (solo referencia; NO usar en el informe):")
    for cond in CONDICIONES:
        vals = []
        for fila in filas:
            if (fila.get(COL_TIPO) or "").strip() == cond and (fila.get(COL_RT) or "").strip():
                vals.append(float(fila[COL_RT]) * 1000.0)
        lineas.append("  {}: {}".format(cond, resumen(vals)))
    lineas.append("")
    lineas.append("Nota: la etiqueta 'piloting=True' del CSV original aparece solo en la")
    lineas.append("fila de metadatos de inicio y no afecta a los ensayos conservados.")

    ruta_informe.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    # Eco en pantalla para que veas que todo salió bien.
    print("Listo.")
    print("  Ensayos conservados:", len(conservadas))
    print("  Filas descartadas:  ", len(descartes))
    print("  Tabla limpia:       ", ruta_limpia)
    print("  Informe:            ", ruta_informe)
    print()
    for cond in CONDICIONES:
        vals = [rt for tipo, rt in conservadas if tipo == cond]
        print("  {}: {}".format(cond, resumen(vals)))


if __name__ == "__main__":
    main()
