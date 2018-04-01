# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:04:44 2016

@author: ewen.brun
"""

s = 1
a = int(input("Entrez un nb entier"))
b = int(input("Entrez un autre nb entier"))

for i in range(1,b+1):
    s*=a
    
print("a ** b = ",s)