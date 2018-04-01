import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

E, R, C = 12, 50, 20e-6
to = R*C

def circuitRC(u,t):
    return (E-u)/to


t = np.arange(0,10*to,10*to/1000)

plt.close()
plt.plot(t,odeint(circuitRC,0,t),label="Solution odeint")
plt.plot(t,E*(1-np.exp(-t/to)),label="Solution analytique")
plt.grid()
plt.ylabel("$u(t)$"+" en V")
plt.xlabel("$t$"+" en s")
plt.title("CIRCUIT RC : odeint vs analytic")
plt.legend()
plt.show()
