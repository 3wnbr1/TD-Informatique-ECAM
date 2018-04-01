max=0
for i in range(1,11):
    nb=float(input("#" + str(i) + ". Donner un nombre : "))
    if nb>max:
        max=nb
print("Le plus grand des nombres entrés est",max)