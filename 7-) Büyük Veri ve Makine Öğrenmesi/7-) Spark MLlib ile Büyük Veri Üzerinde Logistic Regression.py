from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Spark oturumu oluştur
spark = SparkSession.builder.appName("LogisticRegressionBigData").getOrCreate()

# Veri setini oku
data = spark.read.csv("veriler/kalp_hastaliklari.csv", header=True, inferSchema=True)

# Özellik sütunları belirleniyor
feature_cols = [col for col in data.columns if col != "target"]

# Vektörleştirme
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(data)

# Veriyi eğitim ve test olarak böl
train, test = data.randomSplit([0.7, 0.3], seed=42)

# Model oluştur
lr = LogisticRegression(featuresCol="features", labelCol="target")
model = lr.fit(train)

# Tahmin yap
predictions = model.transform(test)

# Değerlendirme
evaluator = BinaryClassificationEvaluator(labelCol="target")
accuracy = evaluator.evaluate(predictions)

print(f"Test Başarısı: {accuracy:.2f}")

spark.stop()

