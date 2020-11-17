import matplotlib.pyplot as plt
import numpy as np


x, y, erry, g, errg = np.loadtxt('GRB.txt',unpack=True, usecols=[0,1,2,3,4])


plt.errorbar(x, y, yerr=erry, fmt=".-")
#plt.plot(x,y, label='grb')

plt.xlabel('tiempo[ms]')
plt.ylabel('cuentas')
plt.title('GRB')
plt.show()
#plt.savefig('graph.png')
