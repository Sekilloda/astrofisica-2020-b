from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import LogNorm

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.sans-serif': ['Helvetica'],
                     'figure.figsize': (10.6, 7.95), 'figure.dpi': 150})
data = pd.read_csv('../datos/muchosdatosfinal.dat', sep=' ', header=None,
                   names=['Type', 'px', 'py', 'pz', 'rx', 'ry', 'FTime', 'Energy'])
particle_type = {1: 'Fotón', 2: 'Positrón', 3: 'Electrón', 5: 'Anti muón', 6: 'Muon'}
data = data.drop(data[data['Type'] == 8].index)
data = data.drop(data[data['Type'] == 9].index)
print(set(data['Type']))

for i in [i for i in range(np.min(data['Type']), np.max(data['Type']) + 1) if i != 4]:
    plt.scatter(data['FTime'].where(data['Type'] == i), data['Energy'].where(data['Type'] == i), label=particle_type[i],
                s=6)
plt.legend(fontsize=15)
plt.xlabel('Tiempo de vuelo [ns]', fontsize=18)
plt.ylabel('Energía [GeV]', fontsize=18)
plt.title('Energía vs. tiempo de vuelo', fontsize=18)
plt.grid(True)
plt.savefig('../daniel_files/images/part1.png')
plt.show()

plt.clf()
# next
labels, counts = np.unique(data['Type'], return_counts=True)
plt.bar(particle_type.values(), counts, align='center', color=['blue', 'green', 'red', 'cyan', 'yellow', 'black'],
        )
plt.xlabel('Tipo de partícula', fontsize=18)
plt.ylabel('Conteo', fontsize=18)
plt.savefig('../daniel_files/images/part2.png')
plt.show()
plt.clf()
# next
plt.hist2d(data['rx'], data['ry'], norm=LogNorm())
plt.xlabel('Posición en el eje x [cm]', fontsize=18)
plt.ylabel('Posición en el eje y [cm]', fontsize=18)
plt.title('Mapa de calor de medición de partículas', fontsize=18)
plt.colorbar()
plt.savefig('../daniel_files/images/part3.png')
plt.show()

plt.clf()
