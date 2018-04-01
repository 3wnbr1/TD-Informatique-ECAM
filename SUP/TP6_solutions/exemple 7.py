import numpy as np
import matplotlib.pyplot as plt

def h(x,alpha,f):
    return np.exp(-alpha*x)*np.sin(2*np.pi*f*x)

f = 0.4
X = np.arange(0,5*np.pi,0.01)

for alpha in np.arange(0,1,.2):
    Y = h(X,alpha,f)
    plt.plot(X,Y, label=r"$\alpha =$" + str(alpha) + r"$s^{-1}$")
    plt.legend()

plt.grid()
plt.title(r"$h(x)=e^{-\alpha x}\sin(2\pi f x) $", fontsize = 20, ) 
plt.xlabel("$x (s)$", fontsize = 20) 
plt.ylabel("$h(x)$", fontsize = 20)
plt.axis([0,5*np.pi,-1,1])
plt.text(6,0.85,r"$f =$" + str(f) + r" $rad.s^{-1}$", color = "k", fontsize=13)

plt.show()
