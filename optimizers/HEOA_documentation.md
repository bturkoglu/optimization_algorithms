### HEOA (Human Evolutionary Optimization Algorithm)

## Giriş
HEOA İnsan evriminden ilham alan bir meta-sezgisel optimizasyon algoritmasıdır. HEOA algoritması iki temel aşamadan oluşur: global arama yaparak çözüm uzayını keşfetmeye odaklanan İnsan Keşif Fazı ve popülasyonun dört gruba ayrıldığı İnsan Gelişim Fazı. Bu gruplar - en iyi çözümleri bulan liderler, yeni alanları keşfeden kaşifler, liderlerin başarılı stratejilerini takip eden takipçiler ve en düşük performanslı kaybedenler - farklı arama stratejileri kullanır. Algoritma, Lojistik Kaos Haritalaması ile başlangıç popülasyonunu oluşturur ve süreç boyunca keşif ve sömürü arasında dinamik bir denge kurar.

### Temel Özellikler ve Parametreler
Bu bölüm, HEOA algoritmasında kullanılan temel parametreleri ve bunların rollerini açıklamaktadır.

- **dim**: Problemin boyut sayısı. Arama alanını tanımlar.
- **N**: Popülasyon boyutu, yani algoritmada kullanılan parçacık sayısı.
- **Max_iter**: Algoritmanın çalışacağı maksimum iterasyon sayısı.
- **lb**: Arama alanı için alt sınır(lar).
- **ub**: Arama alanı için üst sınır(lar).
- **A**: Lider stratejisinde kullanılan sabit değer (0.6 olarak ayarlanmış).
- **LN**: Popülasyonun lider olarak atanacak yüzdesi (0.4 olarak ayarlanmış).
- **EN**: Popülasyonun kaşif olarak atanacak yüzdesi (0.4 olarak ayarlanmış).
- **FN**: Popülasyonun takipçi olarak atanacak yüzdesi (0.1 olarak ayarlanmış).


**HEOA Akış Diyagramı**

1. **Başlangıç:**
   - Popülasyon, **Logistic Chaos Mapping** yöntemi kullanılarak başlatılır.
   - Bu yöntem, popülasyonun başlangıçtaki çeşitliliğini artırır ve kaotik bir başlangıç sağlar.


2. **Uygunluk Hesaplama:**
    - Her bir aday çözüm için uygunluk (**fitness**) değerleri hesaplanır.
    - Bu değerler, hangi çözümlerin daha iyi olduğunu belirlemek için kullanılır.

2. **Arama Başlat:**
   - **Döngü:** i = 1'den Max\_iter'a kadar (tüm iterasyonlar boyunca):
     - En iyi uygunluk (BestF) ve en kötü uygunluk (WorstF) değerlerini al.
     - R = rand(1) (rastgele bir değer atama).

