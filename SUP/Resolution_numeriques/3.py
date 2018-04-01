import scipy.optimize as sc
import numpy as np
import matplotlib.pyplot as plt

plt.close()

def f(x):
    return x**3+2*x**2-x-2

x = np.linspace(-2.5, 1.5, 1000)

print("Les zeros sont :",np.roots([-1,2,-1,-2]))

plt.plot(x,f(x))
plt.show()
