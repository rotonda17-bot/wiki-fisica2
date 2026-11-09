import os
import numpy as np
import matplotlib.pyplot as plt

# Directorio del script y destino en docs/assets/Imagenes-4
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# GRAFICO: FRENTES DE ONDA ESFERICOS / CIRCULARES Y RAYOS (2D/3D)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6))

# Fuente puntual en el origen
ax.plot(0, 0, 'ro', markersize=10, label="Fuente Puntual (Origen)")

# Frentes de onda (Círculos concéntricos desfasados por lambda)
radios = [0.6, 1.2, 1.8, 2.4]
for r in radios:
    circle = plt.Circle((0, 0), r, color='crimson', fill=False, lw=2, linestyle='--')
    ax.add_patch(circle)

# Etiqueta para un frente de onda
ax.text(1.7, 1.7, "Frente de Onda", color="crimson", fontsize=11, fontweight='bold')

# Rayos (Perpendiculares a los frentes de onda)
angulos = np.linspace(0, 2 * np.pi, 8, endpoint=False)
for ang in angulos:
    dx = 2.8 * np.cos(ang)
    dy = 2.8 * np.sin(ang)
    ax.arrow(0, 0, dx, dy, head_width=0.08, head_length=0.12, fc='darkorange', ec='darkorange', lw=1.5)

# Etiqueta de Rayo
ax.text(1.5, 0.2, r"Rayo ($\perp$ Frente)", color="darkorange", fontsize=11, fontweight='bold')

# Cotas de Longitud de Onda (\lambda) entre frentes
ax.annotate('', xy=(1.2, 0), xytext=(1.8, 0),
            arrowprops=dict(arrowstyle='<->', color='navy', lw=2))
ax.text(1.5, -0.25, r"$\lambda$", color="navy", fontsize=13, fontweight='bold', ha='center')

ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-3.2, 3.2)
ax.set_aspect('equal')
ax.set_title("Propagación de Frentes de Onda Circular/Esférica y Rayos", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "4.1-frente-de-onda.png"), dpi=300)
plt.close()

print(f"¡Gráfico de la 4.1 generado con éxito en: {OUTPUT_DIR}!")