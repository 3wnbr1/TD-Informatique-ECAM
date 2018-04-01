# -*- coding: utf-8 -*-

ma_liste = 6*[0] # indispensable de créer une liste de 6 éléments au préalable !
# ou ma_liste = list(range(6))

ma_liste[0]="a"
ma_liste[1]="e"
ma_liste[2]="i"
ma_liste[3]="o"
ma_liste[4]="u"
ma_liste[5]="y"
print(ma_liste)

#OU

ma_liste2 = list()
voyelles = "aeiouy"
for lettre in voyelles:
    ma_liste2.append(lettre)
print(ma_liste2)
    
    