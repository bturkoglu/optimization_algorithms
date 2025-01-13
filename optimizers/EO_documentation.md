# Equilibrium Optimizer (EO) Algoritması Dokümantasyonu

## Giriş
Equilibrium Optimizer (EO), 2020 yılında Faramarzi ve arkadaşları tarafından önerilen, denge kontrol hacmi kavramına dayanan popülasyon tabanlı bir meta-sezgisel optimizasyon algoritmasıdır. Algoritma, parçacıkların denge durumuna ulaşma sürecini taklit eder.

## Temel Özellikler
- **Denge Durumları**: Algoritma 4 farklı denge durumu (ceq1, ceq2, ceq3, ceq4) ve bunların ortalamasını (ceq_ave) kullanır
- **Dinamik Parametreler**: 
  - V_max: Maksimum hız (1 olarak sabitlenmiş)
  - a₁: Keşif parametresi (2 olarak sabitlenmiş) 
  - a₂: Sömürü parametresi (1 olarak sabitlenmiş)
  - GP: Global havuz oranı (0.5 olarak sabitlenmiş)

## Konum Güncelleme Denklemleri
EO algoritmasında parçacıkların konumları şu ana denklemlerle güncellenir:

$\vec{X} = \vec{X}_{eq} + (\vec{X} - \vec{X}_{eq})F + \frac{\vec{G}}{\lambda V_{max}}(1-F)$

Burada:
- $\vec{X}_{eq}$: Seçilen denge durumu
- $F = a_1 \cdot sign(r-0.5)(e^{-\lambda t}-1)$: Üstel azalma faktörü 
- $\vec{G} = G_0F$: Üretilen G vektörü
- $G_0 = GCP(X_{eq} - \lambda\vec{X})$: Başlangıç G vektörü
- $\lambda$: Rastgele üretilen kontrol parametresi
- $t = (1-\frac{l}{T})^{a_2\frac{l}{T}}$: Zaman fonksiyonu

## Keşif ve Sömürü Mekanizmaları

1. **Keşif (Exploration)**:
   - Erken iterasyonlarda F değeri büyük olduğundan, parçacıklar geniş arama yapar
   - a₁ parametresi keşif yeteneğini kontrol eder
   - F fonksiyonu: $F = a_1 \cdot sign(r-0.5)(e^{-\lambda t}-1)$

2. **Sömürü (Exploitation)**:
   - İterasyonlar ilerledikçe t değeri küçülür ve F azalır
   - a₂ parametresi sömürü dengesini ayarlar
   - Zaman fonksiyonu: $t = (1-\frac{l}{T})^{a_2\frac{l}{T}}$

## Referanslar
1. Faramarzi, A., Heidarinejad, M., Stephens, B., & Mirjalili, S. (2020). Equilibrium optimizer: A novel optimization algorithm. Knowledge-Based Systems, 191, 105190. DOI: 10.1016/j.knosys.2019.105190
