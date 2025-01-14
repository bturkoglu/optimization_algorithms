# Flow Direction Algorithm (FDA) - Documentation

## Giriş
Flow Direction Algorithm (FDA), optimizasyon problemlerini çözmek için geliştirilen bir meta-sezgisel algoritmadır. Algoritma, bir akışın hareketini simüle ederek hem global hem de lokal optimum çözümler arar. Keşif ve sömürü mekanizmalarını birleştirerek global optimum çözüme ulaşmayı hedefler.

FDA, mühendislik ve endüstri gibi farklı alanlardaki zorlu optimizasyon problemlerini çözmek için kullanılabilir. Akış yönlerini hedef fonksiyon eğimlerine göre günceller ve lokal optimal tuzaklardan kaçınmak için rastgele hareketler uygular.

---

## Temel Özellikler

1. **Global ve Lokal Arama Dengesi**:
   - FDA, iterasyonlar boyunca global ve lokal arama arasında denge sağlar.
   - Dinamik olarak güncellenen ağırlık faktörü \( W \), keşif ve sömürü arasındaki geçişi kontrol eder.

2. **Komşu Pozisyonların Oluşturulması**:
   - Her akışın çevresinde komşular oluşturulur.
   - Komşular, normal dağılım ve komşuluk yarıçapı (\( \Delta \)) ile hesaplanır.

3. **Eğim ve Hız Güncellemesi**:
   - Akış pozisyonları, eğim ve hız hesaplamalarına dayanarak güncellenir.

4. **Lokal Optimalden Kaçış Mekanizması**:
   - Rastgele yönlendirilmiş hareketler, algoritmanın lokal optimumdan kaçmasını sağlar.

---

## Konum Güncelleme Denklemleri

### 1. Komşu Pozisyonlarının Oluşturulması:
Komşular şu formülle hesaplanır:
Neighbor X(j) = Flow X(i) + randn * Δ

Burada:
- **Flow X(i)**: Akışın mevcut pozisyonu.
- **randn**: Ortalama 0 ve standart sapma 1 olan rastgele sayı.
- **Δ**: Komşuluk yarıçapı, şu şekilde hesaplanır:
Δ = (rand * Xrand - rand * Flow X(i)) * ||Best X - Flow X(i)|| * W


### 2. Eğim ve Hız Hesaplaması:
Eğim (\( S0 \)) şu şekilde hesaplanır:
S0 = (Flow fitness(i) - Neighbor fitness(j)) / ||Flow X(i) - Neighbor X(j)||

Hız (\( V \)) şu şekilde hesaplanır:
V = randn * S0


### 3. Yeni Pozisyonun Güncellenmesi:
Yeni pozisyon şu formülle güncellenir:
Flow newX(i) = Flow X(i) + V * (Flow X(i) - Neighbor X(j)) / ||Flow X(i) - Neighbor X(j)||


### 4. Akış Yönünün Simülasyonu:
Eğer başka bir akış (\( Flow X(r) \)) daha iyi bir fitness değerine sahipse:
Flow newX(i) = Flow X(i) + randn * (Flow X(r) - Flow X(i))

Aksi durumda:
Flow newX(i) = Flow X(i) + 2 * randn * (Best X - Flow X(i))


---

## Keşif ve Sömürü Mekanizmaları

1. **Keşif Mekanizması**:
   - FDA, başlangıç iterasyonlarında geniş bir çözüm alanını tarar.
   - Komşu pozisyonlar rastgele oluşturulur ve global aramayı destekleyen \( W \) faktörü yüksektir.

2. **Sömürü Mekanizması**:
   - İterasyonlar ilerledikçe \( W \) küçülür ve lokal arama odaklanır.
   - Akış pozisyonları en iyi komşu pozisyona doğru güncellenir.

3. **Dinamik Ağırlık Güncellemesi**:
Ağırlık faktörü (\( W \)) iterasyona bağlı olarak şu şekilde hesaplanır:
W = ((1 - iter / MaxIter)^(2 * rand)) * ((rand * iter) / MaxIter) * rand

Burada:
- **iter**: Mevcut iterasyon sayısı.
- **MaxIter**: Maksimum iterasyon sayısı.
- **rand**: [0, 1] aralığında rastgele bir sayı.

---

## Referanslar
1. Karami, H., Shoorehdeli, M. A., & Teshnehlab, M. (2021). Flow direction algorithm: A novel optimization approach for solving optimization problems. *Computers & Industrial Engineering, 156,* 107224. https://doi.org/10.1016/j.cie.2021.107224
