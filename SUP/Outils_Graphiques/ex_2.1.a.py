#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def exp(m):
    return m**2*x*np.exp(-m*x)

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)


x = np.arange(-0.1,3,0.01)
plt.close()
printer("Exercice 2.1.a")

for m in np.arange(1,9,1):
    plt.plot(x, exp(m),label="m ="+str(m))

plt.legend()

plt.grid()
plt.xlabel(r"$x$")
plt.ylabel(r"$y(x)$")
plt.title(r"$y=m^{2}x exp(-m x)$")
plt.axis([-0.1,3,-2,4])
plt.show()
