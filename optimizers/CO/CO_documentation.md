# Giriş
Doğal yırtıcılar olan çitaların, habitatlarında dolaşırken bir avla karşılaşmaları mümkündür. 
Avı bulduklarında çitalar oturup avın yaklaşmasını bekleyebilir ve daha sonra saldırmaya başlayabilirler.
Çitaların sldırı eyleminde koşma ve yakalama kısımları bulunmaktadır. Çitalar bazı koşullarda (enerji limitine ulaşılması, 
avın hızlıca kaçması, vb.) avlanmayı bırakabilir. Bu durumda çita eve döner, dinlenir ve yeni bir avlanma periyoduna başlar.
Çitalar belirli faktörleri değerlendirerek bu stratejilerden birini seçer. 
Bu faktörler: avın durumu, kendi durumu, bulunduğu alan, ava olan uzaklığı. 
Çita optimizasyon algoritması bu stratejilerin av sırasında akıllıca seçilmesi ve uygulanması prensibine dayanır.

# Temel Özellikler
Çita optimizasyon algoritması, çitaların avlanma stratejilerini referans alarak tasarlanmış meta-sezgisel bir optimizasyon yöntemidir. 
Çitalar avlanırken 4 farklı stratejiden faydalanır: *arama (search)*, *otur-ve-bekle (sit-and-wait)*, *saldır (attack)* ve *avı-bırak-ve-eve-dön (leave-the-prey-and-go-back-home)*.
<br/>
Aşağıda bu 3 stratejinin detayları verilmiştir. 
Bu bölümde verilen denklemler kısaca açıklanmış, **Konum Güncelleme Denklemleri** kısmında detaylı olarak incelenmiştir. 

<br/>
<br/>

### Arama (Search)
Çitalar avlanırken belirli faktörleri (avın durumu, avcının alanı kapsama durumu, avcının kendi durumu) göz önünde bulundurarak, iki stratejiden birini seçip arama yaparlar: durup alanı taramak veya alanda dolaşmak. 
Durup etrafı taramak eğer av yoğunsa (ör: sürü halinde dolaşıyorsa) veya avın kendisi de alanda dolaşıyorsa iyi bir seçimdir. 
Öte yandan dolaşarak arama ise av daha hareketli olduğunda seçilir ama avcı için enerji maliyeti daha fazladır. <br/>
Aşağıda *arama* stratejisinin denklemi ve parametrelerin açıklaması verilmiştir: <br/>
$$X_{i,j}^{t+1} = X_{i,j}^t + \hat r_{i,j}^{-1} \cdot a_{i,j}^t$$ <br/>
*i*: çitaların indexi *(i = 1, 2, ..., n)*, *j*: pozisyonun boyutu *(j = 1, 2, ..., D)*, 
*n*: popülasyondaki toplam birey (çita) sayısı ve *D*: optimizasyon probleminin boyutu olmak üzere : 
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{i,j}^{t+1}$$ : *i.* çitanın bir sonraki pozisyonunun *j.* boyuttaki değeri
* *t* : şu anki zaman (*t.* iterasyon)
* *T* : avlanmak için harcanabilecek maksimum zaman (max iterasyon)
* $$\hat r_{i,j}^{-1}$$ : *i.* çitanın pozisyonunun *j.* boyuttaki değeri için rastgele bir sayısal değer
* $$a_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için adım sayısı (step size) değeri <br/>
_Arama_ stratejisinin grafiksel gösterimi:
![search_graphical](<Screenshot 2024-12-19 192824.png>)

<br/>
<br/>

### Otur-ve-Bekle (Sit and Wait)
Çitalar _arama_ fazındayken avın çitayı fark edip kaçması gibi bir risk oluşabilmektedir. 
Avın kaçması riskini ortadan kaldırmak için çitalar oldukları yerde bekleyip pusu kurarlar ve avın onlara yaklaşmasını beklerler.
Bu strateji algoritmik olarak popülasyondaki bireylerin aynı anda hareket etmesini engeller ve böylece erken yakınsama (convergence) 
problemini ortadan kaldırmaya yardımcı olur. Böylece daha iyi bir sonuca ulaşılabilir.
Aşağıda *otur-ve-bekle* stratejisinin denklemi ve parametrelerin açıklaması verilmiştir: <br/>
$$X_{i,j}^{t+1} = X_{i,j}^t$$ <br/>
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{i,j}^{t+1}$$ : *i.*çitanın bir sonraki pozisyonunun *j.* boyuttaki değeri <br/>

