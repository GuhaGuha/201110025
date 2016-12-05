import findspark
findspark.init("C:\Users\DB400T2A\spark-1.6.0-bin-hadoop2.6")
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
sc._conf.get("spark.jars.packages")

c=list([39.2,36.5,37.3,37.0])
def c2f(c):
    f=list()
    for x in c:
        _c = 9./5*x+32
        f.append(_c)
    return f
print c2f(c)
def c2f_(c):
    return 9./5*c+32

map(c2f_,c)
map(lambda c:(float(9)/5)*c+32,c)