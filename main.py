import ETLDemo

if __name__ == '__main__':
    responseData=ETLDemo.getApiData()
    clientcon=ETLDemo.mongodb_conn()
    coll=ETLDemo.ExtractDB(clientcon,responseData)
    ETLDemo.mongo_export_to_file(coll)
