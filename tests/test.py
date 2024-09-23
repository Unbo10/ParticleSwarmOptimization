import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-10, num=100, stop=10)
y = np.linspace(start=-10, num=100, stop=10)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure(figsize=(5, 5))

ax = fig.add_subplot(111)
contour = ax.contourf(x, y, z, cmap="viridis")
fig.colorbar(contour, ax=ax)
ax.set_title("Test graph")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

plt.tight_layout()
plt.show()
