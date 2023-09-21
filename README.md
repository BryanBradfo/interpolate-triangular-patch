# Geometric Modeling

For this project, we decided to choose the topic that implements interpolating triangular patch surfaces (and we will proceed using the butterfly scheme).

## Method principle

The basic principle of the interpolating triangular patch surface is to divide a surface into several small triangles, then interpolate a surface function on each of these triangles. Interplating surface functions can be calculated using different methods, one of the most common being the butterfly scheme.

The butterfly scheme is a surface subdivision method that creates a smooth surface by connecting adjacent control points using triangles. The method consists of dividing each triangle into four smaller triangles by applying weights to each point in the direct neighborhood of each initial triangle. Then, a new control point grid is created from the new points obtained by dividing the sides.

## Advantages and limitations

Interpolating triangular patch surfaces have many advantages over other surface modeling methods, including their flexibility, ease of use, and ability to model complex surfaces. However, they also have limitations in terms of representation accuracy and ability to handle large-sized surfaces.

## Testing sample



<!---
# Modélisation Géométrique

Pour ce projet, nous avons décidé de choisir le sujet qui implémente les surfaces à patches triangulaires interpolantes (et on va procéder par le schéma butterfly).

## Principe de la méthode

Le principe de base de la surface à patches triangulaires interpolantes est de diviser une surface en plusieurs petits triangles, puis d'interpoler une fonction de surface sur chacun de ces triangles. Les fonctions de surface interpolantes peuvent être calculées en utilisant différentes méthodes, l'une des plus courantes étant le schéma butterfly. 

Le schéma butterfly est une méthode de subdivision de surface qui crée une surface lisse en reliant les points de contrôle adjacents à l'aide de triangles. La méthode consiste à diviser chaque triangle en quatre triangles plus petits en appliquant des poids à chaque point dans le voisinage direct de chaque triangle initial. Ensuite, une nouvelle grille de points de contrôle est créée à partir des nouveaux points obtenus en divisant les côtés.

## Avantages et limites

Les surfaces à patches triangulaires interpolantes présentent de nombreux avantages par rapport à d'autres méthodes de modélisation de surface, notamment leur flexibilité, leur facilité d'utilisation et leur capacité à modéliser des surfaces complexes. Cependant, elles ont également des limites en termes de précision de la représentation et de capacité à gérer des surfaces de grande taille. 
---->
