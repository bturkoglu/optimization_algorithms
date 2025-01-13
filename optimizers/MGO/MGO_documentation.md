# MGO (Mountain Gazelle Optimizer - Dağ Ceylanı Optimizasyon Algoritması) Dokümantasyonu

## Giriş
Mountain Gazelle Optimizer (MGO), doğanın ilham verici dengesini, dağ ceylanlarının sosyal davranışları ve hareket modelleri üzerinden modelleyen yenilikçi bir metasezgisel algoritmadır. Bu algoritma, dağ ceylanlarının kaynak bulma, tehlikeden kaçınma ve grup dinamiklerini optimize etme becerilerinden esinlenerek tasarlanmıştır. Abdollahzadeh vd. (2022) tarafından geliştirilen bu algoritma, doğanın karmaşık ve dinamik yapısını modern optimizasyon problemlerine uyarlamaktadır. 

MGO'nun temel amacı, çözüm uzayındaki hem yerel hem de global en iyi çözümlere etkin bir şekilde yaklaşmaktır. Bu doğrultuda, algoritma farklı hareket stratejilerini ve kolektif zekaya dayalı sosyal davranışları birleştirir.

## Temel Özellikler
MGO algoritması, doğadan esinlenilen bir yaklaşımla, ceylanların bireysel ve grup davranışlarından ilham alan benzersiz özelliklere sahiptir:

- **Dinamik Keşif ve Sömürü Dengesi:**
  MGO, iterasyon süresince keşif ve sömürü mekanizmaları arasında dengeli bir şekilde geçiş yapar. Erken aşalarda rastgeleliğe dayalı keşif mekanizmaları öne çıkarken, iterasyon ilerledikçe algoritma daha hassas yerel arama odaklı hale gelir.

- **Sosyal Etkileşim ve Kolektif Zeka:**
  Bireylerin, popülasyonun ortalama konumuna ve en iyi bilinen çözüme dayalı hareket etmesi, algoritmanın sosyal öğrenme kapasitesini arttırır. Bu sayede çözüm kalitesi zamanla iyileşir.

- **Adaptif Parametre Kullanımı:**
  Hareket stratejileri ve konum güncellemelerinde kullanılan parametreler, iterasyon bazlı olarak dinamik bir şekilde uyarlanır. Bu, algoritmanın farklı optimizasyon problemlerine adapte olma kapasitesini artırır.

- **Bölgesel ve Global Arama Yeteneği:**
  Rastgele arama stratejileriyle çözüm uzayını geniş bir perspektiften tararken, en iyi çözüm odaklı hareket modelleri ile umut verici bölgelerde hassasiyet sağlar.

- **Hareket Modellerinin Çeşitliliği:**
  Algoritma, bireylerin yerel en iyilere, global en iyilere ve ortalama konumlara dayalı çoklu hareket stratejileri benimsemesini sağlar. Bu, çözüm çeşitliliğini ve kalitesini arttırır.

## Konum Güncelleme Denklemleri

Algoritmanın temel işleyişi, bireylerin yeni konumlara güncellenmesi üzerine kuruludur. MGO algoritması, çözüm uzayında farklı stratejiler kullanarak hem keşif hem de sömürü yeteneklerini optimize eder.

- **Rastgele Arama:**
```
NewX(1,:) = (ub - lb) * rand + lb
```
Bu denklem, bireylerin çözüm uzayında rastgele pozisyonlar almasını sağlar. Rastgele arama mekanizması, çözüm uzayının geniş bir şekilde taranması için kullanılır. Burada `ub` ve `lb` arama uzayının üst ve alt sınırlarını temsil ederken, `rand` rastgele bir değerdir.

- **En İyi Konum Tabanlı Güncelleme:**
```
NewX(2,:) = BestX - abs((r1 * M - r2 * X(i,:)) * A) * cofi(k,:)
```
Bu formül, bireylerin popülasyonun şu ana kadarki en iyi çözümüne doğru yaklaşmasını sağlar. Burada:
  - `BestX`, algoritmanın en iyi çözümünü temsil eder.
  - `M`, seçilen bireylerin ortalama konumudur ve sosyal etkileri yansıtır.
  - `A`, iterasyon bazlı adaptif bir parametredir ve bireylerin hareket çaplarını kontrol eder.
  - `cofi(k,:)`, bireylerin dinamik hareketine katkı sağlayan katsayılardır.

Bu denklem, yerel arama kapasitesini arttırır ve daha hassas çözüm bulma potansiyeli sunar.

- **Ortalama Konum Tabanlı Güncelleme:**
```
NewX(3,:) = (M + cofi(k,:)) + (r1 * BestX - r2 * X(j,:)) * cofi(k,:)
```
Ortalama konum tabanlı güncelleme, bireylerin sosyal öğrenme kapasitesini simüle eder. Burada bireyler, hem toplu ortalama bilgiye hem de en iyi çözümün etkisine dayanarak pozisyonlarını günceller. Bu mekanizma, çözüm uzayını daha dengeli bir şekilde taramaya olanak tanır ve çözüm kalitesini arttırır.

- **Dinamik Adaptasyon:** Algoritmanın adaptif parametreleri, iterasyon boyunca güncellenir. Bu, bireylerin hareketlerinin çözüm uzayında daha etkili bir şekilde dağılmasını sağlar. Adaptasyon, hem rastgeleliği hem de mevcut çözüm bilgilerini birleştirerek keşif ve sömürü dengesi kurar.

## Keşif ve Sömürü Mekanizmaları
MGO algoritması, keşif ve sömürü arasında dinamik bir denge kurar. Bu mekanizmalar algoritmanın çok yönlülük kazanmasına olanak tanır:

- **Keşif:** Algoritma, rastgele üretilen konumlarla global arama yeteneğini geliştirir. Rastgele arama stratejileri, popülasyonun çözüm uzayının çeşitli bölgelerine yayılmasını sağlar ve bu sayede yerel optimumlardan kaçınma olasılığı artar. Bu aşamada, bireylerin birbirinden bağımsız hareketleri, çözüm uzayını daha geniş bir perspektiften taramaya olanak tanır.

- **Sömürü:** Algoritma, umut verici çözüm bölgelerine odaklanarak bu alanlarda hassas arama yapar. En iyi bilinen çözüm etrafında yoğunlaşmak, algoritmanın belirli bir bölgede yerel optimumlara daha yakın çözümler elde etmesini sağlar. Sosyal öğrenme mekanizması, bireylerin diğerlerinin deneyimlerinden yararlanarak daha etkili bir sömürü stratejisi benimsemelerine olanak tanır.

- **Dinamik Dengeleme:** MGO algoritması, iterasyon ilerledikçe keşif ve sömürü mekanizmaları arasındaki dengenin otomatik olarak uyarlanmasını sağlar. Adaptif parametreler, iterasyonun erken aşamalarında keşif kapasitesini öne çıkarırken, ilerleyen aşalarda sömürü mekanizmasına daha fazla odaklanır.

MGO'nun kendine özgü özelliği, bireylerin sosyal etkileşim davranışlarıyla zenginleştirilmiş bir keşif ve sömürü düzeni sunmasıdır. Bu, algoritmanın hem global hem de lokal optimumlara etkili bir şekilde ulaşmasına olanak tanır.

## Referanslar
Abdollahzadeh, B., Soleimanian Gharehchopogh, F., Khodadadi, N., & Mirjalili, S. (2022). Mountain Gazelle Optimizer: A new Nature-inspired Metaheuristic Algorithm for Global Optimization Problems. Advances in Engineering Software, 174, 103282. https://doi.org/10.1016/j.advengsoft.2022.103282

