#The original version of: [Equilibrium Optimizer]

# Created by "Ege Kavak" on 08.01.2025 -----------------------------%
#       Email: ekavak2003@gmail.com                                 %
#       Github: https://github.com/EgeKavak1                        %
#-------------------------------------------------------------------%

#Links:
#    1. https://www.sciencedirect.com/science/article/pii/S0950705119305295
#References:
#    [1] 1. Faramarzi, A., Heidarinejad, M., Stephens, B., & Mirjalili, S. (2020).,
#    "Equilibrium optimizer: A novel optimization algorithm." *Knowledge-Based Systems*,
#    191, 105190. DOI: [10.1016/j.knosys.2019.105190](https://doi.org/10.1016/j.knosys.2019.105190).

import random
import numpy as np
from solution import solution
import time

def EO(objf, lb, ub, dim, PopSize, iters):
    """
    Equilibrium Optimizer (EO) implementation in Python.
    """

    # EO parameters
    Vmax = 1
    a1 = 2
    a2 = 1
    GP = 0.5

    s = solution()
    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim

    ######################## Initializations

    pos = np.zeros((PopSize, dim))
    for i in range(dim):
        pos[:, i] = np.random.uniform(0, 1, PopSize) * (ub[i] - lb[i]) + lb[i]

    fitness = np.full(PopSize, float("inf"))
    ceq1, ceq2, ceq3, ceq4 = np.zeros(dim), np.zeros(dim), np.zeros(dim), np.zeros(dim)
    ceq1_fit, ceq2_fit, ceq3_fit, ceq4_fit = float("inf"), float("inf"), float("inf"), float("inf")

    convergence_curve = np.zeros(iters)

    ############################################
    print('EO is optimizing  "' + objf.__name__ + '"')

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    for l in range(iters):
        for i in range(PopSize):
            pos[i, :] = np.clip(pos[i, :], lb, ub)

            # Calculate objective function for each particle
            fitness[i] = objf(pos[i, :])

            if fitness[i] < ceq1_fit:
                ceq1_fit = fitness[i]
                ceq1 = pos[i, :].copy()
            elif ceq1_fit < fitness[i] < ceq2_fit:
                ceq2_fit = fitness[i]
                ceq2 = pos[i, :].copy()
            elif ceq2_fit < fitness[i] < ceq3_fit:
                ceq3_fit = fitness[i]
                ceq3 = pos[i, :].copy()
            elif ceq3_fit < fitness[i] < ceq4_fit:
                ceq4_fit = fitness[i]
                ceq4 = pos[i, :].copy()

        ceq_ave = (ceq1 + ceq2 + ceq3 + ceq4) / 4
        c_pool = np.vstack([ceq1, ceq2, ceq3, ceq4, ceq_ave])

        t = (1 - l / iters) ** (a2 * l / iters)

        for i in range(PopSize):
            lambda_ = np.random.rand(dim)
            r = np.random.rand(dim)
            ceq = c_pool[np.random.randint(c_pool.shape[0]), :]
            f = a1 * np.sign(r - 0.5) * (np.exp(-lambda_ * t) - 1)
            r1, r2 = random.random(), random.random()
            gcp = 0.5 * r1 * np.ones(dim) * (r2 >= GP)
            g0 = gcp * (ceq - lambda_ * pos[i, :])
            g = g0 * f
            pos[i, :] = ceq + (pos[i, :] - ceq) * f + (g / (lambda_ * Vmax)) * (1 - f)

        convergence_curve[l] = ceq1_fit

        if l % 1 == 0:
            print(
                [
                    "At iteration "
                    + str(l + 1)
                    + " the best fitness is "
                    + str(ceq1_fit)
                ]
            )

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "EO"
    s.objfname = objf.__name__

    return s
