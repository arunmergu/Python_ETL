import ETLDemo
import Configfile


def main():

    # Calling getApiData and passing the API_URL from configfile
    responseData = ETLDemo.getApiData(Configfile.API_URL)

    # Instantiating the mongodb_conn function with host name and port number from configfile
    mongo_client = ETLDemo.mongodb_conn(Configfile.HOST_NAME, Configfile.PORT_No)

    # Calling the ExtractDB function with mongo_client and response data with Data base and collection name
    coll = ETLDemo.ExtractDB(mongo_client, responseData, Configfile.DB_NAME, Configfile.COLL_NAME)

    # Finally exporting the data to csv file from mongo collection which we inserted data
    ETLDemo.mongo_export_to_file(coll, Configfile.CSV_PATH)


if __name__ == '__main__':
    main()
