prix = float(input("Donnez le prix HT d'un article :"))
nb = int(input("Donnez le nombre d'articles :"))
tva = float(input("Donnez le taux de TVA (en %) :"))
print("Le prix total TTC est de",prix*(tva/100+1)*nb,"€.")
