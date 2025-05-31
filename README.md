# 🌌 Langermann

## 🧠 Optimización de la Función Langermann con Búsqueda Tabú

Este módulo implementa la metaheurística de **Búsqueda Tabú** para 
optimizar la función **Langermann**. Incluye herramientas para:

✅ Visualizar resultados  
✅ Simular combinaciones de parámetros  
✅ Refinar soluciones mediante descenso por gradiente numérico

---

## 🗂️ Estructura del Proyecto

📄 **`BusquedaTabuEjemplo.py`**  
🔍 Ejemplo básico del algoritmo aplicado a la función Gramacy-Lee (1D).  
📈 Muestra la mejor solución encontrada y el historial gráfico.

📄 **`GradientDescent.py`**  
📉 Implementación de descenso por gradiente numérico (2D).  
🔬 Afina soluciones obtenidas por Búsqueda Tabú.

📄 **`PlotLangermann.py`**  
🖼️ Genera visualizaciones 2D/3D de la función y las soluciones.  
📊 Incluye la evolución del valor objetivo por iteración.

📄 **`TabuLangermann.py`**  
🧩 Núcleo del algoritmo de Búsqueda Tabú sobre Langermann.  
📌 Incluye evaluación, control tabú y `tabu_search()`.

📄 **`Solver.py`**  
🚀 Script principal. Ejecuta funciones clave, imprime y grafica resultados.  
👥 Ideal para usuarios que deseen probar el sistema fácilmente.

📄 **`SimulationGradient.py`**  
⚙️ Explora múltiples configuraciones de descenso de gradiente.  
🏅 Lista las 5 mejores soluciones obtenidas.

📄 **`SimulationTabu.py`**  
📊 Simulación intensiva del algoritmo Tabú (~100 combinaciones).  
📈 Promedia resultados, calcula desviación y muestra top 5 ejecuciones.

---

## 🧪 Instrucciones de Uso

1. 🧬 **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
2. 📦 **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
3. 🚀 **Ejecutar el módulo principal:**
   ```bash
   python Solver.py
4. 🧭 **Simulaciones opcionales:**
   ```bash
   python SimulationGradient.py
   python SimulationTabu.py

## 🧩 Solución

## Resultados

# 📉 Valor mínimo encontrado
-4.15425
# 🛠️ Parámetros óptimos
Estos parámetros han sido calculados mediante la simulación del módulo SimulationTabu.py
![imagen](https://github.com/user-attachments/assets/3ec07e4c-f960-48e9-94e3-da13cc900d70)

## 👤 Autor

Proyecto desarrollado por:
## [Samuel Palomino](https://www.linkedin.com/in/spalominor/)

Con apoyo de modelos de inteligencia artificial
## [ChatGPT](https://chatgpt.com)


