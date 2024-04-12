import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
func = lambda y, t: t**2
dt = 1e-3
t = np.arange(0, 1, dt)
res = odeint(func, y0=0, t=t)
plt.figure(figsize=(5, 4))
plt.plot(t, res, label='ODE Solution')
plt.plot(t[::50], t[::50]**3/3, 'o', label='Analytical solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('')
plt.grid()
plt.show()