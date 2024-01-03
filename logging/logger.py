#Levels of logging
# 1. notset (level code - 0)
# 2. debug (level code - 10) - it is purly for devlopper
# 3. info (level code - 20)
# 4. warnings (level code - 30)
# 5.error (level code - 40)
# 6. critical (level code - 50)

import logging

import pandas as pd

logging.basicConfig(filename='loerror.txt',level=logging.CRITICAL,filemode='W')
#default level is set to warning (code-30)
logging.debug("This is debug logger")
logging.info("This is info logger")
logging.warning("This is warning logger")
logging.error("This is error logger")
logging.critical("This is critical logger")

def read_file(path,filtype):
    if file_type=="csv":
        df = pd.read_csv(path)
        print("CSV file read sucessfully ",path)
    elif file_type=='excel':
        df=pd.read_excel(path)
        print("EXCEL file read sucessfully ",path)
    elif file_type=='json':
        df=pd.read_json(path)
          print("JSON file read sucessfully ",path)
    else:
        pass

read_file()
