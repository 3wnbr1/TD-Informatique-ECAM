def pgcd(a,b):
    while a!=b:
        if a<b:
            b=b-a
        else:
            a=a-b
    return a
    
a = int(input("Entrer le premier nombre :"))
b = int(input("Entrer le second nombre :"))

print("PGCD de "+ str(a) + " et de " + str(b) + " = " + str(pgcd(a,b)))