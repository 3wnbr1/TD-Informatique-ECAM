# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:52:58 2016

@author: ewen.brun
"""

a = int(input("Entrez A :"))
b = int(input("Entrez B :"))

if a * b == 0:
    print("Produit nul")
elif a * b < 0:
    print("Produit négatif")
else:
    print("Produit Positif")