# -*- coding: utf-8 -*-

#------------------------ début création tableau aléatoire
import random
tableau = list()
occurence = 0
for k in range(20):
    tableau.append(random.randint(0,1))
    #tableau.sort()
#------------------------ fin création tableau
    
tableau = [1,0,1,0,0,0,0,1,1,0,0,0,0] # test
nb_zero = 0
max = 0
i_max = 0
l_max = list()
l_i = list()
tableau.append("X")

for i in range(len(tableau)):
    debut = i
    nb_zero = 0
    while tableau[i] == 0 and i < len(tableau):
        nb_zero += 1
        i += 1
    if nb_zero > max: # cas où on alémiore la plus longue série
        max = nb_zero
        i_max = debut
        l_max = [nb_zero]
        l_i = [debut]
    elif nb_zero == max: # cas où une nouvelle meilleure série est trouvée
        l_max.append(nb_zero)
        l_i.append(debut)
        
for k in range(len(l_max)):
    print("La plus longue série de 0 (" + str(l_max[k]) +" zéro(s)) commence à l'indice",l_i[k],"\b.")
tableau.remove("X")
print(tableau)