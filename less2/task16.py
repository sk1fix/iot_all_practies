import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import warnings
from scipy.optimize import minimize
warnings.filterwarnings('ignore')
dx = 0.001
x = np.arange(-10, 10, dx)
f = lambda x: x**2 * ( 1 - 0.1 * (x) **2 )* np.exp(- 0.1 * (x)**2)
fig, ax = plt.subplots()
def get_path(xc):
 global path
 path.append(xc)
x0 = 2.4
path = [x0]
result = minimize(f, x0=x0, tol=1e-2, callback=get_path)
x1 = result.x
print(result)

ax.set(xlabel='x', ylabel='f(x)')
ax.plot(x, f(x))
plt.show()