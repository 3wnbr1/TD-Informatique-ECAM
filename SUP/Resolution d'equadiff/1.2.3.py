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

def pendule(z,zp):
    '''z, v(z '''
    return -10-0.02*zp*np.abs(zp)

def euler2Order(f,a,b,dt,y0,yp0):
    '''Fonction, min, max, pas, CI 1, CI 2'''
    t, y, yp, n = [a],[y0],[yp0], 0
    while t[n] < b:
        y.append(y[n] + yp[n]*dt)
        yp.append(yp[n] + f(y[n],yp[n])*dt)
        t.append(t[n]+dt)
        n+=1
    return t,y,yp


t, z, zp = euler2Order(pendule,0,10,1e-5,10,5)

plt.subplot(1,2,1)
plt.plot(t,z,label="dt = 1e-5")
plt.grid()
plt.title("Chute Libre")
plt.xlabel("$t$")
plt.ylabel("$z(t)$")
plt.legend(loc=4)
plt.axis([0,10,-160,20])


plt.subplot(1,2,2)
plt.plot(t,zp,label="dt = 1e-5")
plt.grid()
plt.title("Vitesse en chute Libre")
plt.xlabel("$t$")
plt.ylabel("$v(t)$"+" en m/s")
plt.legend(loc=4)
plt.axis([0,10,-25,10])

plt.tight_layout()

plt.show()
