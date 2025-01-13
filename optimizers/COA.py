from solution import solution
import numpy as np
import time
import math

def initialization(N: int, dim: int, ub, lb):
    """Initialize population"""
    if isinstance(ub, (int, float)):
        X = np.random.uniform(0, 1, (N, dim)) * (ub - lb) + lb
    else:
        X = np.zeros((N, dim))
        for i in range(dim):
            X[:, i] = np.random.uniform(0, 1, N) * (ub[i] - lb[i]) + lb[i]
    return X

def p_obj(x):
    """Probability objective function (Eq. 4)"""
    return 0.2 * (1/(np.sqrt(2*np.pi)*3)) * np.exp(-(x-25)**2/(2*3**2))

def COA(objf, lb, ub, dim, SearchAgents_no, Max_iter):
   
    # Initialize variables for recording convergence
    s = solution()
    print('COA is optimizing "' + objf.__name__ + '"')
    
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Initialize convergence curve
    convergence_curve = np.zeros(Max_iter)
    
    # Initialize population
    X = initialization(SearchAgents_no, dim, ub, lb)
    fitness = np.zeros(SearchAgents_no)
    
    # Evaluate initial population
    for i in range(SearchAgents_no):
        fitness[i] = objf(X[i, :])
    
    # Find initial best solution
    best_fitness = np.min(fitness)
    best_idx = np.argmin(fitness)
    best_position = X[best_idx, :].copy()
    
    # Initialize tracking variables
    global_position = best_position.copy()
    global_fitness = best_fitness
    
    # Main loop
    for t in range(Max_iter):
        # Update control parameter (Eq. 7)
        C = 2 - (t/Max_iter)
        
        # Current temperature (Eq. 3)
        temp = np.random.rand() * 15 + 20
        
        # Calculate food position (Eq. 5)
        xf = (best_position + global_position) / 2
        Xfood = best_position.copy()
        
        Xnew = np.zeros((SearchAgents_no, dim))
        
        # Update each crayfish
        for i in range(SearchAgents_no):
            if temp > 30:  # Summer behavior
                if np.random.rand() < 0.5:
                    # Summer resort movement (Eq. 6)
                    Xnew[i, :] = X[i, :] + C * np.random.rand(dim) * (xf - X[i, :])
                else:
                    # Competition behavior (Eq. 8, 9)
                    for j in range(dim):
                        z = np.random.randint(0, SearchAgents_no)
                        Xnew[i, j] = X[i, j] - X[z, j] + xf[j]
            else:  # Temperature-dependent foraging
                # Calculate food size probability (Eq. 4)
                P = 3 * np.random.rand() * fitness[i] / objf(Xfood)
                
                if P > 2:  # Food is too big
                    # Adjust food size (Eq. 12)
                    Xfood = np.exp(-1/P) * Xfood
                    # Movement pattern for large food (Eq. 13)
                    for j in range(dim):
                        Xnew[i, j] = (X[i, j] + 
                                    np.cos(2*np.pi*np.random.rand()) * Xfood[j] * p_obj(temp) -
                                    np.sin(2*np.pi*np.random.rand()) * Xfood[j] * p_obj(temp))
                else:
                    # Movement pattern for small food (Eq. 14)
                    Xnew[i, :] = ((X[i, :] - Xfood) * p_obj(temp) + 
                                 p_obj(temp) * np.random.rand(dim) * X[i, :])
        
        # Boundary handling
        if isinstance(ub, (int, float)):
            Xnew = np.clip(Xnew, lb, ub)
        else:
            for i in range(SearchAgents_no):
                for j in range(dim):
                    Xnew[i, j] = np.clip(Xnew[i, j], lb[j], ub[j])
        
        # Update population
        for i in range(SearchAgents_no):
            new_fitness = objf(Xnew[i, :])
            
            if new_fitness < fitness[i]:
                X[i, :] = Xnew[i, :].copy()
                fitness[i] = new_fitness
                
                if fitness[i] < best_fitness:
                    best_fitness = fitness[i]
                    best_position = X[i, :].copy()
        
        # Update global best
        if best_fitness < global_fitness:
            global_fitness = best_fitness
            global_position = best_position.copy()
        
        # Store convergence history
        convergence_curve[t] = global_fitness
        
        if (t % 1 == 0):
            print(f'At iteration {t} the best fitness is {global_fitness}')
    
    # Record results
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "COA"
    s.objfname = objf.__name__
    s.best = global_fitness
    s.bestIndividual = global_position
    
    return s