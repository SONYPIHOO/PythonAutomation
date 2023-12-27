#scenario based simple example

import pandas as pd

source=pd.read_csv("Path")
target=pd.read_csv("Path")

print("SOURCE Details")
print("Number of rows",source.shape[0])
print("Number of Columns",source.shape[1])
print(source.head(2))
print("*"*20)
print("Target Details")
print("Number of rows",source.shape[0])
print("Number of Columns",source.shape[1])
print(source.head(2))

def count_validation(sdata,tdata):
    scount=sdata.shape[0]
    tcount=tdata.shape[0]
    if(scount==tcount):
        print("Count Matched")
    else:
        print("Count not matched"abs(scount-tcount))
