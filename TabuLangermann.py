"""
Module for the Tabu search algorithm on the Langermann function in 2D.

This module implements the Tabu search algorithm to find the minimum of the 
Langermann function in two dimensions.

Methods:
    evaluate_langermann(position): Evaluates the Langermann function at a 
        given position.
    generate_neighbors(position, num_neighbors, sigma): Generates nearby 
        solutions with Gaussian noise.
    is_tabu(position, tabu_list, tolerance): Checks if a solution is in the 
        tabu list based on Euclidean distance.
    tabu_search(): Executes the Tabu search algorithm to optimize the 
        Langermann function.
"""
import math  
import random
from typing import Dict, List, Union



# Definir constantes globales para la función de Langermann
A: List[float] = [3, 5, 2, 1, 7]
B: List[float] = [5, 2, 1, 4, 9]
C: List[float] = [1, 2, 5, 2, 3]



def evaluate_langermann(position: List[float]) -> float:
    """
    Evalúa la función de Langermann en dos dimensiones.

    La función está definida como una suma ponderada de términos exponenciales 
    y cosenoidales, basados en parámetros globales A, B y C.

    Args:
        position (List[float]):
            Coordenadas [x, y] en las que se evalúa la función.

    Returns:
        float:
            Resultado de la evaluación de la función en el punto dado.
    """
    # Extraer coordenadas x e y
    x, y = position

    # Inicializar el acumulador de la suma
    total = 0

    # Iterar sobre cada término de la función (m = 5)
    for i in range(5):
        # Calcular diferencia cuadrática
        dx = x - A[i]
        dy = y - B[i]
        sq = dx**2 + dy**2

        # Calcular el término i del sumatorio
        term = C[i] * math.exp(-sq / math.pi)
        term *= math.cos(sq * math.pi)

        # Sumar el término al total
        total += term

    return total


def generate_neighbors(
    position: List[float],
    num_neighbors: int,
    sigma: float
) -> List[List[float]]:
    """
    Genera vecinos cercanos aplicando ruido gaussiano restringido a [0, 10].

    Args:
        position (List[float]):
            Punto base [x, y] desde el cual se generan los vecinos.
        num_neighbors (int):
            Número de vecinos a generar.
        sigma (float):
            Desviación estándar del ruido gaussiano aplicado.

    Returns:
        List[List[float]]:
            Lista de puntos vecinos generados dentro del rango [0, 10].
    """
    neighbors = []

    # Generar cada vecino individualmente
    for _ in range(num_neighbors):
        # Aplicar ruido gaussiano a x e y
        x = random.gauss(position[0], sigma)
        y = random.gauss(position[1], sigma)

        # Restringir a dominio [0, 10]
        x = max(0, min(10, x))
        y = max(0, min(10, y))

        neighbors.append([x, y])

    return neighbors



def is_tabu(position: List[float], 
            tabu_list: List[List[float]], 
            tolerance: float = 0.01) -> bool:
    """
    Verifica si una solución está en la lista tabú basada en distancia 
    euclídea.

    Args:
        position (List[float]): Solución candidata [x, y].
        tabu_list (List[List[float]]): Lista de soluciones tabú.
        tolerance (float): Distancia mínima para considerar la solución tabú.

    Returns:
        bool: True si la solución está dentro de la tolerancia en la lista 
            tabú, False en caso contrario.
    """
    # Iterar sobre cada solución pasada en la lista tabú
    for past in tabu_list:
        # Calcular diferencia en la coordenada x
        dx = position[0] - past[0]
        # Calcular diferencia en la coordenada y
        dy = position[1] - past[1]
        # Calcular distancia euclídea entre position y past
        dist = math.sqrt(dx**2 + dy**2)
        # Verificar si la distancia es menor que la tolerancia
        if dist < tolerance:
            # La solución está demasiado cerca y es tabú
            return True
    # No se encontró solución cercana en la lista tabú
    return False


def tabu_search(num_iterations: int = 1000, 
                num_neighbors: int = 50, 
                tabu_size: int = 30, 
                sigma: float = 0.8
                ) -> Dict[str, Union[List[float], float]]:
    """
    Ejecuta el algoritmo de Búsqueda Tabú para optimizar Langermann 2D.

    Args:
        num_iterations (int): Número de iteraciones del algoritmo.
        num_neighbors (int): Cantidad de vecinos generados por iteración.
        tabu_size (int): Tamaño máximo de la lista tabú.
        sigma (float): Desviación estándar del ruido gaussiano para vecinos.

    Returns:
        Dict[str, Union[List[float], float]]:
            Diccionario con:
            - 'best': Mejor solución [x, y] encontrada.
            - 'best_value': Valor mínimo encontrado.
            - 'history': Lista de valores mínimos por iteración.
            - 'initial_point': Punto inicial desde donde comenzó la búsqueda.
    """
    # Inicializar solución aleatoria dentro del dominio
    current = [random.uniform(0, 10), random.uniform(0, 10)]

    # Guardar el valor de la posición inicial
    initial_point = current

    # Evaluar la solución actual
    current_value = evaluate_langermann(current)

    # Inicializar mejor solución global
    best = current
    best_value = current_value

    # Inicializar lista tabú e historial
    tabu_list = [current]
    history = [best_value]

    # Bucle principal de iteraciones
    for _ in range(num_iterations):
        # Generar vecinos con perturbaciones gaussianas
        neighbors = generate_neighbors(current, num_neighbors, sigma)

        # Inicializar mejor vecino y su valor
        candidate = None
        candidate_value = float("inf")

        # Evaluar vecinos
        for neighbor in neighbors:
            # Calcular valor del vecino
            value = evaluate_langermann(neighbor)

            # Verificar si es tabú
            if is_tabu(neighbor, tabu_list):
                # Aplicar criterio de aspiración
                if value < best_value:
                    candidate = neighbor
                    candidate_value = value
            else:
                if value < candidate_value:
                    candidate = neighbor
                    candidate_value = value

        # Actualizar la solución actual con el mejor vecino
        current = candidate
        current_value = candidate_value

        # Agregar a la lista tabú
        tabu_list.append(current)

        # Limitar el tamaño de la lista tabú
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        # Actualizar mejor solución global si es necesario
        if current_value < best_value:
            best = current
            best_value = current_value

        # Registrar valor mínimo actual en el historial
        history.append(best_value)

    # Construir resultado en diccionario
    result = {
        "best": best,
        "best_value": best_value,
        "history": history,
        "initial_point": initial_point
    }


    return result