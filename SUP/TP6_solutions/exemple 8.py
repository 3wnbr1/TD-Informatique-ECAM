import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.exp(-0.1*t)*np.cos(t)

def y(t):
    return np.exp(-0.1*t)*np.sin(t)    
    
t = np.arange(0,150*np.pi,0.1)
plt.plot(x(t),y(t))
plt.grid()
plt.show()


