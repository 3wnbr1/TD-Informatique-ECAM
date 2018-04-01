# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:56:34 2016

@author: ewen.brun
"""

age = int(input("Entrez l'age : "))

if age < 5 or age > 13:
    print("Age non adapté")
elif age >= 6 and age < 8 :
    print("Poussin")
elif age >= 8 and age < 10 :
    print("Benjamin")
else:
    print("Minime")