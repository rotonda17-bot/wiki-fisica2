import os
import matplotlib.pyplot as plt
import numpy as np

# Ruta exacta de destino según tu árbol de directorios
RUTA_SALIDA = os.path.join("docs", "assets", "Imagenes-5")
os.makedirs(RUTA_SALIDA, exist_ok=True)
plt.style.use("dark_background")


def generar_grafico_b1():
    """Genera gráfico visual de Área vs Presión para el cimiento (Ejercicio B1)."""
    presiones = np.linspace(10, 60, 100)  # kg_f/cm^2
    peso_kgf = 8e7  # 80,000 ton -> kg_f
    areas_m2 = (peso_kgf / presiones) / 10000.0

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(presiones, areas_m2, color="#00bcd4", linewidth=2.5, label="A(P)")
    ax.scatter(
        [40],
        [200],
        color="#ff4081",
        s=70,
        zorder=5,
        label="Cimiento B1 (40 kg/cm², 200 m²)",
    )

    ax.annotate(
        "P = 40 kg/cm²\nA = 200 m²",
        (40, 200),
        textcoords="offset points",
        xytext=(15, 10),
        fontsize=9,
        color="#ffffff",
        bbox=dict(
            boxstyle="round,pad=0.3", fc="#006064", ec="#00bcd4", alpha=0.85
        ),
    )

    ax.set_title(
        "Relación Área de Apoyo vs. Presión Admisible del Suelo",
        fontsize=11,
        pad=12,
    )
    ax.set_xlabel("Presión Admisible P [kg_f/cm²]", fontsize=9.5)
    ax.set_ylabel("Área Requerida A [m²]", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.25)
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig(
        os.path.join(RUTA_SALIDA, "grafico_cimientos_b1.png"), dpi=300
    )
    plt.close()


def generar_grafico_b2():
    """Genera la gráfica de Presión Manométrica vs Profundidad en Glicerina (Ejercicio B2)."""
    rho_glicerina = 1250.0
    g = 9.80

    h = np.linspace(0, 1.0, 100)
    P_man_kPa = (rho_glicerina * g * h) / 1000.0

    h_puntos = np.array([0.30, 0.90])
    P_puntos_kPa = (rho_glicerina * g * h_puntos) / 1000.0

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(
        h,
        P_man_kPa,
        color="#5c6bc0",
        linewidth=2.5,
        label=r"$P_{man}(h) = \rho \cdot g \cdot h$",
    )
    ax.scatter(
        h_puntos,
        P_puntos_kPa,
        color="#ff4081",
        s=60,
        zorder=5,
        label="Puntos B2 (30 cm y 90 cm)",
    )

    for hp, Pp in zip(h_puntos, P_puntos_kPa):
        ax.annotate(
            f"h={hp} m\nP={Pp:.2f} kPa",
            (hp, Pp),
            textcoords="offset points",
            xytext=(12, -10),
            ha="left",
            fontsize=9,
            color="#ffffff",
            bbox=dict(
                boxstyle="round,pad=0.3", fc="#1a237e", ec="#5c6bc0", alpha=0.85
            ),
        )

    ax.set_title(
        "Presión Manométrica vs. Profundidad en Glicerina", fontsize=11, pad=12
    )
    ax.set_xlabel("Profundidad h [m]", fontsize=9.5)
    ax.set_ylabel("Presión Manométrica [kPa]", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.25)
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    plt.savefig(
        os.path.join(RUTA_SALIDA, "grafico_presion_glicerina.png"), dpi=300
    )
    plt.close()


def generar_grafico_b7():
    """Genera gráfico de balance de fuerzas sobre el cubo sumergido (Ejercicio B7)."""
    fuerzas = ["F_sup (Tapa)", "F_inf (Base)", "Empuje (E)", "Peso (W)", "Tensión (T)"]
    valores = [37558.15, 39738.46, 2180.31, 4410.00, 2229.69]
    colores = ["#e53935", "#43a047", "#00acc1", "#ffb300", "#8e24aa"]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(fuerzas, valores, color=colores, width=0.55, alpha=0.85)

    for bar, val in zip(bars, valores):
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval + 800,
            f"{val:,.2f} N",
            ha="center",
            va="bottom",
            fontsize=8.5,
            color="#ffffff",
            fontweight="bold",
        )

    ax.set_yscale("log")  # Escala logarítmica para comparar fuerzas grandes y pequeñas
    ax.set_title(
        "Balance de Fuerzas y Tensiones en el Cubo Sumergido (Caso B7)",
        fontsize=11,
        pad=12,
    )
    ax.set_ylabel("Magnitud de Fuerza [N] (Escala Log)", fontsize=9.5)
    ax.grid(True, which="both", linestyle="--", alpha=0.2)

    plt.tight_layout()
    plt.savefig(
        os.path.join(RUTA_SALIDA, "grafico_balance_cubo_b7.png"), dpi=300
    )
    plt.close()


if __name__ == "__main__":
    generar_grafico_b1()
    generar_grafico_b2()
    generar_grafico_b7()