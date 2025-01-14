#The original version of: [Marine Predators Algorithm]

# Created by "[Bilge Göksel]" on [23.12.2024] -----------------------------%
#       Email: [bilgegoksell@gmail.com]                                %
#       Github: https://github.com/BilgeGoksel             %
# --------------------------------------------------------------%

#Links:
#    1. [https://www.sciencedirect.com/science/article/abs/pii/S0957417420302025]
#References:
#    [1] X. Zhun, Q. Heidari, A. Mirjalili, “Marine Predators Algorithm: A Nature-Inspired
#        Metaheuristic,” Expert Systems with Applications, 2020.


import numpy as np
from solution import solution
import time

# MPA - Marine Predators Algorithm
# objf: Objective function to minimize
# lb: Lower bounds of the search space
# ub: Upper bounds of the search space
# dim: Dimensionality of the problem
# PopSize: Number of agents (population size)
# Max_iter: Maximum number of iterations
def MPA(objf, lb, ub, dim, PopSize, Max_iter):
    if isinstance(ub, (int, float)):
        ub = np.full(dim, ub)
    if isinstance(lb, (int, float)):
        lb = np.full(dim, lb)
    Top_predator_pos = np.zeros(dim) #best solution position
    Top_predator_fit = float("inf") #best fitness value 
    Convergence_curve = np.zeros(Max_iter)
    stepsize = np.zeros((PopSize, dim))
    fitness = np.full(PopSize, float("inf"))

    Prey = initialize(PopSize, dim, ub, lb)

    Xmin = np.tile(lb, (PopSize, 1))
    Xmax = np.tile(ub, (PopSize, 1))

    # Algorithm parameters
    Iter = 0 # iteration counter
    FADs = 0.2 # probability of Fish Aggregating Devices effect
    P = 0.5 # scaling factor for movement prob

    s = solution()
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    while Iter < Max_iter:
        # Detecting top predator
        for i in range(PopSize):
            Prey[i, :] = np.clip(Prey[i, :], lb, ub)
            fitness[i] = objf(Prey[i, :])

            # update the top predator if a better solution is found
            if fitness[i] < Top_predator_fit:
                Top_predator_fit = fitness[i]
                Top_predator_pos = Prey[i, :].copy()

        # Marine Memory saving
        if Iter == 0:
            fit_old = fitness.copy()
            Prey_old = Prey.copy()

        Inx = fit_old < fitness
        Prey = np.where(Inx[:, None], Prey_old, Prey)
        fitness = np.where(Inx, fit_old, fitness)

        fit_old = fitness.copy()
        Prey_old = Prey.copy()

        Elite = np.tile(Top_predator_pos, (PopSize, 1))
        CF = (1 - Iter / Max_iter) ** (2 * Iter / Max_iter) # calculate convergence factor to control movement scale

        # Lévy flight and Brownian motion 
        RL = 0.05 * levy_flight(PopSize, dim, 1.5)  
        RB = np.random.randn(PopSize, dim)

        # update prey positions based on optimization phases
        for i in range(PopSize):
            R = np.random.rand()
            if Iter < Max_iter / 3:
                #Phase1:high exploration using Brownian motion
                stepsize[i, :] = RB[i, :] * (Elite[i, :] - RB[i, :] * Prey[i, :])
                Prey[i, :] += P * R * stepsize[i, :]
            elif Iter < 2 * Max_iter / 3:
                if i > PopSize / 2:
                    #Phase2:Brownian motion
                    stepsize[i, :] = RB[i, :] * (RB[i, :] * Elite[i, :] - Prey[i, :])
                    Prey[i, :] = Elite[i, :] + P * CF * stepsize[i, :]
                else:
                    #Phase2:Lévy flight
                    stepsize[i, :] = RL[i, :] * (Elite[i, :] - RL[i, :] * Prey[i, :])
                    Prey[i, :] += P * R * stepsize[i, :]
            else:
                # Phase3: high exploitation using Lévy flight
                stepsize[i, :] = RL[i, :] * (RL[i, :] * Elite[i, :] - Prey[i, :])
                Prey[i, :] = Elite[i, :] + P * CF * stepsize[i, :]

        # Detecting top predator again
        for i in range(PopSize):
            Prey[i, :] = np.clip(Prey[i, :], lb, ub)
            fitness[i] = objf(Prey[i, :])

            if fitness[i] < Top_predator_fit:
                Top_predator_fit = fitness[i]
                Top_predator_pos = Prey[i, :].copy()

        # Marine Memory saving
        Inx = fit_old < fitness
        Prey = np.where(Inx[:, None], Prey_old, Prey)
        fitness = np.where(Inx, fit_old, fitness)

        fit_old = fitness.copy()
        Prey_old = Prey.copy()

        # Eddy formation and FADs effect
        if np.random.rand() < FADs:
            U = np.random.rand(PopSize, dim) < FADs
            Prey += CF * ((Xmin + np.random.rand(PopSize, dim) * (Xmax - Xmin)) * U)
        else:
            r = np.random.rand() #random rearrangement of prey positions
            Rs = PopSize
            stepsize = (FADs * (1 - r) + r) * (Prey[np.random.permutation(Rs), :] - Prey[np.random.permutation(Rs), :])
            Prey += stepsize

        #print(f"At iteration {Iter + 1} the best fitness is {Top_predator_fit}")

        Iter += 1
        Convergence_curve[Iter - 1] = Top_predator_fit

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = Convergence_curve
    s.optimizer = "MPA"
    s.objfname = objf.__name__
    
    #print(f"\nThe best solution found is: {Top_predator_pos}")
    #print(f"The best fitness value is: {Top_predator_fit}")
    return s


# function to initialize population positions within given bounds
def initialize(SearchAgents_no, dim, ub, lb):
    Boundary_no = len(ub)

    if Boundary_no == 1:
        Positions = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb
    else:
        Positions = np.zeros((SearchAgents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            Positions[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

    return Positions


from scipy.special import gamma

# function to generate Lévy flight steps
def levy_flight(n, m, beta):
    #calculate the scale factor sigma_u for Lévy distribution
    num = gamma(1 + beta) * np.sin(np.pi * beta / 2)
    den = gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2)
    sigma_u = (num / den) ** (1 / beta)

    u = np.random.normal(0, sigma_u, (n, m)) #Lévy numerator (scaled normal distribution)
    v = np.random.normal(0, 1, (n, m)) #Lévy denominator (standard normal distribution)

    z = u / (np.abs(v) ** (1 / beta))# Lévy flight steps
    return z    

