# Created by "[Mustafa Surhay Samsa]" on [2.01.2025] ------------------%
#       Email: [samsasurhay@gmail.com]                    %
#       Github: https://github.com/surhaysamsa                 %
# --------------------------------------------------------------%

# Links:
#     1. https://www.sciencedirect.com/science/article/abs/pii/S0957417420301639
# References:
#     [1] Abualigah, L. M., Abd Elaziz, M., Sumari, P., Gandomi, A. H., Al-qaness, M. A., & Alsharif, M. H. (2021). 
# Wind speed forecasting using optimal hybrid machine learning model: A case study of Malaysia. 
# Expert Systems with Applications, 166, 114077. https://doi.org/10.1016/j.eswa.2020.114077
from solution import solution
import numpy
import math
import time
import random

def ChOA(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    # Initialize positions and scores
    Attacker_pos = numpy.zeros(dim)
    Attacker_score = float('inf')
    Barrier_pos = numpy.zeros(dim)
    Barrier_score = float('inf')
    Chaser_pos = numpy.zeros(dim)
    Chaser_score = float('inf')
    Driver_pos = numpy.zeros(dim)
    Driver_score = float('inf')
    
    # Initialize search agents and their velocities
    Positions = numpy.random.uniform(0, 1, (SearchAgents_no, dim)) * (ub - lb) + lb
    Velocities = numpy.zeros((SearchAgents_no, dim))
    convergence_curve = numpy.zeros(Max_iter)
    
    s = solution()
    print('ChOA is optimizing "' + objf.__name__ + '"')
    
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Parameters
    w_start = 0.9  # starting inertia weight
    w_end = 0.4    # ending inertia weight
    c1 = 2.0       # cognitive coefficient
    c2 = 2.0       # social coefficient
    
    # Main loop
    for t in range(Max_iter):
        # Update inertia weight
        w = w_end + (w_start - w_end) * math.exp(-2 * (t/Max_iter))
        
        for i in range(SearchAgents_no):
            # Calculate objective function for each search agent
            fitness = objf(Positions[i])
            
            # Update Attacker, Barrier, Chaser, and Driver
            if fitness < Attacker_score:
                Attacker_score = fitness
                Attacker_pos = Positions[i].copy()
            elif fitness < Barrier_score:
                Barrier_score = fitness
                Barrier_pos = Positions[i].copy()
            elif fitness < Chaser_score:
                Chaser_score = fitness
                Chaser_pos = Positions[i].copy()
            elif fitness < Driver_score:
                Driver_score = fitness
                Driver_pos = Positions[i].copy()
        
        # Update the position of search agents
        a = 2 * math.exp(-4 * (t/Max_iter))  # Exponential decrease from 2 to ~0
        
        for i in range(SearchAgents_no):
            r1 = random.random()
            r2 = random.random()
            r3 = random.random()
            r4 = random.random()
            
            # Calculate attraction to the best positions
            A1 = 2 * a * r1 - a
            C1 = 2 * r2
            A2 = 2 * a * r2 - a
            C2 = 2 * r3
            A3 = 2 * a * r3 - a
            C3 = 2 * r4
            A4 = 2 * a * r4 - a
            C4 = 2 * r1
            
            # Adaptive parameter for position update
            m = 0.5 + 0.5 * math.exp(-t/Max_iter)
            
            # Calculate distances to the best positions
            D_Attacker = numpy.abs(C1 * Attacker_pos - m * Positions[i])
            D_Barrier = numpy.abs(C2 * Barrier_pos - m * Positions[i])
            D_Chaser = numpy.abs(C3 * Chaser_pos - m * Positions[i])
            D_Driver = numpy.abs(C4 * Driver_pos - m * Positions[i])
            
            # Calculate candidate positions
            X1 = Attacker_pos - A1 * D_Attacker
            X2 = Barrier_pos - A2 * D_Barrier
            X3 = Chaser_pos - A3 * D_Chaser
            X4 = Driver_pos - A4 * D_Driver
            
            # Adaptive weights based on current iteration
            prog = t/Max_iter
            w1 = 0.4 + 0.1 * math.exp(-prog)  # Attacker weight
            w2 = 0.3 + 0.1 * math.exp(-prog)  # Barrier weight
            w3 = 0.2 + 0.05 * math.exp(-prog)  # Chaser weight
            w4 = 0.1 + 0.05 * math.exp(-prog)  # Driver weight
            
            weights = numpy.array([w1, w2, w3, w4])
            weights = weights / numpy.sum(weights)  # Normalize weights
            
            new_pos = weights[0]*X1 + weights[1]*X2 + weights[2]*X3 + weights[3]*X4
            
            # Add small random movement for diversity
            if random.random() < 0.1:  # 10% chance
                new_pos += numpy.random.normal(0, 0.1 * math.exp(-2*prog), dim)
            
            # Update velocity using momentum
            Velocities[i] = w * Velocities[i] + \
                           c1 * random.random() * (new_pos - Positions[i]) + \
                           c2 * random.random() * (Attacker_pos - Positions[i])
            
            # Update position with velocity
            Positions[i] = numpy.clip(Positions[i] + 0.7 * Velocities[i], lb, ub)
        
        print(['At iteration ' + str(t) + ' the best fitness is ' + str(Attacker_score)])
        convergence_curve[t] = Attacker_score
    
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "ChOA"
    s.objfname = objf.__name__
    s.bestIndividual = Attacker_pos
    
    return s
