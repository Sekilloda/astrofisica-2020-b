import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy import optimize
#ingreso de datos (x,y)

x = np.array([0,2,4,7,10,14])
y = np.array([1,3,5,7,11,21])
m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(x*x) - np.sum(x) ** 2)
b = (np.sum(y) - m *np.sum(x)) / len(x)

print(m)
print(b)

def predict(x):
    return m*x - b
vec = np.arange(16)
plt.scatter(x,y, color='black')
plt.plot(vec,predict(vec))
plt.xlabel("x")
plt.ylabel("y= mx + b")
plt.title('Regresión lineal')

plt.show()
