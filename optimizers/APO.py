# Created by "[Baran Bingöl]" on [29.12.2024] ------------------%
#       Email: [baranbingol212121@gmail.com]                    %
#       Github: https://github.com/baranbingol1                 %
# --------------------------------------------------------------%

# Links:
#     1. https://www.sciencedirect.com/science/article/pii/S0950705124003721
# References:
#     [1] Wang, X., Snášel, V., Mirjalili, S., Pan, J.-S., Kong, L., & Shehadeh, H. A. (2024). 
#         Artificial Protozoa Optimizer (APO): A novel bio-inspired metaheuristic algorithm for engineering optimization. 
#         Knowledge-Based Systems, 295, 111737. https://doi.org/10.1016/j.knosys.2024.111737
import numpy as np
import time
from solution import solution

def APO(objf, lb, ub, dim, SearchAgents_no, Max_iter):

    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim
        
    # algorithm parameters
    ps = SearchAgents_no  # protozoa size
    np_val = 1  # neighbor pairs
    pf_max = 0.1  # proportion fraction maximum
    
    protozoa = np.zeros((ps, dim))
    new_protozoa = np.zeros((ps, dim))
    epn = np.zeros((np_val, dim))  # effect of paired neighbors
    
    for i in range(ps):
        protozoa[i, :] = np.random.uniform(lb, ub, dim)
    
    s = solution()
    print('APO is optimizing  "' + objf.__name__ + '"')
    timer_start = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # find initials
    protozoa_fit = np.array([objf(p) for p in protozoa])
    best_idx = np.argmin(protozoa_fit)
    best_protozoa = protozoa[best_idx].copy()
    best_fit = protozoa_fit[best_idx]
    convergence_curve = np.zeros(Max_iter)
    convergence_curve[0] = best_fit
    
    # main loop
    for iter in range(1, Max_iter):
        # sort protozoa by fitness
        sort_idx = np.argsort(protozoa_fit)
        protozoa = protozoa[sort_idx]
        protozoa_fit = protozoa_fit[sort_idx]
        
        # proportion fraction
        pf = pf_max * np.random.random()
        ri = np.random.permutation(ps)[:int(np.ceil(ps * pf))]
        
        for i in range(ps):
            if i in ri:  # dormancy or reproduction form
                pdr = 0.5 * (1 + np.cos((1 - i/ps) * np.pi))  # probability
                
                if np.random.random() < pdr:  # dormancy form
                    new_protozoa[i] = np.random.uniform(lb, ub, dim)
                else:  # reproduction form
                    flag = np.random.choice([-1, 1])
                    mr = np.zeros(dim)
                    mr[np.random.permutation(dim)[:int(np.ceil(np.random.random() * dim))]] = 1
                    new_protozoa[i] = protozoa[i] + flag * np.random.random() * (
                        np.random.uniform(lb, ub, dim)) * mr
            
            else:  # foraging form
                f = np.random.random() * (1 + np.cos(iter/Max_iter * np.pi))
                mf = np.zeros(dim)
                mf[np.random.permutation(dim)[:int(np.ceil(dim * i/ps))]] = 1
                pah = 0.5 * (1 + np.cos(iter/Max_iter * np.pi))
                
                if np.random.random() < pah:  # autotroph form
                    j = np.random.randint(ps)
                    for k in range(np_val):
                        if i == 0:
                            km, kp = i, i + np.random.randint(1, ps)
                        elif i == ps-1:
                            km, kp = np.random.randint(ps-1), i
                        else:
                            km = np.random.randint(i)
                            kp = i + np.random.randint(1, ps-i)
                        
                        wa = np.exp(-abs(protozoa_fit[km]/(protozoa_fit[kp] + np.finfo(float).eps)))
                        epn[k] = wa * (protozoa[km] - protozoa[kp])
                    
                    new_protozoa[i] = protozoa[i] + f * (
                        protozoa[j] - protozoa[i] + np.mean(epn, axis=0)) * mf
                
                else:  # heterotroph form
                    for k in range(np_val):
                        if i == 0:
                            imk, ipk = i, i + k
                        elif i == ps-1:
                            imk, ipk = ps-1-k, i
                        else:
                            imk, ipk = i-k, i+k
                        
                        imk = max(0, min(imk, ps-1))
                        ipk = max(0, min(ipk, ps-1))
                        
                        wh = np.exp(-abs(protozoa_fit[imk]/(protozoa_fit[ipk] + np.finfo(float).eps)))
                        epn[k] = wh * (protozoa[imk] - protozoa[ipk])
                    
                    flag = np.random.choice([-1, 1])
                    x_near = (1 + flag * np.random.random(dim) * (1 - iter/Max_iter)) * protozoa[i]
                    new_protozoa[i] = protozoa[i] + f * (
                        x_near - protozoa[i] + np.mean(epn, axis=0)) * mf
        
        # bound constraint handling
        new_protozoa = np.clip(new_protozoa, lb, ub)
        
        # evaluate new positions
        new_protozoa_fit = np.array([objf(p) for p in new_protozoa])
        
        # selection
        improve_idx = new_protozoa_fit < protozoa_fit
        protozoa[improve_idx] = new_protozoa[improve_idx]
        protozoa_fit[improve_idx] = new_protozoa_fit[improve_idx]
        
        # update best
        best_idx = np.argmin(protozoa_fit)
        if protozoa_fit[best_idx] < best_fit:
            best_fit = protozoa_fit[best_idx]
            best_protozoa = protozoa[best_idx].copy()
        
        convergence_curve[iter] = best_fit
        
        if iter % 1 == 0:
            print(["At iteration " + str(iter) + " the best fitness is " + str(best_fit)])
    
    timer_end = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timer_end - timer_start
    s.convergence = convergence_curve
    s.optimizer = "APO"
    s.objfname = objf.__name__
    s.best = best_fit
    s.bestIndividual = best_protozoa
    
    return s