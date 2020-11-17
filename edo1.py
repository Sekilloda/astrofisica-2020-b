import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define la función a derivar/integrar dy/dx = 2x - 3y
def dy_dx(y, x):
    return 2*x - 3*y

xs = np.linspace(0,5,100)
y0 = 3.0  # condición inicial
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()
plt.rcParams.update({'font.size': 14})  # tamaño de la fuente
plt.xlabel("x")
plt.ylabel("y")
plt.title('dy/dx = 2x - 3y con y(0)=3')
plt.plot(xs, ys);
plt.show ()

