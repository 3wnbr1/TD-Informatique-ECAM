# -*- coding: utf-8 -*-

s = 0
nb = input("Donnez un nombre à plusieurs chiffres :")
for c in nb:
    s += int(c)
print("La somme des chiffres de",nb,"est",s)