# -*- coding: utf-8 -*-

ma_liste = list()
for i in range(5):
    ma_liste.append(float(input("Saisir la note n°" + str(i+1) + " : ")))
print("La moyenne des notes est",sum(ma_liste)/len(ma_liste))