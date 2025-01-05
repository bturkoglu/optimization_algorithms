# Giriş
Doğal yırtıcılar olan çitaların, habitatlarında dolaşırken bir avla karşılaşmaları mümkündür. 
Avı bulduklarında çitalar oturup avın yaklaşmasını bekleyebilir ve daha sonra saldırmaya başlayabilirler.
Çitaların sldırı eyleminde koşma ve yakalama kısımları bulunmaktadır. Çitalar bazı koşullarda (enerji limitine ulaşılması, 
avın hızlıca kaçması, vb.) avlanmayı bırakabilir. Bu durumda çita eve döner, dinlenir ve yeni bir avlanma periyoduna başlar.
Çitalar belirli faktörleri değerlendirerek bu stratejilerden birini seçer. 
Bu faktörler: avın durumu, kendi durumu, bulunduğu alan, ava olan uzaklığı. 
Çita optimizasyon algoritması, bu stratejilerin av sırasında stratejik bir şekilde seçilmesi ve uygulanması prensibine dayanır.

<br/>
<br/>

# Temel Özellikler
Çita optimizasyon algoritması, çitaların avlanma stratejilerini referans alarak tasarlanmış meta-sezgisel bir optimizasyon yöntemidir. 
Çitalar avlanırken 4 farklı stratejiden faydalanır: *arama (search)*, *otur-ve-bekle (sit-and-wait)*, *saldır (attack)* ve *avı-bırak-ve-eve-dön (leave-the-prey-and-go-back-home)*.

<br/>

