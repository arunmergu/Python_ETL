import ETLDemo
import Configfile

def main():
    responseData=ETLDemo.getApiData(Configfile.API_URL)
    clientcon=ETLDemo.mongodb_conn(Configfile.HOST_NAME,Configfile.PORT_No)
    coll=ETLDemo.ExtractDB(clientcon,responseData,Configfile.DB_NAME,Configfile.COLL_NAME)
    ETLDemo.mongo_export_to_file(coll,Configfile.CSV_PATH)

if __name__ == '__main__':
    main()