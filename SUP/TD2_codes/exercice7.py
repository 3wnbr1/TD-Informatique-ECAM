# -*- coding: utf-8 -*-

t = [1]
for i in range(1,6):
    t.append(t[i-1]+2)
print(t)

# OU 

t = list(range(1,13,2))
print(t)