import pymongo
import os
import sys
import pprint

def main():
connection_string = os.environ["MONGO_CONNECTION_STRING"]
db_name = os.environ["MONGO_DBNAME"]

client = pymongo.MongoClient(connection_string)
db = client[db_name]
collection = db['Test'] #1. put the name of your collection in the quotes
post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"]}
#2. add a document to your collection using the insert_one method
post_id = collection.insert_one(post).inserted_id
post_id
#3. print the number of documents in the collection
collection.count_documents({})
#4. print the first document in the collection
pprint.pprint(collection.find_one())
#5. print all documents in the collection
for post in collection.find():
pprint.pprint(post)
#6. print all documents with a particular value for some attribute
for post in collection.find({"author": "Mike"}):
pprint.pprint(post)
#ex. print all documents with the birth date 12/1/1990


if name=="main":
main()
