# The original version of: Coati Optimization Algorithm [COA]
#
# Created by "Eriş Söylemez" on 01/01/2025 ------------%
#       Email: erssylmz12 [at] gmail [dot] com         %
#       Github: https://github.com/kekekekekkeke       %
# -----------------------------------------------------%
#
# Links:
#    1. https://www.sciencedirect.com/science/article/pii/S0950705122011042
# References:
#    [1] Dhiman G.
#    SSC: A hybrid nature-inspired meta-heuristic optimization algorithm for engineering applications 
#    Knowl.-Based Syst. (2021), Article 106926 https://www.sciencedirect.com/science/article/pii/S0950705121001891

import os
import sys

# Add the project root directory to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, PROJECT_ROOT)

from solution import solution
import numpy as np
import random

def COAti(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    """
    Coati Optimization Algorithm
    Parameters:
        objf: objective function to minimize
        lb: lower bounds for variables
        ub: upper bounds for variables
        dim: number of dimensions (variables)
        SearchAgents_no: number of search agents (population size)
        Max_iter: maximum number of iterations
    """
    # Initialize result object to store optimization results
    s = solution()
    
    # Convert scalar bounds to lists if necessary
    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim
    
    # Convert bounds to numpy arrays for vectorized operations
    lb = np.array(lb)
    ub = np.array(ub)
    
    # Initialize population: Positions matrix stores the current location of all search agents
    # Each row represents one agent, each column represents one dimension
    Positions = np.zeros((SearchAgents_no, dim))
    for i in range(dim):
        Positions[:, i] = lb[i] + np.random.random(SearchAgents_no) * (ub[i] - lb[i])
    
    # Track the convergence history over iterations
    convergence_curve = np.zeros(Max_iter)
    
    # Store fitness values for each search agent
    fitness = np.zeros(SearchAgents_no)
    for i in range(SearchAgents_no):
        fitness[i] = objf(Positions[i, :])
    
    # Main optimization loop
    for t in range(Max_iter):
        # Keep track of the best solution found so far
        best_idx = np.argmin(fitness)
        if t == 0:
            best_pos = Positions[best_idx].copy()    # Best position found
            best_score = fitness[best_idx]           # Best fitness score found
        elif fitness[best_idx] < best_score:
            best_score = fitness[best_idx]
            best_pos = Positions[best_idx].copy()

        # Phase 1: Hunting and attacking strategy (Exploration Phase)
        # First half of population follows the best solution (iguana)
        for i in range(SearchAgents_no // 2):
            iguana = best_pos                        # Target position (best known solution)
            I = round(1 + random.random())          # Random intensity factor (1 or 2)
            
            # Position update using hunting strategy (Eq. 4)
            X_P1 = Positions[i] + random.random() * (iguana - I * Positions[i])
            X_P1 = np.clip(X_P1, lb, ub)           # Ensure position stays within bounds
            
            # Update position if new solution is better (Eq. 7)
            new_fitness = objf(X_P1)
            if new_fitness < fitness[i]:
                Positions[i] = X_P1
                fitness[i] = new_fitness

        # Second half of population explores new random positions
        for i in range(SearchAgents_no // 2, SearchAgents_no):
            # Generate random target position (Eq. 5)
            iguana = lb + random.random() * (ub - lb)
            F_HL = objf(iguana)                     # Fitness of random target
            I = round(1 + random.random())
            
            # Position update based on fitness comparison (Eq. 6)
            if fitness[i] > F_HL:                   # If current position is worse than random target
                X_P1 = Positions[i] + random.random() * (iguana - I * Positions[i])
            else:                                   # If current position is better than random target
                X_P1 = Positions[i] + random.random() * (Positions[i] - iguana)
            X_P1 = np.clip(X_P1, lb, ub)
            
            # Update position if new solution is better (Eq. 7)
            new_fitness = objf(X_P1)
            if new_fitness < fitness[i]:
                Positions[i] = X_P1
                fitness[i] = new_fitness

        # Phase 2: The process of escaping from predators (Exploitation Phase)
        for i in range(SearchAgents_no):
            # Dynamic local search bounds that decrease with iterations (Eq. 9 and 10)
            LO_LOCAL = lb / (t + 1)                 # Lower bound for local search
            HI_LOCAL = ub / (t + 1)                 # Upper bound for local search
            
            # Local search around current position (Eq. 8)
            X_P2 = Positions[i] + (1 - 2 * random.random()) * (LO_LOCAL + random.random() * (HI_LOCAL - LO_LOCAL))
            X_P2 = np.clip(X_P2, LO_LOCAL, HI_LOCAL)
            
            # Update position if new solution is better (Eq. 11)
            new_fitness = objf(X_P2)
            if new_fitness < fitness[i]:
                Positions[i] = X_P2
                fitness[i] = new_fitness

        # Update convergence curve with best score of current iteration
        convergence_curve[t] = best_score
    
    # Prepare the solution object with final results
    s.convergence = convergence_curve
    s.optimizer = "COAti"
    s.objfname = objf.__name__
    s.best = best_score
    s.bestIndividual = best_pos
    
    return s