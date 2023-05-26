import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Définition des points du cube
points = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0]
])

# Définition des triangles du cube
triangles = np.array([
    [0, 1, 2], [0, 2, 3],  # Face avant
    [4, 5, 6], [4, 6, 7],  # Face arrière
    [0, 1, 4], [1, 4, 5],  # Côté gauche
    [2, 3, 6], [3, 6, 7],  # Côté droit
    [0, 3, 4], [3, 4, 7],  # Dessous
    [1, 2, 5], [2, 5, 6]   # Dessus
])

# Plot des points et des triangles
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot des points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')

# Plot des triangles
for tri in triangles:
    poly = Poly3DCollection([points[tri]])
    poly.set_edgecolor('k')
    poly.set_facecolor('cyan')
    ax.add_collection3d(poly)

# Configuration des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Affichage du plot
plt.show()
