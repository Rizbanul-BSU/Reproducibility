import hashlib
 
#filename = input("Enter the input file name: ")
filename = "b.pfb"
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())

'''Below are the codes for adding hash to mongoDB database'''

from pymongo import MongoClient #need to install pymongo first [pip install pymongo]

try:
    client = MongoClient("mongodb://127.0.0.1:27017")
    #print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
# Access database
mydatabase = client['hash'] # If not already created, a new database will be created
  
# Access collection of the database
mycollection=mydatabase['files']

item_1 = {
  "Hash" : sha256_hash.hexdigest()
}

mycollection.insert_one(item_1)


cursor = mycollection.find()
for record in cursor: # prints all the records
    print(record)
client.close()