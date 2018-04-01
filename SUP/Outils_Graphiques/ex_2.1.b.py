#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def exp(m):
    return (1+m*x)/(1+x**2)

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)


x = np.arange(-5,5,0.01)
plt.close()
printer("Exercice 2.1.b")

for m in np.arange(1,6,1):
    plt.plot(x, exp(m),label="m ="+str(m))

plt.legend()

plt.grid()
plt.xlabel(r"$x$")
plt.ylabel(r"$y(x)$")
plt.title(r"$y = \frac{1+mx}{1+x^2}$")
plt.axis([-5,5,-2,4])
plt.show()
