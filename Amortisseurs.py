#! /usr/bin/python3


"""Dis donc, est ce que tu n'avais pas l'intention de me traiter de sale con !"""


import numpy as np
from classes import Point
from Databases import nitron
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


nitronEngine = create_engine('sqlite:///Databases/nitron.db')
nitron.Base.metadata.bind = nitronEngine

DBSession = sessionmaker()
DBSession.bind = nitronEngine

session = DBSession()


def lbi2kgmm(value):
    return value * 0.45 / 25.4


class Ressort:
    def __init__(self, lenght, array):
        self._lenght = lenght
        self._raideurs = array


class NitronGeometry:
    def __init__(self, nitron):
        self.nitron = nitron
        self._A
        self._B = Point(0, 0)
        self._J = Point(10, -30)
        self._K
        self.BC
        self.BE
        self.CD
        self.CE
        self.EF
        self.HI

    @property
    def BD(self):
        return (self.BC**2 + self.CD**2)**(1 / 2)

    @property
    def CDB(self):
        return np.arcsin(self.CD / self.BD)

    @property
    def gamma(self):
        return np.arcsin(self._ze / self.BE)

    @property
    def _ze(self):
        return self.HI - self.EF - self.nitron._h

    @property
    def D(self):
        D = []
        for x, y in zip(self.BE*np.cos(self.alpha), self.BE*np.sin(self.alpha)):
            D.append(Point(x, y))
        return D

    @property
    def AD(self):
        D, L = self.D, []
        for d in D:
            L.append((d - self._A).vectorize().norm())
        return L

    @property
    def alpha(self):
        # return np.arcsin((self._A._x**2 + self._A._y**2 + self.BD**2 - self.AD**2) / (2 * self.BD * self._A.vectorize().norm())) - np.arctan(self._A._x / self._A._y)
        return self.CDB + self.gamma


class NitronGeometryAV(NitronGeometry):
    def __new__(self, nitron):
        self.__init_subclass__()
        return super(NitronGeometry, self).__new__(self)

    def __init_subclass__(self):
        self._K = Point(0, 300)
        self._A = Point(50, 300)
        self.BC = 260
        self.BE = 350
        self.CD = 45
        self.CE = 90
        self.EF = 110
        self.HI = 285


class NitronGeometryAR(NitronGeometry):
    def __new__(self, nitron):
        self.__init_subclass__()
        return super(NitronGeometry, self).__new__(self)

    def __init_subclass__(self):
        self._K = Point(0, 290)
        self._A = Point(250, 290)
        self.BC = 290
        self.BE = 380
        self.CD = 35
        self.CE = 110
        self.EF = 120
        self.HI = 280


class Nitron:
    def __init__(self, hStat, hMaxi, hMini):
        self._poid_supporte
        self.ressortPrincipal
        self.ressortHelper
        self.Bumpstop
        self.TopEye
        self.BottomEye


class NitronAV(Nitron):
    def __new__(self, hStat, hMaxi, hMini):
        self.__init_subclass__(hStat, hMaxi, hMini)
        return super(Nitron, self).__new__(self)

    def __init_subclass__(self, hStat, hMaxi, hMini):
        self._h = np.array([hMini, hStat, hMaxi])
        self.geometry = NitronGeometryAV(self)
        self._poid_supporte = 115
        self.ressortPrincipal = Ressort(
            5, [lbi2kgmm(400), lbi2kgmm(450), lbi2kgmm(500)])
        self.ressortHelper = Ressort(2, [lbi2kgmm(150)])
        self.Bumpstop = session.query(nitron.Bumpstop).filter(
            nitron.Bumpstop.Name == "B").first()
        self.TopEye = session.query(nitron.TopEye).filter(
            nitron.TopEye.Name == "A").first()
        self.BottomEye = session.query(nitron.BottomEye).filter(
            nitron.BottomEye.Name == "D").first()

    def __str__(self):
        return "Amortisseur Nitron Avant"

    def __repr__(self):
        return "<Amortisseur Nitron Avant>"


class NitronAR(Nitron):
    def __new__(self, hStat, hMaxi, hMini):
        self.__init_subclass__(hStat, hMaxi, hMini)
        return super(Nitron, self).__new__(self)

    def __init_subclass__(self, hStat, hMaxi, hMini):
        self._h = np.array([hMini, hStat, hMaxi])
        self.geometry = NitronGeometryAR(self)
        self._poid_supporte = 215
        self.ressortPrincipal = Ressort(
            6, [lbi2kgmm(550), lbi2kgmm(600), lbi2kgmm(650)])
        self.ressortHelper = Ressort(2, [lbi2kgmm(300)])
        self.Bumpstop = session.query(nitron.Bumpstop).filter(
            nitron.Bumpstop.Name == "A").first()
        self.TopEye = session.query(nitron.TopEye).filter(
            nitron.TopEye.Name == "B").first()
        self.BottomEye = session.query(nitron.BottomEye).filter(
            nitron.BottomEye.Name == "A").first()

        def __str__(self):
            return "Amortisseur Nitron Arriere"

        def __repr__(self):
            return "<Amortisseur Nitron Arriere>"


if __name__ == '__main__':
    nitronAV = NitronAV(115, 165, 75)
    nitronAR = NitronAR(120, 180, 80)
