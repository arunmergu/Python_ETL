# Python_ETL

STEPS REQUIRED TO EXECUTE PYTHON_ETL CODE
-----------------------------------------

1.)Firstly need to download and setup python 3.9 SDK in Intellij

2.)Download libraries using pip install
Below are the libraries need to be installed
requests
configparser
pandas
pymongo

3.) We are creating confile.txt to pass the below parameters 

We are passing config file as argument to main class since we can make changes with our disturbing the code
So, here the main entities which are passed as arguments in config file are

API_URL
Host name
Port name
Data base Name
Collection Name
File path where csv file is exported

*********** Command to execute the Python_ETL **************

Python Python_ETL.py configfile.txt

FUNCTIONALITY OF CODE
---------------------

----> main.py
Is the main class of code where execution starts. We should give config file location as first argument.

----> ETLDemo.py
There is etlpipe class which contains multiple fucntions to have ETL pipeline

getApiData()

It accepts one argument which is api url, which it reads from config file.
It read the data from given api url through requests api and returns JSON object.

mongodb_conn()

It accepts two arguments one is host name and port number.
We use pymongo to install library. We connect to mongoclient.

ExtractDB()

It accepts four arguments one is ClientConn, API Data, Data base name and collection name.
It inserts or update the data in collection with given database and collection name in config file.
we have created index on column id to avoid duplicate insertion.

mongo_export_to_file()

It takes two parameters one is collection name and file location where CSV file need to be saved. It reads from config file.
we are converting the list to pandas dataframe to convert to CSV file.

----> Configfile.py

we are using config parser library to get the parameters from configfile.txt


