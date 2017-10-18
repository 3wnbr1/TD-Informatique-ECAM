#! /Users/ewen/anaconda3/bin/python
# coding: utf-8


"""Optimisation du rapport de denture dans un engrenage cylindrique."""


import numpy as np


def inv(x):
    """Involute funtion."""
    return np.tan(x) - x


class Pignon:
    """Pignon class."""
    def __init__(self, upper):
        self.upper = upper
        self.r = None
        self.Z = None
        self.d = None

    @property
    def diametre_reference(self):
        return self.upper._m0 * self.Z

    @property
    def pas_de_base(self):
        return np.pi * self.d / self.Z


class Engrenage:
    """Engrenage is an assembly of 2 Pignons."""
    def __init__(self, u=1, v=2, a=111, m0=1.5, alpha0=20, epsilon=2/100):
        self._u = u
        self._v = v
        self._a = a
        self._m0 = m0
        self._alpha0 = alpha0
        self._epsilon = epsilon
        self.pignon1 = Pignon(self)
        self.pignon2 = Pignon(self)
        self._a0 = None
        self.nombre_de_dents()

    @property
    def K(self):
        return -1 * (self._u / self._v)

    def rayon(self):
        self.pignon1.r = self._a*self._u/(self._u+self._v)
        self.pignon2.r = self._a*self._v/(self._u+self._v)
        return self.pignon1.r, self.pignon2.r

    def nombre_de_dents(self):
        self.rayon()
        self.pignon1.Z = int(2*self.pignon1.r / self._m0)
        self.pignon2.Z = int(2*self.pignon2.r / self._m0)

    @property
    def K_effectif(self):
        self.nombre_de_dents()
        return -1*self.pignon1.Z/self.pignon2.Z

    @property
    def is_K_valid(self):
        if abs(self.K - self.K_effectif)/self.K <= self._epsilon:
            return True
        return False

    @property
    def entraxe(self):
        return self._m0 * (self.pignon1.Z + self.pignon2.Z)

    @property
    def alpha(self):
        return np.arccos(self.entraxe*np.cos(self._alpha0)/self._a)

    @property
    def diametres_de_fonctionement(self):
        self.pignon1.d = 2*self._a*self.pignon1.Z/(self.pignon2.Z+self.pignon1.Z)
        self.pignon2.d = 2*self._a*self.pignon2.Z/(self.pignon2.Z+self.pignon1.Z)
        return (self.pignon1.d, self.pignon2.d)

    @property
    def is_pas_de_base_valid(self):
        """To check wether pas_de_base is valid or not."""
        self.diametres_de_fonctionement
        if self.pignon1.pas_de_base == self.pignon1.pas_de_base:
            return True
        return False

    # Deports computation below this

    @property
    def somme_des_deports(self):
        """Calcule la somme des deports."""
        return (inv(self.alpha) - inv(self._alpha0))*(self.pignon1.Z+self.pignon2.Z)/(2*np.tan(self._alpha0))

    def y(self, x, pignon):
        return np.cos(self.alpha)/np.cos(self._alpha0)*(pignon.Z/2+(1+x)) - pignon.Z/2

    def u(self, x):
        return 1/(np.pi*np.cos(self.alpha))*(np.sqrt(x**2*np.sin(self.alpha)**2/4*x+1)-(x*np.sin(self.alpha)/2))

    # @TODO Recommencer a la question 16
    def g(self, x, n=1):
        return (1+eval("self.pignon%d.Z" % n)/("self.pignon%d.Z" % abs(n-1)))

    def calcul_des_deports(self):
        x1plusx2 = self.somme_des_deports
        x1 = np.arange(-1.5, x1plusx2+1.5, 0.1)
        x2 = np.array([])
        for x in x1:
            x2 = np.append(x2, x1plusx2 - x)
        y1, y2 = self.y(x1, self.pignon1), self.y(x2, self.pignon2)
        n1, n2 = 1/self.pignon1.Z*y1, 1/self.pignon2.Z*y2
        u1, u2 = self.u(n1), self.u(n2)
        C = y1*u1 + y2*u2
        print(C)


if __name__ == '__main__':
    engrenage = Engrenage()
