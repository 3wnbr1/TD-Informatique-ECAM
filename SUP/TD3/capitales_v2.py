#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from levenshtein import leven
from random import choice

#Loding Data :

score = 0
falt = 0
datalist = list()
data = open('jeu_donnees.txt','r')
for line in data:
    datalist.append(line.strip('\r\n').split(';'))

#Start_UI
print('='*48)
print("Bienvenue au jeu des capitales. v2")
print('='*48)
n = int(input("Combien de capitales voulez vous trouver ? "))

#Turn_Loop
for turn in range(n):
    country = choice(datalist)
    print('Debug_ONLY !!! ', country[1])
    inner = input(country[0]+" ? ")
    if inner.lower() == country[1].lower():
        score += 1
        print('Bravo !')
    elif leven(inner, country[1]) < 3:
        score += 1
        falt += 1
        print('Bravo mais attention a l\'orthographe, on ecrit',country[1])
    else:
        print('Non la bonne reponse est',country[1])

#End of the game
print('='*48)
print("Votre score est de",str(score)+"/"+str(n))
print("Vous avez fait %d fautes" % falt)
print('='*48)
