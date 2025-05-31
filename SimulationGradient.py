import numpy as np
import itertools
import TabuLangermann as tl
import GradientDescent as gd



def simulate_parameters(func, start_point, learning_rate, tolerance,
                        h, max_iter=500, num_reps=5):
    """
    Ejecuta múltiples repeticiones del descenso por gradiente numérico
    con una combinación específica de hiperparámetros.

    Args:
        func (callable): Función objetivo f([x, y]) a minimizar.
        start_point (list[float]): Punto inicial [x, y].
        learning_rate (float): Tasa de aprendizaje.
        tolerance (float): Tolerancia para el gradiente.
        h (float): Paso de diferencia finita.
        max_iter (int): Número máximo de iteraciones.
        num_reps (int): Cantidad de repeticiones por combinación.

    Returns:
        dict: Resultados estadísticos de las repeticiones.
    """
    valores_finales = []
    iteraciones = []

    for _ in range(num_reps):
        punto, valor, historial = gd.gradient_descent(
            func=func,
            start_point=start_point,
            learning_rate=learning_rate,
            max_iter=max_iter,
            tolerance=tolerance,
            h=h
        )
        valores_finales.append(valor)
        iteraciones.append(len(historial))

    return {
        "params": (learning_rate, tolerance, h),
        "media_valor": np.mean(valores_finales),
        "std_valor": np.std(valores_finales),
        "media_iters": np.mean(iteraciones)
    }


# Lista de hiperparámetros a probar
learning_rates = [0.001, 0.005, 0.01, 0.02]
tolerances = [1e-3, 1e-5, 1e-7]
hs = [1e-4, 1e-5, 1e-6]

# Punto inicial (desde Búsqueda Tabú)
punto_inicial = [2.7932, 1.6035]

# Lista para almacenar resultados
resultados = []

# Iterar sobre todas las combinaciones posibles
for lr, tol, h in itertools.product(learning_rates, tolerances, hs):
    print(f"Probando: η={lr}, tol={tol}, h={h}")
    resultado = simulate_parameters(
        func=tl.evaluate_langermann,
        start_point=punto_inicial,
        learning_rate=lr,
        tolerance=tol,
        h=h,
        max_iter=500,
        num_reps=5
    )
    resultados.append(resultado)

# Ordenar por menor media de valor final
resultados_ordenados = sorted(resultados, key=lambda r: r["media_valor"])

# Mostrar los 5 mejores
print("\n🏆 Mejores combinaciones:")
for r in resultados_ordenados[:5]:
    lr, tol, h = r["params"]
    print(f"η={lr}, tol={tol}, h={h} | "
          f"media f(x,y): {r['media_valor']:.6f}, "
          f"std: {r['std_valor']:.4e}, "
          f"iters: {r['media_iters']:.1f}")
