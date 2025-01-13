"""The original version of: HOA

 Created by Abdullah YILDIRIM on 13.01.2025 -----------------------------%
       Email: abdullahyldrm250@gmail.com                                 %
       Github: https://github.com/abdullahyildiri                        %
           --------------------------------------------------------------%
Links:
    1. [https://www.sciencedirect.com/science/article/pii/S0950705124005148]
    ## Referanslar
    Tobler, W. (1993). Three presentations on geographical analysis and modeling. National Center for Geographic Information and Analysis.

"""

import numpy as np
import random
from solution import solution
import time


def HOA(objf, lb, ub, dim, hiker, max_iter):
    # Initialize solution instance
    s = solution()

    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim

    # Pre-allocate variables
    fitness = np.zeros(hiker)
    pop = np.zeros((hiker, dim))
    for i in range(dim):
        pop[:, i] = np.random.uniform(0, 1, hiker) * (ub[i] - lb[i]) + lb[i]

    # Evaluate initial fitness
    for i in range(hiker):
        fitness[i] = objf(pop[i, :])

    g_best_score = np.min(fitness)
    g_best_pos = pop[np.argmin(fitness), :].copy()
    convergence_curve = np.zeros(max_iter)

    # Start optimization
    print(f"HOA is optimizing \"{objf.__name__}\"")
    start_time = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    for t in range(max_iter):
        for i in range(hiker):
            x_ini = pop[i, :]

            # Randomize elevation angle and slope
            theta = random.randint(0, 50)
            slope = np.tan(theta)

            # Generate sweep factor
            sf = random.choice([1,2,3,4])

            # Compute new velocity based on Tobler's Hiking Function
            velocity = 6 * np.exp(-3.5 * abs(slope + 0.05))
            new_velocity = velocity + np.random.rand(dim) * (g_best_pos - sf * x_ini)

            # Update position and apply bounds
            new_position = x_ini + new_velocity
            new_position = np.clip(new_position, lb, ub)

            # Evaluate new fitness
            f_new = objf(new_position)
            if f_new < fitness[i]:  # Greedy selection
                pop[i, :] = new_position
                fitness[i] = f_new

        # Update global best solution
        g_best_score = np.min(fitness)
        g_best_pos = pop[np.argmin(fitness), :].copy()

        convergence_curve[t] = g_best_score
        print(f"Iteration {t + 1}: Best Cost = {g_best_score}")

    # Store results in solution object
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = time.time() - start_time
    s.convergence = convergence_curve
    s.optimizer = "HOA"
    s.objfname = objf.__name__
    s.best = g_best_score
    s.bestIndividual = g_best_pos

    return s
