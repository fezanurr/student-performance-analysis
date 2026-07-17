import kagglehub

# Download latest version
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

print("Path to dataset files:", path)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

print('Kütüphaneler başarıyla yüklendi.')
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)
plt.rcParams["axes.titlesize"] = 15
pd.set_option('display.max_columns', None)

df = pd.read_csv(path+"/StudentsPerformance.csv", sep=",", encoding="utf-8", encoding_errors="replace")

print("İLK 5 SATIR")
display(df.head())

print("\nGENEL BİLGİLER")
df.info()

print(f"\n VERİ SETİ BOYUTU:{df.shape[0]} SATIR, {df.shape[1]} SÜTUNDAN OLUŞUYOR")

print("\nSÜTUN İSİMLERİ:", list(df.columns))
print(display(df.dtypes))

print("\nEKSİK DEĞERLER")
display(df.isnull().sum())

print("\nİSTATİSTİKSEL ÖZET")
display(df.describe())

tam_kopya_sayisi = df.duplicated().sum()
print(f"Tamamen birebir kopya satır sayısı: {tam_kopya_sayisi}")

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="math score", kde=True, color="teal", bins=30)
plt.xlabel("Matematik notu")
plt.ylabel("öğrenci sayısı")
plt.title("MATEMATİK SINAV NOTU DAĞILIMI ")
plt.show()

print("Cinsiyet Dağılımı (Sayısal):")
print(df['gender'].value_counts())

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='gender', palette=['skyblue', 'salmon'])
plt.title("ÖĞRENCİLERİN CİNSİYET DAĞILIMI")
plt.xlabel("Cinsiyet")
plt.ylabel("Öğrenci Sayısı")
plt.show()

print("Cinsiyete Göre Matematik Notu Özet İstatistikleri:")
display(df.groupby('gender')['math score'].describe())

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='gender', y='math score', palette=['skyblue', 'salmon'], width=0.5)
plt.title("Cinsiyete Göre Matematik Notu Dağılımı")
plt.xlabel("Cinsiyet")
plt.ylabel("Matematik Sınav Puanı")
plt.show()

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='test preparation course', y='math score', palette=['orange', 'green'], width=0.4)
plt.title('Sınav Hazırlık Kursunun Matematik Notuna Etkisi')
plt.xlabel('Hazırlık Kursu Durumu')
plt.ylabel('Matematik Puanı')
plt.show()

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='test preparation course', y='reading score', palette=['orange', 'green'], width=0.4)
plt.title('Sınav Hazırlık Kursunun Okuma Notuna Etkisi')
plt.xlabel('Hazırlık Kursu Durumu')
plt.ylabel('Okuma Puanı')
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='math score', hue='lunch', fill=True, palette=['blue', 'orange'], alpha=0.4)
plt.title("Ekonomik Durumun Matematik Notu Yoğunluğuna Etkisi")
plt.xlabel("Matematik Notu")
plt.ylabel("Öğrenci Yoğunluğu")
plt.show()

not_sutunlari = df[['math score', 'reading score', 'writing score']]
korelasyon_matrisi = not_sutunlari.corr()

print("Dersler Arası İlişki Katsayıları:")
display(korelasyon_matrisi)

plt.figure(figsize=(7, 5))
sns.heatmap(korelasyon_matrisi, annot=True, cmap='Blues', vmin=0, vmax=1)
plt.title("Ders Notlarının Birbiriyle İlişkisi (Korelasyon)")
plt.show()
