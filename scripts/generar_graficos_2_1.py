import os
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Backend silencioso sin ventanas emergentes
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "assets", "Imagenes-2"))
os.makedirs(ASSETS_DIR, exist_ok=True)

# Configuración de estilo global para legibilidad clara
plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.titlesize": 14
})

# ==============================================================================
# GRÁFICO 1: Diagrama Esfuerzo vs Deformación (Curva de Propiedades Elásticas)
# ==============================================================================
def generar_diagrama_esfuerzo_deformacion():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    # Tramo A-B: Tramo Lineal (Proporcionalidad y Límite Elástico)
    e_lin = np.linspace(0, 0.15, 100)
    s_lin = 200 * e_lin
    
    # Tramo B-C: Fluencia y Comportamiento Plástico
    e_pla = np.linspace(0.15, 0.5, 200)
    s_pla = 30 + 100 * np.sin(np.pi * (e_pla - 0.15) / 0.7)
    
    # Tramo C-D: Resistencia Máxima y Ruptura
    e_rup = np.linspace(0.5, 0.65, 100)
    s_rup = s_pla[-1] - 80 * (e_rup - 0.5)**1.5
    
    # Graficación de las curvas
    ax.plot(e_lin, s_lin, 'b-', linewidth=2.5, label="Región Elástica (Ley de Hooke)")
    ax.plot(e_pla, s_pla, 'g-', linewidth=2.5, label="Región Plástica / Fluencia")
    ax.plot(e_rup, s_rup, 'r--', linewidth=2.0, label="Estrangulamiento y Ruptura")
    
    # Puntos Críticos del Parcial UNCA
    puntos = {
        'a': (0.12, 200*0.12, 'a: Límite de Proporcionalidad'),
        'b': (0.15, 200*0.15, 'b: Límite Elástico'),
        'c': (0.50, s_pla[-1], 'c: Resistencia Máxima (LRR)'),
        'd': (0.65, s_rup[-1], 'd: Punto de Ruptura')
    }
    
    for tag, (ex, ey, label) in puntos.items():
        ax.plot(ex, ey, 'ro', markersize=7)
        ax.annotate(f" {tag}", xy=(ex, ey), xytext=(ex+0.01, ey-2),
                    fontweight='bold', color='darkred')
    
    # Formateo y rótulos
    ax.set_title("Diagrama Esfuerzo ($\sigma$) vs. Deformación Unitaria ($\epsilon$) - UNCA", pad=15)
    ax.set_xlabel("Deformación Unitaria $\epsilon = \Delta L / L_0$ (Adimensional)")
    ax.set_ylabel("Esfuerzo $\sigma = F / A$ (MPa)")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="lower right", frameon=True)
    
    # Guardar imagen en alta resolución
    path_salida = os.path.join(ASSETS_DIR, "2.1-diagrama-esfuerzo-deformacion.png")
    plt.savefig(path_salida, bbox_inches="tight")
    plt.close()
    print(f"[OK] Creado: {path_salida}")

# ==============================================================================
# GRÁFICO 2: Ilustración de Tracción vs. Compresión
# ==============================================================================
def generar_esquema_traccion_compresion():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    # Esquema 1: Tracción
    ax1.add_patch(plt.Rectangle((0.3, 0.2), 0.4, 0.6, color="lightskyblue", ec="black", lw=2))
    ax1.annotate("", xy=(0.5, 0.95), xytext=(0.5, 0.8),
                 arrowprops=dict(arrowstyle="->", color="red", lw=3))
    ax1.annotate("", xy=(0.5, 0.05), xytext=(0.5, 0.2),
                 arrowprops=dict(arrowstyle="->", color="red", lw=3))
    ax1.text(0.5, 0.5, "TRACCIÓN\n$\Delta L > 0$", ha="center", va="center", fontsize=11, fontweight="bold")
    ax1.text(0.55, 0.9, "$F_\perp$", color="red", fontsize=12, fontweight="bold")
    ax1.set_title("Esfuerzo de Tracción")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1.05)
    ax1.axis("off")

    # Esquema 2: Compresión
    ax2.add_patch(plt.Rectangle((0.3, 0.2), 0.4, 0.6, color="salmon", ec="black", lw=2))
    ax2.annotate("", xy=(0.5, 0.8), xytext=(0.5, 0.95),
                 arrowprops=dict(arrowstyle="->", color="red", lw=3))
    ax2.annotate("", xy=(0.5, 0.2), xytext=(0.5, 0.05),
                 arrowprops=dict(arrowstyle="->", color="red", lw=3))
    ax2.text(0.5, 0.5, "COMPRESIÓN\n$\Delta L < 0$", ha="center", va="center", fontsize=11, fontweight="bold")
    ax2.text(0.55, 0.9, "$F_\perp$", color="red", fontsize=12, fontweight="bold")
    ax2.set_title("Esfuerzo de Compresión")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1.05)
    ax2.axis("off")

    path_salida = os.path.join(ASSETS_DIR, "2.1-traccion-compresion-young.png")
    plt.savefig(path_salida, bbox_inches="tight")
    plt.close()
    print(f"[OK] Creado: {path_salida}")

# ==============================================================================
# GRÁFICO 3: Ilustración de Esfuerzo de Corte / Cizalladura
# ==============================================================================
def generar_esquema_corte_cizalla():
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)
    
    # Bloque original (punteado)
    ax.add_patch(plt.Rectangle((0.1, 0.1), 0.5, 0.6, fill=False, edgecolor="gray", linestyle="--", linewidth=1.5))
    
    # Bloque deformado por cizalla
    polygon = np.array([[0.1, 0.1], [0.6, 0.1], [0.8, 0.7], [0.3, 0.7]])
    ax.add_patch(plt.Polygon(polygon, color="gold", alpha=0.6, ec="darkgoldenrod", lw=2))
    
    # Flecha de Fuerza Paralela
    ax.annotate("", xy=(0.75, 0.7), xytext=(0.3, 0.7),
                 arrowprops=dict(arrowstyle="->", color="crimson", lw=3))
    ax.text(0.5, 0.75, "$F_\parallel$", color="crimson", fontsize=12, fontweight="bold")
    
    # Indicadores de desplazamiento angular y lateral
    ax.plot([0.1, 0.3], [0.7, 0.7], "k:", lw=1)
    ax.text(0.2, 0.72, "$\Delta x$", ha="center", fontsize=10)
    ax.text(0.14, 0.25, "$\theta$", fontsize=12, fontweight="bold", color="darkgreen")
    
    ax.set_title("Esfuerzo de Corte o Cizalladura (Módulo $M$)")
    ax.set_xlim(0, 0.9)
    ax.set_ylim(0, 0.85)
    ax.axis("off")
    
    path_salida = os.path.join(ASSETS_DIR, "2.1-esfuerzo-corte-cizalla.png")
    plt.savefig(path_salida, bbox_inches="tight")
    plt.close()
    print(f"[OK] Creado: {path_salida}")

# Ejecución principal
if __name__ == "__main__":
    print("Generando gráficos del Tema 2.1...")
    generar_diagrama_esfuerzo_deformacion()
    generar_esquema_traccion_compresion()
    generar_esquema_corte_cizalla()
    print("¡Proceso completado exitosamente!")