#----------------------------------
# IMPORTS
#----------------------------------

## Import Time
import time

## Import pyodbc
import pyodbc

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

#----------------------------------
# SETUP
#----------------------------------

token=config.get("personalKey", "personalKey missing from config.json")
connector="Driver={Dremio ODBC Driver 64-bit};ConnectionType=Direct;HOST=sql.dremio.cloud;PORT=443;AuthenticationType=Plain;" + f"UID=$token;PWD={token};ssl=true;"

#----------------------------------
# CREATE CONNECTION AND CURSOR
#----------------------------------

# establist connection
cnxn = pyodbc.connect(connector, autocommit=True)

# set encoding
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

# creating a cursor to send messages through the connection
cursor = cnxn.cursor()

#----------------------------------
# RUN QUERY
#----------------------------------

## Start Clock
begin = time.time()

## run a query
cursor.execute("SELECT * FROM \"@dremio.demo@gmail.com\".\"nyc-taxi-data\" limit 100")

## End Clock Clock
end = time.time()

## Print results of query
while True:
    row = cursor.fetchone()
    if not row:
        break
    print(row)
    
## Print time it took
print(f"took {end-begin} seconds to complete query")