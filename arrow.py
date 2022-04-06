#----------------------------------
# IMPORTS
#----------------------------------
## Import Pyarrow
from pyarrow import flight
from pyarrow.flight import FlightClient

## import pandas
import pandas as pd

## Import Time
import time

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

#----------------------------------
# Setup
#----------------------------------

## Headers for Authentication
headers = [
    (b"authorization", f"bearer {config.get('personalKey', 'oops')}".encode("utf-8"))
    ]

## Create Client
client = FlightClient(location=("grpc+tls://data.dremio.cloud:443"))

#----------------------------------
# Function Definitions
#----------------------------------

## makeQuery function
def make_query(query, client, headers):
    
    sbegin = time.time()
    ## Get Schema Description and build headers
    flight_desc = flight.FlightDescriptor.for_command(query)
    options = flight.FlightCallOptions(headers=headers)
    schema = client.get_schema(flight_desc, options)
    send = time.time()
    print(f"getting schema took {send-sbegin} seconds")
    
    sbegin = time.time()
    ## Get ticket to for query execution, used to get results
    flight_info = client.get_flight_info(flight.FlightDescriptor.for_command(query), options)
    send = time.time()
    print(f"getting ticket took {send-sbegin} seconds")
    
    sbegin = time.time()
    ## Get Results 
    results = client.do_get(flight_info.endpoints[0].ticket, options)
    send = time.time()
    print(f"getting results took {send-sbegin} seconds")
    return results

#----------------------------------
# Run Query
#----------------------------------

begin = time.time() # Start Clock
results = make_query("SELECT * FROM \"@dremio.demo@gmail.com\".\"nyc-taxi-data\" limit 100", client, headers)
end = time.time() # End Clock


print(results.read_pandas())
print(f"Query Completed in {end-begin} seconds")