<br/>
<br/>

### Saldır (Attack)
Saldırı stratejisi temel olarak 2 adımdan oluşmaktadır: 
hücum (çita saldırmaya karar verdiğinde ava doğru hızlıca koşması) ve yakalama (çitanın hız ve esneklik kabiliyetlerini kullanarak avını yakalaması). Çita avını gördükten sonra hızlıca koşmaya ve böylece aralarındaki mesafeyi azaltmaya çalışır, buna *hücum (rushing)* fazı denir. Aralarındaki mesafe küçüldükten sonra çita esneklik kabiliyetlerini kullanarak avın ani hareketlerine göre hareket eder ve onu sıkıştırmaya çalışır, buna da *yakalama (capturing)* fazı denir.
*saldır* stratejisini tek bir çitanın uygulayabileceği gibi -böyle bir durumda bazı çitalar hareketsiz kalabilir-, grup halinde saldırı da yapılabilir. Böyle bir durumda gruptaki bireyler, pozisyonlarını kaçan ava göre veya lider ya da komşu çitaya göre günceller.
Aşağıda *saldır* stratejisinin denklemi ve parametrelerin 
açıklaması verilmiştir: <br/>
$$X_{i,j}^{t+1} = X_{B,j}^t + \check r_{i,j} \cdot \beta_{i,j}^t$$ <br/>
* $$X_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri
* $$X_{B,j}^t$$ : avın şu anki pozisyonunun *j.* boyuttaki değeri (popülasyondaki en iyi pozisyon)
* $$\check r_{i,j}$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için dönüş faktörü (turning factor) değeri
* $$\beta_{i,j}^t$$ : *i.* çitanın şu anki pozisyonunun *j.* boyuttaki değeri için etkileşim faktörü (interaction factor) değeri <br/>
*saldır* stratejisinin *hücum* fazının grafiksel gösterimi:
![attack-rushing_graph](<Screenshot 2024-12-19 192912.png>) <br/>
*saldır* stratejisinin *yakalama* fazının grafiksel gösterimi: 
![attack-capturing_graph](<Screenshot 2024-12-19 192924.png>)

<br/>
<br/>

### Avı-Bırak-ve-Eve-Dön (Leave-the-Prey-and-Go-Back-Home)
Bu stratejin görevi, av sürecini ilerletmekten çok, en iyi çözüme ulaşmak için bir "güvenlik önlemi" olarak düşünülmelidir. Kullanılması için 2 olası durum dikkate alınır: (1) Çita kovaladığı avı yakalamada başarısız olduysa posizyonunu değiştirmeli veya eve dönmelidir. (2) Çita belirli bir zaman aralığında başarılı bir avlanma süreci geçirmediyse tespit edilen son avın pozisyonuna yaklaşmalı ve *arama* aşamasına geri dönmelidir. Bu stratejinin matematiksel bir denklemi yoktur. Algoritmaya dahil edilme sebebi erken yakınsama ve local-optimum noktasında takılı kalma problemlerinin önüne geçmektir.

# Konum Güncelleme Denklemleri

# Keşif ve Sömürü Mekanizmaları
Algoritmada keşif süreci *arama* ve sömürü süreci *saldırı* adı altında uygulanmış ve $$r_2$$ ve $$r_3$$ katsayıları kullanılarak keşif-sömürü dengesi sağlanmıştır. $$r_2$$ ve $$r_3$$
Her ne kadar  çitanın enerji seviyesi bir faktör olarak kabul edildiği için iterasyon sayısı arttıkça bireylerin keşif yapma olasılıkları artmaktadır.

## Referanslar
