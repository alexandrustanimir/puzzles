# Python distribution containing tools for working with MongoDB
# http://api.mongodb.org/python/current/tutorial.html
import pymongo

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
database = client['tb']
collection = database['contact']
historycollection = database['h_contact']
def create_contact(author, contact_name, contact_email, contact_birthday):
    # Write your code here
    collection.insert({"author":author,
                      "contact_name":contact_name,
                      "contact_email":contact_email,
                      "birthday":contact_birthday})
    historycollection.insert({"author":author,
                              "field":"contact_name",
                              "email":contact_email,
                              "value":contact_name })
    historycollection.insert({"author":author,
                              "field":"contact_email",
                              "email":contact_email,
                              "value":contact_email })
    historycollection.insert({"author":author,
                              "field":"birthday",
                              "email":contact_email ,
                              "value":contact_birthday})



def edit_contact(author, contact_email, field, value):
    # Write your code here
    item = list(collection.find({"contact_email" : contact_email}))[0]
    item[field] = value
    item['author']=author
    collection.save(item)
    historycollection.insert({"author":author,
                              "field":field,
                              "email":contact_email ,
                              "value":value})
    
    
    

def field_history(contact_email, field):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    items = list(historycollection.find({"email":contact_email,"field":{'$regex':field}}).sort('contact_name'))
    for item in items:
        print(item['author'] + ' ' + item['value'])

def get_birthdays(month):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    strMonth = str(month)
    if len(strMonth) == 1:
        strMonth = strMonth.zfill(2)
    strMonth = '-' + strMonth+'-'    
    items = list(collection.find({"birthday":{'$regex': strMonth}}))
    for item in items:
        print(item['contact_name'])
collection.remove()
historycollection.remove()
create_contact("Jayce","Andrei Soare","andrei@talentbuddy.co","1989-01-01")
create_contact("John","Vlad Berteanu","vlad@talentbuddy.co","1989-01-02")
edit_contact("Mia","andrei@talentbuddy.co","birthday","1989-03-03")
edit_contact("Mia","andrei@talentbuddy.co","birthday","1989-04-04")
field_history("andrei@talentbuddy.co","birthday")
field_history("vlad@talentbuddy.co","email")
get_birthdays(4)    
get_birthdays(1)

