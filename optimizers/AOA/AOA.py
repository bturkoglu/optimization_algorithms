
import numpy as np
import time
from solution import solution

def AOA(objf, lb, ub, dim, popSize, Iter):

    # Parametreler
    MOA_Max = 0.9
    MOA_Min = 0.2
    Alpha = 5
    Mu = 0.4999


    # Popülasyonu başlatma
    population = np.random.uniform(lb, ub, (popSize, dim))
    Xnew = np.copy(population)

    # Yakınsama eğrisi
    convergence_curve = np.zeros(Iter)


    # Solution sınıfından nesne
    s = solution()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    timerStart = time.time()

    print(f'AOA is optimizing "{objf.__name__}"')

    # En iyi değerin başlatılması
    BestScore = float("inf")
    BestPos = np.zeros(dim)

    # Başlangıç popülasyonun değerlerinin hesaplanması
    print("Initial Population and Fitness Values:")
    for i in range(popSize):
        fitness = objf(population[i, :])
        if fitness < BestScore:
            BestScore = fitness
            BestPos = population[i, :].copy()

    # ANA DÖNGÜ
    for current_iter in range(1, Iter + 1):

        for z in range(popSize):
            fitness = objf(population[z,:])
            if fitness < BestScore:
                BestScore = fitness
                BestPos = population[z, :].copy()



        convergence_curve[current_iter-1] = BestScore

        # MOA ve MOP parametreleri güncelleme denklemleri
        mop = 1 - (current_iter ** (1 / Alpha) / Iter ** (1 / Alpha))
        moa = MOA_Min + current_iter * ((MOA_Max - MOA_Min) / Iter)



        for i in range(popSize):
            for j in range(dim):
                r1 = np.random.uniform(0.0, 1.0)
                r2 = np.random.uniform(0.0, 1.0)
                r3 = np.random.uniform(0.0, 1.0)

                if r1 > moa:
                    # Keşif kısmı
                    if r2 > 0.5:
                        # Bölme operatörü konum güncelleme denklemi

                        Xnew[i, j] = BestPos[j] / (mop + 1e-6) * ((ub - lb) * Mu + lb)

                    else:
                        # Çarpma operatörü konum güncelleme denklemi

                        Xnew[i, j] = BestPos[j] * mop * ((ub - lb) * Mu + lb)

                else:

                    # Sömürü kısmı
                    if r3 < 0.5:
                        # Çıkarma operatörü konum güncelleme denklemi

                        Xnew[i, j] = BestPos[j] - mop * ((ub - lb) * Mu + lb)

                    else:
                        # Toplama operatörü konum güncelleme denklemi

                        Xnew[i, j] = BestPos[j] + mop * ((ub - lb) * Mu + lb)

                # Çözümleri sınırlara göre ayarlama
                Xnew[i, :] = np.clip(Xnew[i, :], lb, ub)
                # Yeni fitness değerini hesapla
                population[i, :] = Xnew[i, :].copy()



        if current_iter % 100 == 0:
            print(f"At iteration {current_iter}, the best fitness is {BestScore}")

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "AOA"
    s.objfname = objf.__name__
    s.best = BestScore
    s.bestIndividual = BestPos

    return s
