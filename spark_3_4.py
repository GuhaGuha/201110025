import findspark
findspark.init("C:\Users\DB400T2A\spark-1.6.0-bin-hadoop2.6")
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
sc._conf.get("spark.jars.packages")

b = ["this is a line","this is another line"]
myrdd2 = sc.parallelize(b)
words = myrdd2.map(lambda x:x.split(' '))
words.collect()
myrdd2.map(lambda x:x.split(' ')).collect()
myrdd2.map(lambda x:x.replace("a","AA")).collect()