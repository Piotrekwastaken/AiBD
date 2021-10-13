#Piotr Żak zadanie 3
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 5

x1 = np.linspace(-1, 1, 100)
x2 = np.linspace(-6, 6, 100)
x3 = np.linspace(0, 5, 100)

y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

plt.plot(x1, y1)
plt.xlabel('x1')
plt.ylabel('f(x1)')
plt.show()

#plt.plot(x2, y2)
#plt.plot(x3, y3)