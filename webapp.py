import pymongo
import os
import sys
import pprint

from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test'] #1. put the name of your collection in the quotes
    
    #2. add a document to your collection using the insert_one method
    doc = {“key1”:“value1”, “key2”:“value2”}
    collection.insert_one(doc)

    #3. print the number of documents in the collection
    
    #4. print the first document in the collection
    
    #5. print all documents in the collection
    
    #6. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990
    
    
if __name__=="__main__":
    main()
