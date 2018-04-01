import numpy as np
import matplotlib.pyplot as plt
from time import clock

def fct(x):
    return 1-x*np.exp(x)


plt.close()

x = np.linspace(-2, 2, 1000)

plt.plot(x, fct(x))
plt.grid()
plt.title("$f(x)=1-x.e^{x}$")
plt.show()
