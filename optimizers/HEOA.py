#The original version of: [Human Evlautoniary Optimzation Algorithm]

# Created by "[Beyzanur Saygıner]" on [10.01.2025] -----------------------------%
#       Email: [sayginerbeyzanur@gmail.com]                                %
#       Github: https://github.com/BeyzanurSa             %
# --------------------------------------------------------------%

#Links:
#    1. [https://www.sciencedirect.com/science/article/abs/pii/S0957417423031408]
#References:
#    [1] [Junbo Lian, Guohua Hui (2024)
#         Human Evolutionary Optimization Algorithm 
#         Expert Systems with Applications 241,122638. https://doi.org/10.1016/j.eswa.2023.122638]
from solution import solution  
import numpy as np
import time
from scipy.special import gamma

def HEOA(objf, lb, ub, dim, N, Max_iter):
    """
    Human Exploration Optimization Algorithm (HEOA)
    """
    print("HEOA started with parameters:", f"dim={dim}, N={N}, Max_iter={Max_iter}")

    try:
        # Alt ve üst sınırları listeye dönüştürme
        if not isinstance(lb, list):
            lb = [lb] * dim
        if not isinstance(ub, list):
            ub = [ub] * dim

        # Parameters
        jump_factor = abs(lb[0] - ub[0]) / 1000
        A = 0.6  # Warning value
        LN = 0.4  # Percentage of leaders
        EN = 0.4  # Percentage of explorers
        FN = 0.1  # Percentage of followers

        LNNumber = round(N * LN)  # Number of leaders
        ENNumber = round(N * EN)  # Number of explorers
        FNNumber = round(N * FN)  # Number of followers

        # Initialization
        print("Initializing population...")
        X = initializationLogistic(N, dim, ub, lb)
        fitness = np.zeros(N)
        for i in range(N):
            fitness[i] = objf(X[i, :])

        sorted_indices = np.argsort(fitness)
        fitness = fitness[sorted_indices]
        X = X[sorted_indices, :]

        BestF = fitness[0]
        WorstF = fitness[-1]
        GBestF = fitness[0]  # Global best fitness value
        AveF = np.mean(fitness)

        GBestX = X[0, :]  # Global best position
        X_new = np.copy(X)

        # Initialize convergence array
        print("Initializing convergence tracking...")
        Convergence_curve = np.zeros(Max_iter)

        print(f'HEOA is optimizing "{objf.__name__}"')
        
        # Create solution object early
        s = solution()
        s.optimizer = "HEOA"
        s.objfname = objf.__name__
        timerStart = time.time()
        s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

        # Main loop
        print("Starting main optimization loop...")
        for i in range(Max_iter):
            if i % 10 == 0:
                print(f'At iteration {i}, the fitness is {GBestF}')

            # Tracking the progress
            BestF = fitness[0]
            WorstF = fitness[-1]
            AveF = np.mean(fitness)
            Convergence_curve[i] = BestF

            # Random number
            R = np.random.rand()

            for j in range(N):
                # Human exploration stage
                if i <= (1 / 4) * Max_iter:
                    X_new[j, :] = GBestX * (1 - i / Max_iter) + (np.mean(X[j, :]) - GBestX) * np.floor(np.random.rand() / jump_factor) * jump_factor + 0.2 * (1 - i / Max_iter) * (X[j, :] - GBestX) * Levy(dim)
                else:
                    # Human development stage
                    if j < LNNumber:  # Leaders
                        if R < A:
                            X_new[j, :] = 0.2 * np.cos(np.pi / 2 * (1 - (i / Max_iter))) * X[j, :] * np.exp((-i * np.random.randn()) / (np.random.rand() * Max_iter))
                        else:
                            X_new[j, :] = 0.2 * np.cos(np.pi / 2 * (1 - (i / Max_iter))) * X[j, :] + np.random.randn() * np.ones(dim)
                    elif j < LNNumber + ENNumber:  # Explorers
                        X_new[j, :] = np.random.randn() * np.exp((X[-1, :] - X[j, :]) / (j**2))
                    elif j < LNNumber + ENNumber + FNNumber:  # Followers
                        X_new[j, :] = X[j, :] + 0.2 * np.cos(np.pi / 2 * (1 - (i / Max_iter))) * np.random.rand(dim) * (X[0, :] - X[j, :])
                    else:  # Losers
                        X_new[j, :] = GBestX + (GBestX - X[j, :]) * np.random.randn()

            # Boundary control
            if isinstance(lb, (int, float)):
                X_new = np.clip(X_new, lb, ub)
            else:
                for j in range(dim):
                    X_new[:, j] = np.clip(X_new[:, j], lb[j], ub[j])

            # Fitness evaluation
            fitness_new = np.array([objf(X_new[k, :]) for k in range(N)])

            # Update positions and fitness
            better_indices = fitness_new < fitness
            X[better_indices] = X_new[better_indices]
            fitness[better_indices] = fitness_new[better_indices]

            # Update the global best
            min_idx = np.argmin(fitness)
            if fitness[min_idx] < GBestF:
                GBestF = fitness[min_idx]
                GBestX = X[min_idx, :]

        # End timer
        timerEnd = time.time()
        
        print("Optimization completed, preparing solution object...")
        
        # Updating solution object
        s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
        s.executionTime = timerEnd - timerStart
        s.convergence = Convergence_curve
        s.best = GBestF
        s.bestIndividual = GBestX
        
        print(f"Solution object created successfully with convergence length: {len(s.convergence)}")
        
        return s

    except Exception as e:
        print(f"Error occurred in HEOA: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        raise  # Hatayı yukarı fırlatıyoruz

def Levy(dim):
    """
    Levy flight strategy to update position in HEOA algorithm.
    """
    beta = 1.5
    sigma = (gamma(1 + beta) * np.sin(np.pi * beta / 2) / 
             (gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    u = np.random.randn(dim) * sigma
    v = np.random.randn(dim)
    step = u / np.abs(v) ** (1 / beta)
    return step


def initializationLogistic(N, dim, ub, lb):
    """
    Logistic chaotic mapping initialization for population.
    """
    positions = np.zeros((N, dim))
    for i in range(N):
        for j in range(dim):
            x0 = np.random.rand()
            a = 4
            x = a * x0 * (1 - x0)
            if isinstance(ub, (int, float)):
                positions[i, j] = (ub - lb) * x + lb
                positions[i, j] = np.clip(positions[i, j], lb, ub)
            else:
                positions[i, j] = (ub[j] - lb[j]) * x + lb[j]
                positions[i, j] = np.clip(positions[i, j], lb[j], ub[j])
            x0 = x
    return positions
