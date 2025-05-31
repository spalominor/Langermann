"""
Module for numerical gradient descent optimization.

This module implements a numerical gradient descent algorithm to minimize a 
given function in two dimensions. Works by approximating the gradient
using finite differences and iteratively updating the position based on the
gradient.

Methods:
    - compute_numerical_gradient(func, point, h=1e-5): Computes the numerical 
    gradient of a function at a given point.
    - gradient_descent(func, start_point, learning_rate=0.01, max_iter=500, 
    tolerance=1e-6, h=1e-5): Executes the gradient descent algorithm.
"""
from typing import Callable, Tuple, List
import numpy as np



def compute_numerical_gradient(
    func: Callable[[List[float]], float],
    point: List[float],
    h: float
) -> np.ndarray:
    """
    Calcula el gradiente numérico en un punto dado usando diferencias finitas.

    Args:
        func (Callable[[List[float]], float]):
            Función objetivo f([x, y]) a minimizar.
        point (List[float]):
            Punto [x, y] donde se estima el gradiente.
        h (float):
            Paso para la diferencia finita.

    Returns:
        np.ndarray:
            Vector gradiente aproximado en el punto (como arreglo de NumPy).
    """
    # Separar coordenadas
    x, y = point

    # Aproximar derivada parcial con respecto a x
    fxh1 = func([x + h, y])
    fxh2 = func([x - h, y])
    dfdx = (fxh1 - fxh2) / (2 * h)

    # Aproximar derivada parcial con respecto a y
    fyh1 = func([x, y + h])
    fyh2 = func([x, y - h])
    dfdy = (fyh1 - fyh2) / (2 * h)

    # Devolver gradiente como vector numpy
    return np.array([dfdx, dfdy])


def gradient_descent(
    func: Callable[[list[float]], float],
    start_point: List[float],
    learning_rate: float = 0.005,
    max_iter: int = 100,
    tolerance: float = 1e-7,
    h: float = 0.0001
) -> Tuple[List[float], float, List[Tuple[float, float, float]]]:
    """
    Ejecuta descenso por gradiente numérico sobre una función objetivo.

    Args:
        func (Callable[[list[float]], float]): 
            Función objetivo f([x, y]) a minimizar.
        start_point (List[float]): 
            Punto inicial [x, y].
        learning_rate (float): 
            Tasa de aprendizaje η.
        max_iter (int, opcional): 
            Número máximo de iteraciones. Por defecto 500.
        tolerance (float, opcional): 
            Umbral para detener cuando ||grad|| es pequeño. Por defecto 1e-6.
        h (float, opcional): 
            Paso para diferencia finita. Por defecto 1e-5.

    Returns:
        Tuple[List[float], float, List[Tuple[float, float, float]]]:
            - Punto final optimizado.
            - Valor de la función en ese punto.
            - Historial de puntos y evaluaciones por iteración.
    """
    # Inicializar punto de partida
    current_point = np.array(start_point)
    history = []

    for i in range(max_iter):
        # Evaluar gradiente numérico
        grad = compute_numerical_gradient(func, current_point, h)

        # Calcular magnitud del gradiente
        grad_norm = np.linalg.norm(grad)

        # Guardar historial
        f_val = func(current_point)
        history.append((current_point[0], current_point[1], f_val))

        # Mostrar progreso cada 50 iteraciones
        if i % 50 == 0:
            print(f"Iteración {i}: f({current_point}) = {f_val:.6f}, "
                  f"||grad|| = {grad_norm:.6e}")

        # Verificar condición de parada por gradiente pequeño
        if grad_norm < tolerance:
            print("Gradiente suficientemente pequeño. Deteniendo.")
            break

        # Actualizar posición
        current_point = current_point - learning_rate * grad

    # Devolver resultado final
    return current_point.tolist(), func(current_point), history