#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:45:10 2017

@author: ewen
"""

import matplotlib.pyplot as plt

plt.close()
plt.grid()
plt.axis([0,7,0,40])
plt.xlabel(r"$n$")
plt.ylabel(r"$n^2$")
plt.title("Premiers carres")
plt.plot([1,2,3,4,5,6],[1,4,9,16,25,36],ls=":",color="r",marker="o")
plt.text(5,20,"Courbe n1",color="r")
plt.show()

