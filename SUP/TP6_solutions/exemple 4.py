import numpy as np
import matplotlib.pyplot as plt
plt.close()
def h(x,alpha,f):
    return np.exp(-alpha*x)*np.sin(2*np.pi*f*x) # fonctions mathématiques de la bibliothèque numpy

x = np.arange(0,5*np.pi,0.01) # tableau de valeurs entre 0 et 5pi tous les 0.01
alpha = 0.3
f = 0.4
y = h(x,alpha,f)
plt.plot(x,y)
plt.grid()
plt.title(r"$h(x)=e^{-\alpha x}\sin(2\pi f x) $", fontsize = 20, ) 
plt.xlabel("$x(s)$", fontsize = 20) 
plt.ylabel("$h(x)$", fontsize = 20)
plt.axis([0,5*np.pi,-1,1])

plt.show() # affiche  le graphique
