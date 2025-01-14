# -*- coding: utf-8 -*-
"""

The original version of: [African vultures optimization algorithm]

# Created by "[BERAT ÇALIK]" on [Mon Jan 13 19:13:28 2025] -----------------------------% 
#       Email: [42berat1907@gmail.com]                                %
#       Github: https://github.com/beratcalik           %
# --------------------------------------------------------------%

Links:
    1. [https://www.sciencedirect.com/science/article/pii/S0360835221003120]
References:
    [1] [Abdollahzadeh, B., Soleimanian Gharehchopogh, F., & Mirjalili, S. (2021). African vultures optimization algorithm: A new nature-inspired metaheuristic algorithm for global optimization problems. Computers & Industrial Engineering, 158, 107408.]

"""

import random
import numpy as np
import time
from solution import solution  # Sonuçları kaydetmek için

def AVOA(objf, lb, ub, dim, N, Max_time):
    """
    African Vultures Optimization Algorithm (AVOA)
    
    Args:
        objf: Optimize edilecek hedef fonksiyon.
        lb: Alt sınır (list veya tek bir değer).
        ub: Üst sınır (list veya tek bir değer).
        dim: Problemin boyutu (değişken sayısı).
        N: Popülasyon boyutu.
        Max_time: Maksimum iterasyon sayısı.
        
    Returns:
        s: Çözüm objesi (optimizer, en iyi sonuç, yürütme süresi vb. bilgileri içerir).
    """
    # Sınırları ayarla
    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim

    # Popülasyonu rastgele başlat
    Vultures = np.random.uniform(0, 1, (N, dim)) * (np.array(ub) - np.array(lb)) + np.array(lb)
    Fitness = np.array([objf(ind) for ind in Vultures])
    
    # En iyi iki akbabayı belirle
    BestVulture1 = Vultures[np.argmin(Fitness)]
    BestVulture2 = Vultures[np.argsort(Fitness)[1]]

    # Convergence eğrisini takip et
    convergence_curve = np.zeros(Max_time)

    # Optimizasyon döngüsü
    s = solution()
    print(f'AVOA is optimizing "{objf.__name__}"')
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    for iteration in range(Max_time):
        F = 2 * random.random() - 1  # Keşif ve sömürü parametresi

        for i in range(N):
            R = np.random.uniform(-1, 1, dim)  # Rastgele vektör

            if abs(F) >= 1:
                if random.random() < 0.5:
                    Vultures[i] = BestVulture1 + F * R
                else:
                    Vultures[i] = BestVulture2 - F * R
            else:
                if abs(F) >= 0.5:
                    if random.random() < 0.5:
                        Vultures[i] = BestVulture1 + F * R * random.random()
                    else:
                        Vultures[i] = BestVulture2 - F * R * random.random()
                else:
                    if random.random() < 0.5:
                        Vultures[i] = BestVulture1 + F * (BestVulture1 - Vultures[i])
                    else:
                        Vultures[i] = BestVulture2 + F * (BestVulture2 - Vultures[i])

            # Sınırları kontrol et
            Vultures[i] = np.clip(Vultures[i], lb, ub)

        # Fitness değerlerini güncelle
        Fitness = np.array([objf(ind) for ind in Vultures])
        BestVulture1 = Vultures[np.argmin(Fitness)]
        BestVulture2 = Vultures[np.argsort(Fitness)[1]]
        convergence_curve[iteration] = min(Fitness)

        print(f"At iteration {iteration + 1}, the best fitness is {min(Fitness)}")

    # Çıktıları kaydet
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "AVOA"
    s.objfname = objf.__name__
    s.best = BestVulture1  # En iyi çözüm vektörü
    s.bestFitness = min(Fitness)  # En iyi fitness değeri

    return s