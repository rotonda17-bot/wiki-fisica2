import os
import matplotlib.pyplot as plt
import numpy as np

# Configurar la ruta de salida a la carpeta Imagenes-6
output_dir = os.path.join("docs", "assets", "Imagenes-6")
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
# Gráfico 1: Dilatación Térmica Libre vs. Esfuerzo Térmico de Compresión
# ==============================================================================
fig, ax1 = plt.subplots(figsize=(9, 5.5))

# Parámetros (Barra de Acero de L0 = 1.0 m)
L0 = 1.0
alpha_acero = 11e-6       # 1/°C
Y_acero = 20e10           # Pa (200 GPa)
delta_T = np.linspace(0, 100, 200) # °C

# Cálculos
delta_L_mm = (alpha_acero * L0 * delta_T) * 1000 # mm
esfuerzo_MPa = (alpha_acero * Y_acero * delta_T) / 1e6 # MPa

# Curva 1: Dilatación libre
color1 = '#00e5ff'
ax1.set_xlabel(r'Variación de Temperatura $\Delta T$ (°C)', fontsize=12, labelpad=10)
ax1.set_ylabel(r'Dilatación Lineal Libre $\Delta L$ (mm)', color=color1, fontsize=12)
line1 = ax1.plot(delta_T, delta_L_mm, color=color1, linewidth=2.5, label=r'Dilatación Libre ($\Delta L$)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True)

# Curva 2: Esfuerzo térmico (eje secundario)
ax2 = ax1.twinx()
color2 = '#ff4081'
ax2.set_ylabel(r'Esfuerzo Térmico de Compresión $\sigma$ (MPa)', color=color2, fontsize=12)
line2 = ax2.plot(delta_T, esfuerzo_MPa, color=color2, linewidth=2.5, linestyle='--', label=r'Esfuerzo Impedido ($F/A$)')
ax2.tick_params(axis='y', labelcolor=color2)

# Título y Leyenda
plt.title(r'Unidad 6.1: Dilatación Libre vs. Esfuerzo Térmico (Acero)', fontsize=14, pad=15, weight='bold')

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_dilatacion_vs_esfuerzo.png"), dpi=300)
plt.close()

# ==============================================================================
# Gráfico 2: Energía Cinética Traslacional Media y Velocidad rms vs T
# ==============================================================================
fig, ax1 = plt.subplots(figsize=(9, 5.5))

# Parámetros (Gas Nitrógeno / Aire)
kB = 1.380649e-23   # J/K
R = 8.314462         # J/(mol K)
Mm = 0.02897         # kg/mol (Masa molar promedio del aire)
T_kelvin = np.linspace(100, 600, 250) # K

# Cálculos
K_media_eV = (1.5 * kB * T_kelvin) / 1.60218e-19 # eV
v_rms = np.sqrt(3 * R * T_kelvin / Mm)          # m/s

# Curva 1: Energía Cinética Media (eV)
color1 = '#76ff03'
ax1.set_xlabel(r'Temperatura Absoluta $T$ (Kelvin)', fontsize=12, labelpad=10)
ax1.set_ylabel(r'Energía Cinética Media $\bar{K}$ (eV)', color=color1, fontsize=12)
line1 = ax1.plot(T_kelvin, K_media_eV, color=color1, linewidth=2.5, label=r'Energía Cinética $\bar{K}(T)$')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True)

# Curva 2: Velocidad cuadrática media v_rms (eje secundario)
ax2 = ax1.twinx()
color2 = '#ffab40'
ax2.set_ylabel(r'Velocidad Cuadrática Media $v_{rms}$ (m/s)', color=color2, fontsize=12)
line2 = ax2.plot(T_kelvin, v_rms, color=color2, linewidth=2.5, linestyle='-.', label=r'Velocidad $v_{rms}(T)$')
ax2.tick_params(axis='y', labelcolor=color2)

# Título y Leyenda
plt.title(r'Unidad 6.1: Teoría Cinética — $\bar{K}$ y $v_{rms}$ en Función de $T$ (Aire)', fontsize=14, pad=15, weight='bold')

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='#1e1e1e', edgecolor='#444444')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_distribucion_energia_cinetica.png"), dpi=300)
plt.close()

print(f"¡Gráficos de la Unidad 6.1 generados exitosamente en {output_dir}/!")