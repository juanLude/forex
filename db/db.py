from pymongo import MongoClient, errors

from constants.defs import MONGO_CONN_STR

class DataDB:

    SAMPLE_COLLECTION = "forex_sample"
    CALENDAR_COLLECTION = "forex_calendar"
    INSTRUMENTS_COLLECTION = "forex_instruments"

    def __init__(self):
        self.client = MongoClient(MONGO_CONN_STR)
        self.db = self.client.forex_db

    def test_connection(self):
        print(self.db.list_collection_names())

    def add_one(self, collection, obj):
        try:
            self.db[collection].insert_one(obj)
        except errors.InvalidOperation as error:
            print("add_one error: ", error)
    def delete_many(self, collection, **kwargs):
        try:
            _ = self.db[collection].delete_many(kwargs)
        except errors.InvalidOperation as error:
            print("delete_many error: ", error)
    
    def add_many(self, collection, list_obj):
        try:
            self.db[collection].insert_many(list_obj)
        except errors.InvalidOperation as error:
            print("add_many error: ", error)
    def query_distinct(self, collection, key):
        try:
            result = self.db[collection].distinct(key)
            return result
        except errors.InvalidOperation as error:
            print("query_distinct error: ", error)
    
    def query_single(self, collection, **kwargs):
        try:
            result = self.db[collection].find_one(kwargs, {'_id': 0})
            return result
        except errors.InvalidOperation as error:
            print("query_single error: ", error)

    def query_all(self, collection, **kwargs):
        try:
            data = []
            result = self.db[collection].find(kwargs, {'_id': 0})
            for item in result:
                data.append(item)
            return data
        except errors.InvalidOperation as error:
            print("query_all error: ", error)