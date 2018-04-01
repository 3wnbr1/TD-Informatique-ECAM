#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:41:47 2017

@author: ewen
"""

import matplotlib.pyplot as plt
import numpy as np

plt.close()

g = 9.81
L = 2

def pendule(tt,ttp):
    '''theta, theta.'''
    return -g/L*np.sin(tt)

def euler2Order(f,a,b,dt,y0,yp0):
    '''Fonction, min, max, pas, CI 1, CI 2'''
    t, y, yp, n = [a],[y0],[yp0], 0
    while t[n] < b:
        y.append(y[n] + yp[n]*dt)
        yp.append(yp[n] + f(y[n],yp[n])*dt)
        t.append(t[n]+dt)
        n+=1
    return t,y,yp

for dt in [0.1,0.01,0.001,0.0001,0.00001]:
    t, tt, ttp = euler2Order(pendule,0,8,dt,3*np.pi/4,0)
    plt.plot(t,tt,label="dt ="+str(dt))
    
plt.grid()
plt.title("Oscilateur Mecanique")
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.legend(loc=4)
plt.axis([0,8,-5,5])

plt.show()