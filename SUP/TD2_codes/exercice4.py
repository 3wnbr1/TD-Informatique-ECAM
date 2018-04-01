# -*- coding: utf-8 -*-

ma_liste= list()
for i in range(5):
    ma_liste.append(i**2)
for i in range(5):
    print(ma_liste[i])

# Version raccourcie :
ma_liste= list()
for i in range(5):
    ma_liste.append(i**2)
    print(ma_liste[i])
    
# OU avec une compréhension de liste :
ma_liste = list(range(5))
ma_liste = [x ** 2 for x in ma_liste] # compréhension de liste
for i in range(5):
    print(ma_liste[i])
