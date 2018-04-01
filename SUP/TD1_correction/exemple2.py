x =float(input("Donner la valeur de x :"))
if x >= 3 and x < 10:
    print("x dans l'intervalle [3, 10[.")
elif x < 3:
    print("x trop petit pour être dans l'intervalle.")
else:
    print("x trop grand pour être dans l'intervalle.")
    
    # exemple des pb de comparaison si x=9.99999999999999999
