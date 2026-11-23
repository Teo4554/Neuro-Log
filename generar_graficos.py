#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los 3 gráficos a partir de los datos reales ya recolectados."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

# --- P1 ---
zonas = ["Yema\níndice", "Dorso\nmano", "Antebrazo", "Mentón", "Nuca"]
intensidad = [8, 6, 4, 6, 4]
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.scatter(zonas, intensidad, s=70, color="#2f4f6f", zorder=3)
ax.plot(zonas, intensidad, color="#2f4f6f", alpha=0.25)
ax.set_ylim(0, 11)
ax.set_ylabel("Intensidad percibida (1-10)")
ax.set_title("P1 - Intensidad por zona cutánea")
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "p1_dispersion.png", dpi=160)
plt.close(fig)

# --- P2 (19 ensayos limpios) ---
ensayos = list(range(1, 20))
cond = ["A", "V", "A", "V", "A", "V", "V", "A", "V", "A",
        "V", "A", "V", "V", "A", "V", "A", "A", "V"]
rt = [291, 351, 654, 421, 910, 534, 440, 360, 495, 350,
      393, 669, 351, 279, 318, 456, 634, 343, 740]
colores = {"A": "#b3541e", "V": "#2f6f8f"}
fig, ax = plt.subplots(figsize=(8, 4.4))
for c, etiqueta in [("V", "Visual"), ("A", "Auditivo")]:
    x = [e for e, k in zip(ensayos, cond) if k == c]
    y = [v for v, k in zip(rt, cond) if k == c]
    ax.scatter(x, y, s=55, color=colores[c], label=etiqueta, alpha=0.85, zorder=3)
ax.axhline(503.2, color=colores["A"], ls="--", lw=1, alpha=0.6)
ax.axhline(446.0, color=colores["V"], ls="--", lw=1, alpha=0.6)
ax.set_xlabel("Número de ensayo (tras la limpieza)")
ax.set_ylabel("Tiempo de reacción (ms)")
ax.set_title("P2 - RT por ensayo y modalidad")
ax.legend(frameon=False)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(OUT / "p2_dispersion.png", dpi=160)
plt.close(fig)

# --- P3 ---
ens = [1, 2, 3, 4, 5]
post = [10, 6, 6, 8, 0]
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.scatter(ens, post, s=70, color="#4f6f52", zorder=3)
ax.plot(ens, post, color="#4f6f52", alpha=0.25)
ax.set_xticks(ens)
ax.set_xlabel("Ensayo")
ax.set_ylabel("Duración de la postimagen (s)")
ax.set_title("P3 - Duración de la postimagen por ensayo")
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "p3_dispersion.png", dpi=160)
plt.close(fig)

print("Gráficos generados en", OUT)
