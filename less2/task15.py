import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import warnings
from scipy.optimize import minimize


mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')
dx = 0.001
x = np.arange(-10, 10, dx)
f0 = lambda x: (x - 0.5)**2
result = minimize(f0, x0=1)
print(result)
plt.plot(x, f0(x))
plt.show()