# **Coati Optimizasyon Algoritması (COA) Dokümantasyonu**

## **1. Giriş**
**Coati Optimizasyon Algoritması (COA)**, koatilerin sosyal davranışlarını modelleyen biyolojik ilhamlı bir optimizasyon algoritmasıdır. Bu algoritma, çok modlu ve doğrusal olmayan optimizasyon problemlerini çözmek için geliştirilmiştir. COA, küresel ve yerel arama süreçlerini dengelemek için keşif ve sömürü mekanizmalarını dinamik olarak uygular.

## **2. Temel Özellikler**
- **Dinamik Keşif ve Sömürü**: Küresel ve yerel arama süreçleri arasında geçiş yaparak hem çeşitliliği artırır hem de yakınsamayı hızlandırır.
- **İki Aşamalı Yapı**:
  - **Keşif Aşaması**: Yeni bölgeleri araştırarak küresel optimumu bulmaya odaklanır.
  - **Sömürü Aşaması**: Mevcut en iyi çözüm etrafında daha hassas bir arama yapar.
- **Uyarlanabilirlik**: Çeşitli optimizasyon problemlerine kolayca uyarlanabilir.

## **3. Konum Güncelleme Denklemleri**
Koatilerin hareketlerini simüle eden denklemler, algoritmanın keşif ve sömürü aşamalarında uygulanır.

### **3.1 Keşif Aşaması**
#### İlk Yarının Güncellenmesi (Eq. 4)
```python
iguana = best_pos  # Şu ana kadarki en iyi çözüm
I = round(1 + random.random())  # Rastgele yoğunluk faktörü (1 veya 2)

# Pozisyon güncelleme denklemi (Eq. 4)
X_P1 = Positions[i] + random.random() * (iguana - I * Positions[i])
X_P1 = np.clip(X_P1, lb, ub)  # Pozisyon sınırlarını kontrol et

# Eğer yeni çözüm daha iyiyse pozisyonu güncelle
new_fitness = objf(X_P1)
if new_fitness < fitness[i]:
    Positions[i] = X_P1
    fitness[i] = new_fitness
```

#### İkinci Yarının Güncellenmesi (Eq. 5 ve Eq. 6)
```python
iguana = lb + random.random() * (ub - lb)  # Rastgele hedef konumu (Eq. 5)
F_HL = objf(iguana)  # Rastgele hedefin uygunluğu
I = round(1 + random.random())

if fitness[i] > F_HL:  # Hedeften kötü olan pozisyonlar için
    X_P1 = Positions[i] + random.random() * (iguana - I * Positions[i])
else:  # Hedeften iyi olan pozisyonlar için
    X_P1 = Positions[i] + random.random() * (Positions[i] - iguana)

X_P1 = np.clip(X_P1, lb, ub)  # Pozisyon sınırlarını kontrol et

# Eğer yeni çözüm daha iyiyse pozisyonu güncelle
new_fitness = objf(X_P1)
if new_fitness < fitness[i]:
    Positions[i] = X_P1
    fitness[i] = new_fitness
```

### **3.2 Sömürü Aşaması**
#### Yerel Arama (Eq. 8, Eq. 9, Eq. 10 ve Eq. 11)
```python
LO_LOCAL = lb / (t + 1)  # Yerel alt sınır (Eq. 9)
HI_LOCAL = ub / (t + 1)  # Yerel üst sınır (Eq. 10)

# Yerel arama (Eq. 8)
X_P2 = Positions[i] + (1 - 2 * random.random()) * (LO_LOCAL + random.random() * (HI_LOCAL - LO_LOCAL))
X_P2 = np.clip(X_P2, LO_LOCAL, HI_LOCAL)  # Pozisyon sınırlarını kontrol et

# Eğer yeni çözüm daha iyiyse pozisyonu güncelle
new_fitness = objf(X_P2)
if new_fitness < fitness[i]:
    Positions[i] = X_P2
    fitness[i] = new_fitness
```

## **4. Keşif ve Sömürü Mekanizmaları**
### **4.1 Keşif Mekanizması**
- Popülasyonun bir kısmı, şimdiye kadar bulunan en iyi çözümü (iguana) takip eder.
- Rastgele pozisyonlarla yeni alanlar keşfedilir.

### **4.2 Sömürü Mekanizması**
- Yerel arama yapılarak mevcut en iyi çözüm etrafında daha hassas bir arama gerçekleştirilir.
- Yinelemeler ilerledikçe yerel arama sınırları daraltılır, bu da yakınsamayı hızlandırır.

## **5. Kaynakça**
1. **COA Makalesi**:
   - Başlık: "Coati Optimization Algorithm: A New Bio-Inspired Metaheuristic Algorithm for Solving Optimization Problems"
   - Yazarlar: Mohammad Dehghani, Zeinab Montazeri, Pavel Trojovský
   - Dergi: Knowledge-Based Systems, 2021.
   - DOI: [10.1016/j.knosys.2021.106926](https://www.sciencedirect.com/science/article/pii/S09507051210106926)

2. **Ek Kaynaklar**:
   - Dhiman G., SSC: "Mühendislik Uygulamaları için Hibrit Doğa İlhamlı Meta-Sezgisel Optimizasyon Algoritması". Knowledge-Based Systems, 2021.
   - DOI: [10.1016/j.knosys.2021.106926](https://www.sciencedirect.com/science/article/pii/S09507051210106926)
