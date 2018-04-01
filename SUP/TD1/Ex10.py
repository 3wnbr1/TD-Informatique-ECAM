# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:26:10 2016

@author: ewen.brun
"""
fact = 1
n = int(input("Entrer un entier : "))
for i in range(1,n+1):
    fact *= i

print("Factorielle de ",n," = ",fact)