'''
The original version of: FDA

# Created by "Ege Çıtak" on 29.12.2024 -----------------------------%
#       Email: egec9557@gmail.com                                %
#       Github: https://github.com/egecitax            %
# --------------------------------------------------------------%

Links:
     https://www.sciencedirect.com/science/article/abs/pii/S0360835221001285
References:
     Karami, H., Shoorehdeli, M. A., & Teshnehlab, M. (2021). Flow direction algorithm: A novel optimization approach for solving optimization problems. Computers & Industrial Engineering, 156, 107224. https://doi.org/10.1016/j.cie.2021.107224
    '''

from solution import solution
import numpy as np
import random
import time


def FDA(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    s = solution()
    s.optimizer="FDA"
    s.objfname = objf.__name__
    s.lb = lb
    s.ub = ub
    s.dim = dim
    s.popnum = SearchAgents_no
    s.maxiers = Max_iter
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    # Flow X başlangıç pozisyonu
    Flow_X = np.random.uniform(lb, ub, (SearchAgents_no, dim))
    Flow_fitness = np.array([objf(ind) for ind in Flow_X])

    # Best X'i başlat
    best_index = np.argmin(Flow_fitness)
    Best_X = Flow_X[best_index].copy()
    Best_fitness = Flow_fitness[best_index]

    # Convergence eğrisi
    convergence_curve = np.zeros(Max_iter)

    print(f"FDA is optimizing \"{objf.__name__}\"")
    timerStart = time.time()

    for iteration in range(Max_iter):
        # Ağırlık faktörü (W) hesaplama
        rand = np.random.uniform(0, 1)
        W = ((1 - iteration / Max_iter)**(2 * rand)) * ((rand * iteration) / Max_iter) * rand

        for i in range(SearchAgents_no):
            # Neighbor X oluştur
            Neighbor_X = generate_neighbors(Flow_X[i], W, Best_X, dim)
            Neighbor_fitness = np.array([objf(neigh) for neigh in Neighbor_X])

            # En iyi komşuyu bul
            best_neighbor_index = np.argmin(Neighbor_fitness)
            Best_Neighbor_X = Neighbor_X[best_neighbor_index]
            Best_Neighbor_fitness = Neighbor_fitness[best_neighbor_index]

            # Eğim (S0) hesapla
            S0 = calculate_slope(Flow_X[i], Best_Neighbor_X, Flow_fitness[i], Best_Neighbor_fitness)

            # Hız (V) hesapla
            V = np.random.normal(0, 1) * S0

            # Yeni pozisyonu güncelle
            Flow_newX = update_position(Flow_X[i], Best_Neighbor_X, V, lb, ub)

            # Akış yönünü simüle et
            random_flow = Flow_X[random.randint(0, SearchAgents_no - 1)]
            random_fitness = objf(random_flow)

            if random_fitness < Flow_fitness[i]:
                Flow_newX = np.clip(Flow_X[i] + np.random.normal(0, 1) * (random_flow - Flow_X[i]), lb, ub)
            else:
                Flow_newX = np.clip(Flow_X[i] + 2 * np.random.normal(0, 1) * (Best_X - Flow_X[i]), lb, ub)

            # Yeni fitness değerini hesapla ve güncelle
            new_fitness = objf(Flow_newX)
            Flow_X[i] = Flow_newX
            Flow_fitness[i] = new_fitness

            # Best X'i güncelle
            if new_fitness < Best_fitness:
                Best_X = Flow_newX.copy()
                Best_fitness = new_fitness

        # Convergence eğrisini güncelle
        convergence_curve[iteration] = Best_fitness

        if iteration % 10 == 0:
            print(f"At iteration {iteration} the best fitness is {Best_fitness}")

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.bestIndividual = Best_X
    s.best = Best_fitness

    return s

def generate_neighbors(Flow_X, W, Best_X, dim):
    rand = np.random.uniform(0, 1, dim)
    Delta = (rand * (Best_X - Flow_X) + 1e-6) * W
    return Flow_X + np.random.normal(0, 1, (5, dim)) * Delta

def calculate_slope(Flow_X, Neighbor_X, Flow_fitness, Neighbor_fitness):
    norm = np.linalg.norm(Flow_X - Neighbor_X)
    if norm == 0:
        return 0  # Eğim sıfır
    return (Flow_fitness - Neighbor_fitness) / norm

def update_position(Flow_X, Neighbor_X, V, lb, ub):
    norm = np.linalg.norm(Flow_X - Neighbor_X)
    if norm == 0:
        Flow_newX = Flow_X  # Hiçbir güncelleme yapma
    else:
        Flow_newX = Flow_X + V * (Flow_X - Neighbor_X) / norm
    return np.clip(Flow_newX, lb, ub)

