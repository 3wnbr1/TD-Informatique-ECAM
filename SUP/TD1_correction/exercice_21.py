# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:58:37 2015

@author: Pierre
"""

n = input("DOnner un nombre entier.")
s = 0
for c in n:
    s += int(c)
print("La somme des chiffres de",n,"vaut",s)    