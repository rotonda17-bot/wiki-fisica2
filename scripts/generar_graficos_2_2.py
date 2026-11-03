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
# GRÁFICO: Interpretación Gráfica de E, K y U en función de la Posición x
# ==============================================================================
def generar_grafico_energia_mecanica():
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    
    # Parámetros del sistema elástico
    x_max = 0.18  # Amplitud de 18 cm en metros
    k = 19.6      # Constante N/m (Ejemplo Cátedra UNCA)
    
    x = np.linspace(-x_max, x_max, 300)
    
    # Funciones de Energía en función de la posición
    U = 0.5 * k * (x**2)                   # Parábola de Energía Potencial
    E_total = 0.5 * k * (x_max**2)         # Línea constante de Energía Mecánica
    K = E_total - U                        # Parábola invertida de Energía Cinética
    
    # Graficación de Curvas
    ax.plot(x, U, 'r-', linewidth=2.5, label=r"Energía Potencial $U(x) = \frac{1}{2}k x^2$")
    ax.plot(x, K, 'b-', linewidth=2.5, label=r"Energía Cinética $K(x) = \frac{1}{2}m v^2$")
    ax.plot(x, [E_total]*len(x), 'k--', linewidth=2.0, label=r"Energía Mecánica Total $E = K + U$")
    
    # Puntos de Cruce e Intersección (Mitad Cinética y Mitad Potencial)
    x_cruce = x_max / np.sqrt(2)
    E_mitad = E_total / 2.0
    
    ax.plot([x_cruce, -x_cruce], [E_mitad, E_mitad], 'go', markersize=7)
    ax.annotate(r"$\frac{1}{2}E$ ($K = U$)", xy=(x_cruce, E_mitad), 
                xytext=(x_cruce + 0.015, E_mitad), fontweight='bold', color='darkgreen')
    ax.annotate(r"$\frac{1}{2}E$ ($K = U$)", xy=(-x_cruce, E_mitad), 
                xytext=(-x_cruce - 0.055, E_mitad), fontweight='bold', color='darkgreen')
    
    # Líneas punteadas indicadoras de los límites de retorno
    ax.axvline(x=x_max, color='gray', linestyle=':', linewidth=1.2)
    ax.axvline(x=-x_max, color='gray', linestyle=':', linewidth=1.2)
    ax.axvline(x=0, color='gray', linestyle=':', linewidth=1.0)
    
    # Rótulos de ejes y puntos notables
    ax.set_xticks([-x_max, -x_cruce, 0, x_cruce, x_max])
    ax.set_xticklabels([r"$-x_{\max}$", r"$-\frac{x_{\max}}{\sqrt{2}}$", r"$0$", r"$\frac{x_{\max}}{\sqrt{2}}$", r"$x_{\max}$"])
    
    ax.set_yticks([0, E_mitad, E_total])
    ax.set_yticklabels([r"$0$", r"$\frac{1}{2}E$", r"$E = U_{\max}$"])
    
    ax.set_title(r"Energía Mecánica $E$, Cinética $K$ y Potencial $U$ vs. Posición $x$", pad=15)
    ax.set_xlabel("Posición $x$ (m)")
    ax.set_ylabel("Energía (J)")
    ax.set_xlim(-x_max * 1.15, x_max * 1.15)
    ax.set_ylim(-0.02, E_total * 1.15)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper right", frameon=True)
    
    # Guardar imagen en alta resolución
    path_salida = os.path.join(ASSETS_DIR, "2.2-grafico-energia-mecanica.png")
    plt.savefig(path_salida, bbox_inches="tight")
    plt.close()
    print(f"[OK] Creado: {path_salida}")

if __name__ == "__main__":
    print("Generando gráficos del Tema 2.2...")
    generar_grafico_energia_mecanica()
    print("¡Proceso completado exitosamente!")