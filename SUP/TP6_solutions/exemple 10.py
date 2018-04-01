import matplotlib.pyplot as plt
import numpy as np

e = 0.8

theta = np.arange(0,np.pi*2,0.01)
r=2/(1+e*np.cos(theta))
plt.polar(theta,r)

plt.show()