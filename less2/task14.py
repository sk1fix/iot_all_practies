from scipy.integrate import odeint
import numpy as np

f0 = float(input())
dt = 0.001
t = np.arange(0, 2, dt)
def func(f, t):
    return f + t
res = odeint(func, f0, t)

index_t1 = int(1 / dt)
result = res[index_t1][0]

print('%.2f' % result)