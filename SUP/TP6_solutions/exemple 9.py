import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('donnees.txt', unpack=True)

plt.plot(x,y, marker= 'o')
plt.title('Tracé à partir d\'un fichier texte')
plt.grid()
plt.show()