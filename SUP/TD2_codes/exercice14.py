# -*- coding: utf-8 -*-

#------------------------ début création tableau aléatoire
import random
ma_liste = list()
for k in range(20):
    ma_liste.append(random.randint(1,10))
#ma_liste.sort() # A ajouter pour tester avec un tableau trié
print(ma_liste)
#------------------------ fin création tableau


tri = True
i = 1

for i in range(1,len(ma_liste)):
    if ma_liste[i] < ma_liste[i-1]:
        tri = False
if tri == False:
    print("Le tableau n'est pas trié.")
else:
    print("Le tableau est trié.")
    
    