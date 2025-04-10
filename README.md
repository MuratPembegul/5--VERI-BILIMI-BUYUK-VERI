# 5--VERI-BILIMI-BUYUK-VERI

# 📊 Büyük Veri (Big Data)

## 📌 Büyük Veri Nedir?
Büyük Veri (**Big Data**), geleneksel veri işleme yöntemleriyle yönetilemeyecek kadar büyük, hızlı ve çeşitli veri kümelerini ifade eder. Genellikle **3V Modeli** ile tanımlanır:

1️⃣ **Hacim (Volume)**: Veri setlerinin çok büyük boyutlarda olması. (Örn: Petabaytlarca veri)
2️⃣ **Hız (Velocity)**: Verinin sürekli ve yüksek hızda üretilmesi. (Örn: Canlı yayınlar, sensör verileri)
3️⃣ **Çeşitlilik (Variety)**: Farklı türlerdeki yapılandırılmış ve yapılandırılmamış verilerin varlığı. (Örn: Metin, görüntü, ses, video, log dosyaları)

Günümüzde bu modele **Değişkenlik (Variability)** ve **Doğruluk (Veracity)** gibi ek özellikler de eklenmektedir.

## 🔥 Neden Büyük Veri Önemlidir?
- **İşletmeler için karar verme süreçlerini iyileştirir.**
- **Makine öğrenmesi ve yapay zeka modellerini besler.**
- **Gerçek zamanlı analizlerle tahminleme yapmayı mümkün kılar.**
- **Sağlık, finans, perakende, üretim gibi birçok sektörde devrim yaratır.**

## 🏗️ Büyük Veri Teknolojileri
Büyük veriyi işlemek için birçok teknoloji kullanılır:

### 1️⃣ **Hadoop Ekosistemi**
🔹 **HDFS (Hadoop Distributed File System)** → Büyük veriyi dağıtarak saklar.  
🔹 **MapReduce** → Büyük ölçekli veri işleme modelidir.  
🔹 **YARN (Yet Another Resource Negotiator)** → Kaynak yönetimi sağlar.  
🔹 **Hive** → SQL benzeri sorgularla büyük veriyi analiz etmeye yarar.  
🔹 **Pig** → Hadoop üzerinde veri akışlarını işlemek için kullanılır.  

### 2️⃣ **Gerçek Zamanlı Veri İşleme**
🔹 **Apache Spark** → Hadoop’a kıyasla daha hızlı işleyebilen bir çerçeve.  
🔹 **Apache Flink** → Gerçek zamanlı veri işleme için optimize edilmiştir.  
🔹 **Apache Storm** → Düşük gecikmeli veri akışı işlemede kullanılır.  

### 3️⃣ **Veri Depolama ve Yönetim**
🔹 **NoSQL Veritabanları** (MongoDB, Cassandra, HBase) → Büyük hacimli verileri esnek bir şekilde saklar.  
🔹 **Amazon S3, Google BigQuery, Azure Data Lake** → Bulut tabanlı büyük veri çözümleri.  

## 🎯 Büyük Veri Kullanım Alanları
📌 **Sağlık**: Hastalık tahmini, genetik analizler, hasta verileri.
📌 **Finans**: Sahtekarlık tespiti, algoritmik ticaret, kredi risk analizleri.
📌 **Perakende**: Müşteri davranış analizleri, kişiselleştirilmiş öneriler.
📌 **Lojistik**: Rota optimizasyonu, tedarik zinciri yönetimi.
📌 **Sosyal Medya**: Trend analizleri, kullanıcı duygu analizi.

## 🚀 Büyük Veri ile Kariyer Olanakları
Büyük Veri alanında uzmanlaşarak şu mesleklerde çalışabilirsin:
- **Veri Bilimcisi (Data Scientist)**
- **Büyük Veri Mühendisi (Big Data Engineer)**
- **Makine Öğrenmesi Uzmanı (ML Engineer)**
- **Veri Analisti (Data Analyst)**

## 🛠️ Uygulama Örneği (Python ile Basit Büyük Veri İşleme)
```python
from pyspark.sql import SparkSession

# Spark oturumu başlat
spark = SparkSession.builder.appName("BigDataExample").getOrCreate()

# Örnek veri yükleme
veri = [(1, "Böcüşü", 100), (2, "Vıccıcık", 200), (3, "Minik Böcüşü", 300)]
kolonlar = ["ID", "Ad", "Puan"]

df = spark.createDataFrame(veri, kolonlar)

# Veriyi göster
df.show()
```

## 📚 Kaynaklar
- [Apache Hadoop Resmi Sitesi](https://hadoop.apache.org/)
- [Apache Spark Resmi Sitesi](https://spark.apache.org/)
- [Google BigQuery](https://cloud.google.com/bigquery)
## Açık Veri Kaynakları
- [Kaggle Veri Setleri](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [AWS Open Data](https://registry.opendata.aws/)

# Güncelleme: Büyük Veri Giriş Pyspark Kodları Eklendi.
# Güncelleme: Büyük Veri Teknolojileri Kodları Eklendi.
# Güncelleme: Dağıtık Veri İşleme Kodları Eklendi.
# Güncelleme: Gerçek Zamanlı Veri Analizi Kodları Eklendi.
# Güncelleme: Büyük Veri Depolama Kodları Eklendi.
# Güncelleme: Veri Akışı İşleme Kodları Eklendi.
# Güncelleme: Büyük Veri ve Makine Öğrenmesi Kodları Eklendi.


