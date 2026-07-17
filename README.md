# 📊 Verinin Dilinden Eğitim: Öğrenci Sınav Başarısı Analizi

Bu proje, Kaggle üzerinde yer alan popüler "Students Performance in Exams" veri seti kullanılarak, öğrencilerin akademik başarılarını etkileyen faktörleri incelemek amacıyla geliştirilmiş bir **Keşifçi Veri Analizi (EDA)** çalışmasıdır.

Bir matematik öğretmenliği geçmişi ve analitik bakış açısıyla; eğitimdeki sosyo-ekonomik ve pedagojik faktörlerin (hazırlık kursları, aile eğitim durumu, maddi imkanlar) sınav notları üzerindeki etkisini Python kütüphanelerini kullanarak görselleştirdim ve derinlemesine inceledim.

---

## 📌 Proje Kapsamında Yanıt Aranan Sorular
* Matematik, okuma ve yazma notları arasında nasıl bir korelasyon (ilişki) var?
* Sınav hazırlık kursunu tamamlamak öğrencilerin not dağılımını nasıl etkiliyor?
* Öğle yemeği türü (sosyo-ekonomik durum göstergesi) ile akademik başarı arasında bir bağ var mı?
* Cinsiyete göre ders bazlı başarı varyansları ve dağılımları nasıl değişiyor?

---

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler
* **Python 3.x**
* **Pandas & NumPy** (Veri manipülasyonu ve temel istatistiksel özetler)
* **Matplotlib & Seaborn** (Gelişmiş veri görselleştirme, dağılım ve yoğunluk analizleri)
* **Kagglehub** (Veri setinin kütüphane üzerinden dinamik olarak çekilmesi)

---

## 📈 Öne Çıkan Analiz Bulguları

* **Dersler Arası İlişki (Heatmap):** Okuma ve yazma notları arasında son derece yüksek ($r \approx 0.95$) pozitif bir korelasyon bulunurken, matematik notunun bu iki derse olan ilişkisi biraz daha bağımsız bir seyir izlemektedir. Bu durum, sayısal ve sözel becerilerin gelişim süreçlerinin farklılığını istatistiksel olarak doğrulamaktadır.
* **Kursun Gücü (Box Plot):** Sınav hazırlık kursunu tamamlayan öğrencilerin matematik medyan notları, kurs almayan öğrencilere kıyasla bariz şekilde yüksektir. Ayrıca kurs alan öğrencilerin not dağılımı daha dar bir aralıktadır, yani kurs başarıyı daha homojen hale getirmektedir.
* **Sosyo-Ekonomik Faktör (KDE Eğrisi):** Standart öğle yemeği alan öğrencilerin yoğunluk eğrisi, indirimli/ücretsiz yemek alan öğrencilere göre belirgin şekilde sağa (yani yüksek notlara) doğru kaymaktadır. Bu durum, maddi imkanların ve beslenme şartlarının akademik performans üzerindeki doğrudan etkisini göstermektedir.

---

## 🚀 Projeyi Yerelde Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Bu depoyu klonlayın:
   git clone https://github.com/KULLANICI_ADINIZ/student-performance-analysis.git

2. Gerekli kütüphaneleri yükleyin:
   pip install pandas numpy matplotlib seaborn kagglehub

3. Kod dosyasını çalıştırarak analiz adımlarını ve grafikleri inceleyebilirsiniz.

