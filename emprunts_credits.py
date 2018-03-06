#! /Users/ewen/anaconda3/bin/python
# coding: utf-8


"""Emprunts, credits immobiliers."""


import numpy as np
import matplotlib.pyplot as plt


class Pret:
    def __init__(self, C0, N, ta):
        self._C0 = C0  # montant de l'emprunt
        self._N = N  # duree en mois
        self._tm = ta/1200  # taux menusuel

    @property
    def M(self):
        return round(self._C0*self._tm*(1+self._tm)**self._N/((1+self._tm)**self._N - 1), 2)

    @property
    def I(self):
        return round(self.M*self._N - self._C0, 2)

    @property
    def cout_total(self):
        return round(self._C0 + self.I, 2)

    def tableau_amortissement(self):
        self.interests = []
        self.refunds = []
        self.C = [self._C0]
        for i in range(self._N):  # TODO : Clean up the code
            if i == 0:
                self.interests.append(self.C[-1]*self._tm)
                self.refunds.append(self.M - self.interests[-1])
                self.C.append(self.C[-1]*(1+self._tm) - self.M)
            else:
                self.interests.append(self.interests[-1] + self.C[-1]*self._tm)
                self.refunds.append(self.refunds[-1] + self.M - self.C[-1]*self._tm)
                self.C.append(self.C[-1]*(1+self._tm) - self.M)

    def plot(self):
        self.tableau_amortissement()
        months = np.arange(self._N)
        plt.subplot(1, 2, 1)
        plt.plot(months, self.refunds)
        plt.title("Somme remboursée")
        plt.subplot(1, 2, 2)
        plt.plot(months, self.interests)
        plt.title("Interêts cummulés")
        plt.show()

    def export(self):
        self.tableau_amortissement()
        with open('exported.txt', 'w') as f:
            f.write("Month\t|\tRefund\t|\tInterests\n")
            for i in range(self._N):
                f.write("Mois %i\t|\t%f\t|\t%f\n" % (i, self.refunds[i], self.interests[i]))


if __name__ == '__main__':
    pret = Pret(150000, 240, 4.8)
    print("Mensualités:", pret.M)
    print("Interets:", pret.I)
