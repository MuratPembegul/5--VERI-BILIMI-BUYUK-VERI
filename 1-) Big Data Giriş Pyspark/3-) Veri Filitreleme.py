from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Filtreleme").getOrCreate()

veri = [("Murat", 28), ("Ayşe", 35), ("Ahmet", 42)]
sutunlar = ["isim", "yas"]
df = spark.createDataFrame(veri, sutunlar)

# Yaşı 30'dan büyük olanları filtrele
buyukler = df.filter(df.yas > 30)

buyukler.show()
spark.stop()
