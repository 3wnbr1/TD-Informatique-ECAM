# -*- coding: utf-8 -*-

ma_liste = list()
nb = int(input("Donnez un premier nombre :"))
ma_liste.append(nb)

i = 0

while len(ma_liste) < 5:
    nb=int(input("Donnez un nombre supérieur au précédent (" + str(ma_liste[i]) + ") :" ))
    if nb > ma_liste[i]:
        ma_liste.append(nb)
        i += 1
    else:
        print("Lisez les consignes !")
print(ma_liste)