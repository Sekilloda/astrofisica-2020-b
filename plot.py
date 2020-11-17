#from astropy.io import fits
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from math import *
from numpy import *
import time
from decimal import *
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from matplotlib.ticker import ScalarFormatter
from datetime import date
import matplotlib.patches as patches
plt.style.use('classic')


def extraer_filter(filename):
    datos = loadtxt(filename, float)
    energia = []
    for i in range (0,len(datos)):
        energia.append(datos[i])
    return energia


energia_electrones=extraer_filter('Energia_e.dat')
energia_piones=extraer_filter('Energia_pion.dat')


all_data=np.concatenate((energia_electrones,energia_piones), axis=None)

fig=plt.figure(figsize=(6.0, 6.0), dpi=100)
fig.patch.set_facecolor('white')
ax1 = fig.add_subplot(1, 1, 1)


ax1.hist(energia_piones,bins = 10 ** np.linspace(np.log10(1e-4), np.log10(1e3), 100),
         density=False,histtype='step',stacked=True, fill=False,label='$\pi^\pm$',linewidth=2.0,color='green')

ax1.hist(energia_electrones,bins = 10 ** np.linspace(np.log10(1e-4), np.log10(1e3), 100),
         density=False,histtype='step',stacked=True, fill=False,linewidth=2.0,color='m',label='$e^\pm$')
ax1.hist(all_data,bins = 10 ** np.linspace(np.log10(1e-4), np.log10(1e3), 100),
         density=False,histtype='step',stacked=True, fill=False,linewidth=2.0,color='k',label='$All$')

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
ax1.set_ylim(1e0,1e7)
ax1.legend(loc=1,fontsize=10.,ncol=2)
ax1.set_xlabel('$\mathrm{Energía(GeV)}$',fontsize=12.)
ax1.set_ylabel('$\mathrm{Flujo \\ de\\ partículas \\ secundarias \\ [m^{-2}s^{-1}]}$',fontsize=12.)
plt.title("Ejemplo de histograma (fluencia de partículas de Corsika)",fontsize=11)
plt.grid(True,linestyle=':')
plt.subplots_adjust(top=0.95, bottom=0.18, left=0.15, right=0.98, hspace=0.5,wspace=0.2)
plt.show()

