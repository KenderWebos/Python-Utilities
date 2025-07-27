import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dibujar_pared(ax, inicio, fin, color='black'):
    ax.plot([inicio[0], fin[0]], [inicio[1], fin[1]], color=color, linewidth=3)

def dibujar_puerta(ax, pos, rotacion=0):
    if rotacion == 0:  # Puerta horizontal
        ax.plot([pos[0], pos[0] + 0.8], [pos[1], pos[1]], 'brown', linewidth=3)
        arco = patches.Arc(pos, 0.8, 0.8, theta1=0, theta2=90, color='brown')
    else:  # Puerta vertical
        ax.plot([pos[0], pos[0]], [pos[1], pos[1] + 0.8], 'brown', linewidth=3)
        arco = patches.Arc(pos, 0.8, 0.8, theta1=90, theta2=180, color='brown')
    ax.add_patch(arco)

def dibujar_ventana(ax, pos, ancho=1.2):
    ax.plot([pos[0], pos[0] + ancho], [pos[1], pos[1]], 'blue', linewidth=2)

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(15, 10))

# Dimensiones de la casa (en metros)
ancho_casa = 10
largo_casa = 20

# Dibujar paredes exteriores
paredes_exteriores = [
    ((0, 0), (ancho_casa, 0)),
    ((ancho_casa, 0), (ancho_casa, largo_casa)),
    ((ancho_casa, largo_casa), (0, largo_casa)),
    ((0, largo_casa), (0, 0))
]

for inicio, fin in paredes_exteriores:
    dibujar_pared(ax, inicio, fin)

# Dibujar paredes interiores
# Sala y comedor
dibujar_pared(ax, (0, 8), (6, 8))  # División sala-comedor
dibujar_pared(ax, (6, 0), (6, 12))  # Pared vertical principal

# Cocina
dibujar_pared(ax, (0, 12), (6, 12))  # División comedor-cocina

# Pasillo
dibujar_pared(ax, (6, 12), (6, largo_casa))  # Pasillo vertical
dibujar_pared(ax, (6, 16), (ancho_casa, 16))  # División dormitorios superiores

# Dormitorios
dibujar_pared(ax, (6, 12), (ancho_casa, 12))  # División dormitorio inferior

# Baños
dibujar_pared(ax, (8, 12), (8, 16))  # División baños

# Dibujar puertas
# Puerta principal
dibujar_puerta(ax, (3, 0), 0)
# Puerta sala a comedor
dibujar_puerta(ax, (4, 8), 0)
# Puerta comedor a cocina
dibujar_puerta(ax, (4, 12), 0)
# Puertas a dormitorios
dibujar_puerta(ax, (6, 14), 1)  # Dormitorio 1
dibujar_puerta(ax, (6, 18), 1)  # Dormitorio 2
dibujar_puerta(ax, (6, 10), 1)  # Dormitorio principal
# Puertas baños
dibujar_puerta(ax, (8, 14), 1)  # Baño 1
dibujar_puerta(ax, (8, 18), 1)  # Baño 2

# Dibujar ventanas
dibujar_ventana(ax, (1, 0))  # Ventana sala
dibujar_ventana(ax, (7, 0))  # Ventana dormitorio principal
dibujar_ventana(ax, (0, 10))  # Ventana cocina
dibujar_ventana(ax, (10, 14))  # Ventana dormitorio 1
dibujar_ventana(ax, (10, 18))  # Ventana dormitorio 2

# Añadir etiquetas de las habitaciones
plt.text(3, 4, 'SALA\n25m²', ha='center', va='center', fontsize=10)
plt.text(3, 10, 'COMEDOR\n20m²', ha='center', va='center', fontsize=10)
plt.text(3, 16, 'COCINA\n20m²', ha='center', va='center', fontsize=10)
plt.text(8, 8, 'DORMITORIO\nPRINCIPAL\n18m²', ha='center', va='center', fontsize=10)
plt.text(8, 14, 'DORMITORIO 1\n15m²', ha='center', va='center', fontsize=10)
plt.text(8, 18, 'DORMITORIO 2\n15m²', ha='center', va='center', fontsize=10)
plt.text(9.5, 14, 'BAÑO 1\n6m²', ha='center', va='center', fontsize=8)
plt.text(9.5, 18, 'BAÑO 2\n6m²', ha='center', va='center', fontsize=8)
plt.text(6.5, 15, 'PASILLO', ha='center', va='center', rotation=90, fontsize=8)

# Configurar el aspecto del plano
plt.title('Plano Arquitectónico - Casa 10x20m', pad=20, fontsize=14)
plt.grid(True, linestyle='--', alpha=0.3)
plt.axis('equal')
plt.xlim(-1, ancho_casa + 1)
plt.ylim(-1, largo_casa + 1)

# Mostrar dimensiones
plt.text(ancho_casa/2, -0.8, f'{ancho_casa} metros', ha='center', fontsize=10)
plt.text(-0.8, largo_casa/2, f'{largo_casa} metros', va='center', rotation=90, fontsize=10)

# Añadir escala
plt.plot([0, 1], [-0.5, -0.5], 'k-', linewidth=2)
plt.text(0.5, -0.3, '1 metro', ha='center', fontsize=8)

# Añadir norte
plt.arrow(9, 19, 0, 0.5, head_width=0.2, head_length=0.2, fc='k', ec='k')
plt.text(9, 19.8, 'N', ha='center', va='bottom')

plt.show()