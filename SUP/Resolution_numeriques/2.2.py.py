import numpy as np
from time import clock


def fct(x):
    return 1-x*np.exp(x)

def fctp(x):
    return -np.exp(x)*(x+1)

def newton(f, fp, x0, p):
    n = 0
    t1 = clock()
    u = x0
    v = u - f(u)/fp(u)
    while abs(u-v) > p:
        n += 1
        u = v
        v = u - f(u)/fp(u)
    t2 = clock()
    return v, n, t2 - t1

root, n, time = newton(fct, fctp, 0, 1e-10)
print("La fonction vaut", 0, "pour x=", root)
print("Il a fallu", n, "iterations en", time, "secondes")
