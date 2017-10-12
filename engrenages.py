#! /Users/ewen/anaconda3/bin/python
# coding: utf-8


"""Optimisation du rapport de denture dans un engrenage cylindrique."""


epsilon = 2/100
alpha0 = 20
m0 = 1.5
a = 111


class Pignon:
    def __init__(self):
        self.r = None
        self.Z = None
        self.d = None


class Engrenage:
    def __init__(self, u=1, v=2, a=111, m0=1.5, alpha0=20, epsilon=2/100):
        self._u = u
        self._v = v
        self._a = a
        self._m0 = m0
        self._alpha0 = alpha0
        self._epsilon = epsilon
        self.pignon1 = Pignon()
        self.pignon2 = Pignon()
        self._a0 = None

    @property
    def K(self):
        return -1 * self._u / self._v

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

    def entraxe(self):
        self.nombre_de_dents()
        self._a0 = self._m0 * (self.pignon1.Z + self.pignon2.Z)
        return self._a0


if __name__ == '__main__':
    engrenage = Engrenage()
