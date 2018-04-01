puissance=1
a = int(input("Donner un nombre entier : "))
b = int(input("Donner un exposant : "))
for i in range(1,b+1):
    puissance*=a
print (a,"^",b,"=",puissance)
