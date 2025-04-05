from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Ortalama Yaş").getOrCreate()

veri = [("Murat", 28), ("Ayşe", 35), ("Ahmet", 42)]
sutunlar = ["isim", "yas"]
df = spark.createDataFrame(veri, sutunlar)

ortalama_yas = df.agg(avg("yas"))
ortalama_yas.show()

spark.stop()

