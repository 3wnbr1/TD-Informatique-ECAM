# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:06:55 2016

@author: ewen.brun
"""

list = []
for i in range(10):
    list.append(int(input("Entrez un entier : ")))
list.sort()
print("Le plus grand entier est : ",list[9])