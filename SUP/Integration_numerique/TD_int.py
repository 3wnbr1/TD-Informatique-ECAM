import sys
import numpy as np


def maFonction(x):
    return np.exp(x)*np.sin(3*x)


def trapezes(fct, a, b, n):
    h = (b-a)/n
    r = (h/2)*(fct(a)+fct(b))
    for i in range(1, n):
        r += h*fct(a+i*h)
    return r


def rectanglesG(fct, a, b, n):
    h, r = (b-a)/n, 0
    for i in range(n):
        r += h*fct(a+i*h)
    return r


if __name__ == '__main__':
    n, a, b = "", -1*np.pi/2, np.pi/2
    while n.isdigit() is False:
        n = input("Nombre de points d'integration : ")
    n, method = int(n), ""
    while method != "t" and method != "r":
        method = input("Choix de la methode : [T] Trapezes / [R] Rectangles ? ").lower()
        if method == "t":
            print("Resultat par la methode des Trapezes :", trapezes(maFonction, a, b, n))
        elif method == "r":
            print("Resultat par la methode des Rectangles :", rectanglesG(maFonction, a, b, n))
        else:
            print("ERROR : Not a number")
