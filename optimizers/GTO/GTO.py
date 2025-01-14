"""
   The original version of: GTO

   # Created by Edagül Akdeniz on 13.01.2025 --------------------------%
   #       Email: edagula40@gmail.com                                %
   #       Github: https://github.com/Edagla                        %
   # --------------------------------------------------------------%

   Links:
       1. https://onlinelibrary.wiley.com/doi/10.1002/int.22535
   References:
       [1] Benyamin Abdollahzadeh, Farhad Soleimanian Gharehchopogh. Artificial gorilla troops optimizer

   """
import random
import numpy as np
import math
from solution import solution
import time

#random şekilde popülasyon oluşturulur
def initialization(pop_size,dim,ub,lb):
    boundary_no=np.size(ub)
    X=np.zeros((pop_size,dim))
    if boundary_no==1:
        X=np.random.rand(pop_size,dim)*(ub-lb)+lb
    if boundary_no>1:
       for i in range (dim):
           ub_i=ub[i]
           lb_i=lb[i]
           X[:,i]=np.random.rand(pop_size)*(ub_i-lb_i)+lb_i
    
    return X

#boundary kontrolü yapılır
def boundary_check(X,lb,ub):
   
   lb = np.array(lb)
   ub = np.array(ub)

   X = np.clip(X, lb, ub)
   return X




def GTO(objf, lb, ub, dim, pop_size, max_iter):

    silverback=np.zeros(dim)
    silverback_Score=float('inf')

    X=initialization(pop_size,dim,ub,lb)

    pop_Fit=np.full(pop_size, float('inf'))
    convergence_curve=np.zeros((max_iter))
    s=solution()

    print('GTO is now tackling  "' + objf.__name__ + '"')

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    t = 0

    for i in range (1,pop_size):   
        pop_Fit[i]=objf(X[i,:])
        if pop_Fit[i]<silverback_Score :
            
            silverback_Score=pop_Fit[i]
            silverback=X[i,:].copy()

    GX = X.copy()

    #sabit parametreler tanımlanır    
    p=0.03
    Beta=3
    w=0.8

    for iter in range(max_iter):

        #formül 2 ve 4 kullanılarak a ve C değerleri hesaplanır  
        a=math.cos(2*random.random()+1)*(1-iter/max_iter)
        C=a*(2*random.random()-1) 

        for i in range(pop_size):
             #exploration aşaması
             #denklem 1 kullanılarak konum güncellemesi yapılır

                if random.random()<p:
                    GX[i,:]=(np.array(ub)-np.array(lb))*np.random.rand(dim)+np.array(lb)

                else:
                    if random.random()>=0.5:

                        Z = np.random.uniform(-a, a, dim)
                        H = Z * X[i, :]
                        random_index = np.random.randint(0, pop_size)
                        GX[i, :] = (np.random.random() - a) * X[random_index, :] + C * H
                    else:    
                        rand_idx = np.random.randint(0, pop_size)
                        rand_idx1 = np.random.randint(0, pop_size)
                        GX[i,:] = X[i,:] - C * (C * (X[i,:] - GX[rand_idx,:]) + 
                        np.random.random() * (X[i] - GX[rand_idx1]))
        
        GX = boundary_check(GX, lb, ub) 
        
        #fittness değerleri hesaplanır ve güncellenir
        #silverback değeri en iyiye göre güncellenir
        for i in range(pop_size):
            New_Fit = objf(GX[i])
            if New_Fit < pop_Fit[i]:
                pop_Fit[i] = New_Fit
                X[i] = GX[i].copy()
            if New_Fit < silverback_Score:
                silverback_Score = New_Fit
                silverback = GX[i].copy()
                      
        #exploitation aşaması
        for i in range(pop_size):
            if a >= w:
                g = 2**C
                delta = (np.abs(np.mean(GX, axis=0))**g)**(1/g)
                GX[i] = C * delta * (X[i] - silverback) + X[i]
            else:
                if np.random.random() >= 0.5:
                    h = np.random.randn(dim)
                else:
                    h = np.random.randn()
                r1 = np.random.random()
                GX[i] = silverback - (silverback*(2*r1-1) - X[i]*(2*r1-1)) * (Beta*h)
        
        GX = boundary_check(GX, lb, ub)
        
       
        #fittness değerleri hesaplanır ve güncellenir
        #silverback değeri en iyiye göre güncellenir
        for i in range(pop_size):
            New_Fit = objf(GX[i])
            if New_Fit < pop_Fit[i]:
                pop_Fit[i] = New_Fit
                X[i] = GX[i].copy()
            if New_Fit < silverback_Score:
                silverback_Score = New_Fit
                silverback = GX[i].copy()
      
        convergence_curve[iter]=silverback_Score
        if iter % 10 == 0:
            print(
                [ "At iteration "+ str(iter) +  " the best fitness is " + str(silverback_Score)]
            )
        t = t + 1
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "GTO"
    s.objfname = objf.__name__
    s.best = silverback_Score
    s.bestIndividual = silverback
    return s