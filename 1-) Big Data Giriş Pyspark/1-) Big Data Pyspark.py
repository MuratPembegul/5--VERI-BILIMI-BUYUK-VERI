from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# 🔥 Spark oturumu başlat
spark = SparkSession.builder.appName("BigDataAnalysis").getOrCreate()

# 📂 CSV dosyasını oku
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# 📌 Veriyi göster
df.show()

# 📊 Ortalama harcama puanı hesapla
df.select(avg("Spending_Score")).show()

# 📌 Yaşı 30’dan büyük olan müşterileri filtrele
df.filter(col("Age") > 30).show()

# 🛑 Spark’ı kapat
spark.stop()
