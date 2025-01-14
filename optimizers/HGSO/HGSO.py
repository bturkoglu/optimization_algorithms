
# Algoritma Adı: HGSO (Heuristic Gradient Search Optimization)
#
# Created by "Serpil Umay Gedikli" on 14.01.2025 --------------------%
#       Email: srplgdkl@gmail.com                                 %
#       Github: https://github.com/SerpilUmayGedikli/optimization_algorithms  %
# --------------------------------------------------------------%
#
# Links:
#    Links:
#    1. https://www.sciencedirect.com/science/article/abs/pii/S0167739X19306557#:~:text=Henry's%20law%20is%20an%20essential,space%20and%20avoid%20local%20optima
#
# References:
#    [1] Author(s), (Year). Title of the article. *Journal Name*, Volume(Issue), Page Range. DOI/Link
#

import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# HGSO algoritması 
class HGSO:
    def __init__(self, population_size, iterations, dimension, bounds, fitness_function):
        self.population_size = population_size
        self.iterations = iterations
        self.dimension = dimension
        self.bounds = bounds
        self.fitness_function = fitness_function
        
        # Başlangıç popülasyonunu oluştur
        self.population = np.random.uniform(bounds[0], bounds[1], (population_size, dimension))
        self.best_solution = None
        self.best_fitness = float('inf')
        self.convergence_curve = []

    def update_position(self, individual, best_solution, alpha, beta, iteration, max_iterations):
            # Yeni pozisyon güncelleme formülü
        inertia = 0.9 - 0.7 * (iteration / max_iterations)  # Eylemsizlik azalarak sömürüye geçiş
        exploration = np.random.uniform(-2, 2, size=self.dimension)  # Keşif aralığı genişletildi
        learning_rate = np.random.uniform(0.2, 0.7)  # Daha geniş öğrenme oranı
        return inertia * individual + learning_rate * alpha * (best_solution - individual) + beta * exploration

    def optimize(self):
        alpha = 2.0
        beta = 1.0
        gamma = 0.98  # Daha yavaş adaptif azaltma

        for t in range(self.iterations):
            fitness_values = np.array([self.fitness_function(ind) for ind in self.population])

            # En iyi çözümü güncelle
            min_index = np.argmin(fitness_values)
            if fitness_values[min_index] < self.best_fitness:
                self.best_fitness = fitness_values[min_index]
                self.best_solution = self.population[min_index]

            # Yakınsama eğrisini güncelle
            self.convergence_curve.append(self.best_fitness)

            # Popülasyonu güncelle
            for i in range(self.population_size):
                self.population[i] = self.update_position(
                    self.population[i], 
                    self.best_solution, 
                    alpha, 
                    beta, 
                    t,  # iteration
                    self.iterations  # max_iterations
                )
                self.population[i] = np.clip(self.population[i], self.bounds[0], self.bounds[1])

            # Öğrenme oranlarını azalt
            alpha *= gamma
            beta *= gamma

        return self.best_solution, self.best_fitness


# Fitness fonksiyonu (örnek olarak Sphere fonksiyonu kullanıldı)
def sphere_function(x):
    return np.sum(x ** 2)

# HGSO algoritmasının çalıştırılması
if __name__ == "__main__":
    # Parametreler
    population_size = 50
    iterations = 200
    dimension = 2
    bounds = (-10, 10)
    
    # Optimize edici oluştur
    optimizer = HGSO(population_size, iterations, dimension, bounds, sphere_function)

    # Optimizasyonu çalıştır
    best_solution, best_fitness = optimizer.optimize()

    # Sonuçları yazdır
    print("En iyi çözüm:", best_solution)
    print("En iyi fitness değeri:", best_fitness)

    # Yakınsama eğrisini çiz
    plt.figure()
    plt.plot(optimizer.convergence_curve, label="Yakınsama Eğrisi")
    plt.xlabel("İterasyon")
    plt.ylabel("Fitness")
    plt.title("HGSO Yakınsama Grafiği")
    plt.legend()
    plt.grid()

    # Tarih ve saat tabanlı klasör oluştur
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_dir = f"results_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)

    # Grafik kaydet
    plt.savefig(os.path.join(results_dir, "convergence_plot.png"))
    plt.show()

    # Sonuçları dosyaya kaydet
    np.savetxt(os.path.join(results_dir, "best_solution.csv"), [best_solution], delimiter=",", header="En iyi çözüm")
    np.savetxt(os.path.join(results_dir, "convergence_curve.csv"), optimizer.convergence_curve, delimiter=",", header="Yakınsama eğrisi")
