# -*- coding: utf-8 -*-

ma_liste = list()
ma_liste1 = [12, 23, 67, 13, 78]
ma_liste2 = [23, 98, 1, 98, 431]

for i in range(5):
    ma_liste.append(ma_liste1[i] + ma_liste2[i])
print(ma_liste)