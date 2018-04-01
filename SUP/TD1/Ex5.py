# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:41:23 2016

@author: ewen.brun
"""

prix = float(input("Entrez le prix de l'article :"))
nombre = int(input("Entrez le nombre d'articles :"))
tva = float(input("Entrez la TVA :"))

a = prix * nombre + prix * nombre * tva

print("prix total",a," €")