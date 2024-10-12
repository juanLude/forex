from pymongo import MongoClient, errors

from constants.defs import MONGO_CONN_STR

class DataDB:

    SAMPLE_COLLECTION = "forex_sample"

    def __init__(self):
        self.client = MongoClient(MONGO_CONN_STR)
        self.db = self.client.forex_db

    def test_connection(self):
        print(self.db.list_collection_names())