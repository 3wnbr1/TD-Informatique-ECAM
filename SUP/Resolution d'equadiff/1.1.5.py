#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:39:31 2017

@author: ewen
"""

import matplotlib.pyplot as plt
import numpy as np

E, R, C = 12, 50, 20e-6


def u(t):
    return E*(1-np.exp(-t/(R*C)))


def circuitRC(u):
    return (E-u)/(R*C)


def euler1Order(f, a, b, dt, u0):
    '''Fonction, min, max, pas, CI'''
    t, y, n = [a], [u0], 0
    while t[n] < b:
        y.append(y[n] + f(y[n])*dt)
        t.append(t[n]+dt)
        n += 1
    return t, y


plt.close()

t = np.arange(0, 0.01, 1e-5)


plt.plot(t, u(t), label="Solution analytique")
for dt in [0.002, 0.001, 0.0001, 0.00001]:
    t, y = euler1Order(circuitRC, 0, 0.01, dt, 0)
    plt.plot(t, y, label="solution numerique : dt ="+str(dt))

plt.grid()
plt.title("Charge du condensateur")
plt.xlabel("$t$")
plt.ylabel("$u(t)$")
plt.legend(loc=4)
plt.axis([0, 0.01, 0, 15])

plt.show()
