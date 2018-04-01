# -*- coding: utf-8 -*-

notes = list()
i = 1
nb = float(input("Saisir la note n°1 (saisir 999 pour terminer): "))
while nb != 999:
    notes.append(nb)
    nb = float(input("Saisir la note n°" + str(i+1) + " (saisir 999 pour terminer): "))
    i += 1
print("La moyenne des",i-1,"notes est",round(sum(notes)/(i-1),1))