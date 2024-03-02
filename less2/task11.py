import matplotlib.pyplot as plt
import numpy as np


R, r = 5, 3 
phi = np.linspace(0, 2*np.pi, 100)
teta = np.linspace(0, 2*np.pi, 100)
phi,teta=np.meshgrid(phi,teta)

x = (R+r*np.cos(phi))*np.cos(teta)
y = (R + r*np.sin(phi))*np.sin(teta)
z = r*np.sin(phi)

fig, ax = plt.subplots(1, 1, figsize=(10, 10), subplot_kw={'projection': "3d"})
ax.plot_surface(x, y, z, cmap="viridis")
ax.view_init(30, 60)
plt.show()
