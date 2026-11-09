import os
import matplotlib.pyplot as plt
import numpy as np

# Definir ruta absoluta para guardar en docs/assets/Imagenes-6
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, "docs", "assets", "Imagenes-6")
os.makedirs(output_dir, exist_ok=True)

# Estilo visual oscuro
plt.style.use('dark_background')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.edgecolor': '#444444',
    'axes.linewidth': 1.2,
    'grid.color': '#333333',
    'grid.linestyle': '--',
    'grid.alpha': 0.6
})

# ==============================================================================
# Gráfico 1: Curva de Calentamiento del Agua (Q vs T con mesetas de fase)
# ==============================================================================
fig, ax = plt.subplots(figsize=(9, 5.5))

Q_acum = [0, 41.8, 375.8, 794.4, 3050.4, 3092.2] # kJ por kg de agua
T_agua = [-20, 0, 0, 100, 100, 120]             # °C

ax.plot(Q_acum, T_agua, color='#00e5ff', linewidth=3, label='Trayectoria Térmica')
ax.scatter(Q_acum, T_agua, color='#ff4081', s=50, zorder=5)

# Anotaciones de mesetas con raw strings (r'...') para evitar avisos
ax.annotate(r'Fusión (Hielo + Agua)' + '\n' + r'$T = 0^\circ$C ($L_f$)', xy=(200, 0), xytext=(120, -15),
            arrowprops=dict(facecolor='#00e5ff', shrink=0.05, width=1, headwidth=6),
            bbox=dict(boxstyle='round,pad=0.3', fc='#1e1e1e', ec='#00e5ff', alpha=0.8))

ax.annotate(r'Vaporización (Agua + Vapor)' + '\n' + r'$T = 100^\circ$C ($L_v$)', xy=(1900, 100), xytext=(1400, 75),
            arrowprops=dict(facecolor='#00e5ff', shrink=0.05, width=1, headwidth=6),
            bbox=dict(boxstyle='round,pad=0.3', fc='#1e1e1e', ec='#00e5ff', alpha=0.8))

ax.set_title(r'Unidad 6.2: Curva de Calentamiento del Agua ($1\text{ kg}$)', fontsize=14, pad=15, weight='bold')
ax.set_xlabel(r'Energía Térmica Agregada $Q$ (kJ)', fontsize=12, labelpad=10)
ax.set_ylabel(r'Temperatura $T$ (°C)', fontsize=12)
ax.grid(True)
ax.legend(loc='upper left', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_curva_calentamiento_agua.png"), dpi=300)
plt.close()

# ==============================================================================
# Gráfico 2: Trabajo en Diagrama P-V (Área bajo la curva)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 5.5))

V = np.linspace(1.0, 4.0, 200)
P = 120 / V # Isoterma en kPa

ax.plot(V, P, color='#ffab40', linewidth=2.8, label=r'Proceso $P(V)$')
ax.fill_between(V, P, color='#ffab40', alpha=0.25, label=r'Trabajo $W = \int P \, dV$ (Área)')

ax.set_title(r'Unidad 6.2: Trabajo Cuasiestático en Diagrama $P-V$', fontsize=14, pad=15, weight='bold')
ax.set_xlabel(r'Volumen $V$ ($\text{m}^3$)', fontsize=12, labelpad=10)
ax.set_ylabel(r'Presión $P$ (kPa)', fontsize=12)
ax.set_ylim(0, 140)
ax.grid(True)
ax.legend(loc='upper right', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_trabajo_diagrama_pv.png"), dpi=300)
plt.close()

# ==============================================================================
# Gráfico 3: Comparativa de Procesos Termodinámicos en Plano P-V
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 5.5))

V_init = 2.0
P_init = 100.0
V_eval = np.linspace(2.0, 5.0, 200)

# Curvas desde (V_init, P_init)
P_isobar = np.full_like(V_eval, P_init)
P_isoterm = P_init * (V_init / V_eval)
P_adiabat = P_init * (V_init / V_eval)**1.4

ax.plot(V_eval, P_isobar, color='#76ff03', linewidth=2.5, label=r'Isobárico ($P = \text{cte}$)')
ax.plot(V_eval, P_isoterm, color='#00bcd4', linewidth=2.5, label=r'Isotérmico ($T = \text{cte}$)')
ax.plot(V_eval, P_adiabat, color='#e91e63', linewidth=2.5, label=r'Adiabático ($P V^\gamma = \text{cte}$)')
ax.vlines(x=V_init, ymin=30, ymax=P_init, color='#ff4081', linewidth=2.5, linestyle='--', label=r'Isocórico ($V = \text{cte}$)')

ax.scatter([V_init], [P_init], color='#ffffff', s=70, zorder=5)
ax.annotate(r'Estado Inicial $(V_0, P_0)$', xy=(V_init, P_init), xytext=(V_init + 0.2, P_init + 5), fontsize=10)

ax.set_title(r'Unidad 6.2: Trayectorias Termodinámicas en Diagrama $P-V$', fontsize=14, pad=15, weight='bold')
ax.set_xlabel(r'Volumen $V$ ($\text{m}^3$)', fontsize=12, labelpad=10)
ax.set_ylabel(r'Presión $P$ (kPa)', fontsize=12)
ax.set_ylim(20, 120)
ax.grid(True)
ax.legend(loc='upper right', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_procesos_termodinamicos_pv.png"), dpi=300)
plt.close()

# ==============================================================================
# Gráfico 4: Ciclo Termodinámico abcd (Ejemplo 19.4 / TP10)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 5.5))

V_a, V_c = 2.0, 5.0 # en 1e-3 m3
P_a, P_b = 30.0, 80.0 # en kPa

# Vértices del ciclo
ax.plot([V_a, V_a, V_c, V_c, V_a], [P_a, P_b, P_b, P_a, P_a], color='#00e5ff', linewidth=3, label=r'Ciclo $abcd$')
ax.scatter([V_a, V_a, V_c, V_c], [P_a, P_b, P_b, P_a], color='#ff4081', s=60, zorder=5)

ax.annotate('a', (V_a, P_a), xytext=(-15, -15), textcoords='offset points', fontsize=12, color='#ffffff', weight='bold')
ax.annotate('b', (V_a, P_b), xytext=(-15, 10), textcoords='offset points', fontsize=12, color='#ffffff', weight='bold')
ax.annotate('d', (V_c, P_b), xytext=(10, 10), textcoords='offset points', fontsize=12, color='#ffffff', weight='bold')
ax.annotate('c', (V_c, P_a), xytext=(10, -15), textcoords='offset points', fontsize=12, color='#ffffff', weight='bold')

ax.set_title(r'Unidad 6.2: Diagrama $P-V$ del Ciclo $abcd$ (TP10 - Ejercicio B9)', fontsize=14, pad=15, weight='bold')
ax.set_xlabel(r'Volumen $V$ ($10^{-3}\ \text{m}^3$)', fontsize=12, labelpad=10)
ax.set_ylabel(r'Presión $P$ (kPa)', fontsize=12)
ax.set_xlim(1.0, 6.0)
ax.set_ylim(10, 100)
ax.grid(True)
ax.legend(loc='upper right', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_ciclo_termodinamico_abcd.png"), dpi=300)
plt.close()

print(f"¡Los 4 gráficos de la Unidad 6.2 se generaron exitosamente sin advertencias en:\n{output_dir}")