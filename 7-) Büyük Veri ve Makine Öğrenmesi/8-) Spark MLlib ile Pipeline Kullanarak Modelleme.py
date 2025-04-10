from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Spark başlat
spark = SparkSession.builder.appName("PipelineWithSparkML").getOrCreate()

# Veriyi oku
df = spark.read.csv("veriler/iris.csv", header=True, inferSchema=True)

# Özellikler
features = df.columns[:-1]  # son sütun etiket
label = "label"

# Vektörleştir
assembler = VectorAssembler(inputCols=features, outputCol="raw_features")
scaler = MinMaxScaler(inputCol="raw_features", outputCol="features")
dt = DecisionTreeClassifier(labelCol=label, featuresCol="features")

# Pipeline oluştur
pipeline = Pipeline(stages=[assembler, scaler, dt])
model = pipeline.fit(df)

# Tahmin
preds = model.transform(df)

# Değerlendirme
evaluator = MulticlassClassificationEvaluator(labelCol=label, predictionCol="prediction", metricName="accuracy")
acc = evaluator.evaluate(preds)
print(f"Pipeline ile Başarı: {acc:.2f}")

spark.stop()

