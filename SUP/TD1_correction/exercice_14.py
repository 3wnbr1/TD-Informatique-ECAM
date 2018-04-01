produit=0
a = int(input("Donner un premier nombre entier : "))
b = int(input("Donner un second nombre entier : "))
for i in range(1,b+1):
    produit+=a
print ("Le produit de",a,"par",b,"est",produit,"\b.")
