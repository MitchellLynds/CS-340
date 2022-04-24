from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, port, database, authDB):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:%s/%s' % (username, password, port, authDB))
        self.database = self.client[database]
    
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Method to implement the R in CRUD. 
    def read(self, query):
        return self.database.animals.find(query, {"_id": False})

# Method to implement the U in CRUD.
    def update(self, query, data):
        if data is not None:
            return self.database.animals.update_many(query,{ '$set' : data}, upsert=False)
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
# Method to implement the D in CRUD.
    def delete(self, query):
        result = self.database.animals.delete_many(query)
        return result
        
        
