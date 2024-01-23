import pandas as pd

dict = {'name': ['Vishal', 'Sony', 'Pihoo'], 'Batch': ['b1', 'b2', 'b3'], 'age': [40, 13, 9]}
list = [1, 2, 3, 4]
print(dict)

df = pd.DataFrame(dict)

print(type(df))

print(df)

df1 = pd.DataFrame(list, columns=['slno'])

# print(dir(pd.DataFrame))

print(df1)

df3 = pd.read_csv(r'C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv')
print("Top 2 rows")
print(df3.head(2))
print("bottom 3 rows")
print(df3.tail(3))
print("Columns*********************")
print(df3.columns)
print("Datatypes***************")
print(df3.dtypes)
print("DF rows and columns")
print(df3.shape)

df4 = pd.read_csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")
df5 = pd.read_csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info_t.csv")
print("Concat Operation=========================")
df6 = pd.concat([df4, df5], axis=1)
print(df6)

dict2 = {'cust': ['x', 'y', 'z'], 'prod_code': [1, 2, 3]}
dict3 = {'cust': ['a', 'b', 'c', 'z'], 'prod_code': [11, 22, 33, 44]}

df10 = pd.DataFrame(dict2)
df11 = pd.DataFrame(dict3)
print("Concat of 2DF's")
print(pd.concat([df10, df11]))  # vertical join
print("concat of DF's with axis")
print(pd.concat([df10, df11], axis=1))
print("concat of DF's with axis and Join")
print(pd.concat([df10, df11], axis=1, join='inner'))
print("merge of DF's *************")

print(pd.merge(df10, df11, on='cust', how='outer'))
print("@@@@@@@@@@@@@columnwise data@@@@@@@@@@@")
df8 = pd.read_csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")
print(df8.Identifier)  # print(df8['identifier']
print("@@@@@@@@@@@@@ multiple columnwise data using loc function @@@@@@@@@@@")
print(df8.loc[3:6, 'Identifier':'Phone'])
print("@@@@@@@@@@@@@ multiple row/columnwise data slicing using i loc @@@@@@@@@@@")
print(df8.iloc[3:6, 0:5])

from pandasql import sqldf

df9 = sqldf("select identifier,surname from df8")
print("SQL QUERY")
print(df9)
print("Record count")
df21 = sqldf("select count(*) from df8")
print(df21)

import pandas as pd
from ydata_profiling import ProfileReport

df22 = pd.read_csv(r"C:\Users\HP\PycharmProjects\PythonAutomation\source_files\Contact_info.csv")
profile = ProfileReport(df22)
print(profile)
profile.to_notebook_iframe()

profile.to_html()

import os

print(os.getcwd())
profile.to_html()
