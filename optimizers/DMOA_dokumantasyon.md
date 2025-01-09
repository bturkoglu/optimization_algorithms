1. Giriş
Dwarf Mongoose Optimization Algorithm (DMOA), cüce mangustaların sosyal davranışlarından esinlenerek geliştirilmiş bir meta-sezgisel optimizasyon algoritmasıdır. Bu algoritma, mangustaların yeni bölgeleri keşfetme ve mevcut bölgelerdeki kaynakları optimize etme stratejilerini taklit eder. DMOA, yüksek boyutlu ve karmaşık optimizasyon problemlerinde etkili bir performans göstermektedir.

2. Temel Özellikler
Keşif ve Sömürü Dengesi: DMOA, yeni bölgeleri keşfetme ve mevcut iyi çözümleri iyileştirme arasında dengeli bir yapı sunar.
Adaptif Mekanizmalar: Yerel minimumlardan kaçınmak için rastgele ve uyarlanabilir davranışlar kullanır.
Biyolojik İlham: Algoritma, alfa grubu, keşifçi (scout) ve bakıcı (babysitter) rollerini simüle ederek optimizasyon sürecini yönlendirir.
3. DMOA’nın Ana Bileşenleri
Popülasyon Boyutu (nPop): Algoritmadaki bireylerin sayısı.
İterasyon Sayısı (MaxIt): Algoritmanın gerçekleştireceği toplam adım sayısı.
Değişken Aralığı (VarMin, VarMax): Parametrelerin alt ve üst sınırları.
Boyut Sayısı (nVar): Optimizasyon problemindeki değişken sayısı.
Amaç Fonksiyonu (F_obj): Minimum değeri bulunması gereken hedef fonksiyon.
4. Algoritmanın Akışı
Popülasyonun Başlatılması:
Tüm bireylerin pozisyonları, VarMin ve VarMax arasında rastgele seçilir.

Alpha Grubu (Lider Grup):

Her iterasyonda lider grup bireyleri güncellenir.
Yeni pozisyonlar, komşu bireyler arasındaki farklara dayalı olarak hesaplanır.
Keşifçi (Scout) Grubu:

Belli bir iterasyon sonrası başarısız bireyler rastgele pozisyonlara taşınır.
Yeni pozisyonlar için uyarlanabilir ağırlıklar kullanılır.
Bakıcılar (Babysitters):

Belli koşullarda, bazı bireyler popülasyonun çeşitli bölgelerine dağıtılır.
Konum Güncelleme:
Konum güncelleme şu denkleme göre yapılır:

Yeni Pozisyon
=
Eski Pozisyon
+
𝜙
⋅
(
Eski Pozisyon
−
Kom
s
¸
u Pozisyon
)
Yeni Pozisyon=Eski Pozisyon+ϕ⋅(Eski Pozisyon−Kom 
s
¸
​
 u Pozisyon)
Burada φ rastgele bir ağırlık katsayısıdır.

5. Keşif ve Sömürü Mekanizmaları
Keşif Mekanizması:
Yeni pozisyonlar hesaplanırken bireylerin rastgele yönlere hareket etmesi sağlanır.

Sömürü Mekanizması:
İyi sonuçlar elde eden bireylerin etrafındaki çözümler iyileştirilir ve en iyi pozisyonların çevresi daha detaylı incelenir.

6. Algoritma Parametreleri
nBabysitter: Bakıcı sayısı, sömürü aşamalarında kullanılır.
peep: Alfa bireyin vokalizasyon katsayısı.
CF: Adaptasyon katsayısı, iterasyon ilerledikçe güncellenir.
7. Örnek Kullanım
python
Kodu kopyala
def sphere(x):
    return np.sum(x ** 2)

nPop = 50  # Popülasyon büyüklüğü
MaxIt = 100  # Maksimum iterasyon sayısı
VarMin = -10  # Alt sınır
VarMax = 10  # Üst sınır
nVar = 5  # Değişken sayısı

BEF, BEP, BestCost = DMOA(nPop, MaxIt, VarMin, VarMax, nVar, sphere)
print(f"En iyi fitness değeri: {BEF}")
print(f"En iyi pozisyon: {BEP}")
8. Çıktı ve Yorumlama
Her iterasyon için en iyi fitness değeri yazdırılır.
Algoritma tamamlandığında, en iyi pozisyon ve minimum değer ekrana basılır.
9. Sonuç ve Değerlendirme
DMOA, keşif ve sömürü mekanizmalarını başarılı bir şekilde birleştiren güçlü bir optimizasyon algoritmasıdır. Performansı, rastgele başlangıç pozisyonlarına rağmen etkileyici sonuçlar sunar. Ancak, parametrelerin uygun seçilmesi, algoritmanın etkinliğini artırabilir.