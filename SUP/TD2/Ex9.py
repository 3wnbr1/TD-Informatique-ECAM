#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lst = [1,2,3,4,5,6,7,8]

somme = 0

for i in lst:
    somme += lst[i-1]

print(somme)
