#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def dkart(a,tt):
    return (3*a*np.sin(tt)*np.cos(tt))/((np.cos(tt)**3+(np.sin(tt))**3))

def printer(string):
    print("="*len(string)*2)
    print(" "*int(len(string)/2)+string)
    print("="*len(string)*2)

printer("Exercice 2.3")
plt.close()
tt = np.arange(0,2*np.pi,0.1)

for a in np.arange(1,5,1):
    plt.polar(tt,dkart(a,tt))

plt.title("Folium de Descartes")
plt.axis([0,2*np.pi,0,10])

plt.show()