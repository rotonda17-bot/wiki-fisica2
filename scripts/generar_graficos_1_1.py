import os
import matplotlib

# Desactivar GUI para guardar directo a archivo
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 1. Definir la ruta exacta hacia la nueva carpeta docs/assets/Imagenes-1/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "assets", "Imagenes-1"))
os.makedirs(ASSETS_DIR, exist_ok=True)

# 2. Datos físicos y cálculos
G = 6.674e-11
MT = 5.972e24
RT = 6.371e6

K = (4 * (np.pi**2)) / (G * MT)

h = np.linspace(300e3, 40000e3, 400)
r = RT + h

T_horas = np.sqrt(K * (r**3)) / 3600
v_kms = np.sqrt((G * MT) / r) / 1000

# 3. Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

ax1.plot(r / 1e6, T_horas, color="navy", lw=2.5)
ax1.axhline(24, color="crimson", linestyle="--", alpha=0.7)
ax1.set_title("3a Ley de Kepler: Periodo T vs Radio r")
ax1.set_xlabel("Radio Orbital r [miles de km]")
ax1.set_ylabel("Periodo T [Horas]")
ax1.grid(True, linestyle=":", alpha=0.7)

ax2.plot(r / 1e6, v_kms, color="darkgreen", lw=2.5)
ax2.set_title("Rapidez Orbital v vs Radio r")
ax2.set_xlabel("Radio Orbital r [miles de km]")
ax2.set_ylabel("Rapidez v [km/s]")
ax2.grid(True, linestyle=":", alpha=0.7)

plt.tight_layout()

# 4. Definir la variable ruta_salida e invocar savefig
ruta_salida = os.path.join(ASSETS_DIR, "1.1-kepler-periodo-y-velocidad.png")
plt.savefig(ruta_salida, dpi=300)
plt.close()

print(f"✅ Gráfico guardado exitosamente en: {os.path.abspath(ruta_salida)}")