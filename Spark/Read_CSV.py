from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local[1]").appName("csv").getOrCreate()

#df_csv=spark.read.csv("C:\\Users\\HP\\PycharmProjects\\PythonAutomation\\source_files\\Contact_info.csv")
df_csv=spark.read.csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")
#df_csv=spark.read.csv("C:/Users/HP/PycharmProjects/PythonAutomation/source_files/Contact_info.csv")
df_csv.show()

print(df_csv.count())

df_csv.printSchema()

print("***** 2nd Method******")

df_csv2=spark.read.option("header",True).option("inferSchema",True).csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")
df_csv2.show()

print(df_csv2.count())

df_csv2.printSchema()

print("******3rd approch************")
df_csv3=spark.read.format('csv').\
            option("header",True).\
            option("inferSchema",True).\
            load(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")

df_csv3.show()

print(df_csv3.count())

df_csv3.printSchema()
