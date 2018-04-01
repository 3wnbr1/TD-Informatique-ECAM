#!/usr/bin/env python3
# -*- coding: utf-8 -*-



nlist = [0]
i = 1

while nlist[-1] != 999 or nlist == [0]:
    nlist.append(int(input("Entrer la "+str(i)+" note ( Saisir 999 pour terminer ): ")))
    i += 1
del nlist[0], nlist[-1]

print("La meilleure note est de : ",max(nlist))
print("La moyenne est de : ", sum(nlist)/len(nlist))

sommed = 0

for i in nlist:
    sommed += (int(i) - sum(nlist)/len(nlist))**2

print("L'ecart type est de : ", (sommed/(len(nlist)-1))**1/2)
