import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener la carpeta donde está este script y apuntar directamente a docs/assets/Imagenes-3
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-3")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GRAFICO: PENDULO FISICO Y TORSION (Diagramas de Fuerzas / Torcas)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Subplot 1: Péndulo Físico
theta = np.radians(20)
d = 1.0
x_cm = d * np.sin(theta)
y_cm = -d * np.cos(theta)

ax1.plot([0, x_cm], [0, y_cm], color="black", lw=3, label="Vara / Cuerpo")
ax1.plot(0, 0, 'ro', markersize=8, label="Pivote O")
ax1.plot(x_cm, y_cm, 'go', markersize=10, label="Centro de Masa (CM)")

# Vector peso y componentes
ax1.arrow(x_cm, y_cm, 0, -0.6, head_width=0.04, head_length=0.06, fc='blue', ec='blue')
ax1.text(x_cm + 0.05, y_cm - 0.5, r"$m \vec{g}$", color="blue", fontsize=11)

ax1.set_xlim(-0.5, 1.0)
ax1.set_ylim(-1.4, 0.2)
ax1.set_aspect('equal')
ax1.set_title(r"Péndulo Físico: $\tau = -m g d \sin\theta$", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(loc="upper right")

# Subplot 2: Péndulo de Torsión
circle = plt.Circle((0, 0), 0.7, color='lightblue', ec='darkblue', lw=2)
ax2.add_patch(circle)
ax2.plot([0, 0], [0, 1.2], color="black", lw=4, label="Eje / Alambre")
ax2.plot(0, 0, 'ko', markersize=6)

# Flecha indicadora de rotación / torca
ax2.annotate("", xy=(0.4, 0.4), xytext=(0.5, 0.1),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.4", color="red", lw=2))
ax2.text(0.3, 0.5, r"$\tau = -\kappa \theta$", color="red", fontsize=12)

ax2.set_xlim(-1.0, 1.0)
ax2.set_ylim(-1.0, 1.4)
ax2.set_aspect('equal')
ax2.set_title(r"Péndulo de Torsión: $T = 2\pi\sqrt{I/\kappa}$", fontsize=11)
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "3.3-pendulo-fisico-y-torsion.png"), dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. GRAFICO: RELACION MCU VS MAS (Círculo de Referencia)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6))

# Círculo MCU
theta_val = np.pi / 3  # 60 grados
A = 1.0
x_p = A * np.cos(theta_val)
y_p = A * np.sin(theta_val)

circle_ref = plt.Circle((0, 0), A, color='none', ec='tab:blue', linestyle='--', lw=2, label="Trayectoria MCU")
ax.add_patch(circle_ref)

# Radio y punto en MCU
ax.plot([0, x_p], [0, y_p], color="tab:blue", lw=2)
ax.plot(x_p, y_p, 'ro', markersize=9, label="Partícula en MCU")

# Proyección sobre el eje X (MAS)
ax.plot([x_p, x_p], [y_p, 0], color="tab:red", linestyle=":", lw=2)
ax.plot(x_p, 0, 'go', markersize=10, label=r"Proyección MAS $x(t)$")

# Ejes principales
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Textos descriptivos
ax.text(x_p / 2, y_p / 2 + 0.05, r"$R = A$", color="tab:blue", fontsize=11)
ax.text(x_p + 0.05, -0.15, r"$x = A \cos(\omega t + \phi)$", color="tab:green", fontsize=11, fontweight='bold')

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.set_title("Relación entre MCU (Círculo) y MAS (Proyección)", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "3.3-mcu-vs-mas.png"), dpi=300)
plt.close()

print(f"¡Gráficos de la 3.3 generados con éxito en: {OUTPUT_DIR}!")