#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:04:32 2016

@author: ewen
"""
nlist = list()

for i in range(1,6):
    nlist.append(int(input("Entrer la "+str(i)+" note : ")))

print("La moyenne est de : ",sum(nlist)/len(nlist))