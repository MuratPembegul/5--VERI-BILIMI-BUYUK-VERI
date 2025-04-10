import mlflow
import mlflow.spark
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

# Spark başlat
spark = SparkSession.builder.appName("MLflowExample").getOrCreate()

# Veri oku
data = spark.read.csv("mlflow_data.csv", header=True, inferSchema=True)

# Özellik vektörü
assembler = VectorAssembler(inputCols=["x1", "x2"], outputCol="features")
data = assembler.transform(data)

# MLflow takibi başlasın
mlflow.set_experiment("BigData_ML_Experiment")

with mlflow.start_run():
    lr = LinearRegression(featuresCol="features", labelCol="target")
    model = lr.fit(data)
    
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.spark.log_model(model, "model")
    mlflow.log_metric("RMSE", model.summary.rootMeanSquaredError)

    print("Model RMSE:", model.summary.rootMeanSquaredError)

spark.stop()

