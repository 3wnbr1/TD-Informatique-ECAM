# -*- coding: utf-8 -*-

ma_liste1 = [4,8,7,12]
ma_liste2 = [3,6]

x = 0
for i in range(4):
    for j in range(2):
        x += ma_liste1[i] * ma_liste2[j]
print("Le X des deux tableaux est",x,"\b.")
    
# OU
    
x = 0
for elt1 in ma_liste1:
    for elt2 in ma_liste2:
        x += elt1*elt2
print("Le X des deux tableaux est",x,"\b.")