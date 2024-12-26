import numpy as np

def HGSO(pop_size, dim, lb, ub, max_iter, obj_func):
    # Başlatma
    positions = np.random.uniform(lb, ub, (pop_size, dim))
    henry_const = np.random.uniform(0, 1, pop_size)
    partial_pressure = np.random.uniform(0, 1, pop_size)
    best_fitness = float('inf')
    best_solution = None

    for t in range(max_iter):
        # Fitness hesapla
        fitness = np.array([obj_func(pos) for pos in positions])
        if fitness.min() < best_fitness:
            best_fitness = fitness.min()
            best_solution = positions[fitness.argmin()]

        # Henry sabiti ve çözünürlük güncelle
        T = np.exp(-t / max_iter)
        henry_const *= np.exp(-np.random.uniform(0, 1) * (1 / T - 1 / 298.15))
        solubility = henry_const * partial_pressure

        # Pozisyonları güncelle
        r = np.random.random((pop_size, dim))
        positions += r * solubility[:, None] * (best_solution - positions)
        positions = np.clip(positions, lb, ub)

        # Yerel optimumdan kaçış
        if t % 10 == 0:
            worst_indices = fitness.argsort()[-int(0.2 * pop_size):]
            positions[worst_indices] = np.random.uniform(lb, ub, (len(worst_indices), dim))

    return best_solution, best_fitness

# Rastrigin amaç fonksiyonu
def rastrigin(x):
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

# Parametreler
pop_size, dim, lb, ub, max_iter = 50, 30, -5.12, 5.12, 1000

# Çalıştırma
best_solution, best_fitness = HGSO(pop_size, dim, lb, ub, max_iter, rastrigin)
print("En iyi çözüm:", best_solution)
print("En iyi fitness:", best_fitness)
