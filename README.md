# Modelisation_geometrique

Pour ce projet, nous avons décidé de choisir le sujet qui implémente les surfaces à patches triangulaires interpolantes (et on va procéder par le schéma butterfly). 

## Principe de la méthode

Le principe de base de la surface à patches triangulaires interpolantes est de diviser une surface en plusieurs petits triangles, puis d'interpoler une fonction de surface sur chacun de ces triangles. Les fonctions de surface interpolantes peuvent être calculées en utilisant différentes méthodes, l'une des plus courantes étant le schéma butterfly. \\

Le schéma butterfly est une méthode de subdivision de surface qui crée une surface lisse en reliant les points de contrôle adjacents à l'aide de triangles. La méthode consiste à diviser chaque triangle en quatre triangles plus petits en appliquant des poids à chaque point dans le voisinage direct de chaque triangle initial. Ensuite, une nouvelle grille de points de contrôle est créée à partir des nouveaux points obtenus en divisant les côtés.

## Avantages et limites

Les surfaces à patches triangulaires interpolantes présentent de nombreux avantages par rapport à d'autres méthodes de modélisation de surface, notamment leur flexibilité, leur facilité d'utilisation et leur capacité à modéliser des surfaces complexes. Cependant, elles ont également des limites en termes de précision de la représentation et de capacité à gérer des surfaces de grande taille. 
