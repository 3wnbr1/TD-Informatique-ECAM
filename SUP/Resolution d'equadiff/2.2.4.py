# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def fct(X, t):
    return [X[1], -10-0.02*X[1]*np.abs(X[1])]


t = np.arange(0, 10, 0.1)
X = odeint(fct, [10, 5], t)

plt.close()

plt.subplot(1, 2, 1)
plt.plot(t, X[:, 0])
plt.xlabel("$t$ en s")
plt.ylabel(r"$z$ en m")
plt.title("Chute libre odeint")
plt.grid()
plt.axis([0, 10, -160, 20])

plt.subplot(1, 2, 2)
plt.plot(t, X[:, 1])
plt.xlabel("$v$ en m/s")
plt.ylabel(r"$z$ en m")
plt.title("Vitesse Chute libre odeint")
plt.grid()
plt.axis([0, 10, -25, 10])

plt.tight_layout()

plt.show()
