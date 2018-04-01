a = float(input("Donner un nombre relatif : "))
b = float(input("Donner un second nombre relatif : "))
if a==0 or b==0:
    print("Le produit des deux nombres est nul.")
elif (a<0 and b<0) or (a>0 and b>0):
    print("Le produit des deux nombres est positif.")
else:
    print("Le produit des deux nombres est négatif.")
