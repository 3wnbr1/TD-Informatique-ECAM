from math import exp
from math import factorial

x=int(input("Donner un entier : "))
prec= float(input("Donner une précision voulue :")) # précision : 0.01 ou 0.001
expo=0
i=0
while abs(expo-exp(x))>prec:   
    expo+=x**i/factorial(i)
    i+=1
    print(expo,i)
print("exp(" + str(x) + ") = " + str(round(expo,3)) + " avec une précision de " + str(prec) + " (valeur obtenue avec " + str(i+1) + " termes de la série).")