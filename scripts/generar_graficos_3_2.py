import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener la carpeta donde está este archivo script y apuntar directamente a docs/assets/Imagenes-3
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(WIKI_DIR, "docs", "assets", "Imagenes-3")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GRAFICO: ENERGIA VS POSICION E(x), K(x), U(x)
# -------------------------------------------------------------
A = 0.18  # Amplitud (m)
k = 19.6  # Constante del resorte (N/m)
E_total = 0.5 * k * (A**2)

x = np.linspace(-A, A, 500)
U = 0.5 * k * (x**2)
K = E_total - U

plt.figure(figsize=(8, 5))
plt.plot(x, U, label=r"$U(x)$ (Potencial Elástica)", color="tab:blue", lw=2)
plt.plot(x, K, label=r"$K(x)$ (Cinética)", color="tab:green", lw=2)
plt.axhline(y=E_total, color="tab:red", linestyle="--", label=r"$E$ (Mecánica Total)", lw=2)

plt.axvline(x=0, color="gray", linestyle=":", alpha=0.6)
plt.axvline(x=A, color="gray", linestyle=":", alpha=0.6)
plt.axvline(x=-A, color="gray", linestyle=":", alpha=0.6)

plt.title("Intercambio de Energía según la Posición (MAS)", fontsize=12)
plt.xlabel("Posición x [m]", fontsize=10)
plt.ylabel("Energía [J]", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper center")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "3.2-energia-vs-posicion.png"), dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. GRAFICO: ENERGIA VS TIEMPO E(t), K(t), U(t)
# -------------------------------------------------------------
w = 8.08  # Frecuencia angular (rad/s)
t = np.linspace(0, 2 * np.pi / w, 500)

U_t = E_total * (np.cos(w * t)**2)
K_t = E_total * (np.sin(w * t)**2)

plt.figure(figsize=(8, 5))
plt.plot(t, U_t, label=r"$U(t)$ (Potencial Elástica)", color="tab:blue", lw=2)
plt.plot(t, K_t, label=r"$K(t)$ (Cinética)", color="tab:green", lw=2)
plt.axhline(y=E_total, color="tab:red", linestyle="--", label=r"$E$ (Mecánica Total)", lw=2)

plt.title("Evolución Temporaria de la Energía (MAS)", fontsize=12)
plt.xlabel("Tiempo t [s]", fontsize=10)
plt.ylabel("Energía [J]", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "3.2-energia-vs-tiempo.png"), dpi=300)
plt.close()

print(f"¡Gráficos guardados con éxito en: {OUTPUT_DIR}!")