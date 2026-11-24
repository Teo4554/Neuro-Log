<div align="center">

# Neuro-Log.

**Sitio web, experimentos y código**
Tres protocolos de psicología experimental · datos y análisis reproducibles

![Python 3](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PsychoPy](https://img.shields.io/badge/PsychoPy-experiments-6B4C9A)
![Design](https://img.shields.io/badge/design-N%20%3D%201-2f4f6f)
![Deploy](https://img.shields.io/badge/deploy-Vercel-000000?logo=vercel&logoColor=white)
![Data](https://img.shields.io/badge/data-anonymised-2f4f6f)

[🇪🇸 Español](#español) · [🇬🇧 English](#english)

</div>

---

<a id="español"></a>

## 🇪🇸 Español

> 🌐 **Sitio:** https://neuroportafolio.vercel.app/
>
> Este repositorio contiene el sitio estático, los archivos del experimento de PsychoPy y el código que genera gráficos, tablas y anexo a partir de los datos.

### ✨ De un vistazo

| | |
| --- | --- |
| 🧪 Proyectos | 3: discriminación táctil, tiempo de reacción y postimagen |
| 👥 Muestra | N = 1 por protocolo |
| 📊 Datos | copias anonimizadas; ningún valor empírico modificado |
| 🔁 Reproducible | gráficos, anexo y tablas se regeneran desde los datos |

### 📂 Contenido

| Página | Protocolo | Variable | Resultado central |
| --- | --- | --- | --- |
| `modulo1.html` | Discriminación táctil | Intensidad percibida, escala 1-10 | 8, 6, 4, 6, 4 según zona cutánea |
| `modulo2.html` | Tiempos de reacción | RT visual y auditivo, en ms | Visual 446,0 ms · Auditivo 503,2 ms |
| `modulo3.html` | Postimagen por flash | Duración de la postimagen, en s | Media 6,0 s · DE 3,7 s |

Cada módulo presenta fundamentos, diseño, datos y discusión. `conclusiones.html` integra los tres protocolos. `anexo_p2.html` muestra el experimento de PsychoPy, el script de limpieza y las tablas antes y después.

### 🌳 Estructura

```text
.
├── index.html                 ← índice, cuatro tarjetas y enlace al anexo
├── modulo1.html
├── modulo2.html
├── modulo3.html
├── conclusiones.html
├── anexo_p2.html              ← código, limpieza y tablas comparadas del P2
├── styles.css
├── assets/                    ← tres gráficos generados con los datos reales
├── datos/                     ← fuentes anonimizadas del P2
│   ├── MODULO2.py
│   ├── MODULO2.psyexp
│   ├── limpiar_datos_p2.py
│   ├── P2_crudo.csv
│   ├── P2_limpio.xlsx
│   ├── P2_informe_limpieza.txt
│   └── AUDIOREACCIOn.mp3
├── descargas/                 ← los mismos archivos, enlazados desde el anexo
├── CONTENIDO.md               ← texto de los bloques, editado y revisado
├── generar_graficos.py
├── generar_anexo_p2.py
└── insertar_contenido.py
```

### ▶️ Reproducir

Requiere Python 3, `matplotlib` y `openpyxl`.

```bash
python3 generar_graficos.py      # regenera assets/*.png desde los datos
python3 generar_anexo_p2.py      # regenera anexo_p2.html y descargas/
python3 insertar_contenido.py    # inserta el texto de CONTENIDO.md en las páginas
```

Los scripts no generan contenido teórico: solo grafican datos, construyen el anexo a partir de las fuentes y colocan en el HTML el texto escrito en `CONTENIDO.md`.

### 🧹 Criterios de limpieza del P2

El CSV crudo de PsychoPy tiene 22 filas. Se conservaron **19 ensayos** y se descartaron 3: las filas de inicio y despedida, y un ensayo con RT de 1151 ms, fuera del rango definido de **150-1000 ms**.

| Condición | n | Media | Mediana | DE |
| --- | ---: | ---: | ---: | ---: |
| Visual | 10 | 446,0 ms | 430,5 ms | 127,4 ms |
| Auditivo | 9 | 503,2 ms | 360,0 ms | 218,5 ms |

La diferencia observada, **+57,2 ms a favor del visual**, es inversa a lo habitual en la literatura y se discute como tal en el módulo 2. Los números no fueron reescritos para ajustarlos a la expectativa teórica.

### 🤖 Uso de IA

- **Código:** el script de limpieza del P2 (`datos/limpiar_datos_p2.py`) y sus docstrings fueron generados con asistencia de IA y luego **revisados, ejecutados y verificados** contra el CSV real.
- **Sin asistencia de IA:** diseño de los experimentos, recolección de datos, definición del umbral de 150-1000 ms e interpretación de los resultados.

### ✍️ Autoría

Teófilo Angulo.

---

<a id="english"></a>

## 🇬🇧 English

> 🌐 **Site:** https://neuroportafolio.vercel.app/
>
> This repository contains the static site, the PsychoPy experiment files and the code that generates the plots, tables and annex from the data.

### ✨ At a glance

| | |
| --- | --- |
| 🧪 Projects | 3: tactile discrimination, reaction time and visual afterimage |
| 👥 Sample | N = 1 per protocol |
| 📊 Data | anonymised copies; no empirical value was changed |
| 🔁 Reproducible | plots, annex and tables can be regenerated from the data |

### 📂 Contents

| Page | Protocol | Measure | Main result |
| --- | --- | --- | --- |
| `modulo1.html` | Tactile discrimination | Perceived intensity, 1-10 scale | 8, 6, 4, 6, 4 by skin site |
| `modulo2.html` | Reaction time | Visual and auditory RT, in ms | Visual 446.0 ms · Auditory 503.2 ms |
| `modulo3.html` | Flash afterimage | Afterimage duration, in s | Mean 6.0 s · SD 3.7 s |

Each module presents background, design, data and discussion. `conclusiones.html` integrates the three protocols. `anexo_p2.html` shows the PsychoPy experiment, the cleaning script and the before/after tables.

### 🌳 Structure

```text
.
├── index.html                 ← index, four cards and link to the annex
├── modulo1.html
├── modulo2.html
├── modulo3.html
├── conclusiones.html
├── anexo_p2.html              ← code, cleaning and compared P2 tables
├── styles.css
├── assets/                    ← three plots generated from the real data
├── datos/                     ← anonymised P2 sources
│   ├── MODULO2.py
│   ├── MODULO2.psyexp
│   ├── limpiar_datos_p2.py
│   ├── P2_crudo.csv
│   ├── P2_limpio.xlsx
│   ├── P2_informe_limpieza.txt
│   └── AUDIOREACCIOn.mp3
├── descargas/                 ← the same files, linked from the annex
├── CONTENIDO.md               ← block texts, edited and reviewed
├── generar_graficos.py
├── generar_anexo_p2.py
└── insertar_contenido.py
```

### ▶️ Reproduce

Requires Python 3, `matplotlib` and `openpyxl`.

```bash
python3 generar_graficos.py      # regenerates assets/*.png from the data
python3 generar_anexo_p2.py      # regenerates anexo_p2.html and descargas/
python3 insertar_contenido.py    # inserts the text from CONTENIDO.md into the pages
```

The scripts do not generate theoretical content: they only plot data, build the annex from the sources and place in the HTML the text written in `CONTENIDO.md`.

### 🧹 P2 cleaning criteria

The raw PsychoPy CSV has 22 rows. **19 trials** were kept and 3 were discarded: the welcome and farewell rows, and one trial with an RT of 1151 ms, outside the defined **150-1000 ms** range.

| Condition | n | Mean | Median | SD |
| --- | ---: | ---: | ---: | ---: |
| Visual | 10 | 446.0 ms | 430.5 ms | 127.4 ms |
| Auditory | 9 | 503.2 ms | 360.0 ms | 218.5 ms |

The observed difference, **+57.2 ms in favour of the visual condition**, is the reverse of the usual finding in the literature and is discussed as such in module 2. The numbers were not rewritten to fit the theoretical expectation.

### 🤖 AI use

- **Code:** the P2 cleaning script (`datos/limpiar_datos_p2.py`) and its docstrings were generated with AI assistance and then **reviewed, run and verified** against the actual CSV.
- **Without AI assistance:** experiment design, data collection, the 150-1000 ms threshold and interpretation of the results.

### ✍️ Authorship

Teófilo Angulo.

---

<div align="center">

Hecho con datos reales, no con promesas. · Built with real data, not promises.

</div>
