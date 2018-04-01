from time import time
d=time()
nb = 1

for i in range(1, 21):
    print("Solution pour", i,"entiers :")
    min = nb # on repart du résultat précédent
    while nb % i > 0: #si le résultat précédent ne se divise pas par l'entier suivant on entre dans la boucle
        print("Résultat négatif pour", nb)
        nb += min # on lui rajoute le résultat précédent ce qui donne un nombre qui fonctionne avec les i-1 premiers entiers et on le teste avec i.
    print("Résultat positif pour",nb)
    print()
    
f=time()
print(f-d,"secondes")