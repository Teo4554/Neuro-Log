<div align="center">

# Neuro-Log. · Neurociencias II — Unidad IV

**Portafolio web de la Actividad Sumativa Nº 4**
Tres protocolos de fisiología sensorial · N = 1 por protocolo · datos y análisis reproducibles

![Python 3](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PsychoPy](https://img.shields.io/badge/PsychoPy-experiments-6B4C9A)
![Design](https://img.shields.io/badge/design-N%20%3D%201-2f4f6f)
![Deploy](https://img.shields.io/badge/deploy-Vercel-000000?logo=vercel&logoColor=white)
![Use](https://img.shields.io/badge/use-academic-6c757d)

[🇪🇸 Español](#español) · [🇬🇧 English](#english)

</div>

---

<a id="español"></a>

## 🇪🇸 Español

> 🌐 **Sitio publicado:** https://neuroportafolio.vercel.app/
>
> Este repositorio es el **código fuente** del sitio. Vercel es el enlace que se entregó con la actividad. El PDF reglamentario no se incluye acá porque contiene datos personales.

### ✨ De un vistazo

| | |
| --- | --- |
| 🧪 Actividad | Sumativa Nº 4 · Unidad IV |
| 🧠 Protocolos | 3: discriminación táctil, tiempo de reacción y postimagen |
| 👥 Muestra | N = 1 por protocolo, estudiante como participante y experimentador |
| 📊 Datos | copias anonimizadas; ningún valor empírico modificado |
| 🔁 Reproducible | gráficos, anexo y tablas se regeneran desde los datos |

### 📂 Contenido

| Página | Protocolo | Variable | Resultado central |
| --- | --- | --- | --- |
| `modulo1.html` | Discriminación táctil | Intensidad percibida, escala 1-10 | 8, 6, 4, 6, 4 según zona cutánea |
| `modulo2.html` | Tiempos de reacción | RT visual y auditivo, en ms | Visual 446,0 ms · Auditivo 503,2 ms |
| `modulo3.html` | Postimagen por flash | Duración de la postimagen, en s | Media 6,0 s · DE 3,7 s |

Cada módulo sigue los cuatro bloques de la rúbrica: fundamentos neurofisiológicos, diseño metodológico y muestra, tablas y gráfico, y discusión. `conclusiones.html` integra los tres protocolos. `anexo_p2.html` expone el experimento de PsychoPy, el script de limpieza y las tablas antes y después.

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

El CSV crudo de PsychoPy tiene 22 filas. Se conservaron **19 ensayos** y se descartaron 3: las filas de inicio y despedida, y un ensayo con RT de 1151 ms, fuera del rango acordado de **150-1000 ms**.

| Condición | n | Media | Mediana | DE |
| --- | ---: | ---: | ---: | ---: |
| Visual | 10 | 446,0 ms | 430,5 ms | 127,4 ms |
| Auditivo | 9 | 503,2 ms | 360,0 ms | 218,5 ms |

La diferencia observada, **+57,2 ms a favor del visual**, es inversa a lo habitual en la literatura y se discute como tal en el módulo 2. Los números no fueron reescritos para ajustarlos a la expectativa teórica.

### 🤖 Uso de asistencia de IA

Transparencia sobre qué partes fueron asistidas y cuáles no:

- **Redacción:** los módulos 1 y 2 y las conclusiones fueron escritos por el estudiante. El módulo 3 se redactó con apoyo de IA a pedido del estudiante, de forma resumida y adaptada a su estilo. La revisión de redacción del conjunto también contó con apoyo de IA.
- **Código:** el script de limpieza del P2 (`datos/limpiar_datos_p2.py`) y sus docstrings fueron generados con asistencia de IA, y luego **revisados, ejecutados y verificados por el estudiante** contra el CSV real.
- **Documentación:** este README, las explicaciones del anexo y el procesamiento de los gráficos fueron apoyados por IA, siempre a partir de datos y decisiones proporcionadas por el estudiante.
- **No delegado a la IA:** la recolección de los datos, el diseño de los experimentos, la definición del umbral de 150-1000 ms, la interpretación de los resultados y la aprobación final de los textos.

> Esta sección describe el uso de IA **en el repositorio**. La declaración correspondiente a la entrega académica permanece en el PDF reglamentario y no fue modificada.

### 🔒 Privacidad

Los archivos publicados son copias anonimizadas: el identificador original del participante se reemplazó por `Participante_01` y las rutas locales se cambiaron por rutas relativas. **Ningún valor empírico fue modificado**. Los originales sin anonimizar y el PDF con datos personales permanecen fuera del repositorio.

### ✍️ Autoría

Teófilo Angulo · Universidad Bicentenaria de Aragua.

Uso académico. Pedir autorización antes de reutilizar los datos o el diseño experimental.

---

<a id="english"></a>

## 🇬🇧 English

> 🌐 **Published site:** https://neuroportafolio.vercel.app/
>
> This repository holds the **source code** for the site. Vercel hosts the link submitted with the assignment. The official PDF is not included here because it contains personal data.

### ✨ At a glance

| | |
| --- | --- |
| 🧪 Assignment | Summative Activity No. 4 · Unit IV |
| 🧠 Protocols | 3: tactile discrimination, reaction time and visual afterimage |
| 👥 Sample | N = 1 per protocol; the student acted as both participant and experimenter |
| 📊 Data | anonymised copies; no empirical value was changed |
| 🔁 Reproducible | plots, annex and tables can be regenerated from the data |

### 📂 Contents

| Page | Protocol | Measure | Main result |
| --- | --- | --- | --- |
| `modulo1.html` | Tactile discrimination | Perceived intensity, 1-10 scale | 8, 6, 4, 6, 4 by skin site |
| `modulo2.html` | Reaction time | Visual and auditory RT, in ms | Visual 446.0 ms · Auditory 503.2 ms |
| `modulo3.html` | Flash afterimage | Afterimage duration, in s | Mean 6.0 s · SD 3.7 s |

Each module follows the four rubric blocks: neurophysiological background, methodological design and sample, tables and plot, and discussion. `conclusiones.html` integrates the three protocols. `anexo_p2.html` shows the PsychoPy experiment, the cleaning script and the before/after tables.

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

The raw PsychoPy CSV has 22 rows. **19 trials** were kept and 3 were discarded: the welcome and farewell rows, and one trial with an RT of 1151 ms, outside the agreed **150-1000 ms** range.

| Condition | n | Mean | Median | SD |
| --- | ---: | ---: | ---: | ---: |
| Visual | 10 | 446.0 ms | 430.5 ms | 127.4 ms |
| Auditory | 9 | 503.2 ms | 360.0 ms | 218.5 ms |

The observed difference, **+57.2 ms in favour of the visual condition**, is the reverse of the usual finding in the literature and is discussed as such in module 2. The numbers were not rewritten to fit the theoretical expectation.

### 🤖 AI assistance

Transparency about what was assisted and what was not:

- **Writing:** modules 1 and 2 and the conclusions were written by the student. Module 3 was drafted with AI support at the student's request, kept concise and adapted to their style. Proofreading of the whole set also involved AI support.
- **Code:** the P2 cleaning script (`datos/limpiar_datos_p2.py`) and its docstrings were generated with AI assistance and then **reviewed, run and verified by the student** against the actual CSV.
- **Documentation:** this README, the annex explanations and the plot processing were supported by AI, always using data and decisions supplied by the student.
- **Not delegated to AI:** data collection, experiment design, the 150-1000 ms threshold, interpretation of the results and final approval of the texts.

> This section describes AI use **in the repository**. The declaration for the academic submission remains in the official PDF and was not changed.

### 🔒 Privacy

The published files are anonymised copies: the original participant identifier was replaced with `Participante_01` and local paths were changed to relative paths. **No empirical value was modified**. The unanonymised originals and the PDF containing personal data remain outside the repository.

### ✍️ Authorship

Teófilo Angulo · Universidad Bicentenaria de Aragua.

Academic use only. Please ask for permission before reusing the data or the experimental design.

---

<div align="center">

Hecho con datos reales, no con promesas. · Built with real data, not promises.

</div>
