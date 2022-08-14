# Python_ETL

STEPS REQUIRED TO EXECUTE PYTHON_ETL CODE

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


