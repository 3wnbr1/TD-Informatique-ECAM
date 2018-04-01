import numpy as np
import matplotlib.pyplot as plt
from time import clock

# *********constantes*******

V0 = 10
g = 9.81
h = 1.5
c = 0.47
M = 0.7
alpha = np.pi/6
d = 0.07
S = ((np.pi)*d**2)/4
rho = 1.2
k = (1/2)*rho*c*S

# *********equations horaires sans frottements**********
t = 1

def x(t):
    return V0*t*np.cos(alpha)

def y(t):
    return h-(1/2)*g*t**2+V0*np.sin(alpha)*t


# *********equations horaires avec frottements**********

arctgte = np.arctan(V0*np.sin(alpha)*np.sqrt(k/(M*g)))

A = np.cos(t*np.sqrt(g*k/M)-arctgte)

B = M*g/(k*(V0*np.sin(alpha))**2 + M*g)

def xx(t):
    xx = (M/k)*np.log((k*V0*np.cos(alpha)*t+M)/M)
    return xx

def yy(t):
    yy = h + (M/k)*np.log(A) - (M/(2*k))*np.log(B)
    return yy

def dichotomia(f, v, a, b, p):
    n = 0
    t1 = clock()
    found = False
    while found is False and (b - a) > p:
        n += 1
        c = (b + a)/2
        if f(a)*f(c) < v:
            a = c
        elif f(a)*f(c) > v:
            b = c
        else:
            found = True
    t2 = clock()
    return c

t1 = dichotomia(y, 0, 0, 2, 1e-5)
t2 = dichotomia(yy, 0, 0, 2, 1e-5)
print("X0 sans frottements = ", t1, "metres")
print("X0 avec frottements = ", t2, "metres")

tt1 = np.linspace(0,t1,1000)
tt2 = np.linspace(0,t2,1000)
plt.plot(x(t1),y(t1),label="Equation sans frottements :")
plt.plot(xx(t2), yy(t2), label="Equation avec frottements")
plt.grid()
plt.legend()
plt.show()
