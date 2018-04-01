i=1
nb=1
max=0
while (i<=10 and nb!=0):
    nb=float(input("#" + str(i) + ". Donner un nombre : "))
    if nb>max:
        max=nb
    i+=1
print("Le plus grand des nombres entrés est ",max)