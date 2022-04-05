## Import Time
import time

## Import pyodbc
import pyodbc

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

token=config.get("personalKey", "personalKey missing from config.json")
connector="Driver={Dremio ODBC Driver 64-bit};ConnectionType=Direct;HOST=sql.dremio.cloud;PORT=443;AuthenticationType=Plain;"
print(connector)



# establist connection
cnxn = pyodbc.connect(connector)

# set encoding
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

# creating a cursor to send messages through the connection
cursor = cnxn.cursor()

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
    print('id:', row.user_id)
    
## Print time it took
print(f"the took {end-begin} seconds to complete query")