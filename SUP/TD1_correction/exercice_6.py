T = float(input("Donner la température de l'eau : "))
if T < 0:
    print("L'eau est sous forme de glace.")
elif T<100:
    print("L'eau est sous forme liquide.")
else:
    print("L'eau est sous forme de vapeur.")
