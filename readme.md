## Getting Data from Dremio (in progress)

In this repository you'll find scripts on how to get data from Dremio using Dremio's REST API, ODBC and Arrow. The default scripts are designed to capture the time for these requests.

**NOTE: Make sure you have the right C++ libraries for ODBC and turbodbc to work correctly, these are listed here: https://turbodbc.readthedocs.io/en/latest/pages/getting_started.html

To customize to your dremio instance create a config.json with the following information:

```json
{
    "personalKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==",
    "projectID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "JDBC_string": "jdbc:dremio:direct=sql.dremio.cloud:443;ssl=true;PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxxxxx;",
    "username": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "jdbcjar": "/xxxxxx/dremio-jdbc-driver-20.1.0-202202061055110045-36733c65.jar"
}
```
*personalKey = personal access token from Dremio Cloud (under account settings)

make sure to create and activate a virtual environment and install all the libraries in the requirements.txt. 

- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`

- go [here to download](https://docs.dremio.com/cloud/client-applications/dremio-drivers/) and install odbc drivers 

## Troubleshooting Tips

#### For ODBC

- make sure unixODBC is installed
- make sure the odbc.ini and odbcinst.ini have the right driver data
- make sure autocommit is on