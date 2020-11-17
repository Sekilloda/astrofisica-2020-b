import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#defino el parametro
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
vu = np.linspace(-4, 4, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
#especifico la "trayectoria" x(r,theta),y(r, theta),z o w(vu)
x = r * np.sin(theta)
y = r * np.cos(theta)
w = vu - 2
ax.plot(x, y, z, label='curva paramétrica 1')
ax.plot(x, w, z, label='curva paramétrica 2')
ax.legend()

plt.show()
