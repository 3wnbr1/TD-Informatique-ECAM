#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nlist = [0]
i = 1

while nlist[-1] != 999 or nlist == [0]:
    nlist.append(int(input("Entrer la "+str(i)+" note ( Saisir 999 pour terminer ): ")))
    i += 1
del nlist[0], nlist[-1]

print("La moyenne est de : ",sum(nlist)/len(nlist))
