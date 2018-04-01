c=""
while c!="s" and c!="p":
    c = input("Tapez \"s\" pour un montage en série ou \"p\" pour un montage en parallèle : ")
r1=float(input("Valeur de la résistance n°1 : "))
r2=float(input("Valeur de la résistance n°2 : "))
if c=="s":
    req=r1+r2
    type="série" 
else:
    req=1/(1/r1+1/r2)
    type="parallèle"
print("La résistance équivalente au montage en",type,"est de",req,"ohms.")