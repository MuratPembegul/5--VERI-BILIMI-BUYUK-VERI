from pyspark.sql import SparkSession

# Spark oturumu başlat
spark = SparkSession.builder.appName("MinikBöcüşSpark").getOrCreate()

# Basit veri oluştur
veri = [("Murat", 30), ("Böcüş", 25), ("Minik", 20)]
df = spark.createDataFrame(veri, ["İsim", "Yaş"])

# 25 yaş üstünü filtrele
df.filter(df["Yaş"] > 25).show()

