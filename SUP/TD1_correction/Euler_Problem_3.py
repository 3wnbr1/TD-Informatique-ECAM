# Version rapide (non optimisée) mais simmple à comprendre.

n = 600851475143 
factor = 2
lastfactor = 1
while n>1:
    if n%factor == 0:
        lastfactor = factor
        n = n/factor
        while n%factor ==0:
            n = n/factor
    factor +=1
print(lastfactor)
