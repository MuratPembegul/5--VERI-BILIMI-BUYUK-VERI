from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

# Spark oturumu
spark = SparkSession.builder.appName("LinearRegressionExample").getOrCreate()

# Veri seti
data = spark.read.csv("data.csv", header=True, inferSchema=True)

# Özellikleri vektöre çevir
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
output = assembler.transform(data)

# Model
lr = LinearRegression(featuresCol='features', labelCol='label')
lr_model = lr.fit(output)

print("Katsayılar:", lr_model.coefficients)
print("Kesim noktası:", lr_model.intercept)

spark.stop()

