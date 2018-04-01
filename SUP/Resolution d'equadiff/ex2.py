#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:41:47 2017

@author: ewen
"""

import matplotlib.pyplot as plt
import numpy as np

plt.close()

m = 1
R = 1
f = 1.75
g = 10
tt = np.pi/4
ttp = 0
alpha = np.pi/6

def pendule(tt,ttp):
    '''theta, theta.'''
    return -(4*f*ttp+4*m*R*g*np.sin(alpha)*np.sin(tt))/(7*m*R**2)

def euler2Order(f,a,b,dt,y0,yp0):
    '''Fonction, min, max, pas, CI 1, CI 2'''
    t, y, yp, n = [a],[y0],[yp0], 0
    while t[n] < b:
        y.append(y[n] + yp[n]*dt)
        yp.append(yp[n] + f(y[n],yp[n])*dt)
        t.append(t[n]+dt)
        n+=1
    return t,y,yp


t, tt, ttp = euler2Order(pendule,0,10,1e-5,np.pi/4,0)
plt.plot(t,tt,label="dt = 1e-5")

plt.grid()
plt.title("Oscilateur Mecanique")
plt.xlabel("$t$"+" en s")
plt.ylabel(r"$\varphi(t)$"+" en rad")
plt.legend(loc=4)
plt.axis([0,10,-0.4ls,1])

plt.show()
