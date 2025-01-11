
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:50:25 2016

@author: hossam
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from optimizer import run  # DMOA optimizasyon algoritmasını çalıştırmak için run fonksiyonu

# Optimizasyon algoritması listesi (DMOA algoritması seçildi)
optimizer = ["DMOA"]

# Test fonksiyonları (benchmark fonksiyonları)
objectivefunc = ["F8"]  # Sphere fonksiyonu gibi test fonksiyonları (örnek: F8)

# Her algoritma için deney sayısı (genelde istatistiksel analiz için 30 bağımsız koşu yapılır)
NumOfRuns = 3

# Genel parametreler (popülasyon boyutu, iterasyon sayısı, sınırlar)
params = {
    "PopulationSize": 30,  # Popülasyon büyüklüğü
    "Iterations": 500,  # Maksimum iterasyon sayısı
    "LowerBound": -500,  # Alt sınır (örnek F8 fonksiyonu için -500)
    "UpperBound": 500,  # Üst sınır (örnek F8 fonksiyonu için 500)
    "Dimensions": 30  # Problem boyutu (değişken sayısı)
}

# Sonuçların farklı formatlarda dışa aktarılması için ayarlar
export_flags = {
    "Export_avg": True,  # Ortalama sonuçları CSV dosyasına kaydet
    "Export_details": True,  # Ayrıntılı sonuçları kaydet
    "Export_convergence": True,  # Yakınsama grafiği dışa aktarımı
    "Export_boxplot": True,  # Boxplot dışa aktarımı
}

# DMOA algoritmasını çalıştır
try:
    run(optimizer, objectivefunc, NumOfRuns, params, export_flags)
    print("DMOA algoritması başarıyla çalıştırıldı.")
except Exception as e:
    print(f"Algoritma çalıştırılırken hata oluştu: {e}")
=======
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:50:25 2016

@author: hossam
"""

from optimizer import run

# Select optimizers
# "SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS","HHO","SCA","JAYA","DE","MGO","EO","COA","ChOA"
#optimizer = ["SSA", "PSO", "GWO"]

optimizer = ["AAA","SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS","HHO","SCA","JAYA","DE","FDA","APO","COA","MPA","MGO","COAti","EO","ChOA"]



# Select benchmark function"
# "F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19"
# "Ca1","Ca2","Gt1","Mes","Mef","Sag","Tan","Ros"
objectivefunc = ["F12"]

# Select number of repetitions for each experiment.
# To obtain meaningful statistical results, usually 30 independent runs are executed for each algorithm.
NumOfRuns = 1

# Select general parameters for all optimizers (population size, number of iterations) ....
params = {"PopulationSize": 30, "Iterations": 500}

# Choose whether to Export the results in different formats
export_flags = {
    "Export_avg": True,
    "Export_details": True,
    "Export_convergence": True,
    "Export_boxplot": True,
}

run(optimizer, objectivefunc, NumOfRuns, params, export_flags)

