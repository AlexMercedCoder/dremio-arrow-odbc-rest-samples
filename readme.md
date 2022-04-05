## Getting Data from Dremio

In this repository you'll find scripts on how to get data from Dremio using Dremio's REST API, ODBC and Arrow. The default scripts are designed to capture the time for these requests.

To customize to your dremio instance create a config.json with the following information:

```json
{}
```

make sure to create and activate a virtual environment and install all the libraries in the requirements.txt.

- go [here to download](https://docs.dremio.com/cloud/client-applications/dremio-drivers/) and install odbc drivers 