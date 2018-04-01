# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:54:20 2015

@author: Pierre
"""

a = int(input("Entrer une année :"))
if a%4 == 0 and (a%100 != 0 or a%400 == 0):
    print(a,"est une année bissextile.")
else:
    print(a,"n'est pas une année bissextile.")
