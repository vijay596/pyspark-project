from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("read csv").getOrCreate()

df = spark.read.csv("/home/vijay/Downloads/viswanth_sir_tasks/shipment_tracking.csv", header=True, inferSchema=True)
df.show()
