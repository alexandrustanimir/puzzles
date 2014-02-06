# Python distribution containing tools for working with MongoDB
# http://api.mongodb.org/python/current/tutorial.html
import pymongo


def update_indexes():
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    database = client['store']
    collection = database['users']
    idx = list(collection.index_information().keys)[1]
    collection.drop_index(idx)
    collection.create_index('email')
update_indexes()