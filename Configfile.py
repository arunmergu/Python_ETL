import sys

import configparser

config = configparser.ConfigParser()
config.read_file(open(sys.argv[1]))
API_URL=config.get('My Section','API_URL')
HOST_NAME=config.get('My Section','Host_name')
PORT_No=config.getint('My Section','Port_no')
DB_NAME = config.get('My Section', 'DB_NAME')
COLL_NAME = config.get('My Section', 'COLL_NAME')
CSV_PATH = config.get('My Section', 'CSV_WRITEPATH')




