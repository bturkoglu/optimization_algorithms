# Deniz Yırtıcıları Algoritması(Marine Predators Algorithm-MPA )

## Giriş

Marine Predators Algorithm (MPA), deniz yırtıcılarının avlanma stratejilerinden esinlenerek tasarlanmış bir doğadan ilham alan metaheuristik optimizasyon algoritmasıdır. Özellikle Lévy ve Brownian hareketlerine dayanan bu algoritma, yırtıcı ve av arasındaki biyolojik etkileşimlerin en uygun karşılaşma oranı politikasını taklit eder.İlk kez 2020 yılında "Expert Systems with Applications" dergisinde tanıtılmış olan bu algoritma, mühendislik problemleri ve matematiksel fonksiyonlar üzerinde çok başarılı sonuçlar vermiştir.

## Temel Özellikler

1. **Doğadan Esinlenme**: Algoritma, yırtıcı ve avın doğada izlediği stratejilerden esinlenmiştir.
   - **Lévy Hareketi**: Az av yoğunluklu alanlarda kullanılır, küçük adımlar ve uzun sıçramalarla yakın çevreyi derinlemesine inceler.
   - **Brownian Hareketi**: Yüksek av yoğunluklu alanlarda daha düzenli ve kontrollü adımlar izler. Uzak mesafe alanları keşfeder.
2. **Hafıza Mekanizması**: Deniz yırtıcılarının hafıza özellikleri simüle edilmiştir. Bu, algoritmanın önceki başarılı arama alanlarını hatırlamasını sağlar ve çözüm kalitesini artırır. Hafıza mekanizması, yırtıcı ve avın hareketlerini ve pozisyonlarını sürekli iyileştirir.
3. **Keşfetme ve Sömürme Dengesi**: Algoritma,Lévy ve Brownian hareketlerini kombine ederek yerel ve globalde dengeli bir şekilde keşif ve söürü yapar.  
4. **FAD ve Eddy Efektleri**: Doğal veya insan kaynaklı çevresel faktörleri (örneğin, eddy formasyonu ve Balık Çekim Cihazları - FAD) dikkate alır. Bu etkiler, algoritmanın yerel optimumlarda sıkışmasını önlemeye yardımcı olur.
5. **Yapısı**: Sırasıyla keşif (Exploration), geçiş (transition) ve sömürü (exploitation) olacak şekilde 3 ana aşamadan oluşur. İlk aşamada, yırtıcı hareketsiz kalırken av Brownian hareketiyle keşif yapar. İkinci aşamada, av Lévy hareketiyle sömürü yaparken yırtıcı Brownian hareketiyle keşfe devam eder.Son aşamada, yırtıcı Lévy hareketine geçerek en uygun çözüme odaklanır. Algoritmanın bu üç aşaması, av ve yırtıcı arasındaki hız oranına bağlı olarak düzenlenmiştir.

## Konum Güncelleme Denklemleri

MPA, üç temel fazda hareket eder ve her bir faz için farklı konum güncelleme denklemleri kullanılır:

### Faz 1: Yüksek Keşfetme

Avcı avdan daha hızlı hareket ederken (yüksek hız oranında) Brownian hareketi kullanılarak avlar çevrelerini yoğun bir şekilde keşfeder:

```math
stepsize[i, :] = RB[i, :] \cdot (Elite[i, :] - RB[i, :] \cdot Prey[i, :])
```
```math
Prey[i, :] += P \cdot R \cdot stepsize[i, :]
```

### Faz 2: Geçiş

Hem avcı hem de avın aynı hızlarda hareket eder (Birim hız oranı).Bu bölüm, keşfin geçici olarak sömürüye döndürülmeye çalışıldığı optimizasyonun ara aşamasında gerçekleşir. Bu aşamada, hem keşif hem de sömürü önemlidir.Nüfusun yarısı keşif, diğer yarısı ise sömürü için belirlenmiştir. Av sömürüden ve avcı keşiften sorumludur.Av Lévy'de hareket ederse, avcı için en iyi strateji Brownian'dır. 

- **Brownian Hareketi**:

```math
stepsize[i, :] = RB[i, :] \cdot (RB[i, :] \cdot Elite[i, :] - Prey[i, :])
```

```math
Prey[i, :] = Elite[i, :] + P \cdot CF \cdot stepsize[i, :]
```

- **Lévy Hareketi**:

```math
stepsize[i, :] = RL[i, :] \cdot (Elite[i, :] - RL[i, :] \cdot Prey[i, :])
```

```math
Prey[i, :] += P \cdot R \cdot stepsize[i, :]
```

### Faz 3: Yüksek Sömürme

Avcı avdan daha hızlı hareket ettiğinde (düşük hız oranı) Lévy hareketiyle yırtıcılar belirli bölgelerde daha detaylı arama yapar, yüksek sömürü sağlar.

```math
stepsize[i, :] = RL[i, :] \cdot (RL[i, :] \cdot Elite[i, :] - Prey[i, :])
```
```math
Prey[i, :] = Elite[i, :] + P \cdot CF \cdot stepsize[i, :]
```

## Keşfetme ve Sömürü Mekanizmaları

1. **Keşfetme (Exploration)**:

   - Algoritmanın ilk fazında, yırtıcı hareketsiz kalırken avlar Brownian hareketiyle alanı keşfeder.
   - Lévy hareketiyle daha az yoğun alanlarda uzun adımlar atılarak yeni çözüm bölgeleri bulunur.

2. **Sömürme (Exploitation)**:

   - İkinci ve üçüncü fazlarda, algoritma yırtıcının bulunduğu alanı daha detaylı inceleyerek daha iyi çözümler bulur.
   - Hafıza mekanizması, önceki iyi çözümlerin tekrar aranmasını sağlar.

3. **FAD ve Eddy Efektleri**:

   - Algoritmanın tıkanmasını önlemek için rastgele uzun adımlar kullanılır.
   - Yerel optimumlardan çıkılmasını sağlar.

## Referanslar

1. X. Zhun, Q. Heidari, A. Mirjalili, “Marine Predators Algorithm: A Nature-Inspired Metaheuristic,” Expert Systems with Applications, 2020.
2. MPA algoritmasının orijinal yayını: [ScienceDirect Linki](https://www.sciencedirect.com/science/article/abs/pii/S0957417420302025).
