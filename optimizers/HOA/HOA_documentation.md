# Hiking Optimization Algorithm (HOA)

## Giriş

Hiking Optimization Algorithm (HOA), Tobler'in Yürüyüş Fonksiyonu'na dayalı bir doğadan ilham alan optimizasyon algoritmasıdır. Algoritma, küresel optimizasyon problemlerini çözmek için, keşif ve sömürü mekanizmalarını birleştirerek çözüm uzayında en iyi çözümü bulmayı amaçlar.

## Temel Özellikler

Tobler'in Yürüyüş Fonksiyonu: Yokuş yukarı veya aşağı yürüyüş sırasında enerji harcamasını simüle eder.

Rastgele Faktörler: Açılar, eğimler ve süpürme faktörü gibi rastgele bileşenler eklenerek algoritmanın keşif yeteneği artırılır.

Küresel En İyiyi Güncelleme: Algoritma, her iterasyonda küresel en iyi çözümü güncelleyerek sömürü yeteneğini optimize eder.

Alt ve Üst Sınır Uygulaması: Çözüm uzayının sınırları dışına çıkan çözümler, verilen alt ve üst sınırlarla sınırlandırılır.

## Konum Güncelleme Denklemleri

HOA'da, hiker'ların konumları aşağıdaki denklemlere göre güncellenir:

### Rastgele Eğim ve Süpürme Faktörü

#### Rastgele bir şekilde yokuşun açısı ve eğimini atama
theta = random.randint(0, 50)
slope = np.tan(theta)

#### Meyil faktörünün oluşturulması
sf = random.choice([1,2,3,4])

### Yeni Hızın Hesaplanması

Tobler'in Yürüyüş Fonksiyonu'na dayalı olarak hız hesaplanır:

#### Tobler's Hiking Function' a göre yeni hızın hesaplanması 
velocity = 6 * np.exp(-3.5 * abs(slope + 0.05))
new_velocity = velocity + np.random.rand(dim) * (g_best_pos - sf * x_ini)

### Yeni Konumun Güncellenmesi

Yeni hız bilgisi ile konum güncellenir ve sınırlar uygulanır:

#### Konumu güncelle ve sınırlara indirge 
new_position = x_ini + new_velocity
new_position = np.clip(new_position, lb, ub)

## Keşif ve Sömürü Mekanizmaları

### Keşif Mekanizması:

Rastgele eğim, süpürme faktörü ve hız hesaplamaları, hiker'ların çözüm uzayında daha geniş bir alanda arama yapmasını sağlar.

### Sömürü Mekanizması:

Küresel en iyi pozisyon bilgisi kullanılarak çözümler, en iyi bulunan çözümün çevresinde yoğunlaşır ve bu sayede sömürü gerçekleştirilir.

## Referanslar

Tobler, W. (1993). Three presentations on geographical analysis and modeling. National Center for Geographic Information and Analysis.



