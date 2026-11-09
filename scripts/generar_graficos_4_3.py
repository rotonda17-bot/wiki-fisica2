import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener directorio del script y configurar salida en docs/assets/Imagenes-4
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GRAFICO: ONDA DE PRESION VS ONDA DE DESPLAZAMIENTO (DESFASE pi/2)
# -------------------------------------------------------------
x = np.linspace(0, 2.5 * np.pi, 1000)
s = np.cos(x)       # Onda de desplazamiento s(x)
dp = np.sin(x)      # Onda de presión ΔP(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

# Subplot 1: Desplazamiento
ax1.plot(x, s, color="tab:blue", lw=2, label=r"$s(x) = s_{\text{máx}} \cos(kx)$")
ax1.axhline(0, color="gray", linestyle=":", alpha=0.6)
ax1.set_ylabel("Desplazamiento $s$", fontsize=10)
ax1.set_title("Relación de Fase: Onda de Desplazamiento vs. Onda de Presión", fontsize=12)
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(loc="upper right")

# Marcar nodos y crestas de s
ax1.annotate("Equilibrio (s = 0)", xy=(np.pi/2, 0), xytext=(np.pi/2, 0.5),
             arrowprops=dict(arrowstyle="->", color="tab:blue"), color="tab:blue")

# Subplot 2: Presión
ax2.plot(x, dp, color="tab:red", lw=2, label=r"$\Delta P(x) = \Delta P_{\text{máx}} \sin(kx)$")
ax2.axhline(0, color="gray", linestyle=":", alpha=0.6)
ax2.set_xlabel("Posición $kx$ [rad]", fontsize=10)
ax2.set_ylabel("Presión $\Delta P$", fontsize=10)
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend(loc="upper right")

# Marcar coincidencia de presión máxima con s=0
ax2.annotate("Máxima Presión (\Delta P_{máx})", xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.3, 0.6),
             arrowprops=dict(arrowstyle="->", color="tab:red"), color="tab:red")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "4.3-onda-presion-intensidad.png"), dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. GRAFICO: EFECTO DOPPLER (FRENTES DE ONDA COMPRIMIDOS)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Posición de la fuente en movimiento (avanza a la derecha)
x_fuente = 0.8
y_fuente = 0.0

ax.plot(x_fuente, y_fuente, 'ro', markersize=10, label="Fuente en Movimiento ($v_f$)")
ax.arrow(x_fuente, y_fuente, 0.5, 0, head_width=0.1, head_length=0.15, fc='red', ec='red', lw=2)

# Frentes de onda emitidos en posiciones anteriores (excéntricos)
centros_x = [-0.6, -0.2, 0.2, 0.5]
radios = [2.2, 1.7, 1.2, 0.6]

for cx, r in zip(centros_x, radios):
    circle = plt.Circle((cx, 0), r, color='tab:blue', fill=False, lw=1.8, linestyle='--')
    ax.add_patch(circle)

# Observadores
ax.plot(3.0, 0, 'go', markersize=9, label="Observador A (Aproximación)")
ax.plot(-3.0, 0, 'mo', markersize=9, label="Observador B (Alejamiento)")

# Cotas de longitud de onda comprimida vs expandida
ax.annotate(r"$\lambda'$ menor ($f'$ mayor)", xy=(1.5, -0.3), xytext=(2.2, -0.8),
            arrowprops=dict(arrowstyle="->", color="darkgreen"), color="darkgreen", fontweight="bold")
ax.annotate(r"$\lambda''$ mayor ($f''$ menor)", xy=(-1.5, -0.3), xytext=(-2.8, -0.8),
            arrowprops=dict(arrowstyle="->", color="purple"), color="purple", fontweight="bold")

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.8, 2.8)
ax.set_aspect('equal')
ax.set_title("Efecto Doppler: Compresión y Dilatación de Frentes de Onda", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "4.3-efecto-doppler.png"), dpi=300)
plt.close()

print(f"¡Gráficos de la 4.3 generados con éxito en: {OUTPUT_DIR}!")