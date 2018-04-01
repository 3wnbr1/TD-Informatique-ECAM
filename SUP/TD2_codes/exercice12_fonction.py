# -*- coding: utf-8 -*-

def plus_un(liste):
    n = 0
    for elt in liste:
        liste[n] = elt+1
        n += 1
    return(liste)

#  modifie la liste passée en paramètre de la fonction.