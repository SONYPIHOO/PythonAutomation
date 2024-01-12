from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,IntegerType,StringType
spark =(SparkSession.builder.appName("dataframe").getOrCreate())

dataList=[("Java",20000),("Python",50000)]
schema='Language string, fees string'

df=spark.createDataFrame(data=dataList,schema=schema)
#df.show(n=1,truncate=4)#),vertical=True)
df.show()

data=[(1,'Vishal'),(2,'Kavya')]
schema = StructType([StructField("id",IntegerType(),nullable=False),
                    StructField("name",StringType(), nullable=True)])

df1=spark.createDataFrame(data=data,schema=schema)
df1.show()

df.printSchema()
print("Row_count=",df1.count())
print("Cloumn Data",df1.columns)

for i in df1.columns:
    print(i)
