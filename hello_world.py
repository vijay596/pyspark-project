from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Hello World!").getOrCreate()

data = [("vijay", 30), ("Ajay", 25)]
column  = ["Name", "Age"]
df = spark.createDataFrame(data, column)
df.show()

