from pymongo import MongoClient
# Connect to database
connection = MongoClient(host="127.0.0.1",port=27017)
print("connection : ",connection)

db = connection['algo_data']
collection = db['tiingo_test']

# Query
# query = collection.find()
# print("query : ",query)
from bson import ObjectId
from pprint import pprint
str1 = "5ac89c9b4b25c8239c8b9201"
str2 = ObjectId("5ac89c9b4b25c8239c8b9201")
print("str1 : ",type(str1))
print("str2 : ",type(str2))
# for doc in collection.find():
for doc in collection.find({"close":85.7}):
    pprint(doc)
    print("*******************************")
    print(type(doc["_id"]))