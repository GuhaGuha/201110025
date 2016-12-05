import findspark
findspark.init("C:\Users\DB400T2A\spark-1.6.0-bin-hadoop2.6")
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
sc._conf.get("spark.jars.packages")

textFile=sc.textFile("data/ds_spark_wiki.txt")
textFile.take(3)
words = textFile.map(lambda x:x.split(' '))

words.collect()

textFile.map(lambda x:len(x)).collect()
_spark_line = textFile.filter(lambda line:u"½ºÆÄÅ©" in line)
print _spark_line.first()