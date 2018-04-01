import numpy as np
from time import clock

def fct(x):
    return 1-x*np.exp(x)

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
    return c, n, t2 - t1


a = float(input("Entrez la borne superieure : "))
b = float(input("Entrez la borne inferieure : "))
p = float(input("Entrez la precision : "))
v = float(input("Entrez la valeur : "))

root, n, time = dichotomia(fct, 0, -2, 2, 0.01)
print("La fonction vaut", 0, "pour x=", root, "\r\nIl a fallu", n, "iterations en", time, "secondes")
