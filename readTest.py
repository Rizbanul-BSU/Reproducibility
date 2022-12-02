from importlib.resources import path
import pathlib
import os
from pathlib import Path
import hashlib
import sys

#path = pathlib.Path().resolve()
path = sys.argv[0]
# Path.cwd() / 'store'
# print(path)

# Change the directory
#os.chdir(path)



sha256_hash = hashlib.sha256()
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())
  
  
# iterate through all file
# for file in os.listdir():
#     # Check whether file is in text format or not
#     if file.endswith(".pfb"):
#         file_path = f"{path}\{file}"
print(path)
        # call read text file function
read_text_file(path)

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