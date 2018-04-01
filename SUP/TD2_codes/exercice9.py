# -*- coding: utf-8 -*-

t = [6,89,12,23,1,2,34]
s = 0
for nb in t:
    s += nb
print("La somme est",s,"\b.")
print("Avec la fonction sum on obtient :",sum(t),"\b.")
    
# OU

s = 0
for i in range(len(t)):
    s += t[i]
print("La somme est",s,"\b.")
print("Avec la fonction sum on obtient :",sum(t),"\b.")
