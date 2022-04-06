#----------------------------------
# IMPORTS
#----------------------------------
## Import Time
import time

## Import pyodbc
import jaydebeapi

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

#----------------------------------
# SETUP
#----------------------------------
## Create JDBC Connection String
connection_string=f"{config.get('JDBC_string', 'OOPS')}username=$token;password={config.get('personalKey', 'OOPS')};ssl=true;"

#----------------------------------
# CREATE CONNECTION AND CURSOR
#----------------------------------

## Establish Connection
conn = jaydebeapi.connect("com.dremio.jdbc.Driver",
                          connection_string,[],config.get("jdbcjar", "oops"))

## Create Cursor
curs = conn.cursor()

#----------------------------------
# RUN QUERY
#----------------------------------

## Send Query
curs.execute("SELECT * FROM \"@dremio.demo@gmail.com\".\"nyc-taxi-data\" limit 100")
curs.fetchall()

#----------------------------------
# Close Connection and Cursor
#----------------------------------

## Close Connection
curs.close()
conn.close()