3. **Popülasyon İçin Döngü:** j = 1'den popülasyon boyutuna kadar (her bireyi incele):

   - **Keşif Aşaması:**
    - Algoritma, ilk aşamada geniş bir arama gerçekleştirir.
    - Aday çözümler, **Levy uçuşları** ve sıçrama stratejileriyle arama alanında farklı yerlere hareket ettirilir.
     - İf (i <= (1/4) * Max\_iter):
       - Yeni konum:  
         ```
          X_new[j, :] = GBestX * (1 - i/Max_iter) + 
               (np.mean(X[j, :]) - GBestX) * np.floor(np.random.rand()/jump_factor) * jump_factor + 
               0.2 * (1 - i/Max_iter) * (X[j, :] - GBestX) * Levy(dim)
         ```
       
               
   - **İnsan Gelişim Aşaması:**
        - Popülasyon, uygunluk değerlerine göre dört gruba ayrılır:
        - Her grup, kendi stratejilerine göre pozisyonlarını günceller:

     - **Liderler:** 
       - En iyi çözümleri keşfetmek için arama yaparlar.
       - Mevcut en iyi çözüm çevresinde yoğunlaşır.
       - Eğer rastgele sayı R , uyarı değeri A dan küçükse, lider pozisyonunu bir kosinüs fonksiyonu kullanarak günceller. Aksi takdirde, lider rastgele bir yürüyüş yapar
       - j = 1'den LNNNumber'a kadar:
         - İf R < A ise: 
           ```
           X_new(j,:) = w * X(j,:) + exp(-i * randn(1)) / (rand(1) * Max_iter)
           ```
         - Aksi takdirde: 
           ```
           X_new(j,:) = w * X(j,:) + randn() * ones(1, dim)
           ```
            # Eğer R < A (A=0.6 uyarı değeri) ise:
            X_new[j, :] = 0.2 * np.cos(np.pi/2 * (1-(i/Max_iter))) * X[j, :] * 
                        np.exp((-i * np.random.randn())/(np.random.rand() * Max_iter))

            # Değilse:
            X_new[j, :] = 0.2 * np.cos(np.pi/2 * (1-(i/Max_iter))) * X[j, :] + 
                        np.random.randn() * np.ones(dim)  

     - **Kâşifler (Explorers):** 
       - Kaşifler, diğer parçacıklardan uzaklaşarak rastgele bir şekilde arama yapar:
       - Daha geniş bir alanda rastgele hareket eder.
       - j = LNNNumber + 1'den LNNNumber + ENNumber'a kadar:
         ```
        X_new[j, :] = np.random.randn() * np.exp((X[-1, :] - X[j, :])/(j**2))
         ```

     - **Takipçiler (Followers):** 
       - Liderleri takip ederek onların izinden giderler.
       - Takipçiler, global en iyi pozisyona doğru bir kosinüs faktörü ile pozisyonlarını ayarlar
       - Mevcut en iyi çözüm çevresinde yoğunlaşır
       - j = LNNNumber + ENNumber + 1'den LNNNumber + ENNumber + FNNumber'a kadar:
         ```
         X_new[j, :] = X[j, :] + 0.2 * np.cos(np.pi/2 * (1-(i/Max_iter))) * 
               np.random.rand(dim) * (X[0, :] - X[j, :])
         ```
         

     - **Kaybedenler (Losers):** 
       - Uygun olmayan çözümler elenir ve yenileriyle değiştirilir.
       - Başarılı bölgelerden yeniden başlatılır.
       - Global en iyi pozisyona doğru rastgele bir hareket yapar.
       - j = LNNNumber + ENNumber + FNNumber + 1'den N'e kadar:
         ```
         X_new[j, :] = GBestX + (GBestX - X[j, :]) * np.random.randn()
         ```
         

4. **Sınır Güncellemesi ve Kontrol:**
   Parçacıkların pozisyonları, önceden belirlenen sınırlar içinde tutulur. Eğer güncellenmiş pozisyon sınırlar dışına çıkarsa, pozisyonlar **lb** ve **ub** tarafından belirlenen aralıkta kalacak şekilde sınırlandırılır.

5. **En İyi Çözümü Döndür:**
   - Iterasyonlar tamamlandıktan sonra en iyi çözüm "Best Solution" olarak dön.

## Yakınsama Takibi
Algoritma, her iterasyonda en iyi fitness değerini takip eder ve **Convergence_curve** dizisine kaydeder. Bu, optimizasyonun ilerlemesini izlemeye yardımcı olur ve algoritmanın optimal çözüme nasıl yaklaştığını anlamayı sağlar.

## Keşif (Exploration)
- **Human Exploration Stage** ve **Explorers** aşamaları, global en iyi çözüm yönünde hareket ederek daha geniş bir arama alanını hedefler. Levy uçuşu adımı keşfi destekler.

## Sömürü (Exploitation)
- **Leaders**, **Followers** ve **Losers** aşamaları, mevcut çözümler etrafında daha iyi sonuçlar elde etmeye çalışarak sömürüye odaklanır.

## Referanslar
1. Junbo Lian, Guohua Hui (2024) Human Evolutionary Optimization Algorithm Expert Systems with Applications 241,122638. DOI: https://doi.org/10.1016/j.eswa.2023.122638