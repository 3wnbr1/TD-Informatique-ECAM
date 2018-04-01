# -*- coding: utf-8 -*-

suite = [1,1]
for i in range(2,7):
    suite.append(suite[i-2]+suite[i-1])
print(suite)