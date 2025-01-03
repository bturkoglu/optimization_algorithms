# ChOA (Chimp Optimizasyon Algoritması) Dokümantasyonu

## Giriş
Chimp Optimizasyon Algoritması (ChOA), doğanın en zeki yaratıklarından biri olan şempanzelerin avlanma ve sosyal davranışlarından esinlenilerek geliştirilmiştir. 2025 yılında ortaya çıkan bu algoritma, şempanzelerin işbirlikçi ve uyumlu davranışlarını taklit ederek karmaşık optimizasyon problemlerini çözmeyi hedefler. Şempanzelerin doğadaki stratejik zekası, bu algoritmanın temelini oluşturur.

## Temel Özellikler
ChOA, şempanze topluluklarının avlanma sırasında üstlendikleri dört ana role dayanır. Bu roller, algoritmanın keşif ve sömürü dengesini kurmasına yardımcı olur:

1. **Saldırgan**:
   - Avı başlatan ve yöneten lider rolündedir.
   - Yeni alanları keşfederek potansiyel çözümleri belirler.
   - Saldırgan, grubun en cesur üyesi olarak, risk alarak yeni fırsatlar arar.

2. **Engelleyici**:
   - Saldırgana destek olarak kaçış yollarını kapatır.
   - Aramayı iyileştirir ve umut verici alanlara odaklanır.
   - Engelleyici, savunma ve stratejik planlamada ustadır.

3. **Kovalayıcı**:
   - Avı saldırgana doğru yönlendirmeye yardımcı olur.
   - Pozisyonları ayarlayarak keşif ve sömürü arasında denge kurar.
   - Kovalayıcı, hızlı ve çevik hareketleriyle avı yönlendirir.

4. **Sürücü**:
   - Grubu koordine eder ve stratejik uyumu sağlar.
   - Popülasyonu optimal çözümlere yönlendirerek yakınsamayı artırır.
   - Sürücü, grubun akıl hocası olarak, herkesin doğru yolda kalmasını sağlar.

## Konum Güncelleme Denklemleri
ChOA, her bir rolün katkısıyla konumları güncelleyerek çözüme ulaşır. İşte bu denklemler:

### Saldırgan Konum Denklemi:
```
D_Attacker = |C1 * Attacker_pos - m * Positions[i]|
X1 = Attacker_pos - A1 * D_Attacker
```
Burada:
- `C1`, `A1`: Keşif ve sömürü kontrol eden katsayılar.
- `m`: Mevcut iterasyona dayalı uyarlanabilir parametre.

### Engelleyici Konum Denklemi:
```
D_Barrier = |C2 * Barrier_pos - m * Positions[i]|
X2 = Barrier_pos - A2 * D_Barrier
```
Engelleyici, saldırganın başarısını garantilemek için stratejik pozisyon alır.

### Kovalayıcı Konum Denklemi:
```
D_Chaser = |C3 * Chaser_pos - m * Positions[i]|
X3 = Chaser_pos - A3 * D_Chaser
```
Kovalayıcı, avı doğru yöne yönlendirerek ekibin başarısını artırır.

### Sürücü Konum Denklemi:
```
D_Driver = |C4 * Driver_pos - m * Positions[i]|
X4 = Driver_pos - A4 * D_Driver
```
Sürücü, grubun genel stratejisini belirleyerek yakınsamayı hızlandırır.

## Keşif ve Sömürü Mekanizmaları
ChOA, keşif ve sömürü dengesini sağlamak için adaptif ağırlıklar kullanır. Her bir rol, belirli bir stratejiyle hareket ederek arama uzayını etkili bir şekilde keşfeder ve en iyi çözümleri sömürür. Saldırgan ve kovalayıcılar daha çok keşif yaparken, engelleyici ve sürücü daha çok sömürüye odaklanır.
## Referanslar ve Kaynaklar
Abualigah, L. M., Abd Elaziz, M., Sumari, P., Gandomi, A. H., Al-qaness, M. A., & Alsharif, M. H. (2021). Wind speed forecasting using optimal hybrid machine learning model: A case study of Malaysia. Expert Systems with Applications, 166, 114077. https://doi.org/10.1016/j.eswa.2020.114077