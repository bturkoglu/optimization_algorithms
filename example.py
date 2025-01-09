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
