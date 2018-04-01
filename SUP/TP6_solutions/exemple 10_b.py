import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0,np.pi*2,0.01)

for e in np.arange(0.1,1.1,0.2):
    r=2/(1+e*np.cos(theta))
    plt.polar(theta,r,label = "e=" + str(e))

plt.legend()
plt.show()