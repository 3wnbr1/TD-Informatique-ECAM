# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:56:45 2016

@author: ewen.brun
"""

s = 0
a = int(input("Entrez un nb entier"))
b = int(input("Entrez un autre nb entier"))

for i in range(1,a+1):
    s+=b
    
print("a * b = ",s)