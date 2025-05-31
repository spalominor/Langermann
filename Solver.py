"""
Module with the main execution of the Tabu search and gradient descent 
algorithms for solving the Langermann function optimization problem.
"""
import TabuLangermann as tl
import PlotLangermann as pl
import GradientDescent as gd



# Ejecutar la búsqueda tabú
resultados = tl.tabu_search()

# Expandir resultados
mejor_posicion = resultados["best"]
mejor_valor = resultados["best_value"]
historial = resultados["history"]
punto_inicial = resultados["initial_point"]

# Imprimir resultados
print("Tabu Search Results:")
print("Mejor posición encontrada:", mejor_posicion)
print("Valor mínimo:", mejor_valor)
print("Punto inicial:", punto_inicial)

# Mostrar evolución
pl.plot_history(historial)

# Mostrar mapa de calor
pl.plot_heatmap(mejor_posicion)

# Mostrar superficie 3D
pl.plot_surface(mejor_posicion)

# Imprimir el método del gradiente numérico
print("\n\nNumerical Gradient Method:")

# Ejecutar descenso por gradiente numérico
mejor_punto, mejor_valor_teorico, historial = gd.gradient_descent(
    func=tl.evaluate_langermann,
    start_point=mejor_posicion)

print("\nGradient Descent Results:")
print("Punto óptimo:", mejor_punto)
print("Valor mínimo:", mejor_valor_teorico)

# Calcular el error absoluto y relativo
error_absoluto = abs(mejor_valor - mejor_valor_teorico)
error_relativo = error_absoluto / abs(mejor_valor) * 100

# Imprimir errores
print("Error absoluto:", error_absoluto)
print("Error relativo (%):", error_relativo)