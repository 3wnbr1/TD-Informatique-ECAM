# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:47:39 2016

@author: ewen.brun
"""

temp = float(input("Entez la temperature de l'eau : "))

if temp > 0 and temp < 100:
    print("Eau Liquide")
elif temp < 0:
    print("Glace")
else:
    print("Vapeur")