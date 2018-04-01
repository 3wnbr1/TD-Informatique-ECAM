import numpy as np
import matplotlib.pyplot as plt

plt.close()

def h(x,alpha,f):
    return np.exp(-alpha*x)*np.sin(2*np.pi*f*x) # fonctions mathématiques de la bibliothèque numpy

def g(x,alpha):
    return np.exp(-alpha*x)

alpha = 0.3
f = 0.4

X = np.arange(0,5*np.pi,0.01)
X1 = np.arange(0,5*np.pi,0.1)

Y = h(X,alpha,f)
plt.plot(X,Y)

Y1 = g(X,alpha)
plt.plot(X,Y1,ls=":",c="r")
plt.plot(X,-Y1,ls=":",c="r")

Y2 = h(X1,alpha,f)
plt.plot(X1,Y2, ls ="",marker = "x", mec="k")

plt.grid()
plt.title(r"$h(x)=e^{-\alpha x}\sin(2\pi f x) $", fontsize = 20, ) 
plt.xlabel("$x (s)$", fontsize = 20) 
plt.ylabel("$h(x)$", fontsize = 20)
plt.axis([0,5*np.pi,-1,1])
plt.text(8,0.3,r"$\alpha =$" + str(alpha)+ "SI", color = "b")
plt.text(8,0.2,r"$f =$" + str(f)+ "SI", color = "b")

plt.show()
