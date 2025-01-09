#The original version of: [DMOA]

# Created by "[Çağan Barkın Üstüner]" on [08.01.25] -----------------------------%
#       Email: [cbarkinustuner@gmail.com]                                %
#       Github: https://github.com/brkn2274             %
# --------------------------------------------------------------%

#Links:
 #   1. [https://www.mathworks.com/matlabcentral/fileexchange/105125-dwarf-mongoose-optimization-algorithm?utm_source=chatg]
#References:
 #   [1] [https://ww2.mathworks.cn/matlabcentral/fileexchange/127309-improved-dwarf-mongoose-optimization-algorithm/?s_tid=mlc_lp_leafı]
import numpy as np

def roulette_wheel_selection(P):
    """Roulette Wheel Selection for probabilities."""
    r = np.random.rand()
    C = np.cumsum(P)
    i = np.where(r <= C)[0][0]
    return i

def DMOA(nPop, MaxIt, VarMin, VarMax, nVar, F_obj):
    """
     Dwarf Mongoose Optimization Algorithm (DMOA)

     Parameters:
         nPop: int - Population size.
         MaxIt: int - Maximum number of iterations.
         VarMin: float - Lower bound of variables.
         VarMax: float - Upper bound of variables.
         nVar: int - Number of variables.
         F_obj: function - Objective function to minimize.

     Returns:
         BEF: float - Best fitness value found.
         BEP: array - Best solution position.
         BestCost: list - Convergence of best fitness values over iterations.
     """
    # Validate Parameters
    if nPop <= 0:
        raise ValueError("Population size (nPop) must be greater than 0.")
    if MaxIt <= 0:
        raise ValueError("Maximum iterations (MaxIt) must be greater than 0.")
    if VarMin >= VarMax:
        raise ValueError("VarMin must be less than VarMax.")
    if nVar <= 0:
        raise ValueError("Number of variables (nVar) must be greater than 0.")

    # Initialize Parameters
    VarSize = (nVar,)
    nBabysitter = 3
    nAlphaGroup = nPop - nBabysitter
    nScout = nAlphaGroup
    L = round(0.6 * nVar * nBabysitter)  # Babysitter exchange parameter
    peep = 2  # Alpha female's vocalization coefficient

    # Initialize Population
    pop = [{'Position': np.random.uniform(VarMin, VarMax, VarSize), 'Cost': np.inf} for _ in range(nAlphaGroup)]
    for individual in pop:
        individual['Cost'] = F_obj(individual['Position'])

    # Best Solution Ever Found
    BestSol = min(pop, key=lambda x: x['Cost'])
    tau = np.inf  # Initialize tau for scout adaptation
    sm = np.full(nAlphaGroup, np.inf)  # Initialize sleeping mound differences

    # Abandonment Counter
    C = np.zeros(nAlphaGroup)
    CF = (1 - 1 / MaxIt) ** (2 / MaxIt)  # Adaptation factor

    # Convergence Curve
    BestCost = []

    # Main Loop
    for it in range(MaxIt):
        # Alpha Group
        MeanCost = np.mean([ind['Cost'] for ind in pop])
        F = np.exp(-np.array([ind['Cost'] for ind in pop]) / (MeanCost + 1e-9))  # Avoid division by zero
        P = F / np.sum(F)

        for m in range(nAlphaGroup):
            i = roulette_wheel_selection(P)
            K = [k for k in range(nAlphaGroup) if k != i]
            k = np.random.choice(K)
            phi = (peep / 2) * np.random.uniform(-1, 1, VarSize)
            new_position = pop[i]['Position'] + phi * (pop[i]['Position'] - pop[k]['Position'])
            new_cost = F_obj(new_position)

            if new_cost <= pop[i]['Cost']:
                pop[i]['Position'], pop[i]['Cost'] = new_position, new_cost
            else:
                C[i] += 1

        # Scout Group
        for i in range(nScout):
            K = [k for k in range(nAlphaGroup) if k != i]
            k = np.random.choice(K)
            phi = (peep / 2) * np.random.uniform(-1, 1, VarSize)
            new_position = pop[i]['Position'] + phi * (pop[i]['Position'] - pop[k]['Position'])
            new_cost = F_obj(new_position)
            sm[i] = (new_cost - pop[i]['Cost']) / max(new_cost, pop[i]['Cost'])

            if new_cost <= pop[i]['Cost']:
                pop[i]['Position'], pop[i]['Cost'] = new_position, new_cost
            else:
                C[i] += 1

        # Babysitters
        for i in range(min(nBabysitter, nAlphaGroup)):  # Prevent out-of-bound errors
            if C[i] >= L:
                pop[i]['Position'] = np.random.uniform(VarMin, VarMax, VarSize)
                pop[i]['Cost'] = F_obj(pop[i]['Position'])
                C[i] = 0

        # Update Best Solution
        for ind in pop:
            if ind['Cost'] < BestSol['Cost']:
                BestSol = ind

        # Next Mongoose Position
        newtau = np.mean(sm)
        for i in range(nScout):
            M = pop[i]['Position'] * sm[i] / (pop[i]['Position'] + 1e-9)  # Avoid division by zero
            if newtau > tau:
                pop[i]['Position'] -= CF * phi * np.random.rand() * (pop[i]['Position'] - M)
            else:
                pop[i]['Position'] += CF * phi * np.random.rand() * (pop[i]['Position'] - M)
        tau = newtau

        # Store Best Cost
        BestCost.append(BestSol['Cost'])
        print(f"Iteration {it + 1}: Best Cost = {BestSol['Cost']}")

    return BestSol['Cost'], BestSol['Position'], BestCost

# Example Usage
if __name__ == "__main__":
    def sphere(x):
        return np.sum(x ** 2)

    nPop = 50
    MaxIt = 100
    VarMin = -10
    VarMax = 10
    nVar = 5

    BEF, BEP, BestCost = DMOA(nPop, MaxIt, VarMin, VarMax, nVar, sphere)
    print(f"Best Fitness Found: {BEF}")
    print(f"Best Position Found: {BEP}")


def optimizers():
    return None
