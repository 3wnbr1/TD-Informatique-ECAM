# -*- coding: utf-8 -*-
# Calcule la somme des multiples de 3 et de 5 strictement inférieurs à n.
a=input("alors?")

n=int(input("Donner n (on cherche la somme des multiples de 3 et de 5 inférieurs à n) : "))
s=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        s+=i
print("La somme des multiples de 3 et de 5 inférieurs à",n,"vaut",s)
