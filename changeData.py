import hashlib
import sys
from importlib.resources import path
from pymongo import MongoClient

#function definition

"""
    This function makes connection to mongoDB,
    stores the hash to the database

    """
def store_hash(fileHash):
    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
    except:  
        print("Could not connect to MongoDB")
    
    # Access database
    mydatabase = client['hash'] # If not already created, a new database will be created
    
    # Access collection of the database
    mycollection=mydatabase['files']
    item = {
        "Hash": fileHash[0],
        "Previous_Hash": fileHash[1],
        "Author": fileHash[2],
        "Comment": fileHash[3]
    }

    mycollection.insert_one(item)
    
    print(item)

#function definition
"""
    This function takes file path as input 
    and creates the hash for that file

    """
def read_file(file_path):
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)


path = sys.argv[1]


input = [None]*4
c = 0
with open(path, encoding='utf8') as f:
    for line in f:
        file = line.strip()
        input[c] = file
        c += 1

sha256_hash = hashlib.sha256()
read_file(input[0])
cur = sha256_hash.hexdigest()

sha256_hash = hashlib.sha256()
read_file(input[1])
prev = sha256_hash.hexdigest()

input[0] = cur
input[1] = prev

store_hash(input)



