from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSV Okuma").getOrCreate()

# CSV dosyasını oku (örnek: veri.csv diye bir dosya varsa)
df = spark.read.csv("veri.csv", header=True, inferSchema=True)

df.show()
spark.stop()
