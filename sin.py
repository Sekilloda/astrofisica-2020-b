import numpy as np
import matplotlib.pyplot as plt
import quantities as pq

xaxis=np.linspace(0,np.pi*2,100)
yaxis=np.sin(xaxis)*np.cos(xaxis)

plt.plot(xaxis,yaxis)
plt.ylabel('sin(x)')

f = open("chuleta.txt", "w")
for xaxis in np.linspace(0,np.pi*2,100):
	y=np.sin(xaxis)*np.cos(xaxis)
	f.write(str(xaxis))
	f.write(" ")
	f.write(str(y))
	f.write('\n')

plt.show ()

