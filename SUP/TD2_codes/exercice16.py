# -*- coding: utf-8 -*-

#------------------------ début création tableau aléatoire
import random
ma_liste = list()
for k in range(20):
    ma_liste.append(random.randint(0,1))
print(ma_liste)
#------------------------ fin création tableau

# ma_liste = [1,0,1,0,0,0,1,1,0,0,0,0] # : test avec plus longue série à la fin.

nb_zero = 0
max = 0
i_max = 0

ma_liste.append("X")

for i in range(len(ma_liste)):
    debut = i
    nb_zero = 0
    while ma_liste[i] == 0 and i < len(ma_liste): # on a rallongé le tableau avec un 'X' sinon, si le dernier chiffre est un 0, on effectue 1=+1 dans le while et l'appel suivant produit un out of range.
        nb_zero += 1
        i += 1
    if nb_zero > max:
        max = nb_zero
        i_max = debut

print("La première plus longue série de 0 (" + str(max) +" zéro(s)) commence à l'indice",i_max,"\b.")
ma_liste.remove("X")
print(ma_liste)