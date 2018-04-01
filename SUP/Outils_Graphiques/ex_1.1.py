#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def osc(s,f,phi):
    '''Sm, f en Hz, phi en degrees''' 
    y = s*np.cos(2*np.pi*f*t+phi*np.pi/180)
    return y

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)


t = np.arange(0,5,0.01)

printer("Exercice 1.1")

plt.close()

plt.plot(t,osc(2,3,10),color="b",label=r"$s_{1}(t)$")

plt.legend()

plt.grid()
plt.xlabel(r"$t$ en secondes")
plt.ylabel(r"$S_{1}(t)$")
plt.title(r"$S_{m_1}cos(2\pi f_{1}t+\varphi )$")
plt.axis([0,5,-2,2])
plt.show()

