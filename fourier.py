import numpy as np 
from scipy.fft import fft
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('classic')
##########################################
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.figure()
plt.subplot(211)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlabel('frecuencia[Hz]')
plt.ylabel('y')
plt.suptitle('Transformada de Fourier sin (50.2\u03C0x) + 0.5 sin(80.2\u03C0x)')
plt.subplot(212)
plt.plot(x,y,'-r')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
