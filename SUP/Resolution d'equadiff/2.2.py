# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

g = 9.81
L = 2
omcarre = g/L


def fct(X, t):
    return [X[1], -omcarre*np.sin(X[0])]


t = np.arange(0, 8, 0.1)
X = odeint(fct, [3*np.pi/4, 0], t)

plt.close()
plt.plot(t, X[:, 0])
plt.xlabel("$t$ en s")
plt.ylabel("$\theta$ en rad")
plt.title("Oscilateur amorti")
plt.grid()
plt.legend()
plt.axis([0, 8, -3, 3])

plt.show()
