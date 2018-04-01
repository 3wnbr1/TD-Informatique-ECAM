# -*- coding: utf-8 -*-

n = int(input("Entez une année : "))

if n%4 == 0 and ((n%100!=0) or (n%400==0)):
    print("L'année ",n," est bissextile")
else:
    print("L'année ",n," n'est pas bissextile")
