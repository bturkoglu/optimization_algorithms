# APO (Artificial Protozoa Algorithm) Dokümantasyonu

## Giriş
Bu algoritma, protozaların (tek hücreli canlılar) yaşam döngülerini ilham alarak tasarlanmıştır. 2024 yılında X. Wang vd. tarafından geliştirilmiştir. Protozaların hayatta kalma stratejileri, besin arama davranışları ve üreme mekanizmalarını taklit ederek optimizasyon problemlerini çözmeyi amaçlar.

## Temel Özellikler
APO algoritması üç temel yaşam formu üzerine kuruludur:

1. Dinlenme Formu (Dormancy Form):
   - Protozoanın olumsuz koşullarda hayatta kalma stratejisi
   - Rastgele konumlara hareket ederek yeni alanları keşfetme
   - Küresel arama yeteneğini artırır

2. Üreme Formu (Reproduction Form):
   - İkiye bölünme yoluyla çoğalma davranışını simüle eder
   - Mevcut konumdan yeni konumlara kontrollü geçiş
   - Yerel arama kabiliyetini dengeler

3. Beslenme Formu (Foraging Form):
   - İki alt mekanizmadan oluşur:
     * Ototrof beslenme: Komşu protozaların etkileşiminden faydalanır
     * Heterotrof beslenme: Diğer protozaların konumlarını referans alır

## Konum Güncelleme Denklemleri

### Dinlenme Formu Denklemi:
```
newPosition = Xmin + rand * (Xmax - Xmin)
```
Burada:
- Xmin: Arama uzayının alt sınırı
- Xmax: Arama uzayının üst sınırı
- rand: 0-1 arası rastgele sayı

### Üreme Formu Denklemi:
```
newPosition = currentPosition + Flag * rand * (randomPosition) * Mr
```
Burada:
- Flag: +1 veya -1 rastgele yön katsayısı
- Mr: Hareket için rastgele seçilen boyutları belirleyen maske
- randomPosition: Arama uzayında rastgele bir konum

### Beslenme Formu Denklemleri:

Ototrof beslenme:
```
newPosition = currentPosition + f * (neighborPosition - currentPosition + effectOfPairedNeighbors) * Mf
```

Heterotrof beslenme:
```
newPosition = currentPosition + f * (Xnear - currentPosition + effectOfPairedNeighbors) * Mf
```

Burada:
- f: Beslenme faktörü
- Mf: Hareket için seçilen boyutları belirleyen maske
- effectOfPairedNeighbors: Komşu protozaların ağırlıklı etkisi

## Keşif ve Sömürü Mekanizmaları

1. Keşif (Exploration):
   - Dinlenme formu ile geniş arama uzayını keşfetme
   - Rastgele konumlandırma ile yeni bölgeleri araştırma
   - Yerel optimumlardan kaçınma yeteneği

2. Sömürü (Exploitation):
   - Üreme formu ile mevcut iyi çözümlerin etrafını araştırma
   - Beslenme formunda komşu etkileşimleri ile ince ayar
   - En iyi çözümlere yakınsama kontrolü

3. Denge Mekanizmaları:
   - İterasyon sayısına bağlı adaptif parametreler
   - Form seçiminde olasılık bazlı geçişler
   - Komşuluk etkilerinde ağırlıklı hesaplamalar

## Referanslar

Wang, X., Snášel, V., Mirjalili, S., Pan, J.-S., Kong, L., & Shehadeh, H. A. (2024). 
Artificial Protozoa Optimizer (APO): A novel bio-inspired metaheuristic algorithm for engineering optimization. 
Knowledge-Based Systems, 295, 111737. https://doi.org/10.1016/j.knosys.2024.111737