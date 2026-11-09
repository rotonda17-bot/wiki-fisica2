import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener la carpeta donde está este script y apuntar a docs/assets/Imagenes-3
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-3")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GRAFICO: OSCILACION AMORTIGUADA Y SU ENVOLVENTE
# -------------------------------------------------------------
A0 = 1.0       # Amplitud inicial (m)
m = 0.25       # Masa (kg)
b = 0.10       # Coeficiente de amortiguamiento (kg/s)
w0 = 20.0      # Frecuencia natural (rad/s)

gamma = b / (2 * m)
w = np.sqrt(w0**2 - gamma**2)

t = np.linspace(0, 4, 1000)
x_t = A0 * np.exp(-gamma * t) * np.cos(w * t)
envolvente_pos = A0 * np.exp(-gamma * t)
envolvente_neg = -A0 * np.exp(-gamma * t)

plt.figure(figsize=(8, 4.5))
plt.plot(t, x_t, label=r"$x(t) = A_0 e^{-\frac{b}{2m}t} \cos(\omega t)$", color="tab:orange", lw=1.8)
plt.plot(t, envolvente_pos, label=r"Envolvente $+A_0 e^{-\frac{b}{2m}t}$", color="tab:blue", linestyle="--", lw=1.5)
plt.plot(t, envolvente_neg, label=r"Envolvente $-A_0 e^{-\frac{b}{2m}t}$", color="tab:blue", linestyle="--", lw=1.5)

plt.axhline(0, color="gray", linestyle=":", alpha=0.6)
plt.title("Movimiento Armónico Amortiguado (Subamortiguado)", fontsize=12)
plt.xlabel("Tiempo t [s]", fontsize=10)
plt.ylabel("Posición x [m]", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "3.4-oscilacion-amortiguada.png"), dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. GRAFICO: CURVAS DE RESONANCIA PARA DISTINTOS b
# -------------------------------------------------------------
F0 = 12.0
m_res = 2.0
w0_res = 20.0
w_range = np.linspace(5, 35, 1000)

coeficientes_b = [1.0, 4.0, 10.0]  # b chico, mediano, grande
colores = ["tab:red", "tab:blue", "tab:green"]

plt.figure(figsize=(8, 5))

for b_val, color in zip(coeficientes_b, colores):
    denom = np.sqrt((w_range**2 - w0_res**2)**2 + ((b_val * w_range) / m_res)**2)
    A_w = (F0 / m_res) / denom
    plt.plot(w_range, A_w, label=f"b = {b_val} kg/s", color=color, lw=2)

plt.axvline(x=w0_res, color="gray", linestyle="--", label=r"$\omega_0 = 20 \text{ rad/s}$ (Resonancia)")
plt.title(r"Curvas de Resonancia: Amplitud $A(\omega)$ para distintos $b$", fontsize=12)
plt.xlabel(r"Frecuencia impulsora $\omega$ [rad/s]", fontsize=10)
plt.ylabel("Amplitud A [m]", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "3.4-curva-resonancia.png"), dpi=300)
plt.close()

print(f"¡Gráficos de la 3.4 generados con éxito en: {OUTPUT_DIR}!")