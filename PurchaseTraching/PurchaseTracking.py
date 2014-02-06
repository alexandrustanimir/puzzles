


# Python distribution containing tools for working with MongoDB
# http://api.mongodb.org/python/current/tutorial.html
import pymongo


def store_events(ids):
    # Write your code here
    for item in ids:
        print(item)


def query_purchase(id):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
      from pymongo import MongoClient
      client = MongoClient('mongodb://db.talentbuddy.co:27017/')
      database = client['store']
      collection = database['order']
      collection.find({id}).sum()

store_events({1,2,3,4,5,6})
query_purchase({1})
         

