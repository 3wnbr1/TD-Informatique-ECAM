# -*- coding: utf-8 -*-
def syracuse(n):
    syr = [n]
    while syr[-1] != 1:
        if syr[-1]%2 == 0:
            syr.append(syr[-1]//2)
        else:
            syr.append(3*syr[-1]+1)
    return syr

f = open('100syracuse.txt','w')

for i in range(1,101):
    f.write(str(i)+" : "+str(syracuse(i))+'\n')

f.close()
