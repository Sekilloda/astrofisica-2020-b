import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update(
    {'text.usetex': True, 'font.family': 'serif', 'font.sans-serif': ['Helvetica'], 'figure.figsize': (10.6, 7.95),
     'figure.dpi': 150})
table = pd.read_excel('../datos/ngc3532.ods', engine='odf', header=119, na_values='')
table = table.replace(r'^\s*$', np.NaN, regex=True)
plx = table.loc[2:]["Plx"].to_numpy(dtype=np.float64)
e_plx = table.loc[2:]["e_Plx"].to_numpy(dtype=np.float64)
indexes = []
for index in range(len(plx)):
    if e_plx[index] >= 0.35 * np.abs(plx[index]) or e_plx[index] == 'nan' or plx[index] == 'nan':
        indexes.append(False)
    else:
        indexes.append(True)
BP = table.loc[2:]["BPmag"].to_numpy(dtype=np.float64)
BPworkable = BP[indexes]
BPRP = table.loc[2:]["BP-RP"].to_numpy(dtype=np.float64)
BPRPworkable = BPRP[indexes]
plt.scatter(BPRPworkable, BPworkable, label=r'Estrellas')
plt.xlabel(r'Color, dado por $BP-RP$', fontsize='xx-large')
plt.ylabel(r'Magnitud aparente', fontsize='xx-large')
plt.legend(fontsize='xx-large')
plt.title('Diagrama HR para NGC3532', fontsize='xx-large')
plt.gca().invert_yaxis()
plt.grid()
plt.savefig('../daniel_files/images/hrdiagram.png')
