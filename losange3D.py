import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Coordonnées des points
points = np.array([
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0],
    [-1.0, 0.0, 0.0],
    [0.0, 0.0, -1.0],
    [0.0, -1.0, 0.0]
])

# Liste des indices des points formant chaque triangle
triangles = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [0, 3, 4],
    [0, 4, 1],
    [5, 1, 2],
    [5, 2, 3],
    [5, 3, 4],
    [5, 4, 1]
])

# Création de la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracé des points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')

# Tracé des surfaces triangulaires
for triangle in triangles:
    vertices = points[triangle]
    poly = Poly3DCollection([vertices])
    poly.set_edgecolor('k')
    poly.set_facecolor('cyan')
    ax.add_collection3d(poly)

# Configuration de l'axe des coordonnées
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Affichage de la figure
plt.show()
