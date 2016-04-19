# Implimentation of database access layer
import pandas as pd
from pymongo import MongoClient

def mongo_connect(db, collection):
    client = MongoClient()
    coll = client[db][collection]
    return coll


def kdj_insert(db, collection, data):
    coll = mongo_connect(db, collection)
    coll.insert_one(data)
    return True
