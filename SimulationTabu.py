import numpy as np
import itertools
import TabuLangermann as tl


def simular_busqueda_tabu(func, start_bounds, num_iterations, num_neighbors,
                          tabu_size, sigma, num_reps=5):
    """
    Ejecuta múltiples repeticiones de Búsqueda Tabú con hiperparámetros dados.

    Args:
        num_iterations (int): Número total de iteraciones.
        num_neighbors (int): Número de vecinos generados por iteración.
        tabu_size (int): Tamaño de la lista tabú.
        sigma (float): Desviación estándar para mutación.
        num_reps (int): Cantidad de repeticiones por combinación.

    Returns:
        dict: Resultados estadísticos de las repeticiones.
    """
    valores_finales = []

    for _ in range(num_reps):
        # Inicializar Búsqueda Tabú
        results = tl.tabu_search(num_iterations=num_iterations,
                                 num_neighbors=num_neighbors,
                                 tabu_size=tabu_size,
                                 sigma=sigma)

        # Añadir a la lista de valores
        valores_finales.append(results["best_value"])

    return {
        "params": (num_iterations, num_neighbors, tabu_size, sigma),
        "media_valor": np.mean(valores_finales),
        "std_valor": np.std(valores_finales)
    }


# Valores de hiperparámetros a explorar
iteraciones_list = [300, 500, 1000]
vecinos_list = [10, 30, 50]
tabu_sizes = [10, 30, 50]
sigmas = [0.1, 0.3, 0.5, 0.8]

# Dominio de búsqueda
dominio = ([0, 10], [0, 10])

# Lista de resultados
resultados = []

# Probar todas las combinaciones de hiperparámetros
for n_iter, n_vec, t_size, sig in itertools.product(
        iteraciones_list, vecinos_list, tabu_sizes, sigmas):

    print(f"Probando: iters={n_iter}, vecinos={n_vec}, "
          f"tabu={t_size}, sigma={sig}")

    resultado = simular_busqueda_tabu(
        func=tl.evaluate_langermann,
        start_bounds=dominio,
        num_iterations=n_iter,
        num_neighbors=n_vec,
        tabu_size=t_size,
        sigma=sig,
        num_reps=20
    )
    resultados.append(resultado)

# Ordenar por mejor valor promedio
resultados_ordenados = sorted(resultados, key=lambda r: r["media_valor"])

# Mostrar las 5 mejores configuraciones
print("\n🏆 Mejores combinaciones de Búsqueda Tabú:")
for r in resultados_ordenados[:5]:
    n_iter, n_vec, t_size, sig = r["params"]
    print(f"iters={n_iter}, vecinos={n_vec}, tabu={t_size}, sigma={sig} | "
          f"media f(x,y): {r['media_valor']:.6f}, std: {r['std_valor']:.4e}")
