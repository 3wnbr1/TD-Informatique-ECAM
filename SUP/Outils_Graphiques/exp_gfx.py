#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:19:30 2017

@author: ewen
"""

import matplotlib.pyplot as plt
import numpy as np

def h(x,a,f):
    y = np.exp(-a*x)*np.sin(np.pi*2*f*x)
    return y

x = np.arange(0,16,0.01)

plt.close()

plt.plot(x,h(x,1,0.4),color="b",label=r"$\alpha = 1$")
plt.plot(x,h(x,0.5,0.4),color="r",label=r"$\alpha = 0.5$")
plt.plot(x,h(x,0.2,0.4),color="g",label=r"$\alpha = 0.2$")

plt.legend()

plt.grid()
plt.xlabel(r"$x(s)$")
plt.ylabel(r"$h(x)$")
plt.title(r"$h(x)=e^{-\alpha x } sin(2\pi f x)$")
plt.axis([0,16,-1,1])
plt.show()