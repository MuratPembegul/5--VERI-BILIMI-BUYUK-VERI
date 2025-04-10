from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("DecisionTreeExample").getOrCreate()

data = spark.read.csv("data_classification.csv", header=True, inferSchema=True)

assembler = VectorAssembler(inputCols=["f1", "f2", "f3"], outputCol="features")
data = assembler.transform(data)

classifier = DecisionTreeClassifier(featuresCol="features", labelCol="label")
model = classifier.fit(data)

print(model.toDebugString)

spark.stop()

