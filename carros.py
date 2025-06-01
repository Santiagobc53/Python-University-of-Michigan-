# comparativa_niro_kona.py

import numpy as np
import matplotlib.pyplot as plt

# Datos de comparación
items = ['Precio (USD)', 'Calidad (1-10)', 'Eficiencia (mpg)', 'Seguridad (1-5)', 'Garantía (años)', 'Mantenimiento (USD/año)']
kiro_vals = [30000, 8.5, 50, 5, 5, 500]
kona_vals = [32000, 8.2, 48, 5, 5, 450]

# Número de categorías
n_items = len(items)
# Posiciones en el eje x
indices = np.arange(n_items)
# Ancho de las barras
width = 0.35

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Barras para cada modelo
bars_kiro = ax.bar(indices - width/2, kiro_vals, width, label='Kia Niro', hatch='//')
bars_kona = ax.bar(indices + width/2, kona_vals, width, label='Hyundai Kona', hatch='\\\\')

# Etiquetas y título
ax.set_ylabel('Valor')
ax.set_title('Comparativa Kia Niro vs Hyundai Kona')
ax.set_xticks(indices)
ax.set_xticklabels(items, rotation=45, ha='right')
ax.legend()

# Mostrar valores encima de cada barra
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),  # 3 puntos de separación
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars_kiro)
autolabel(bars_kona)

fig.tight_layout()
plt.show()
