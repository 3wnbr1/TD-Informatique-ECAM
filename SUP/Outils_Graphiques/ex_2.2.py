#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def x(m):
    return 3*np.cos(t)-m*np.cos(3*t)

def y(m):
    return 3*np.sin(t)-m*np.sin(3*t)

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)


t = np.arange(0,2*np.pi,0.01)
plt.close()
printer("Exercice 2.2")

for m in np.arange(1,3,0.5):
    plt.plot(t, x(m),label="Xm ="+str(m))
    plt.plot(t, y(m),label="Ym ="+str(m))

plt.legend()

plt.grid()
plt.xlabel(r"$t$")
plt.title("Sinusoides")
plt.axis([0,2*np.pi,-5,5])
plt.show()
