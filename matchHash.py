import hashlib
from numpy import true_divide
 
#filename = input("Enter the input file name: ")
filename = "a.pfb"

sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    #print(sha256_hash.hexdigest())

'''Below are the codes for checking hash to mongoDB database'''

from pymongo import MongoClient #need to install pymongo first [pip install pymongo]

try:
    client = MongoClient("mongodb://127.0.0.1:27017")
    #print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
# Access database
mydb = client['hash'] # If not already created, a new database will be created
  
# Access collection of the database
mycollection=mydb['files']


curHash = sha256_hash.hexdigest()
item_details = mycollection.find()
val = False
for item in item_details:
   if(item['Hash'] == curHash):
       val = True
if(val):
    print("Hash Matches")
else:
    print('Hash does not match')

client.close()