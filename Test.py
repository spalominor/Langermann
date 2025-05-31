import TabuLangermann as tl
import numpy as np



values = []

for i in range(1000):
    results = tl.tabu_search()
    values.append(results["best_value"])
    print(f"Run {i+1}: {results['best_value']}")

print(f"Mean: {sum(values)/len(values)}")
print(f"Std: {np.std(values)}")
print(f"Min: {min(values)}")
print(f"Max: {max(values)}")