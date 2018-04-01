somme = 0
nb=int(input("Donner un nombre entier non nul : "))
for i in range(1,nb+1):
    somme+=i
print("La somme des entiers jusqu'à",nb,"est",somme,"\b.")
