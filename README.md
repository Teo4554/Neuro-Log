# Neurociencias II — Portafolio de la Unidad IV

Portafolio web de la Actividad Sumativa Nº 4. Tres protocolos de fisiología sensorial con **N = 1 por protocolo**, datos recolectados por el estudiante, análisis reproducible y conclusiones integradoras sobre neuroplasticidad aplicada.

**Sitio publicado:** https://neuroportafolio.vercel.app/

Este repositorio es el código fuente del sitio. El despliegue en Vercel es el enlace que se entregó con la actividad; el PDF reglamentario no se incluye acá porque contiene datos personales.

## Contenido

| Página | Protocolo | Variable | Resultado central |
| --- | --- | --- | --- |
| `modulo1.html` | Discriminación táctil | Intensidad percibida, escala 1-10 | 8, 6, 4, 6, 4 según zona cutánea |
| `modulo2.html` | Tiempos de reacción | RT visual y auditivo, en ms | Visual 446,0 ms · Auditivo 503,2 ms |
| `modulo3.html` | Postimagen por flash | Duración de la postimagen, en s | Media 6,0 s · DE 3,7 s |

Cada módulo sigue los cuatro bloques de la rúbrica: fundamentos neurofisiológicos, diseño metodológico y muestra, tablas y gráfico, y discusión. `conclusiones.html` integra los tres protocolos. `anexo_p2.html` expone el experimento de PsychoPy, el script de limpieza y las tablas antes y después.

### Árbol

```
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
├── CONTENIDO.md               ← texto de los bloques, editado a mano
├── generar_graficos.py
├── generar_anexo_p2.py
└── insertar_contenido.py
```

## Reproducir

Requiere Python 3, `matplotlib` y `openpyxl`.

```bash
python3 generar_graficos.py      # regenera assets/*.png desde los datos
python3 generar_anexo_p2.py      # regenera anexo_p2.html y descargas/
python3 insertar_contenido.py    # inserta el texto de CONTENIDO.md en las páginas
```

Los scripts no generan contenido teórico: solo grafican datos, construyen el anexo a partir de las fuentes y colocan en el HTML el texto escrito en `CONTENIDO.md`.

## Criterios de limpieza del P2

El CSV crudo de PsychoPy tiene 22 filas. Se conservaron 19 ensayos y se descartaron 3: las filas de inicio y despedida, y un ensayo con RT de 1151 ms, fuera del rango acordado de 150-1000 ms. El resultado fue visual n = 10, media 446,0 ms, DE 127,4 ms; auditivo n = 9, media 503,2 ms, DE 218,5 ms. La diferencia observada, +57,2 ms a favor del visual, es inversa a lo habitual en la literatura y se discute como tal en el módulo 2.

## Privacidad

Los archivos publicados son copias anonimizadas: el identificador original del participante se reemplazó por `Participante_01` y las rutas locales se cambiaron por rutas relativas. **Ningún valor empírico fue modificado**. Los originales sin anonimizar y el PDF con datos personales permanecen fuera del repositorio.

## Autoría

Teófilo Angulo. Diseño, recolección y redacción de los módulos 1, 2 y las conclusiones por el estudiante. El módulo 3 fue redactado con apoyo de IA a pedido del estudiante, y la revisión de redacción y el procesamiento gráfico también contaron con apoyo de IA. Uso académico; pedir autorización para reutilizar los datos.
