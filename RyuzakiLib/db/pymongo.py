from pymongo import MongoClient

class MongoConnect:
    def __init__(
        self,
        mongo_url=None,
        client=None,
        database=None,
        mongodb_connect: bool=None
    ):
        self.mongo_url
        self.client = client
        self.database = database
        self.mongodb_connect = mongodb_connect

    def get_collection(self):
        if self.mongo_url_connect:
            client_mongo = MongoClient(self.mongo_url)
            db = client_mongo[f"{self.client}"]
            collection = db[f"{self.database}"]
            return collection
        else:
            client_mongo = MongoClient(self.mongo_url)
            db = client_mongo["tiktokbot"]
            collection = db["ryuzakilib"]
            return collection
