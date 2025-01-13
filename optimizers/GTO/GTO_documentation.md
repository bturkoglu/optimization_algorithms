*Gorilla Troops Optimizer (Goril Birlikleri Optimizasyonu)*


Goriller, yetişkin bir erkek veya Silverback goril grubu ve birkaç yetişkin dişi goril ve yavrularından oluşan birlikler olarak yaşarlar.Silverback bir grubun odak noktasıdır. Tüm kararları verir, kavgalara aracılık eder, grup hareketlerini belirler, gorilleri yiyecek kaynaklarına yönlendirir ve grubun güvenlik ve refahından sorumludur. Blackback olarak adlandırılan genç erkek goriller, Silverbackleri takip eder ve grup için yedek koruyucular olarak hizmet ederler. Hem erkek hem de dişi goriller doğdukları yerden göç etme eğilimindedir,  göç eder ve yeni gruplara taşınırlar. Ayrıca, erkek goriller gruplarını terk edip ve göç etmiş dişi gorilleri çekerek yeni gruplar oluştururlar. Ancak erkek goriller bazen doğdukları grupta kalır ve Silverback grubu içine alınırlar. Silverback goril ölürse, bu goriller gruba egemen olabilir ya da grupta egemenlik kurmak için Silverback goril ile işbirliği yapabilirler.

                                    ***Akış Şeması***:

                                    Başla
                                    Problem uzayında gorilla pozisyonlarını başlat ve p, T, F, L parametrelerini ayarla
                                    Gorilla fitness değerlerini hesapla
                                    İterasyon kontrolü (t ≤ T)
                                    "a" parametresini güncelle 

                                    Keşif Fazı:
                                    Eğer t ≤ Pop ise Denklem 1'i kullanarak gorilla pozisyonunu güncelle
                                    Gorilla fitness değerlerini hesapla ve yeni çözümler daha iyiyse güncelle
                                    En iyi çözümü gümüş sırtlının konumu olarak belirle

                                    Sömürü Fazı:
                                    Eğer a < w ise Denklem 7'yi kullanarak gorilla pozisyonunu güncelle
                                    Değilse Denklem 10'u kullanarak gorilla pozisyonunu güncelle
                                    Gorilla fitness değerlerini hesapla ve yeni çözümler daha iyiyse güncelle
                                    En iyi gorilayı döndür
                                    Dur

Gorillerin gruplarını terk etmeleri durumunda, gruptan ayrıldıktan sonra, geçmişte karşılaşmış olabilecekleri ya da olmayabilecekleri doğadaki farklı yerlere göç ederler. GTO algoritmasında, tüm goriller aday çözümler olarak görülür ve her optimizasyon operasyon aşamasında en iyi aday çözüm Silverback bir goril olarak kabul edilir. *Exploration* aşamasında üç farklı mekanizma kullanılır; bilinmeyen bir yere göç, bilinen bir yere göç ve diğer gorillere doğru olan göç. Bu üç mekanizmanın her biri exploration aşamasını oluşturur ve genel bir prosedüre göre seçilir. p parametresi bu mekanizmaların seçiminde kullanılmak ve random değer random üretilmiş değer olmak üzere: İlk mekanizma random değer<p olduğunda seçilir. Ve de eğer random değer>= 0.5 ise diğer gorillere doğru hareket mekanizması seçilir. Eğer random değer < 0.5 ise bilinen bir yere göç mekanizması seçilir. İlk mekanizma, algoritmanın tüm sorun alanını iyi izlemesini mümkün kılar, ikinci mekanizma GTO keşif performansını iyileştirir ve nihayetinde, üçüncü mekanizma, GTO'nun yerel optimal noktalardan kaçışını güçlendirir. Keşif aşamasında kullanılan üç mekanizmanın simülasyonu için  denklem 1 kullanılmıştır.
                                             
                                    ***Denklem 1***:
                                        GX(t + 1) = {
                                        (UB - LB) × r₁ + LB,                  eğer rand < p
                                        (r₂ - C) × Xr(t) + L × H,             eğer rand ≥ 0.5
                                        X(i) - L × (L × (X(t) - GXr(t)) + r₃ × (X(t) - GXr(t))), eğer rand < 0.5
                                    }
                                    ***C, F, L değerleri***:
                                        C = F × (1 - It/MaxIt)
                                        F = cos(2 × r₄) + 1
                                        L = C × l
                                    ***H, Z değerleri***:
                                        H = Z × X(t)
                                        Z = [-C, C]

Birliklerin yiyecek kaynakları bulmak için çeşitli bölgelere gitmekte tüm emirleri takip etmesiyle *exploitation* aşaması gerçekleşir. Ayrıca, üyeler grup hareketinde tüm grup üyelerini etkileyebilir. Bu strateji, C>=W  seçildiğinde seçilir. Bu davranışı simüle etmek için denklem 7 kullanılır. Bir süre sonra, genç goriller ergenlik çağına geldiğinde, yetişkin dişileri seçmek için grubunu genişleten diğer erkek gorillerle savaşırlar ve bu rekabet eğer C<W ise gerçekleşir, bu durum denklem 10 ile simüle edilmiştir.

                                    ***Denklem 7***:
                                        GX(t + 1) = L × M × (X(t) - Xsilverback) + X(t)
                                        M = (|1/N ∑(i=1 to N) GXi(t)|^g)^(1/g)
                                        g = 2^
                                    ***Denklem 10***: 
                                        GX(i) = Xsilverback - (Xsilverback × Q - X(t) × Q) × A
                                        Q = 2 × r₅ - 1
                                        A = β × E
                                        E = {
                                        N₁, eğer rand ≥ 0.5
                                        N₂, eğer rand < 0.5
                                    }

Sonuç: GTO, geniş boyutlarda performans göstererek, kabul edilebilir bir arama yeteneği seviyesine ulaşmayı başarmıştır. Ayrıca, diğer optimizatörlere göre tüm karşılaştırılabilir boyutlarda önemli bir avantaja sahiptir, çünkü diğer karşılaştırılabilir optimizatörler boyutlar arttıkça performanslarını önemli ölçüde azaltır. Ölçeklenebilirlik testleri temelinde, GTO'nun büyük ölçekli sorunlar karşısında keşif ve sömürü yeteneklerini dengeleme konusunda mükemmel bir yeteneğe sahip olduğu görülmüştür.

Referanslar: Benyamin Abdollahzadeh, Farhad Soleimanian Gharehchopogh. Artificial gorilla troops optimizer
