import sys

import configparser

config = configparser.ConfigParser()

# Reading the text file to get the external parameters
config.read_file(open(sys.argv[1]))

# Getting the parameters from text file
API_URL=config.get('My Section','API_URL')
HOST_NAME=config.get('My Section','Host_name')
PORT_No=config.getint('My Section','Port_no')
DB_NAME = config.get('My Section', 'DB_NAME')
COLL_NAME = config.get('My Section', 'COLL_NAME')
CSV_PATH = config.get('My Section', 'CSV_WRITEPATH')




