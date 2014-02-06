# Python distribution containing tools for working with MongoDB
# http://api.mongodb.org/python/current/tutorial.html
import pymongo


def best_brands():
    # Write your code here
    from pymongo import MongoClient
    client = MongoClient('mongodb://db.talentbuddy.co:27017/')
    database = client['tb']
    collection = database['users']
    selectedItems = collection.aggregate([
                          { "$unwind" : "$brands"},
                          { "$group" : { "_id" : "$brands","number" : {"$sum" : 1}}},
                          { "$sort" : { "number" : -1}},
                          { "$limit" : 3}
                          ])
    #print selectedItems['result']
    for item in list(selectedItems['result']):
        print ("{brand} {number}".format(brand=item['_id'], number=item['number']))
        
