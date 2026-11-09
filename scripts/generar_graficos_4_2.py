import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener directorio del script y configurar salida en docs/assets/Imagenes-4
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GRAFICO: ONDA HARMONICA PROGRESIVA Y SUS PARAMETROS
# -------------------------------------------------------------
x = np.linspace(0, 2.5, 1000)
A = 0.15
lmbda = 1.0
k = 2 * np.pi / lmbda
y = A * np.sin(k * x)

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(x, y, color="tab:blue", lw=2.5, label=r"$y(x) = y_m \sin(k x)$")
ax.axhline(0, color="black", lw=1)

# Indicador de Amplitud (ym)
ax.annotate("", xy=(0.25, 0), xytext=(0.25, A),
            arrowprops=dict(arrowstyle="<->", color="crimson", lw=2))
ax.text(0.27, A / 2, r"Amplitud $y_m$", color="crimson", fontsize=11, fontweight="bold", va="center")

# Indicador de Longitud de Onda (lambda)
ax.annotate("", xy=(0.25, A + 0.03), xytext=(1.25, A + 0.03),
            arrowprops=dict(arrowstyle="<->", color="darkgreen", lw=2))
ax.text(0.75, A + 0.05, r"Longitud de onda $\lambda$", color="darkgreen", fontsize=11, fontweight="bold", ha="center")

# Marcar Cresta y Valle
ax.plot(0.25, A, "ro", markersize=7)
ax.text(0.25, A + 0.02, "Cresta", color="crimson", fontsize=10, ha="center")
ax.plot(0.75, -A, "bo", markersize=7)
ax.text(0.75, -A - 0.04, "Valle", color="navy", fontsize=10, ha="center")

ax.set_xlim(0, 2.5)
ax.set_ylim(-A - 0.08, A + 0.1)
ax.set_xlabel("Posición x [m]", fontsize=10)
ax.set_ylabel("Desplazamiento y [m]", fontsize=10)
ax.set_title("Onda Armónica Progresiva: Amplitud, Crestas, Valles y Longitud de Onda", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "4.2-onda-armonica-parametros.png"), dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. GRAFICO: ONDA ESTACIONARIA (NODOS Y ANTINODOS)
# -------------------------------------------------------------
L = 1.2
x_est = np.linspace(0, L, 1000)
k_est = 2 * np.pi / L  # n = 2 armónico (2 bucles)

y1 = 2 * A * np.sin(k_est * x_est)   # Instante de máxima deformación +
y2 = -2 * A * np.sin(k_est * x_est)  # Instante de máxima deformación -

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(x_est, y1, color="tab:red", lw=2, label="Perfil inst. $t_1$")
ax.plot(x_est, y2, color="tab:blue", lw=2, linestyle="--", label="Perfil inst. $t_2$")
ax.axhline(0, color="gray", linestyle=":", alpha=0.7)

# Nodos (y = 0)
nodos_x = [0.0, L / 2, L]
for nx in nodos_x:
    ax.plot(nx, 0, "ko", markersize=9)
    ax.text(nx, -0.06, "Nodo (N)", color="black", fontsize=10, fontweight="bold", ha="center")

# Antinodos (|y| max)
antinodos_x = [L / 4, 3 * L / 4]
for ax_pos in antinodos_x:
    ax.plot(ax_pos, 2 * A, "go", markersize=8)
    ax.text(ax_pos, 2 * A + 0.03, "Antinodo (A)", color="darkgreen", fontsize=10, fontweight="bold", ha="center")

# Distancia entre nodos (\lambda / 2)
ax.annotate("", xy=(0.0, -0.15), xytext=(L / 2, -0.15),
            arrowprops=dict(arrowstyle="<->", color="purple", lw=1.8))
ax.text(L / 4, -0.21, r"Separación entre Nodos = $\frac{\lambda}{2}$", color="purple", fontsize=10, ha="center")

ax.set_xlim(-0.05, L + 0.05)
ax.set_ylim(-2 * A - 0.12, 2 * A + 0.12)
ax.set_xlabel("Posición x [m]", fontsize=10)
ax.set_ylabel("Desplazamiento y [m]", fontsize=10)
ax.set_title("Patrón de Onda Estacionaria (Segundo Armónico n=2)", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "4.2-onda-estacionaria.png"), dpi=300)
plt.close()

print(f"¡Gráficos de la 4.2 generados con éxito en: {OUTPUT_DIR}!")