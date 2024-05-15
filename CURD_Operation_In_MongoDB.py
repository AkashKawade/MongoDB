import pymongo

if __name__ == "__main__":

# Connect MongoDB to Python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
# Create Database
    db = client['Akash']

# Create Connection
    connection = db['Info']

# Insert Documents
    # One
    dict1 = {"Name":"Akash","Location":"Pune","Gender":
             "Male","Roll no":10}
    connection.insert_one(dict1)

    # Many 
    dict2 = ([
        {"Name":"Akash","Location":"Pune","Gender":"Male","Roll no":10},
        {"Name":"Siddesh","Location":"Pune","Gender":"Male","Roll no":20},
        {"Name":"Varun","Location":"Mumbai","Gender":"Male","Roll no":25}
        ])

    connection.insert_many(dict2)
    
# Read Documents
    # All
    All_docs = connection.find()
    for items in All_docs:
        print(items)

    # Specific
    print("For Specific")
    docs = connection.find_one({"Name":"Siddesh"})
    print(docs)

# Uodate 
    # One
    connection.update_one({"Name":"Akash"},{'$set':{"Location":"Ozar"}})

    # Many
    connection.update_many({"Name":"Akash"},{"$set":{"Roll no":5}})

# Delete
    # One
    connection.delete_one({"Name":"Varun"})

    # Many
    connection.delete_many({"Name":"Varun"})

    
# Export Database
  # mongodump
  # run on cmd
    # mongodump ---> for export all database

    # mongodump -d databasename --->for Specific database

    # mongodump -d databasename -c connectionname --->for specific connection


# Import
  # mongorestore
  # run on cmd
    # mongorestore -d newdatabasename pathofdatabase --->import database

    # mongorestore -d newdatabasename -c newconnectionname pathofconnection --->import single connection