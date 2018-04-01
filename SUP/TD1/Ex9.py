# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:06:52 2016

@author: ewen.brun
"""
print("-"*48)
print("Calcul des résistance équivalentes")
print("-"*48)
menu = "1"

while menu != "s" and menu != "p":
    menu = input("Entrer s pour serie et p pour parralleles : ")

r1 = int(input("Entrez R1 : "))
r2 = int(input("Entrez R2 : "))

if menu == "s":
    req = r1 + r2
else :
    req = 1/((1/r1)+1/r2)

print("-"*48)
print("Resistance équivqlente = : ",req)
print("-"*48)