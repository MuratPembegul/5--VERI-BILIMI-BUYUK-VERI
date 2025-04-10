from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# Spark başlat
spark = SparkSession.builder.appName("RandomForestExample").getOrCreate()

# Veri oku
df = spark.read.csv("randomforest_data.csv", header=True, inferSchema=True)

# Özellikleri birleştir
assembler = VectorAssembler(inputCols=["age", "income", "score"], outputCol="features")
df = assembler.transform(df)

# Model
rf = RandomForestClassifier(featuresCol="features", labelCol="label", numTrees=10)
model = rf.fit(df)

# Tahminler
predictions = model.transform(df)
predictions.select("label", "prediction").show()

spark.stop()

