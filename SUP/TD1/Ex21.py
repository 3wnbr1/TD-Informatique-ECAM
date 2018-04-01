# -*- coding: utf-8 -*-

n = input("Entez un nombre entier : ")
s = 0

for i in range(0,len(n)):
    s += int(n[i])

print(s)
