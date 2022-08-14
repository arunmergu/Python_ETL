import pandas
import requests
from pymongo import MongoClient


class etlpipe:

    def getApiData(api_url):
        try:
            # Extracting the data from api
            response = requests.get(api_url).json()
        except:
            print("Internal API error")
        return response

    def mongodb_conn(hostname, portno):
        try:
            # Creating Mongo Client Connection
            clientCon = MongoClient(hostname, portno)
            print('****** connection successful ******')
        except ConnectionError:
            print("Could not connect to server")
        return clientCon

    def ExtractDB(clientCon, response, DBName, CollName):
        # Data Base and collection name given otherwise it will create
        mydb = clientCon[DBName]
        mycol = mydb[CollName]
        try:
            # Creating the index for fast retrival and to avoid inserting duplicates
            mydb[CollName].create_index([("id", 1)], name="id", unique=True)
            print('***** Index created *****')
        except:
            print('Index already exists')

        for i in response:
            # Updating the records, if not it will insert the records based on index created id
            mycol.find_one_and_update(i, {"$set": {"id": i.get("id")}}, upsert=True)
        return mycol

    def mongo_export_to_file(mycol, filepath):

        # Getting the data in collection
        cursor = mycol.find()

        doc_list = []

        # Adding the documents in list to pass this list to  create dataframe
        for i in cursor:
            doc_list.append(i)

        # Convert the doc_list to a DataFrame
        docs = pandas.DataFrame(doc_list)

        # export MongoDB documents to a CSV file
        docs.to_csv(filepath, ",", index=False)  # CSV delimited by commas

        print('Data is written to this path  ', filepath)
