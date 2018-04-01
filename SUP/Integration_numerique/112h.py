#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:40:00 2017

@author: ewen
"""

import numpy as np
import scipy.integrate as sci

def fct(x):
    return (np.cos(x)-np.sin(x))*np.exp(-x)

x = np.arange(0,3*np.pi/2,1e-3)

valeur = -np.exp(-3*np.pi/2)

print("\r\n       Calculs d'integrales de mes 2")
print("               SCIPY.simpson")
print("_"*48+'\r\n')
print("Valeur theorique :",-np.exp(-3*np.pi/2))
print("_"*48+'\r\n')
nValue = sci.simps(fct(x),x)
print("Erreur de",abs(nValue-valeur))
print("_"*48+'\r\n')