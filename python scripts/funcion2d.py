import numpy as np
import matplotlib.pyplot as plt
import quantities as pq

x=np.arange(0,100,1)
y=x*x-3

plt.plot(x,y)
plt.title('Funcion')
plt.ylabel('f(x)')
plt.xlabel('x')

f = open("../datos/chuletita.txt", "w")
for x in np.arange(0,100,1):
	v=x*x-3
	f.write(str(x))
	f.write(" ")
	f.write(str(v))
	f.write('\n')

plt.show()

