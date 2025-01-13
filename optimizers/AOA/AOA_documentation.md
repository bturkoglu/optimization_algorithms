# Arithmetic Optimization Algorithm (AOA) Documentation

## Giriş
Arithmetic Optimization Algorithm (AOA), matematiksel aritmetik operatörlerin (Çarpma, Bölme, Çıkarma ve Toplama) dağılımsal davranışlarını kullanan bir meta-sezgisel optimizasyon algoritmasıdır. AOA, keşif (exploration) ve sömürü (exploitation) mekanizmalarını dengeleyerek optimizasyon problemlerini çözmek için tasarlanmıştır. Bu algoritma, rastgele çözümler oluşturarak belirli bir hedefe yönelik en iyi çözümü bulmaya çalışır.

Bu dokümantasyon, algoritmanın temel özelliklerini, konum güncelleme denklemlerini ve mekanizmalarını açıklamaktadır.

---

## Temel Özellikler
- **Popülasyon Tabanlı:** Birden fazla çözüm (popülasyon) üzerinde çalışır.
- **Keşif ve Sömürü Dengesi:** Çözümleri küresel ve yerel arama alanlarında dengeler.
- **Dinamik Parametreler:**  MOA (Math Optimizer Accelerated) ve MOP  (Math Optimizer Probability) gibi parametreler, keşif ve sömürü mekanizmalarının hassasiyetini kontrol eder.
- **Kısıtlar:** Algoritma, çözüm uzayında belirlenen alt ve üst sınırlar (LB,UB) arasında çalışır.
- **Statik Maliyet Fonksiyonu:** Kısıtları ihlal eden çözümler cezalandırılır ve bu çözümler optimizasyon sürecinde daha az tercih edilir.

---

## Konum Güncelleme Denklemleri
AOA, konum güncelleme denklemlerinde belirli parametreler kullanır bunların hesabı aşağıdaki gibidir :

MOA(Math Optimization Accelerated Function)(Current_Iter) = Min_Moa + Current_Iter * ((Max_Moa-Min_Moa)/M_Iter)
MOP(Mathematical Optimization Probability)(Current_Iter) = 1 - (Current_Iter / M_Iter) ** (1/α) 

AOA, çözümlerin konumlarını şu denklemlerle günceller:

### Keşif (Exploration) Mekanizması:
Keşif, küresel arama alanında geniş bir araştırma yapar. Konum güncellemeleri:
 if r1 >MOA 
    if r2 < 0.5
    xi,j(C Iter + 1)= best(x j) / (M O P + ϵ) * ((U Bj - L Bj) * µ + L Bj), r2 < 0.5
    else 
    xi,j(C Iter + 1)= best(x j) * M O P * ((U Bj - L Bj) * µ + L Bj)



### Sömürü (Exploitation) Mekanizması:
Sömürü, yerel arama alanında yoğunlaşarak en iyi çözüme yaklaşır:

 if r1 < MOA 
    if r3 < 0.5
    xi,j(C Iter + 1)= best(x j) - M O P * ((U Bj - L Bj) * µ + L Bj)
    else 
    xi,j(C Iter + 1)= best(x j) + M O P * ((U Bj - L Bj) * µ + L Bj),


- {best}(x_j): O ana kadarki en iyi çözümün j 'inci boyutundaki değeri.
-  MOA : Math Optimization Accelerated Function'dır 
-  MOP : Math Optimizer Probability, MOA ile ilişkilidir.
-  mu : Arama sürecini kontrol eden sabit bir parametre.(µ)
-   MOA(Math Optimization Accelerated Function)(Current_Iter) = Min_Moa + Current_Iter * ((Max_Moa-Min_Moa)/M_Iter)
-   MOP(Mathematical Optimization Probability)(Current_Iter) = 1 - (Current_Iter / M_Iter) ** (1/α)   
-   Her iterasyonda, MOA ve MOP değerleri dinamik olarak güncellenir:
---

## Keşif ve Sömürü Mekanizmaları
AOA, keşif ve sömürü mekanizmalarını şu şekilde dengeler:
1. **Keşif (Exploration):** Çözümler, küresel arama alanında farklı bölgelere yayılır. Bu süreçte r_1 > MOA  koşulu sağlanır. Çarpım ve bölüm işlemleri yüksek dağılımlı değerlere neden olduğu için keşif kısmında bu iki işlemin konum güncelleme denklemleri kullanılır. Lokal min'lerden kaçmak için bu işlemler daha çok iş görür
2. **Sömürü (Exploitation):** Çözümler, yerel arama alanında yoğunlaşarak mevcut en iyi çözüme yakın bir çözüm bulmaya çalışır. Bu süreçte  r_1 < MOA  koşulu sağlanır. Toplam ve Çıkarma işlemleri daha yoğun bir dağılım yani bir noktada yoğunlaştığı için bu işlemler bizim sömürü aşamamızda kullanılır.



---

## Referanslar
1. L. Abualigah, A. Diabat, S. Mirjalili, et al., "The Arithmetic Optimization Algorithm," *Comput. Methods Appl. Mech. Engrg.*, 2021.  
2. [MathWorks AOA Implementation](http://www.mathworks.com/matlabcentral/fileexchange/84742)

---

