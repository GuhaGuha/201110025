import findspark
findspark.init("C:\Users\DB400T2A\spark-1.6.0-bin-hadoop2.6")
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
sc._conf.get("spark.jars.packages")

inp_file = sc.textFile("./data/ds_spark_2cols.csv")
numbers_rdd = inp_file.map(lambda line: line.split(','))

numbers_rdd.take(10)