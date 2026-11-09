import os
import matplotlib.pyplot as plt

# Definir la ruta absoluta apuntando a docs/assets/Imagenes-6/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, "docs", "assets", "Imagenes-6")
os.makedirs(output_dir, exist_ok=True)

# Configuración de estilo visual oscuro
plt.style.use('dark_background')

def generar_esquema_calorimetro():
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Pared exterior (Aislamiento térmico / Vasija Dewar)
    ax.add_patch(plt.Rectangle((2, 1), 6, 7.5, fill=True, facecolor='#263238', edgecolor='#78909c', lw=3))
    
    # Cámara de vacío / Aislamiento adiabático
    ax.add_patch(plt.Rectangle((2.3, 1.3), 5.4, 7, fill=True, facecolor='#1c252a', edgecolor='#455a64', lw=1.5, linestyle='--'))
    
    # Recipiente Interno (Vaso calorimétrico)
    ax.add_patch(plt.Rectangle((2.7, 1.6), 4.6, 6.2, fill=True, facecolor='#004d40', edgecolor='#00bfa5', lw=2))
    
    # Agua / Mezcla en equilibrio térmico
    ax.add_patch(plt.Rectangle((2.7, 1.6), 4.6, 4.5, fill=True, facecolor='#00897b', alpha=0.6))

    # Lingote / Muestra metálica sumergida
    ax.add_patch(plt.Rectangle((4.3, 2.2), 1.4, 1.4, fill=True, facecolor='#ff7043', edgecolor='#ff3d00', lw=1.5))
    ax.text(5.0, 2.9, r'$m_m, c_m$', color='#ffffff', fontsize=9, ha='center', va='center', weight='bold')

    # Agitador mecánico
    ax.plot([6.0, 6.0], [2.0, 8.8], color='#ffb74d', lw=2.5)
    ax.plot([5.5, 6.5], [2.0, 2.0], color='#ffb74d', lw=2.5)

    # Termómetro graduado
    ax.plot([3.8, 3.8], [3.2, 9.0], color='#ff4081', lw=3)
    ax.scatter([3.8], [2.8], color='#ff4081', s=100, zorder=5)

    # Tapa Aislante Superior
    ax.add_patch(plt.Rectangle((1.8, 7.8), 6.4, 0.8, fill=True, facecolor='#37474f', edgecolor='#cfd8dc', lw=2))

    # Etiquetas explicativas con raw strings r'...'
    ax.text(5.0, 9.4, r'Calorímetro Ideal Aislado', color='#00e5ff', fontsize=12, ha='center', weight='bold')
    ax.text(5.0, 0.5, r'Principio: $\sum Q = Q_{\mathrm{ganado}} + Q_{\mathrm{cedido}} = 0$', color='#ffffff', fontsize=11, ha='center', weight='bold')

    plt.tight_layout()
    
    # Guardar en la carpeta Imagenes-6
    ruta_guardado = os.path.join(output_dir, "esquema_calorimetro.png")
    plt.savefig(ruta_guardado, dpi=300, transparent=True)
    plt.close()
    print(f"¡Imagen generada exitosamente en:\n{ruta_guardado}")

if __name__ == "__main__":
    generar_esquema_calorimetro()