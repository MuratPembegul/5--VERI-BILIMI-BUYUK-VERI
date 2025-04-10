from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("KMeansExample").getOrCreate()

data = spark.read.csv("kmeans_data.csv", header=True, inferSchema=True)

assembler = VectorAssembler(inputCols=["x", "y"], outputCol="features")
dataset = assembler.transform(data)

kmeans = KMeans(k=3, seed=1)
model = kmeans.fit(dataset)

print("Merkezler:")
for center in model.clusterCenters():
    print(center)

spark.stop()

