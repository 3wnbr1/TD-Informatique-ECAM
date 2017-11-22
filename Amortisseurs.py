#! /usr/bin/python3


"""Dis donc, est ce que tu n'avais pas l'intention de me traiter de sale con !"""


from Databases import nitron
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Point

nitronEngine = create_engine('sqlite:///Databases/nitron.db')
nitron.Base.metadata.bind = nitronEngine

DBSession = sessionmaker()
DBSession.bind = nitronEngine

session = DBSession()


def lbi2kgmm(value):
    return value*0.45/25.4


class Ressort:
    def __init__(self, lenght, array):
        self._lenght = lenght
        self._raideurs = array


class NitronGeometry:
    def __init__(self):
        self._B
        self._K
        self._A


class Nitron:
    def __init__(self, hStat, hMaxi, hMini):
        self._hStat = hStat
        self._hMaxi = hMaxi
        self._hMini = hMini
        self._poid_supporte
        self.ressortPrincipal
        self.ressortHelper
        self.Bumpstop
        self.TopEye
        self.BottomEye


class NitronAV(Nitron):
    def __new__(self, hStat, hMaxi, hMini):
        self.__init_subclass__()
        return super(Nitron, self).__new__(self)

    def __init_subclass__(self):
        self._poid_supporte = 115
        self.ressortPrincipal = Ressort(5, [lbi2kgmm(400), lbi2kgmm(450), lbi2kgmm(500)])
        self.ressortHelper = Ressort(2, [lbi2kgmm(150)])
        self.Bumpstop = session.query(nitron.Bumpstop).filter(nitron.Bumpstop.Name == "B").first()
        self.TopEye = session.query(nitron.TopEye).filter(nitron.TopEye.Name == "A").first()
        self.BottomEye = session.query(nitron.BottomEye).filter(nitron.BottomEye.Name == "D").first()

    def __str__(self):
        return "Amortisseur Nitron Avant"

    def __repr__(self):
        return "<Amortisseur Nitron Avant>"


class NitronAR(Nitron):
    def __new__(self, hStat, hMaxi, hMini):
        self.__init_subclass__()
        return super(Nitron, self).__new__(self)

    def __init_subclass__(self):
        self._poid_supporte = 215
        self.ressortPrincipal = Ressort(6, [lbi2kgmm(550), lbi2kgmm(600), lbi2kgmm(650)])
        self.ressortHelper = Ressort(2, [lbi2kgmm(300)])
        self.Bumpstop = session.query(nitron.Bumpstop).filter(nitron.Bumpstop.Name == "A").first()
        self.TopEye = session.query(nitron.TopEye).filter(nitron.TopEye.Name == "B").first()
        self.BottomEye = session.query(nitron.BottomEye).filter(nitron.BottomEye.Name == "A").first()

        def __str__(self):
            return "Amortisseur Nitron Arriere"

        def __repr__(self):
            return "<Amortisseur Nitron Arriere>"


if __name__ == '__main__':
    nitronAV = NitronAV(115, 165, 75)
    nitronAR = NitronAR(120, 180, 80)
