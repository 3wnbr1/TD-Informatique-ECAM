# -*- coding: utf-8 -*-

ma_liste = ["D","E","C","A","L","A","G","E"]
print(ma_liste)

prem = ma_liste[0]

for i in range(1,len(ma_liste)):
    ma_liste[i-1]=ma_liste[i]

ma_liste[len(ma_liste)-1]=prem

print(ma_liste)
