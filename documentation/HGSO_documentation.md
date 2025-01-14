# Henry'nin Gaz Çözünürlüğü Optimizasyonu (HGSO)

## 1. Giriş
Henry'nin Gaz Çözünürlüğü Optimizasyonu (HGSO), gazların sıvılarda çözünürlüğünü tanımlayan **Henry Yasası**'ndan ilham alan bir meta-sezgisel optimizasyon algoritmasıdır. HGSO, gaz çözünürlüğünün sıcaklık ve basınca bağlı dinamik davranışını simüle ederek, karmaşık optimizasyon problemlerinde global ve yerel optimum çözümleri etkin bir şekilde bulmayı hedefler.  
Algoritma, **keşif (exploration)** ve **sömürü (exploitation)** mekanizmalarını dinamik bir şekilde dengeleyerek arama uzayında etkili bir çözüm süreci sunar.

---

## 2. Temel Özellikler

### Uyarlanabilir Keşif ve Sömürü Mekanizmaları
- **Keşif:** Çözünürlük ve rastgele hareketler sayesinde arama uzayının geniş bir bölgesi araştırılır.  
- **Sömürü:** En iyi bilinen çözüm çevresinde yoğun bir arama yapılarak çözüm hassasiyeti artırılır.

### Dinamik Parametre Güncellemeleri
- **Sıcaklık (T), Henry sabiti (H)** ve **çözünürlük (S)** her iterasyonda dinamik olarak güncellenir.

### Esneklik ve Ölçeklenebilirlik
- Algoritma, hem sürekli hem de ayrık optimizasyon problemlerine uygulanabilir ve kullanıcı tanımlı parametrelerle uyarlanabilir.

---

## 3. Matematiksel Modelleme

### Henry Yasası:
\[
S = H \cdot P
\]  
Burada:  
- \(S\): Gazın çözünürlüğü,  
- \(H\): Henry sabiti (gaz-sıvı kombinasyonuna özgü bir değerdir),  
- \(P\): Gazın kısmi basıncıdır.  

### Sıcaklık Dinamikleri:
Sıcaklık, keşif ve sömürü arasındaki dengeyi sağlamak için üstel bir şekilde azaltılır:
\[
T = T_\theta \cdot \exp{(-\text{azalma} \cdot \text{iterasyon})}
\]  
Burada:  
- \(T_\theta\): Başlangıç sıcaklığı (genellikle 298.15 K olarak tanımlanır).  

### Henry Sabiti Güncellemesi:
\[
H(t+1) = H(t) \cdot \exp{\left(-C \cdot \left(\frac{1}{T} - \frac{1}{T_\theta}\right)\right)}
\]  
Burada:  
- \(C\): Sıcaklık bağımlı sabit.

### Pozisyon Güncellemesi:
Ajanların pozisyonları çözünürlük etkisiyle güncellenir:
\[
X_i(t+1) = X_i(t) + r \cdot S \cdot (X_\text{en iyi} - X_i(t))
\]  
Burada:  
- \(X_i(t)\): \(t\)-inci iterasyonda ajan \(i\)’nin pozisyonu,  
- \(X_\text{en iyi}\): Şimdiye kadar bulunan en iyi çözüm,  
- \(r\): Rastgelelik faktörü (genellikle [0, 0.1] aralığında).

---

## 4. Keşif ve Sömürü Mekanizmaları

### Keşif:
- Henry sabiti (\(H\)) ve kısmi basınç (\(P\)), başlangıçta rastgele değerlerle atanır.  
- İlk iterasyonlarda sıcaklık (\(T\)) yüksek tutulur, böylece ajanlar geniş bir arama uzayını keşfedebilir.

### Sömürü:
- Sıcaklık azaldıkça çözünürlük (\(S\)) etkisi artar.  
- Ajanlar, en iyi bilinen çözüm çevresinde daha yoğun bir arama yaparak hassasiyeti artırır.

---

## 5. Parametreler

| Parametre                  | Açıklama                                  | Varsayılan Değer |
|----------------------------|-------------------------------------------|------------------|
| **Hedef Fonksiyon (\(f(x)\))** | Optimize edilecek fonksiyon              | Kullanıcı Tanımlı |
| **Alt Sınır (\(lb\))**       | Arama uzayının alt sınırı                 | Kullanıcı Tanımlı |
| **Üst Sınır (\(ub\))**       | Arama uzayının üst sınırı                 | Kullanıcı Tanımlı |
| **Boyut (\(dim\))**          | Problemin boyutu (değişken sayısı)        | Kullanıcı Tanımlı |
| **Popülasyon Boyutu (\(N\))**| Ajan sayısı                              | 30               |
| **Maksimum İterasyon (\(t_{max}\))** | Algoritmanın toplam iterasyon sayısı  | 100              |
| **Azalma Oranı (\(azalma\))** | Sıcaklık azalım oranı; keşif-sömürü dengesini kontrol eder | 0.01             |

---

## 6. Algoritmanın Çalışma Akışı

1. **Başlatma:**  
   - Ajanların pozisyonları rastgele atanır.  
   - Henry sabiti (\(H\)), kısmi basınç (\(P\)) ve sıcaklık bağımlı sabit (\(C\)) başlatılır.  
   
2. **İteratif Güncelleme:**  
   - Sıcaklık (\(T\)) güncellenir.  
   - Henry sabiti (\(H\)) güncellenir.  
   - Çözünürlük (\(S\)) hesaplanır.  
   - Ajanların pozisyonları en iyi çözüme doğru güncellenir.  

3. **Durdurma Kriteri:**  
   - Maksimum iterasyon sayısına (\(t_{max}\)) ulaşıldığında algoritma durdurulur.

---

## 7. Kullanım Örneği

```python
from optimization_algorithms.test_functions import sphere_function
from optimization_algorithms.optimizers.hgso import HGSO

# Problemin tanımlanması
hedef_fonk = sphere_function  # Test fonksiyonu
alt_sinir = -5.12  # Alt sınır
ust_sinir = 5.12  # Üst sınır
boyut = 30  # Problemin boyutu
pop_boyutu = 50  # Popülasyon boyutu
max_iterasyon = 100  # Maksimum iterasyon sayısı

# HGSO algoritmasını çalıştırma
hgso = HGSO(hedef_fonk, alt_sinir, ust_sinir, boyut, pop_boyutu, max_iterasyon)
en_iyi_cozum, en_iyi_skor = hgso.run()

print(f"En İyi Çözüm: {en_iyi_cozum}")
print(f"En İyi Skor: {en_iyi_skor}")
## 8. Avantajlar

- **Global Optimum Bulma**: Keşif ve sömürü arasındaki dengeyi sağlamak için sıcaklık ve çözünürlük mekanizmalarını dinamik olarak kullanır.
- **Esneklik**: Farklı optimizasyon problemlerine kolayca uyarlanabilir.
- **Verimlilik**: Hesaplama açısından verimli ve uygulanması kolaydır.

## 9. Kaynaklar

- William Henry, *Henry's Law*, 1803.
- Orijinal Yayın: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0167739X19306557)

