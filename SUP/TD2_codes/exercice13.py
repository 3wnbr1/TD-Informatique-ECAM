# -*- coding: utf-8 -*-

#------------------------ début création tableau aléatoire
import random
ma_liste = list()
for k in range(20):
    ma_liste.append(random.randint(1,10))
print(ma_liste)
#------------------------ fin création tableau

occurence = 0
nb = int(input("Donnez un nombre entre 1 et 10 compris :"))
for elt in ma_liste:
    if elt == nb:
        occurence+=1
print("Le nombre",nb,"figure",occurence,"fois dans le tableau.")