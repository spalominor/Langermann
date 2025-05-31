"""
Module for plotting the Langermann function and the results of the Tabu search algorithm.

This module provides functions to visualize the Langermann function in 2D and 3D,
as well as the history of the Tabu search optimization process.

Methods:
    - plot_history(history): Plots the evolution of the minimum value 
        over iterations.
    - plot_heatmap(best_pos): Generates a 2D heatmap of the Langermann 
        function with the best position marked.
    - plot_surface(best_pos): Generates a 3D surface plot of the Langermann 
        function with the best position marked.
"""
import numpy as np  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import TabuLangermann as tl


def plot_history(history):
    """
    Grafica la evolución del valor mínimo en cada iteración.

    Args:
        history (list[float]): Valores mínimos por iteración.
    """
    # Crear la figura y el eje
    plt.figure()
    plt.plot(history, label="Valor mínimo")
    plt.title("Evolución de la búsqueda tabú")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de la función")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_heatmap(best_pos):
    """
    Genera un mapa de calor 2D de la función Langermann
    y marca la mejor posición encontrada.

    Args:
        best_pos (list[float]): Coordenadas [x, y] de la mejor solución.
    """
    # Crear una malla de puntos en el rango [0, 10]
    x = np.linspace(0, 10, 200)
    y = np.linspace(0, 10, 200)
    X, Y = np.meshgrid(x, y)

    # Evaluar la función en cada punto de la malla
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = tl.evaluate_langermann([X[i, j], Y[i, j]])

    # Crear la figura y el mapa de calor
    plt.figure(figsize=(8, 6))
    heatmap = plt.contourf(X, Y, Z, levels=100, cmap='viridis')
    plt.colorbar(heatmap, label='Valor de la función')
    plt.scatter(best_pos[0], best_pos[1], color='red', marker='x',
                label='Mejor posición encontrada')
    plt.title("Mapa de calor de la función Langermann")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_surface(best_pos):
    """
    Genera una gráfica 3D de la superficie de la función Langermann
    y marca la mejor posición encontrada.

    Args:
        best_pos (list[float]): Coordenadas [x, y] de la mejor solución.
    """
    # Crear una malla de puntos en el rango [0, 10]
    x = np.linspace(0, 10, 200)
    y = np.linspace(0, 10, 200)
    X, Y = np.meshgrid(x, y)

    # Evaluar la función en cada punto de la malla
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = tl.evaluate_langermann([X[i, j], Y[i, j]])

    # Crear figura y ejes 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Graficar superficie
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

    # Marcar la mejor posición encontrada
    z_best = tl.evaluate_langermann(best_pos)
    ax.scatter(best_pos[0], best_pos[1], z_best, color='red', s=50,
               label='Mejor posición')

    # Etiquetas y formato
    ax.set_title("Superficie de la función Langermann")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.legend()
    plt.tight_layout()
    plt.show()