### Arama (Search)
Çitalar avlanırken belirli faktörleri (avın durumu, avcının alanı kapsama durumu, avcının kendi durumu) göz önünde bulundurarak, iki stratejiden birini seçip arama yaparlar: durup alanı taramak veya alanda dolaşmak. 
Durup etrafı taramak eğer av yoğunsa (ör: sürü halinde dolaşıyorsa) veya avın kendisi de alanda dolaşıyorsa iyi bir seçimdir. 
Öte yandan dolaşarak arama ise av daha hareketli olduğunda seçilir ama avcı için enerji maliyeti daha fazladır. <br/>
![Screenshot 2024-12-19 192824](https://github.com/user-attachments/assets/87633660-2d59-4fbb-b104-64b0541a866e)
<br/>
_arama_ stratejisinin grafiksel gösterimi

<br/>

### Otur-ve-Bekle (Sit and Wait)
Çitalar _arama_ fazındayken avın çitayı fark edip kaçması gibi bir risk oluşabilmektedir. 
Avın kaçması riskini ortadan kaldırmak için çitalar oldukları yerde bekleyip pusu kurarlar ve avın onlara yaklaşmasını beklerler.
Bu strateji algoritmik olarak popülasyondaki bireylerin aynı anda hareket etmesini engeller ve böylece erken yakınsama (convergence) 
problemini ortadan kaldırmaya yardımcı olur. Böylece daha optimal bir sonuca ulaşılabilir. <br/>
![Screenshot 2024-12-19 192853](https://github.com/user-attachments/assets/d84c38b0-9034-41b1-a72c-a303688db80a)
<br/>
*otur-ve-bekle* stratejisinin grafiksel gösterimi

<br/>

### Saldır (Attack)
Saldırı stratejisi temel olarak 2 adımdan oluşmaktadır: 
hücum (çita saldırmaya karar verdiğinde ava doğru hızlıca koşması) ve yakalama (çitanın hız ve esneklik kabiliyetlerini kullanarak avını yakalaması). Çita avını gördükten sonra hızlıca koşmaya ve böylece aralarındaki mesafeyi azaltmaya çalışır, buna *hücum (rushing)* fazı denir. Aralarındaki mesafe küçüldükten sonra çita esneklik kabiliyetlerini kullanarak avın ani hareketlerine göre hareket eder ve onu sıkıştırmaya çalışır, buna da *yakalama (capturing)* fazı denir.
*saldır* stratejisini tek bir çitanın uygulayabileceği gibi -böyle bir durumda bazı çitalar hareketsiz kalabilir-, grup halinde saldırı da yapılabilir. Böyle bir durumda gruptaki bireyler, pozisyonlarını kaçan ava göre veya lider ya da komşu çitaya göre günceller. <br/>

![Screenshot 2024-12-19 192912](https://github.com/user-attachments/assets/b3a8e60b-916e-44e0-8a8e-5a40ab99bb0f)
<br/>
*saldır* stratejisinin *hücum* fazının grafiksel gösterimi
<br/>
<br/>
![Screenshot 2024-12-19 192924](https://github.com/user-attachments/assets/66579edf-f936-4629-b94f-623e452699f2)
<br/>
*saldır* stratejisinin *yakalama* fazının grafiksel gösterimi
<br/>

<br/>

### Avı-Bırak-ve-Eve-Dön (Leave-the-Prey-and-Go-Back-Home)
Bu stratejin görevi, av sürecini ilerletmekten çok, en iyi çözüme ulaşmak için bir "güvenlik önlemi" olarak düşünülmelidir. Kullanılması için 2 olası durum dikkate alınır: (1) Çita kovaladığı avı yakalamada başarısız olduysa posizyonunu değiştirmeli veya eve dönmelidir. (2) Çita belirli bir zaman aralığında başarılı bir avlanma süreci geçirmediyse tespit edilen son avın pozisyonuna yaklaşmalı ve *arama* aşamasına geri dönmelidir. Bu stratejinin matematiksel bir denklemi yoktur. Algoritmaya dahil edilme sebebi erken yakınsama ve local-optimum noktasında takılı kalma problemlerinin önüne geçmektir.

<br/>

### Avantajları
* CO algoritması, çitaların avlanma sürecini literatürdeki benzer algoritmalardan farklı olarak daha gerçekçi bir şekilde taklit etmiştir. Basit konseptleri az sayıda denklem ile modellediği için anlaşılması ve modifiye etmesi kolaydır.
* Keşif ve sömürü eylemleri dengeli bir şekilde modellenmiştir. Böylece erken yakınsama (premature convergence) sorunu ortadan kalkmıştır.
* CCA algoritmasında [2] çitaların avı yakalama fazı taklit edilmeye çalışılmış, fakat matematiksel olarak iyi modellenememiştir. CO algoritması ise avlanmanın birden fazla fazını kullanmış ve bunları kolay ve anlaşılabilir denklemlerle modellemiştir.
* Başka bir algoritmada [3] ise çitaların avlanma davranışları taklit edilmeye çalışılmıştır. GWO (grey wolf optimizer) algoritmasını temel alan bu algoritma, çitaların grup halinde avlanmalarını (liderlik hiyerarşisi ve avlanma sırasında çitalar arası iletişim) modellemek için modifiye edilmiştir. Fakat bahsedilen algoritma bu özellikleri iyi bir şekilde kullanamamış ve yine matematiksel olarak iyi modelleyememiştir. CO ise avlanma sürecini gerçeğine yakın bir şekilde modellediğinden her denklem birbiriyle bağlantılı olmuştur bu nedenle bir fazın hangi aşamada veya nasıl kullanılacağı herhangi bir sorun yaratmamıştır.

<br/>
<br/>

# Konum Güncelleme Denklemleri

## Arama (Search)

```
X_new = X_current + r_Hat^(-1) * alpha
```

Orijinal denklem:
$X_{i,j}^{t+1} = X_{i,j}^t + \hat r_{i,j}^{-1} \cdot a_{i,j}^t$ <br/>
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{i,j}^{t+1}$$ : *i.* çitanın bir sonraki pozisyonunun *j.* boyuttaki değeri
* *t* : şu anki zaman (*t.* iterasyon)
* $$\hat r_{i,j}^{-1}$$ : *i.* çitanın pozisyonunun *j.* boyuttaki değeri için rastgele bir sayısal değer
* $$a_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için adım sayısı (step size) değeri 

<br/>
<br/>

## Otur ve Bekle (Sit and Wait)
```
X_new = X_current
```

Orijinal denklem:
$$X_{i,j}^{t+1} = X_{i,j}^t$$ <br/>
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{i,j}^{t+1}$$ : *i.*çitanın bir sonraki pozisyonunun *j.* boyuttaki değeri 

<br/>
<br/>

## Saldır (Attack)
```
X_new = X_best + r_Check * beta
```

Orijinal denklem:
$$X_{i,j}^{t+1} = X_{B,j}^t + \check r_{i,j} \cdot \beta_{i,j}^t$$ <br/>
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{B,j}^t$$ : avın şu anki pozisyonunun *j.* boyuttaki değeri (popülasyondaki en iyi pozisyon)
* $$\check r_{i,j}$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için dönüş faktörü (turning factor) değeri
* $$\beta_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için etkileşim faktörü (interaction factor) değeri <br/>

<br/>
<br/>

# Keşif ve Sömürü Mekanizmaları
Modelde keşif süreci *arama* ve sömürü süreci *saldırı* adı altında uygulanmakta ve iterasyon sırasında rastgele seçilmektedir. Fakat her ne kadar rastgelelik söz konusu olsa da çitanın enerji seviyesi bir faktör olarak kabul edildiği için iterasyon sayısı arttıkça bireylerin keşif (*search*) yapma olasılıkları artmaktadır. Bazı durumlarda ise ilk iterasyonlar keşif için ayrılmış, iterasyon sayısı *t* yeterince arttıktan sonra saldırı stratejisine geçilmiştir.
Algoritmada keşif ve sömürü seçimi *r2* ve *r3* katsayılarıyla sağlanmıştır:
* Eğer *r2* ≥ *r3* ise, *otur-ve-bekle* stratejisi seçilir
* Değilse, *H* katsayısının değeri hesaplanılarak *arama* ve *saldır* stratejisi seçilir. ($$H = e^{1-t/T}(2r1 - 1)$$ ve *r1* 0-1 arasında rastgele bir sayı) <br/>

*r3* katsayısını ayarlayarak keşif ve sömürü seçimi üzerinde oynamak mümkündür.

<br/>
<br/>

## Referanslar

[1] Akbari, M.A., Zare, M., Azizipanah-abarghooee, R. et al. The cheetah optimizer: a nature-inspired metaheuristic algorithm for large-scale optimization problems. Sci Rep 12, 10953 (2022). https://doi.org/10.1038/s41598-022-14338-z
[2] Goudhaman, M. (2018). Cheetah chase algorithm (CCA): a nature-inspired metaheuristic algorithm. International Journal of Engineering & Technology, 7(3), 1804-1811. https://doi.org/10.14419/ijet.v7i3.18.14616
[3] Saravanan, D., Paul, P. V., Janakiraman, S., Dumka, A., & Jayakumar, L. (2020). A New Bio-Inspired Algorithm Based on the Hunting Behavior of Cheetah. International Journal of Information Technology Project Management (IJITPM), 11(4), 13-30. https://doi.org/10.4018/IJITPM.2020100102
