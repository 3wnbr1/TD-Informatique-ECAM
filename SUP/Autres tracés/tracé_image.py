import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

Data = np.matrix([[ 25.,  92.,  15.,  10.],
                  [  5.,   2.,  91.,  15.],
                  [ 80.,  35.,   5.,   5.],
                  [ 10.,   4.,  10.,  97.],
                  [  2.,  93.,   3.,   5.]])

plt.imshow(Data, cmap=cm.jet, interpolation='nearest')
plt.show()