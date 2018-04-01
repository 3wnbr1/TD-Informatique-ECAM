nb=20
while nb > 10 or nb <-10:
    nb=int(input("Donner un nombre entre -10 et 10 : "))
    if nb<-10:
        print ("Le nombre saisi est trop petit.")
    elif nb>10:
        print ("Le nombre saisi est trop grand")
