import os
import matplotlib.pyplot as plt
import numpy as np

RUTA = os.path.join("docs", "assets", "Imagenes-5")
os.makedirs(RUTA, exist_ok=True)
plt.style.use("dark_background")

# 1. Torricelli
h = np.linspace(0, 10, 100)
R = 2 * np.sqrt(h * (10 - h))
plt.figure(figsize=(7, 4))
plt.plot(h, R, color="#00bcd4")
plt.title("Torricelli: Alcance vs Profundidad")
plt.tight_layout()
plt.savefig(os.path.join(RUTA, "grafico_torricelli_alcance.png"), dpi=300)
plt.close()

# 2. Venturi
x = np.linspace(0, 10, 100)
v = 2.0 + 8.0 * np.exp(-((x - 5.0) ** 2) / 2.0)
plt.figure(figsize=(7, 4))
plt.plot(x, v, color="#ff9800")
plt.title("Venturi: Perfil de Velocidad")
plt.tight_layout()
plt.savefig(
    os.path.join(RUTA, "grafico_venturi_presion_velocidad.png"), dpi=300
)
plt.close()

# 3. Viscosidad
y = np.linspace(-1, 1, 100)
v_visc = 5.0 * (1 - y**2)
plt.figure(figsize=(7, 4))
plt.plot(v_visc, y, color="#e91e63")
plt.title("Viscosidad: Perfil Parabólico")
plt.tight_layout()
plt.savefig(os.path.join(RUTA, "grafico_perfil_viscosidad.png"), dpi=300)
plt.close()