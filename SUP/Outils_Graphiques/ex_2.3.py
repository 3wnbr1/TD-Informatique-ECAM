#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def r1(tt):
    return np.sin(5*tt)+3*np.cos(tt)

def r2(tt):
    return np.sin(5*tt)-3*np.cos(tt)

def r3(tt):
    return -3*np.cos(2*tt)+np.sin(7*tt)-1

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)

printer("Exercice 2.3")
plt.close()
tt = np.arange(0,2*np.pi,0.1)
plt.polar(tt,r1(tt),color="r")
plt.polar(tt,r2(tt),color="r")
plt.polar(tt,r3(tt),color="r")
plt.title("Papillon de Sautereau")

plt.show()