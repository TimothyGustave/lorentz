#!/usr/bin/python3

# On cherche à tracer dans l'espace des phases, l'équation de lorentz
# On utilise pour cela le schéma d'euler explicite

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

# Schéma d'Euler explicite
def euler_explicite(X, h, *f):
    # X c'est le tableau contenant N élément
    # y[-1] + h * f(t, y[-1]) Ici le pas est de 1
    
    N = len(X) # N est la dimension du vecteur X
    res = ()
    
    for dimension in range(N):
        # On créer un vecteur de dimension N en concaténant les dimensions succesives
        res  = res + (X[dimension] + h * f[dimension](t, X),)
    
    return res

if __name__ == "__main__":
    # Constantes
    alpha = 10  # Nombre de Prandtl
    b = 8 / 3   # Taille typique du système
    r = 25     # Rapport entre le nommbre de Rayleigh et le nombre de Rayleigh critique

    # système de lorentz
    # où X = (x, y, z)
    x = lambda t, X : alpha * (X[1] - X[0])
    y = lambda t, X: r * X[0] - X[1] - X[0] * X[2]
    z = lambda t, X: X[0] * X[1] - b * X[2]

    # Paramètres sur les quantités calculées
    N = 1000   # Nombres de points tracés
    t = 0.01   # unités de temps utilisés
    
    # Ensemble des valeurs initiales
    axe_x = [0]
    axe_y = [1]
    axe_z = [1.05]
    init = (axe_x[-1], axe_y[-1], axe_z[-1])

    # On calcule la trajectoire suivant les points de 
    for i in range(N):
        init = euler_explicite(init, t, x, y, z)
        axe_x.append(init[0])
        axe_y.append(init[1])
        axe_z.append(init[2])
        
    # Maintenant qu'on a tout les points, on les trace sur un graphique en 3D
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot3D(axe_x, axe_y, axe_z)
    # ax.view_init(20, 20)
    plt.show()