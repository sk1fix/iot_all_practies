import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    return (np.sin((x**2+y**2)))/(x**2+y**2)
            #return (np.sin((x**2 + y**2))) / (x**2 + y**2)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)


fig, ax = plt.subplots(1, 1, figsize=(10, 10), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60) 
plt.show()