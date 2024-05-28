# Genel Bakış
Ses tanıma sistemleri, insanların konuşmalarını dijital verilere dönüştüren ve bu veriler üzerinde çeşitli analizler yaparak anlam çıkaran teknolojilerdir. Bu sistemler, konuşulan dili algılayarak metne dönüştürme, komutları tanıma ve çeşitli uygulamalarda sesle etkileşimi sağlama gibi işlevler sunar. Ses tanıma sistemleri, konuşma tanıma (speech recognition) ve doğal dil işleme (NLP) alanlarındaki gelişmelere dayanır.

Ses tanıma sistemlerinin geliştirilmesi sırasında karşılaşılan bazı önemli teknik zorluklar vardır. Gürültü ve ortam sesleri, aksan ve diyalekt farklılıkları,  doğru tanıma yapmayı zorlaştırabilir.

<br>

# asag-ilik-vrs Hakkında
asag-ilik-vrs, ses tanıma ve metne dönüştürme işlemlerini gerçekleştiren bir uygulamadır. Kullanıcılar, mikrofon aracılığıyla seslerini kaydedebilir, bu sesleri metne dönüştürebilir ve ses verilerini analiz edebilir. Proje, Python ve Streamlit kullanılarak [Güray DAĞ](https://github.com/leidorf) ve [Veli YARAR](https://github.com/VeliYarar) tarafından geliştirilmiştir.

<br>

# Proje Dosya İçeriği
<ul>
 <li>Ana Sayfa.py: Projenin ana giriş noktasıdır ve ana arayüzü tanımlar.</li>
<li>LICENSE: Proje lisans bilgilerini içerir.</li>
 <li>models: Ses tanıma modeli ve ölçekleyici dosyalarını içerir.</li>
 <ul>
<li>knn_model21.joblib: K-NN modeli.</li>
 <li>scaler21.joblib: Ölçekleyici dosya.</li> 
 </ul>
 <li>pages: Uygulamanın çeşitli sayfalarını barındırır.</li>
 <ul>
  <li>1_Ses Tanıma.py: Ses tanıma ve metne dönüştürme işlemlerini gerçekleştiren sayfa.</li>
  <li>2_Hakkımızda.py: Proje hakkında bilgiler içeren sayfa.</li>
 </ul>
 <li>README.md: Projenin genel tanımı ve kullanım kılavuzu.</li>
 <li>vrs: Ses işleme ve analiz fonksiyonlarını barındıran modüller.</li>
 <ul>
  <li>audio_processing.py: Ses işleme fonksiyonlarını içerir.</li>
  <li>plot_functions.py: Ses verilerini görselleştirme fonksiyonlarını içerir.</li>
  <li>speech_to_text.py: Sesin metne dönüştürülmesi işlemlerini içerir.</li>
 </ul>
 <li>yarn.lock: Proje bağımlılıklarının versiyonlarını kilitleyen dosya.</li>
 <li>requirements.txt: Proje bağımlılıklarını belirten ve kurulumu kolaylaştıran dosya.</li>
</ul>

<br>

# Kurulum ve Gereksinimler
Projenin çalıştırılması için aşağıdaki adımlar izlenmelidir:
## Gereksinimlerin Yüklenmesi
- Python 3.10.14 kurulumu

Proje, Python 3.10.14 sürümünü gerektirmektedir. Python'un bu sürümünü [Python'un resmi web sitesinden](https://www.python.org/downloads/release/python-31014/) indirip kurabilirsiniz.

### Gerekli Python Paketlerinin Yüklenmesi

```pip install -r requirements.txt```

### Streamlit Uygulamasının Başlatılması
Projeyi başlatmak için terminal üzerinden aşağıdaki komutu çalıştırın:

```streamlit run Ana Sayfa.py```

<br>

# Kullanım
## Ana Sayfa
Ana sayfada, kullanıcılar uygulamanın genel tanıtımını ve kullanım talimatlarını görebilirler. Buradan farklı sayfalara yönlendirilirler.

<br>

![Ana Sayfa Ekran Görüntüsü](https://github.com/leidorf/asag-ilik-vrs/assets/93585259/36c74400-0af0-4c87-894c-8a46967ce89c)
**Şekil 1.** Ana Sayfa Ekran Görüntüsü

<br>

## Ses Tanıma Sayfası
- Mikrofonu Aç/Kapat: Mikrofonu açarak ses kaydetmeye başlayabilirsiniz. Ses kaydedilirken, kaydedilen ses metne dönüştürülür ve analiz edilir.
- Mikrofon AÇIK: Ses kaydediliyor ve metin tanınıyor.
- Mikrofon KAPALI: Kaydedilen ses verisi gösteriliyor ve yeni kayıtlar alınabilir.

<br>

![Ses Tanıma Sayfası Ekran Görüntüsü](https://github.com/leidorf/asag-ilik-vrs/assets/93585259/132d72a1-258d-4d86-aadb-9374500a62f5)
**Şekil 2.** Ses Tanıma Sayfası Ekran Görüntüsü

<br>

### Sonuçların Görüntülenmesi
- Tahmin Edilen Ses: Model tarafından tahmin edilen ses kategorisi.
- Tanınan Metin: Metne dönüştürülen ses.
- Toplam Kelime: Tanınan metindeki kelime sayısı.
- Ses Verisi Histogramı: Kaydedilen ses verisinin dalga formu grafiği.

<br>

![Ses Tanıma Sayfası Sonuç Ekran Görüntüsü](https://github.com/leidorf/asag-ilik-vrs/assets/93585259/74ecd634-29c1-48d1-a47f-c1a95c31f531)
**Şekil 3.** Ses Tanıma Sayfası Sonuç Ekran Görüntüsü

<br>

## Hakkımızda Sayfası
Bu sayfa, proje geliştiricileri hakkında bilgi sağlar. Projenin ve geliştirici ekibin GitHub linkini barındırır.

<br>

![Hakkımızda Sayfası Ekran Görüntüsü](https://github.com/leidorf/asag-ilik-vrs/assets/93585259/06c2b038-58d0-4597-b9b9-4f5240b13788)
**Şekil 4.** Hakkımızda Sayfası Ekran Görüntüsü
