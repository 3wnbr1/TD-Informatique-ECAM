#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:39:31 2017

@author: ewen
"""

import matplotlib.pyplot as plt
import numpy as np

E, R, C = 12, 50, 20e-6


def eqn(E, R, C):
    return E*(1-np.exp(-t/(R*C)))


plt.close()

t = np.arange(0, 0.01, 1e-5)

plt.plot(t, eqn(E, R, C), label="Solution analytique")
plt.grid()
plt.title("Charge du condensateur")
plt.xlabel("$t$")
plt.ylabel("$u(t)$")
plt.legend(loc=4)

plt.show()
