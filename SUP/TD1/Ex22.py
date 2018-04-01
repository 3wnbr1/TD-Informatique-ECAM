# -*- coding: utf-8 -*-
n = 1000
lst = []

for i in range(1,n//3+1):
    if 3*i < n:
        if lst.count(3*i) == 0:
            lst.append(3*i)
    if 5*i < n:
        if lst.count(5*i) == 0:
            lst.append(5*i)
print(lst)
print("Somme = ",sum(lst))
