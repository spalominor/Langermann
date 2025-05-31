import random
import numpy as np
import matplotlib.pyplot as plt



# Función Gramacy & Lee (2012)
def gramacy_lee(x):
    return np.sin(10 * np.pi * x) / (2 * x) + (x - 1)**4

# Función objetivo
def objetivo(x):
    return gramacy_lee(x)

# Generar vecinos en 1D
def generar_vecinos(x, paso=0.05, limites=(0.5, 2.5)):
    vecinos = [x + paso, x - paso]
    vecinos = [np.clip(v, *limites) for v in vecinos]
    return vecinos

# Parámetros de la búsqueda
MAX_ITER = 100
TAM_TABU = 10
paso = 0.05
limites = (0.5, 2.5)

# Inicialización
x_actual = random.uniform(*limites)
mejor_x = x_actual
mejor_valor = objetivo(x_actual)
tabu = []
historial = [x_actual]

# Búsqueda Tabú
for _ in range(MAX_ITER):
    vecinos = generar_vecinos(x_actual, paso, limites)
    
    # Criterio de aspiración incluido (acepta tabú si mejora el global)
    vecinos_validos = [v for v in vecinos if v not in tabu or objetivo(v) < mejor_valor]
    
    if not vecinos_validos:
        break

    vecino = min(vecinos_validos, key=objetivo)
    valor = objetivo(vecino)
    
    x_actual = vecino
    historial.append(x_actual)

    if valor < mejor_valor:
        mejor_x = vecino
        mejor_valor = valor

    tabu.append(vecino)
    if len(tabu) > TAM_TABU:
        tabu.pop(0)

# Resultados
print(f"Mejor solución encontrada: x = {mejor_x:.5f}, f(x) = {mejor_valor:.5f}")

# Graficar función y camino de búsqueda
x_vals = np.linspace(*limites, 1000)
y_vals = [objetivo(x) for x in x_vals]

# Ruta de búsqueda
ruta_y = [objetivo(x) for x in historial]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="Gramacy & Lee Function", linewidth=2)
plt.plot(historial, ruta_y, 'ro-', label="Camino Búsqueda Tabú")
plt.scatter(mejor_x, mejor_valor, c='green', marker='*', s=150, label="Óptimo encontrado")

plt.title("Búsqueda Tabú en la función Gramacy & Lee (2012)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
