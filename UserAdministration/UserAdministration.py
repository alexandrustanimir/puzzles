import pymongo
from operator import lt
   
def mainTest(test):
    get_next_chunk(0)

def get_next_chunk(retrieved_so_far):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
  from pymongo import MongoClient
  client = MongoClient('mongodb://db.talentbuddy.co:27017/')
  database = client['tb']
  collection = database['users']
  query = {'mastery': { "$lte": 100,"$gte" :10}}
  selectedItems = collection.find(query).sort("created_date")[retrieved_so_far:retrieved_so_far+20]
  listItems = list(selectedItems)
  for item in listItems:
     print (item['name'])

