# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:06:55 2016

@author: ewen.brun
"""

list = []
for i in range(10):
    n = int(input("Entrez un entier : "))
    if n == 0:
        break
    list.append(n)
list.sort()
print("Le plus grand entier est : ",max(list))
