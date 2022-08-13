import pandas
import requests
from pymongo import MongoClient

def getApiData():
    try:
        response=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").json()
        print(response['data'][0])
    except:
        print("Internal API error")
    return response

def mongodb_conn():
    try:
        clientCon = MongoClient('localhost', 27017)
    except ConnectionError:
        print("Could not connect to server")
    return clientCon

def ExtractDB(clientCon,response):
    mydb = clientCon["sampleDB"]
    mycol = mydb["sampleColl"]
    mydb["sampleColl"].create_index([("ID Nation",-1)],name="ID Nation")
    mycol.insert_one(response['data'][0])
    return mycol


def mongo_export_to_file(mycol):
    cursor = mycol.find()
    doc_list=[]
    print(type(cursor))
    for i in cursor:
        print(i)
        doc_list.append(i)

    mongo_docs=list(doc_list)
    # Convert the mongo docs to a DataFrame
    docs = pandas.DataFrame(mongo_docs)
    # Discard the Mongo ID for the documents
    print(type(docs))
    docs.info()
    docs.head()

    # export MongoDB documents to a CSV file, leaving out the row "labels" (row numbers)
    docs.to_csv('/users/arunmergu/Documents/mongoexport.csv', ",", index=False) # CSV delimited by commas











