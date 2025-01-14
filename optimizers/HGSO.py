# Algoritma Adı: HGSO (Henry Gaz Çözünürlüğü Optimizasyonu )
#
# Created by "Serpil Umay Gedikli" on 14.01.2025 --------------------%
#       Email: srplgdkl@gmail.com                                 %
#       Github: https://github.com/SerpilUmayGedikli/optimization_algorithms  %
# --------------------------------------------------------------%
#
# Links:
#    Links:
#    1. https://www.sciencedirect.com/science/article/abs/pii/S0167739X19306557#:~:text=Henry's%20law%20is%20an%20essential,space%20and%20avoid%20local%20optima
#
# References:
#    [1] Author(s), (Year). Title of the article. *Journal Name*, Volume(Issue), Page Range. DOI/Link
#

import numpy as np
import time
from solution import solution

def HGSO(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    # Parametreler
    T_θ = 298.15  # Başlangıç sıcaklığı (Kelvin cinsinden)
    azalma = 0.05  # Sıcaklık azalması
    C = 0.1  # Sıcaklık bağımlı sabit
    H = 0.1  # Henry sabiti
    T = T_θ  # Başlangıç sıcaklığı
    ps = SearchAgents_no  # Protozoa sayısı (ajans sayısı)
    
    # Protozoa ve en iyi çözüm için başlangıçlar
    protozoa = np.random.uniform(lb, ub, (ps, dim))
    best_protozoa = protozoa[0, :]
    best_fit = np.inf  # İlk en iyi fitness değeri çok yüksek
    convergence_curve = np.zeros(Max_iter)
    
    # Çözüm objesi
    s = solution()
    print('HGSO is optimizing "' + objf.__name__ + '"')
    
    # Başlangıç zamanlayıcısı
    timer_start = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Başlangıç fitness hesaplaması
    protozoa_fit = np.array([objf(p) for p in protozoa])
    best_idx = np.argmin(protozoa_fit)
    best_protozoa = protozoa[best_idx].copy()
    best_fit = protozoa_fit[best_idx]
    convergence_curve[0] = best_fit
    
    # Ana döngü (iterasyonlar)
    for iter in range(1, Max_iter):
        # Sıcaklık ve Henry sabiti güncellemeleri
        T = T_θ * np.exp(-azalma * iter)
        H = H * np.exp(-C * (1/T - 1/T_θ))
        
        # Protozoa pozisyon güncellemeleri (arama adımları)
        for i in range(ps):
            # Keşif (Exploration) ve Sömürü (Exploitation) mekanizmaları
            r = np.random.random()  # Rastgelelik faktörü
            if r < 0.5:  # Keşif
                protozoa[i] = np.random.uniform(lb, ub, dim)
            else:  # Sömürü
                protozoa[i] = best_protozoa + r * (protozoa[i] - best_protozoa)
            
            # Çözünürlük etkisi
            fitness = objf(protozoa[i])
            protozoa_fit[i] = fitness
            
            # En iyi çözümü güncelleme
            if fitness < best_fit:
                best_fit = fitness
                best_protozoa = protozoa[i].copy()

        convergence_curve[iter] = best_fit
        
        # En iyi fitness her iterasyonda yazdırılır
        if iter % 10 == 0:
            print(f"At iteration {iter} the best fitness is {best_fit}")
    
    # Zamanlayıcı bitişi
    timer_end = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timer_end - timer_start
    s.convergence = convergence_curve
    s.optimizer = "HGSO"
    s.objfname = objf.__name__
    s.best = best_fit
    s.bestIndividual = best_protozoa
    
    return s
