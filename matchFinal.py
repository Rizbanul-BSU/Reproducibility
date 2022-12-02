import hashlib
import sys
from importlib.resources import path
from pymongo import MongoClient

#function definition

"""
    This function stores the hash  
    to the mongoDB database

    """
def check_hash(fileHash):
    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
    except:  
        print("Could not connect to MongoDB")
    
    # Access database
    mydatabase = client['hash'] # If not already created, a new database will be created
    
    # Access collection of the database
    mycollection=mydatabase['files']

    item_details = mycollection.find()
    val = False
    for item in item_details:
        if(item['Hash'] == fileHash):
            val = True
    if(val):
        print("Hash Matches")
    else:
        print('Hash does not match')

    client.close()

#function definition
"""
    This function generates hash for given file 
    
    """
def read_file(file_path):
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)


path = sys.argv[1]
sha256_hash = hashlib.sha256()

read_file(path)
check_hash(sha256_hash.hexdigest())




