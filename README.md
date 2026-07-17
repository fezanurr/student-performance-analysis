# 📊 Bir Matematik Öğretmeninin Gözünden: Öğrenci Performans Analizi & EDA

Bu proje, bir **matematik öğretmeni** ve veri analisti adayı olarak, sınıf içerisinde her gün gözlemlediğim pedagojik ve sosyo-ekonomik gerçekleri veri bilimi araçlarıyla doğrulamak amacıyla geliştirilmiştir. 

Kaggle'ın popüler öğrenci performans veri seti üzerinde çalışılarak; cinsiyetin, hazırlık kurslarının, aile eğitim seviyesinin ve en önemlisi sosyo-ekonomik fırsat eşitliğinin sınav başarıları üzerindeki etkisi **Keşifçi Veri Analizi (EDA)** yöntemleriyle görselleştirilmiştir.

---

## 📋 Veri Seti Yapısı ve Özet Bilgiler

Analiz ettiğimiz veri seti toplam **1000 öğrenciye** ait kayıtları içermektedir. Veri setimizde herhangi bir eksik (null) veya tamamen yinelenen (duplicate) satır bulunmamaktadır.

| Sütun Adı | Veri Tipi | Açıklama | Örnek Değerler |
| :--- | :--- | :--- | :--- |
| **gender** | Categorical | Öğrencinin Cinsiyeti | female, male |
| **race/ethnicity** | Categorical | Etnik Köken / Grup | group A, group B, group C |
| **parental level of education** | Categorical | Ebeveyn Eğitim Seviyesi | associate's degree, high school |
| **lunch** | Categorical | Öğle Yemeği Türü (Ekonomik Gösterge) | standard, free/reduced |
| **test preparation course** | Categorical | Sınav Hazırlık Kursu Durumu | none, completed |
| **math score** | Numerical | Matematik Sınav Notu | 0 - 100 arası puan |
| **reading score** | Numerical | Okuma Sınav Notu | 0 - 100 arası puan |
| **writing score** | Numerical | Yazma Sınav Notu | 0 - 100 arası puan |

---

## 🚀 Projenin Öne Çıkan Bulguları (İçgörü Tablosu)

Grafiklerden elde ettiğimiz analitik içgörüleri ve bu içgörülerin eğitim süreçlerindeki karşılıklarını aşağıdaki tabloda özetledik:

| İncelenen Faktör | Kullanılan Grafik | Keşfedilen Analitik Bulgular | Eğitimsel Karşılığı / İçgörü |
| :--- | :--- | :--- | :--- |
| **Genel Başarı** | `Histplot` (Histogram) | Notlar 60-70 bandında tepe yapmış, simetrik bir Gauss dağılımı var. | Sınıf genelinin başarı durumu standart eğitim eğrisine (Çan Eğrisine) tam uyum sağlıyor. |
| **Hazırlık Kursu** | `Boxplot` (Kutu Grafiği) | Kursu tamamlayanların medyan notları bariz şekilde daha yukarıda. | Okul tarafından sağlanan destek kursları başarıyı doğrudan ve olumlu etkiliyor. |
| **Ekonomik Durum** | `Kdeplot` (Yoğunluk) | Standart yemek alanların yoğunluğu yüksek notlarda, indirimli alanlarınki düşük notlarda kümelenmiş. | Sosyo-ekonomik imkanlar ve fırsat eşitliği, akademik başarı üzerinde ciddi bir rol oynuyor. |
| **Dersler Arası İlişki** | `Heatmap` (Isı Haritası) | Okuma ve Yazma arasında **0.95**, Matematik ile aralarında **0.81+** korelasyon var. | Sözel becerisi (okuma/anlama) güçlü olan öğrencilerin yazma ve sayısal başarıları da doğrusal yükseliyor. |

---

## 🎨 Doğru Grafik Standartları (`vmin/vmax` Hassasiyeti)

Bu projede görsel manipülasyonların önüne geçmek için veri görselleştirme standartlarına tam uyum sağlanmıştır. 

> ⚠️ **Kritik Analist Notu:** Isı haritası (Heatmap) çizilirken renk skalası `vmin=0` ve `vmax=1` parametreleriyle sınırlandırılmıştır. Eğer bu sınır konulmasaydı, birbirine çok yakın ve güçlü olan `0.82` ile `0.95` değerleri sanki aralarında uçurum varmış gibi farklı renklerde görünecek ve okuyucuyu yanıltacaktı. Sabit skala sayesinde verinin gerçek gücü dürüstçe yansıtılmıştır.

---

## 🛠️ Kullanılan Teknolojiler

* **Python 3**
* **Pandas & NumPy** (Veri manipülasyonu ve istatistiksel özetler)
* **Matplotlib & Seaborn** (İleri düzey veri görselleştirme)
* **KaggleHub** (Verinin doğrudan kaynağından güvenli şekilde indirilmesi)

---

## 💻 Projeyi Yerelinizde Çalıştırın

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas numpy matplotlib seaborn kagglehub

