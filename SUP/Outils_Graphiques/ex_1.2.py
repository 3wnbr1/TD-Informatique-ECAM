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

plt.close()
t = np.arange(0,5,0.01)
sp = ""

printer("Exercice 1.2")

plt.plot(t,osc(2,3,10),color="r",label=r"$s_{1}(t)$")
plt.plot(t,osc(2,3.5,0),color="g",label=r"$s_{2}(t)$")


while sp.lower() != "s" and sp.lower() != "p":
    sp = input("Voulez vous effectuer une somme ou un produit ? [S]/[P] : ")
    if sp.lower() == "s":
        plt.plot(t,osc(2,3,10)+osc(2,3.5,0),lw=2,color="b",label=r"$s_{1}(t)+s_{2}(t)$")
    elif sp.lower() == "p":
        plt.plot(t,osc(2,3,10)*osc(2,3.5,0),lw=2,color="k",label=r"$s_{1}(t)\cdot s_{2}(t)$")
    else:
        print("Saisie non valide")

plt.legend()

plt.grid()
plt.xlabel(r"$t$ en secondes")
plt.ylabel(r"$S(t)$")
plt.title("Sommes et produits de sinusoides")
plt.axis([0,5,-4,4])
plt.show()

