# Optimizasyon Algoritmaları Ödevi

Bu depo, Optimizasyona Giriş dersi kapsamında öğrencilerin atanan optimizasyon algoritmalarını Python dilinde uygulamaları ve katkıda bulunmaları için oluşturulmuştur.

## Amaç

- Atanan algoritmanın orijinal makalesini incelemek ve anlamak.
- Algoritmanın Python kodunu yazmak ve bu depoya katkıda bulunmak.
- Algoritmanın temel özelliklerini ve çalışma mekanizmalarını açıklayan bir dokümantasyon hazırlamak.
- Git ve GitHub kullanarak gerçek bir yazılım geliştirme sürecini deneyimlemek.


## Katkıda Bulunma Adımları

1. **Depoyu Fork Edin**
   - GitHub hesabınıza giriş yapın.
   - Bu depoyu kendi hesabınıza fork edin.

2. **Depoyu Klonlayın**
   - Terminal veya komut satırını açın.
   - Fork’ladığınız depoyu bilgisayarınıza klonlayın:

   ```bash
   git clone https://github.com/kullanici_adiniz/optimization_algorithms.git
   ```

3. **Yeni Bir Branch Oluşturun**
   - Kendi çalışmanızı yapmak için yeni bir branch oluşturun:

   ```bash
   git checkout -b kullanici_adiniz-algoritma
   ```

4. **Kendi Klasörünüzü Oluşturun**
   - `optimizers` klasörü altında kendi algoritma adınızın büyük harflerle kısaltmasını içeren bir klasör oluşturun:

   ```bash
   mkdir optimizers/PSOgibi
   ```

5. **Kodunuzu ve Dokümantasyonunuzu Ekleyin**
   - optimizers klasörünüzün içine aşağıdaki dosyaları ekleyin:
     - `algorithm.py`: Algoritmanızın Python kodu.
   - documentation klasörünün içine aşağıdaki dosyaları ekleyin
     - `algoritmaAdı_documentation.md`: Algoritmanın dokümantasyonu.

6. **Kod Başlığı**
   - `algorithm.py` dosyanızın başına aşağıdaki formatta bir bilgilendirme yazısı ekleyin (kendi bilgilerinizle güncelleyin):

   ```
   The original version of: [Algoritma Adı]

   # Created by "[Adınız]" on [Tarih] -----------------------------%
   #       Email: [Email Adresiniz]                                %
   #       Github: https://github.com/kullanici_adiniz             %
   # --------------------------------------------------------------%

   Links:
       1. [Orijinal yayının linki]
   References:
       [1] [Orijinal yayının tam referansı]
   ```

7. **Dokümantasyon Hazırlama**
   - `documentation.md` dosyanızda aşağıdaki bölümleri yazın:
     - Giriş
     - Temel Özellikler
     - Konum Güncelleme Denklemleri
     - Keşif ve Sömürü Mekanizmaları
     - Referanslar

8. **Değişikliklerinizi Commit Edin**
   - Değişikliklerinizi kaydedin ve commit edin:

   ```bash
   git add .
   git commit -m "Added [Algoritma Adı] by [Adınız]"
   ```

9. **Fork’unuza Push Edin**
   - Değişikliklerinizi kendi fork’unuza gönderin:

   ```bash
   git push origin kullanici_adiniz-algoritma
   ```

10. **Pull Request Oluşturun**
    - GitHub üzerinde fork’unuza gidin.
    - Ana depoya (hocanın deposuna) pull request gönderin.
    - Pull request açıklamasına çalışmalarınız hakkında bilgi ekleyin.

## Kodlama Standartları ve Kurallar

- **Kod Kalitesi**
  - Temiz, okunabilir ve yorum satırlarıyla desteklenmiş kod yazın.
  - Değişken ve fonksiyon isimlerini anlamlı seçin. Yayının orjinalinde kullanılan parametre isimlerinden (PSO için c1,c2 gibi)

- **Dosya ve Klasör Yapısı**
  - Kendi klasörünüzü `optimizers` klasörü altında oluşturun.
  - Dosya isimlendirmelerinde algoritmanın kısa ismini kullanın ("PSO.py" gibi).

- **Dokümantasyon**
  - Algoritmanın matematiksel denklemlerini ve çalışma prensiplerini detaylı bir şekilde açıklayın.
  - Gerekli görselleri veya denklemleri eklemek için uygun formatlar kullanın (Markdown formatında kullanabilirsiniz).
  - Kullandığınız kaynakları ve referansları eklemeyi unutmayın.

- **Uyumluluk**
  - Kodunuzun, kütüphanede mevcut test fonksiyonlarıyla uyumlu çalışabilmesini sağlayın.
  - Gerekli kütüphane ve bağımlılıkları belirtin.

## Git ve GitHub Kullanımı

- **Fork Etme ve Branch Oluşturma**
  - Depoyu fork ederek kendi GitHub hesabınıza kopyalayın.
  - Her öğrenci kendi repo/branch’inde çalışmalıdır.

- **Commit Mesajları**
  - Anlamlı ve açıklayıcı commit mesajları kullanın ("Added Particle Swarm Optimization by Bahaeddin Türkoğlu" gibi).

- **Pull Request**
  - Pull request açıklamasında yaptığınız çalışmaları ve eklediğiniz özellikleri belirtin.
  - Gerekirse kodunuz hakkında notlar veya açıklamalar ekleyin.


## Teslim Tarihi

- Çalışmalarınızı Final Sınavı saatine kadar gönderiniz.

## İletişim

- **Öğretim Üyesi**: [Bahaeddin Türkoğlu]
- **E-posta**: [turkoglub@ankara.edu.tr]
- **Ofis Saatleri**: [Perşembe 13:00 14:15 ]

## Contributor
- Emre Diş
- Baran Bingöl
- Ural Altan Bozkurt
- Kenan Şentürk
- Mustafa Surhay Samsa


## Başarılar!

