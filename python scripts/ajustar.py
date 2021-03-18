"""
===============
Ajustar una curva
===============


"""

############################################################
# generar algunos datos
import numpy as np

# generador de números randómicos
np.random.seed(0)

x_data = np.linspace(-5, 5, num=50)
y_data = 3.5 * np.cos(1.5 * x_data) + np.random.normal(size=50)

# dibujar los datos
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)

############################################################
# ajustar con la función coseno
from scipy import optimize

def test_func(x, a, b):
    return a * np.cos(b * x)

params, params_covariance = optimize.curve_fit(test_func, x_data, y_data,
                                               p0=[2, 2])

print(params)

############################################################
# graficar

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, color='red', label='Datos')
plt.plot(x_data, test_func(x_data, params[0], params[1]),
         label='ajuste')
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title('Ajustar una curva')

plt.legend(loc='best')

plt.show()
