# -*- coding: utf-8 -*-

from math import *

notes = list()
i = 1
nb = float(input("Saisir la note n°1 (saisir 999 pour terminer): "))

while nb != 999:
    notes.append(nb)
    nb=float(input("Saisir la note n°" + str(i+1) + " (saisir 999 pour terminer): "))
    i+=1

moy = round(sum(notes)/len(notes),1)
print("La moyenne des",i-1,"notes est",moy)

somquad = 0
supmoy = 0
max = 0
for n in notes:
    somquad += (n-moy)**2 
    if n > moy:
        supmoy += 1
    if n > max:
        max = n
print("Il y a",supmoy,"notes strictement au-dessus de la moyenne.")
print("La meilleure note est :",max,".")
print("L'écart-type des notes saisies est",round(sqrt(somquad/(len(notes)-1)),1),".")

