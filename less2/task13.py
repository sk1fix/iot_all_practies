import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def func(y, t):
    u, f = y
    dydt = [2*u - f, u]
    return dydt
dt = 1e-3
t = np.arange(0, 1, dt)
res = odeint(func, y0=[1, 1], t=t)
plt.figure(figsize=(5, 4))
plt.plot(t, res[:, 1], label='f')
plt.plot(t[::50], np.exp(t[::50]), 'o', label='e^t')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.title('')
plt.grid()
plt.show()