# My implimentation of database access layer

import pandas as pd
from pymongo import MongoClient

def mongo_connect(db, collection):
    client = MongoClient()
    coll = client[db][collection]    
    return coll






