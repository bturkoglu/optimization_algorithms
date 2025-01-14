
# Henry'nin Gaz Çözünürlüğü Optimizasyonu (HGSO)

Bu proje, Henry Yasası'ndan esinlenerek geliştirilmiş bir meta-sezgisel optimizasyon algoritması olan **Henry'nin Gaz Çözünürlüğü Optimizasyonu (HGSO)** algoritmasını içerir. HGSO, gazların sıvılardaki çözünürlüğünü ve bu çözünürlüğün sıcaklık ile basınca bağlı davranışını simüle ederek karmaşık optimizasyon problemlerine çözüm sunmayı hedefler.

---

## 1. Giriş

Henry Yasası'na göre, bir gazın sıvı içindeki çözünürlüğü gazın kısmi basıncıyla doğru orantılıdır:

\[
S = H \cdot P
\]

- **S**: Gazın çözünürlüğü  
- **H**: Henry sabiti  
- **P**: Gazın kısmi basıncı  

HGSO, bu temel yasa doğrultusunda, optimizasyon problemleri için global ve yerel optimum çözümleri bulmak amacıyla tasarlanmıştır.

---

## 2. Özellikler

- **Keşif ve Sömürü Dengesi**: Algoritma, geniş bir arama uzayını keşfetme ve en iyi bilinen çözüm çevresinde yoğunlaşma arasında denge sağlar.  
- **Dinamik Güncellemeler**: Sıcaklık, Henry sabiti ve çözünürlük gibi parametreler her iterasyonda dinamik olarak güncellenir.  
- **Esneklik**: Sürekli ve ayrık optimizasyon problemlerinde uygulanabilir.  

---

## 3. Matematiksel Modelleme

### Henry Yasası  
\[
S = H \cdot P
\]

- **S**: Çözünürlük  
- **H**: Henry sabiti  
- **P**: Kısmi basınç  

### Sıcaklık Dinamikleri  
\[
T = T_\theta \cdot \exp{(-azalma \cdot iterasyon)}
\]

- **\( T_\theta \)**: Başlangıç sıcaklığı (örneğin 298.15 K)  
- **azalma**: Sıcaklık azalma oranı  

### Henry Sabiti Güncellemesi  
\[
H(t+1) = H(t) \cdot \exp{\left(-C \cdot \left(\frac{1}{T} - \frac{1}{T_\theta}\right)\right)}
\]

### Pozisyon Güncellemesi  
\[
X_i(t+1) = X_i(t) + r \cdot S \cdot (X_{en\_iyi} - X_i(t))
\]

- **\( X_i(t) \)**: Ajanın mevcut pozisyonu  
- **\( X_{en\_iyi} \)**: En iyi bilinen çözüm  
- **\( r \)**: Rastgelelik faktörü  

---

## 4. Parametreler

| Parametre               | Açıklama                                      | Varsayılan Değer |
|-------------------------|-----------------------------------------------|------------------|
| Hedef Fonksiyon         | Optimize edilecek fonksiyon                  | Kullanıcı Tanımlı |
| Alt Sınır               | Arama uzayının alt sınırı                    | Kullanıcı Tanımlı |
| Üst Sınır               | Arama uzayının üst sınırı                    | Kullanıcı Tanımlı |
| Boyut                   | Problemin boyutu (değişken sayısı)           | Kullanıcı Tanımlı |
| Popülasyon Boyutu       | Ajan sayısı                                  | 30               |
| Maksimum İterasyon      | Algoritmanın toplam iterasyon sayısı         | 100              |
| Azalma Oranı            | Sıcaklık azalma oranı                        | 0.01             |

---

## 5. Kullanım Örneği

### Python ile Kullanım

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
