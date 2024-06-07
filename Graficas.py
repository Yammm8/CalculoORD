import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Función para graficar áreas bajo la curva
def plot_area(ax, func, x_range, color='blue', alpha=0.3, label=None):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)
    ax.plot(x, y, label=label)
    ax.fill_between(x, y, color=color, alpha=alpha)
    # Calcular el área
    area, _ = quad(func, x_range[0], x_range[1])
    ax.text((x_range[0] + x_range[1]) / 2, max(y) / 2, f'Área = {area:.2f}', horizontalalignment='center')

# Inciso 1a
fig, ax1 = plt.subplots()
plot_area(ax1, lambda x: 2*x + 1, [1, 3], color='blue', label='y = 2x + 1')
ax1.set_title('Área bajo la recta y = 2x + 1 entre t = 1 y t = 3')
ax1.legend()
plt.xlabel('x')
plt.ylabel('y')

# Inciso 1b
fig, ax2 = plt.subplots()
x_value = 4  # Ejemplo de x > 1
plot_area(ax2, lambda x: 2*x + 1, [1, x_value], color='green', label=f'Área bajo y = 2x + 1 entre t = 1 y t = {x_value}')
ax2.set_title(f'Área bajo la recta y = 2x + 1 entre t = 1 y t = {x_value}')
ax2.legend()
plt.xlabel('x')
plt.ylabel('y')

# Inciso 1c
fig, ax2 = plt.subplots()
x_value = 1  # Ejemplo de x > 1
x_range = np.linspace(-2, x_value, 400)
ax2.plot(x_range, x_range**2 + x_range - 2, color='orange', label='$x^2 + x - 2$')
ax2.set_title(f'Recta y = x^2 + x - 2 entre t = -2 y t = {x_value}')
ax2.legend()
plt.xlabel('x')
plt.ylabel('y')


# Inciso 2a
fig, ax3 = plt.subplots()
plot_area(ax3, lambda t: 1 + t**2, [-2, 2], color='red', label='y = 1 + t^2')
ax3.set_title('Área bajo la curva y = 1 + t^2 entre t = -2 y t = 2')
ax3.legend()
plt.xlabel('t')
plt.ylabel('y')

# Inciso 2c
fig, ax4 = plt.subplots()
t_values = np.linspace(-1, 2, 400)
A_prime = 1 + t_values**2
ax4.plot(t_values, A_prime, label="A'(x) = 1 + x^2")
ax4.set_title('Derivada de la función área A(x) = 1 + x^2')
ax4.legend()
plt.xlabel('x')
plt.ylabel('A\'(x)')

# Inciso 3a
fig, ax5 = plt.subplots()
x_range_3a = np.linspace(0, 2, 400)
ax5.plot(x_range_3a, np.cos(x_range_3a**2), label='f(x) = cos(x^2)')
ax5.set_title('Función f(x) = cos(x^2) en el intervalo [0, 2]')
ax5.legend()
plt.xlabel('x')
plt.ylabel('f(x)')

# Inciso 3b
fig, ax6 = plt.subplots()
x_value_3b = 2
plot_area(ax6, lambda t: np.cos(t**2), [0, x_value_3b], color='purple', label=f'Área bajo cos(t^2) de 0 a {x_value_3b}')
ax6.set_title(f'Área bajo la curva cos(t^2) desde 0 hasta {x_value_3b}')
ax6.legend()
plt.xlabel('x')
plt.ylabel('y')

# Inciso 3c
fig, ax7 = plt.subplots()
x_values_3c = np.linspace(0, 2, 50)
g_values = [quad(lambda t: np.cos(t**2), 0, x)[0] for x in x_values_3c]
ax7.plot(x_values_3c, g_values, marker='o', label='g(x) = Integral de cos(t^2) de 0 a x')
ax7.set_title('Función g(x) evaluada en puntos específicos')
ax7.legend()
plt.xlabel('x')
plt.ylabel('g(x)')

# Mostrar todas las gráficas
plt.show()
