import pandas
import requests
from pymongo import MongoClient

def getApiData(api_url):
    try:
        response = requests.get(api_url).json()
    except:
        print("Internal API error")
    return response

def mongodb_conn(hostname, portno):
    try:
        clientCon = MongoClient(hostname, portno)
        print('****** connection successful ******')
    except ConnectionError:
        print("Could not connect to server")
    return clientCon


def ExtractDB(clientCon, response, DBName, CollName):
    mydb = clientCon[DBName]
    mycol = mydb[CollName]
    try:
        mydb[CollName].create_index([("id", 1)], name="id", unique=True)
        print('***** Index created *****')
    except:
        print('Index already exists')

    for i in response:
        mycol.find_one_and_update(i, {"$set": {"id": i.get("id")}}, upsert=True)
    return mycol


def mongo_export_to_file(mycol, filepath):
    cursor = mycol.find()
    doc_list = []
    for i in cursor:
        doc_list.append(i)

    mongo_docs = list(doc_list)
    # Convert the mongo docs to a DataFrame
    docs = pandas.DataFrame(mongo_docs)

    # export MongoDB documents to a CSV file
    docs.to_csv(filepath, ",", index=False)  # CSV delimited by commas

    print('Data is written to this path  ', filepath)