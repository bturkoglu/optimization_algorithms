"""
The original version of: Cheetah Optimization

# Created by Zeynep Cahan on 19/12/2024 -----------------------%
#       Email: zeynepcahan8@gmail.com                          %
#       Github: https://github.com/zypchn                      %
# -------------------------------------------------------------%

Links:
    1. [https://www.nature.com/articles/s41598-022-14338-z]
References:
    [1] Akbari, M. A., Zare, M., Azizipanah-abarghooee, R., Mirjalili, S., Deriche, M.
    "The cheetah optimizer: a nature-inspired metaheuristic algorithm for large-scale optimization problems".
    https://doi.org/10.1038/s41598-022-14338-z
"""

import numpy as np
from solution import solution
import time

def CO(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    
    D = dim
    fobj = objf
    
    if (np.isscalar(lb)):
        ub = np.full(D, ub)     # Lower bound of decision variables
        lb = np.full(D, lb)     # Upper bound of decision variables
        
    n = SearchAgents_no     # Population size
    m = 2                   # Number of search agents in a group
    
    convergence_curve = np.zeros(Max_iter)
    
    # Generate initial population of cheetas
    empty_individual = {
        "Position": [],
        "Cost": []
    }
    best_sol = {
        "Position": [],
        "Cost": np.inf
    }
    pop = [empty_individual.copy() for _ in range(n)]
    
    for i in range(n):
        pop[i]["Position"] = lb + np.random.rand(D) * (ub - lb)
        pop[i]["Cost"] = fobj(pop[i]["Position"])
        if (pop[i]["Cost"] < best_sol["Cost"]):
            best_sol = pop[i].copy()    # Initial leader position
    
    
    # Initialization
    
    pop1 = pop.copy()               # Population's initial home position
    best_cost = []                  # Leader fittnes value in a current hunting period
    x_best = best_sol.copy()        # Prey solution sofar
    globest = best_cost.copy()      # Prey fittnes value sofar
    
    
    # Initial parameters
    
    t = 0                           # Hunting time counter
    it = 1                          # Iteration counter
    MaxIt = Max_iter                # Maximum number of iterations
    T = np.ceil(D / 10) * 60        # Hunting time
    FEs = 0                         # Counter for function evaluations
    
    
    s = solution()
    
    print(f"CO is optimizing {fobj.__name__}")
    
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # CO Main Loop
    
    while it <= MaxIt:
        i0 = np.random.choice(range(n), m, replace=False)       # Select a random memver of cheetas
        for k in range(m):
            i = i0[k]
            
            # Neighbor agent selection
            
            if (k == len(i0)-1):
                a = i0[k - 1]
            else:
                a = i0[k + 1]
                
            x = pop[i]["Position"]              # The current position of i-th cheetah
            x1 = pop[a]["Position"]             # The neighbor position
            xb = best_sol["Position"].copy()    # The leader position
            xbest = x_best["Position"].copy()   # The prey position
            
            kk = 0
            if (i <= 2 and t > 2 and t > np.ceil(0.2 * T + 1) and abs(best_cost[t - 2] - best_cost[t - int(np.ceil(0.2 * T + 1))]) <= 0.0001 * globest[t - 1]):
                x = x_best["Position"].copy()
                kk = 0
            elif (i == 3):
                x = best_sol["Position"].copy()
                kk = (-0.1) * np.random.rand() * t / T
            else:
                kk = 0.25

            if (it % 100 == 0 or it == 1):
                xd = np.random.permutation(len(x))
                
            z = x.copy()
            
            for j in xd:    # Select arbitrary set of arrangements
                r_hat = np.random.randn()   # Randomization parameter, Eq(1)
                r1 = np.random.rand()
                if (k == 1):     # The leader's step length (it is assumed that k==1 is associated to the leade number)
                    alpha = 0.0001 * t / T * (ub[j] - lb[j])    # Step length, Eq(1) [This can be updated by desired equation]
                else:            # The members' step length
                    alpha = 0.0001 * t / T * abs(xb[j] - x[j]) + 0.001 + int(np.random.rand() > 0.9)  # Step length, Eq(1) [This can be updated by desired equation]
                    
                r = np.random.randn()
                r_check = abs(r) ** np.exp(n / 2) * np.sin(2 * np.pi * r)     # turning factor, Eq(3) [This can be updated by desired equation]
                beta = x1[j] - x[j]     # Interaction factor, Eq(3)
                
                h0 = np.exp(2 - 2 * t / T) if T != 0 else np.exp(2)
                
                H = abs(2 * r1 * h0 - h0)
                
                r2 = np.random.rand()
                r3 = kk + np.random.rand()
                
                
                # Strategy selection mechanism
                
                if (r2 <= r3):
                    r4 = 3 * np.random.rand()
                    if (H > r4):
                        z[j] = x[j] + r_hat ** (-1) * alpha     # Search, Eq(1)
                    else:
                        z[j] = xbest[j] + r_check * beta        # Attack, Eq(3)
                else:
                    z[j] = x[j]     # Sit and wait, Eq(2)
            
            
            # Update the solutions of member i
            
            # Check the limits
            xx1 = np.where(z < lb)
            z[xx1] = lb[xx1] + np.random.rand(len(xx1)) * (ub[xx1] - lb[xx1])
            xx1 = np.where(z > lb)
            z[xx1] = lb[xx1] + np.random.rand(len(xx1)) * (ub[xx1] - lb[xx1])
            
            # Evaluate the new position
            new_sol = {
                "Position": z.copy(),
                "Cost": fobj(z.copy())
            }
            if (new_sol["Cost"] < pop[i]["Cost"]):
                pop[i] = new_sol.copy()
                if (pop[i]["Cost"] < best_sol["Cost"]):
                    best_sol = pop[i].copy()
            
            FEs = FEs + 1
        
        t = t + 1
        
        # Leave the prey and go back home
        
        if (t > T and t - int(T) - 1 >= 1 and t > 2):
            if (abs(best_cost[t-1] - best_cost[t - int(T) - 1])
                <= abs(0.01 * best_cost[t-1])):
                
                # Change the leader position
                best = x_best["Position"].copy()
                j0 = np.random.choice(D, int(np.ceil(D / 10 * np.random.rand())), replace=False)
                best[j0] = lb[j0] + np.random.rand(len(j0)) * (ub[j0] - lb[j0])
                best_sol["Cost"] = fobj(best)
                best_sol["Position"] = best.copy()  # Leader's new position
                FEs = FEs + 1
                
                # Go back home
                i0 = np.random.choice(range(n), int(n), replace=False)
                pop[i0[n - m:]] = pop1[i0[:m]].copy()   # Some members back to their initial positions
                
                pop[i] = x_best.copy()  # Substitude the member i by the prey
                
                t = 1   # Reset the hunting time
        
        convergence_curve[it-1] = x_best["Cost"]
        if t % 1 == 0:
            print(
                ["At iteration " + str(t) + " the best fitness is " + str(x_best["Cost"])]
            )
                
        it = it + 1
        
        
        # Update the prey (globat best)
        
        if (best_sol["Cost"] < x_best["Cost"]):
            x_best = best_sol.copy()
        
        best_cost.append(best_sol["Cost"].copy())
        globest.append(x_best["Cost"].copy())
        
        
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "Co"
    s.objfname = objf.__name__
    s.best = best_cost
    s.bestIndividual = best_sol["Position"]
    
    return s