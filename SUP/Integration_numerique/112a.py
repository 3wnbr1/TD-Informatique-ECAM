#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Basic."""

import numpy as np
from matplotlib import pyplot as plt


def fct(x):
    return (np.cos(x)-np.sin(x))*np.exp(-x)


x = np.arange(0, 3*np.pi/2, 1e-4)

plt.close()
plt.plot(x, fct(x), label="$f(x) = (cos(x)-sin(x))e^{-x}$")
plt.legend()
plt.title("Calcul d'une integrale de mes 2")
plt.grid()
plt.show()
