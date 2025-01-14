African Vultures Optimization Algorithm (AVOA) Documentation

Giriş

African Vultures Optimization Algorithm (AVOA), akbabaların av arayışı ve grup davranışlarından ilham alınarak tasarlanmış bir doğadan esinlenilmiş meta-heuristik algoritmadır. Bu algoritma, küresel optimizasyon problemlerini çözmek için tasarlanmıştır ve keşif ve sömürü süreçleri arasında denge kurmayı hedefler. AVOA, farklı çözümler arasındaki çeşitliliği korurken, arama uzayında etkili bir şekilde en iyi çözümleri bulmaya odaklanır.

Bu dokümantasyon, algoritmanın temel özelliklerini, konum güncelleme denklemlerini ve keşif/sömürü mekanizmalarını açıklamaktadır.

Temel Özellikler

Popülasyon Tabanlı: AVOA, çözüm adaylarını temsil eden bir popülasyon ile çalışır (akbabalar).

Keşif ve Sömürü: Parametre olan 

𝐹

F aracılığıyla keşif (arama) ve sömürü (yerel iyileştirme) dengesi sağlanır.

Convergence Eğrisi: Optimizasyon sürecindeki en iyi çözümün değişimini takip eder.

Hedef Fonksiyon Bağımsızlığı: Algoritma, herhangi bir hedef fonksiyon üzerinde çalışabilir.

Çoklu Sınır Tipleri: Algoritma, alt ve üst sınırları liste veya tek bir değer olarak destekler.

Konum Güncelleme Denklemleri

AVOA'nın ana yapı taşlarından biri, akbabaların konumlarının güncellenme şeklidir. Güncellemeler, akbabaların av arayışı sırasında hem rastgelelik hem de en iyi akbabaların konumlarına yakınlaşmayı içerir.

Durum 1: Keşif Fazı (∣𝐹∣≥1∣F∣≥1)

Akbabalar keşif modunda çalışır. Rastgele hareketlerle farklı alanları araştırırlar:

𝑉𝑢𝑙𝑡𝑢𝑟𝑒𝑖={𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒1 +𝐹 ⋅𝑅  if random() < 0.5 

𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒2 −𝐹⋅𝑅   otherwise

Vulture  i ={ 

BestVulture1+F⋅R

BestVulture2−F⋅R if random() < 0.5 otherwise

​



Durum 2: Orta Geçiş Fazı (0.5≤∣𝐹∣<1  0.5≤∣F∣<1)

Akbabalar, rastgele bir faktör ile iyileştirme yapar:

𝑉𝑢𝑙𝑡𝑢𝑟𝑒𝑖 ={𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒1+𝐹⋅𝑅⋅𝑟𝑎𝑛𝑑𝑜m()  if random() < 0.5

𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒2−𝐹⋅𝑅⋅𝑟𝑎𝑛𝑑𝑜𝑚()

otherwise

Vulture i

​={ 

BestVulture1+F⋅R⋅random()  if random() < 0.5

BestVulture2−F⋅R⋅random()  otherwise

​



Durum 3: Sömürü Fazı (

∣𝐹∣<0.5

∣F∣<0.5)

Akbabalar, en iyi bireylere daha fazla yakınlaşır:

𝑉𝑢𝑙𝑡𝑢𝑟𝑒𝑖 ={𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒1+𝐹⋅(𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒1−𝑉𝑢𝑙𝑡𝑢𝑟𝑒𝑖)

if random() < 0.5

𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒2+𝐹⋅(𝐵𝑒𝑠𝑡𝑉𝑢𝑙𝑡𝑢𝑟𝑒2−𝑉𝑢𝑙𝑡𝑢𝑟𝑒𝑖)

otherwise

Vulture i

​

` `={ 

BestVulture1+F⋅(BestVulture1−Vulture i )

BestVulture2+F⋅(BestVulture2−Vulture i )

​



if random() < 0.5

otherwise

​



Keşif ve Sömürü Mekanizmaları

Keşif Mekanizması: Algoritmanın keşif kabiliyeti, 

𝐹

F parametresinin 

∣𝐹∣≥1

∣F∣≥1 olduğu durumlarda devreye girer. Akbabalar bu durumda geniş bir alanda arama yapar.

Sömürü Mekanizması: 

∣𝐹∣<0.5

∣F∣<0.5 olduğunda algoritma, mevcut en iyi çözümlere odaklanır ve daha küçük alanlarda iyileştirme yapar.

Denge: 

𝐹

F parametresi, iterasyon sayısına ve rastgele bir değere bağlı olarak dinamik şekilde ayarlanır. Bu sayede, arama süreci boyunca keşif ve sömürü arasında etkili bir denge sağlanır.

Referanslar

Orijinal Yayın: Abdollahzadeh, B., Soleimanian Gharehchopogh, F., & Mirjalili, S. (2021). African vultures optimization algorithm: A new nature-inspired metaheuristic algorithm for global optimization problems. Computers & Industrial Engineering, 158, 107408.

DOI: 10.1016/j.cie.2021.107408

Kod: Berat Çalık tarafından geliştirilmiştir.

GitHub: https://github.com/beratcalik

