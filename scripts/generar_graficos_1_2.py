import os
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Backend silencioso sin interfaz gráfica
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "assets", "Imagenes-1"))
os.makedirs(ASSETS_DIR, exist_ok=True)

# Configuración estética global
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.titlesize": 14
})

# -----------------------------------------------------------------------------
# 2. Gráfico 1: Líneas de Campo Vectorial y Equipotenciales (2D)
# -----------------------------------------------------------------------------
def generar_lineas_campo_y_equipotenciales():
    x = np.linspace(-3, 3, 250)
    y = np.linspace(-3, 3, 250)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)

    R_safe = np.where(R == 0, np.nan, R)

    V = -1.0 / R_safe

    gx = -X / (R_safe**3)
    gy = -Y / (R_safe**3)

    fig, ax = plt.subplots(figsize=(7, 6), dpi=300)

    levels = np.linspace(-3.0, -0.3, 10)
    CS = ax.contour(X, Y, V, levels=levels, cmap="plasma", linewidths=1.5, linestyles="dashed")
    ax.clabel(CS, inline=True, fontsize=8, fmt=r"$V = %1.1f$")

    ax.streamplot(
        X, Y, gx, gy,
        color="#2b5c8f",
        density=1.2,
        linewidth=1.0,
        arrowsize=1.2,
        arrowstyle="->"
    )

    ax.plot(0, 0, marker="o", markersize=12, color="#d9534f", label="Masa fuente ($M$)")

    ax.set_title(r"Líneas de Campo ($\vec{g}$) y Superficies Equipotenciales ($V$)", pad=12)
    ax.set_xlabel("Posición $x$ [u.a.]")
    ax.set_ylabel("Posición $y$ [u.a.]")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.legend(loc="upper right")
    ax.grid(True, linestyle=":", alpha=0.6)

    output_path = os.path.join(ASSETS_DIR, "1.2-lineas-campo-y-equipotenciales-puntual.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[✓] Gráfico generado exitosamente: {output_path}")

# -----------------------------------------------------------------------------
# 3. Gráfico 2: Pozo de Potencial Gravitatorio y Campo
# -----------------------------------------------------------------------------
def generar_pozo_potencial_y_campo():
    R_astro = 1.0
    r_int = np.linspace(0, R_astro, 100)
    r_ext = np.linspace(R_astro, 4.0, 300)

    V_int = -0.5 * (3.0 - (r_int / R_astro)**2)
    V_ext = -1.0 / r_ext

    g_int = r_int / (R_astro**3)
    g_ext = 1.0 / (r_ext**2)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True, dpi=300)

    # Plot 1: Pozo de Potencial
    ax1.plot(r_int, V_int, color="#d9534f", linewidth=2.0, label="Interior ($r < R$)")
    ax1.plot(r_ext, V_ext, color="#2077b4", linewidth=2.0, label=r"Exterior ($r \geq R$)")
    ax1.axvline(R_astro, color="gray", linestyle="--", alpha=0.7, label=r"Superficie $r = R$")
    ax1.axhline(0, color="black", linewidth=0.8, linestyle="-")
    ax1.set_ylabel(r"Potencial $V(r)$ [$\text{J/kg}$]")
    ax1.set_title("Perfil de Pozo de Potencial y Magnitud de Campo Gravitatorio", pad=10)
    ax1.legend(loc="lower right")
    ax1.grid(True, linestyle=":", alpha=0.6)

    # Plot 2: Módulo del Campo Gravitatorio
    ax2.plot(r_int, g_int, color="#d9534f", linewidth=2.0)
    ax2.plot(r_ext, g_ext, color="#2077b4", linewidth=2.0)
    ax2.axvline(R_astro, color="gray", linestyle="--", alpha=0.7)
    ax2.set_xlabel("Distancia radial $r / R$")
    ax2.set_ylabel(r"Módulo $|\vec{g}(r)|$ [$\text{m/s}^2$]")
    ax2.grid(True, linestyle=":", alpha=0.6)

    output_path = os.path.join(ASSETS_DIR, "1.2-potencial-vs-distancia.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[✓] Gráfico generado exitosamente: {output_path}")

# -----------------------------------------------------------------------------
# Ejecución Principal
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("Iniciando generación de gráficos para el Tema 1.2...")
    generar_lineas_campo_y_equipotenciales()
    generar_pozo_potencial_y_campo()
    print("¡Proceso finalizado correctamente!")