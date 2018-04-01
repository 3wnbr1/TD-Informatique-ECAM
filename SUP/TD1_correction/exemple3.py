x =float(input("Donner la valeur de x :"))
a = x >= 3
b = x < 10
if a and b:
    print("x dans l'intervalle [3, 10[.")
elif not(a):
    print("x trop petit pour être dans l'intervalle.")
else:
    print("x trop grand pour être dans l'intervalle.")
   
