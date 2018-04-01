#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ls1 = [4,8,7,12]
ls2 = [3,6]

somme = 0

for i in ls2:
    for ii in ls1:
        somme += i * ii

print(somme)
