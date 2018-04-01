# Calcule la différence entre la somme des carrés jusqu'à n et le carré de la somme.

n=int(input("Donner n (on cherche la différence entre la somme des carrés jusqu'à n et le carré de la somme.) : "))
s1=0
s2=0
for i in range(1,n+1):
    s1+=i**2
    s2+=i
print("La différence des carrés est :",s2**2-s1)
