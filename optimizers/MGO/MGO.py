# The original version of: MGO
#
# Created by "Ural Altan Bozkurt" on 30.12.2024 ----------------%
#       Email: uralaltan10 [at] gmail [dot] com                 %
#       Github: https://github.com/uralaltan                    %
# --------------------------------------------------------------%
#
# Links:
#     1. https://www.sciencedirect.com/science/article/pii/S0965997822001831
# References:
#     [1] Abdollahzadeh, B., Soleimanian Gharehchopogh, F., Khodadadi, N., & Mirjalili, S. (2022).
#     Mountain Gazelle Optimizer: A new Nature-inspired Metaheuristic Algorithm for Global Optimization Problems.
#     Advances in Engineering Software, 174, 103282. https://doi.org/10.1016/j.advengsoft.2022.103282

import numpy as np
import random
from solution import solution
import time

def MGO(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    
    def initialization(SearchAgents_no, dim, ub, lb):
        if not isinstance(lb, list):
            Positions = np.random.uniform(0, 1, (SearchAgents_no, dim)) * (ub - lb) + lb
        else:
            Positions = np.zeros((SearchAgents_no, dim))
            for i in range(dim):
                Positions[:, i] = np.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]
        return Positions

    def boundary_check(X, lb, ub):
        if not isinstance(lb, list):
            lb = [lb] * X.shape[1]
            ub = [ub] * X.shape[1]
        
        for i in range(X.shape[0]):
            FU = X[i, :] > ub
            FL = X[i, :] < lb
            X[i, :] = X[i, :] * (~(FU + FL)) + np.array(ub) * FU + np.array(lb) * FL
        return X

    def coefficient_vector(dim, Iter, MaxIter):
        a2 = -1 + Iter * (-1/MaxIter)
        u = np.random.normal(0, 1, dim)
        v = np.random.normal(0, 1, dim)
        
        cofi = np.zeros((4, dim))
        cofi[0, :] = np.random.rand(dim)
        cofi[1, :] = (a2 + 1) + np.random.rand()
        cofi[2, :] = a2 * np.random.normal(0, 1, dim)
        cofi[3, :] = u * v**2 * np.cos((np.random.rand()*2)*u)
        
        return cofi

    def solution_imp(X, BestX, lb, ub, N, cofi, M, A, D, i):
        NewX = np.zeros((4, X.shape[1]))
        
        NewX[0, :] = (ub - lb) * np.random.rand(X.shape[1]) + lb
        NewX[1, :] = BestX - abs((random.randint(1,2)*M - random.randint(1,2)*X[i, :])*A) * cofi[random.randint(0,3), :]
        NewX[2, :] = (M + cofi[random.randint(0,3), :]) + (random.randint(1,2)*BestX - random.randint(1,2)*X[random.randint(0,N-1), :]) * cofi[random.randint(0,3), :]
        NewX[3, :] = (X[i, :] - D) + (random.randint(1,2)*BestX - random.randint(1,2)*M) * cofi[random.randint(0,3), :]
        
        return NewX

    s = solution()
    
    X = initialization(SearchAgents_no, dim, ub, lb)
    
    BestX = np.zeros(dim)
    BestFitness = float('inf')
    
    Sol_Cost = np.zeros(SearchAgents_no)
    for i in range(SearchAgents_no):
        Sol_Cost[i] = objf(X[i, :])
        if Sol_Cost[i] < BestFitness:
            BestFitness = Sol_Cost[i]
            BestX = X[i, :].copy()
    
    convergence_curve = np.zeros(Max_iter)
    
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    print('MGO is optimizing "' + objf.__name__ + '"')
    
    for Iter in range(Max_iter):
        for i in range(SearchAgents_no):
            RandomSolution = np.random.permutation(SearchAgents_no)[:int(np.ceil(SearchAgents_no/3))]
            M = X[random.randint(int(np.ceil(SearchAgents_no/3)), SearchAgents_no-1), :] * np.floor(np.random.rand()) + \
                np.mean(X[RandomSolution, :], axis=0) * np.ceil(np.random.rand())
            
            cofi = coefficient_vector(dim, Iter, Max_iter)
            A = np.random.normal(0, 1, dim) * np.exp(2 - Iter*(2/Max_iter))
            D = (abs(X[i, :]) + abs(BestX)) * (2*np.random.rand() - 1)
            
            NewX = solution_imp(X, BestX, lb, ub, SearchAgents_no, cofi, M, A, D, i)
            NewX = boundary_check(NewX, lb, ub)
            
            Sol_CostNew = np.zeros(4)
            for j in range(4):
                Sol_CostNew[j] = objf(NewX[j, :])
            
            X = np.vstack((X, NewX))
            Sol_Cost = np.append(Sol_Cost, Sol_CostNew)
            
            if np.min(Sol_Cost) < BestFitness:
                BestFitness = np.min(Sol_Cost)
                BestX = X[np.argmin(Sol_Cost), :].copy()
        
        SortOrder = np.argsort(Sol_Cost)
        X = X[SortOrder]
        Sol_Cost = Sol_Cost[SortOrder]
        
        X = X[:SearchAgents_no]
        Sol_Cost = Sol_Cost[:SearchAgents_no]
        
        convergence_curve[Iter] = BestFitness
        
        if (Iter + 1) % 1 == 0:
            print(f"At iteration {Iter + 1} the best fitness is {BestFitness}")
    
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "MGO"
    s.objfname = objf.__name__
    s.best = BestFitness
    s.bestIndividual = BestX
    
    return s