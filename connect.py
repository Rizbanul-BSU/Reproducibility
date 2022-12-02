from pymongo import MongoClient #need to install pymongo first [pip install pymongo]

try:
    client = MongoClient("mongodb://127.0.0.1:27017")
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
# Access database
mydatabase = client['cscorner'] # If not already created, a new database will be created
  
# Access collection of the database
mycollection=mydatabase['students']

item_1 = {
  "_id" : "U1IT00001",
  "Name" : "Riz",
  "ID" : 2,
}

mycollection.insert_one(item_1)


cursor = mycollection.find()
for record in cursor: # prints all the records
    print(record)
client.close()


#The following one returns the database


# from pymongo import MongoClient
# def get_database():
 
#    client = MongoClient("mongodb://127.0.0.1:27017")
 
#    mydatabase = client['cs']
  
#    mycollection=mydatabase['students2']

#    item_2 = {
#     "Name" : "Riz2",
#     "ID" : 22,
#     }

#    mycollection.insert_one(item_2)
 
#    return client['cs']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()
#    print(dbname)