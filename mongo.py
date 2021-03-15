import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celibrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to the database: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {"first": "douglas", "last": "adams", "DOB": "11/03/1952",
           "hair_color": "grey", "occupation": "writer",
           "nationality": "british"}

coll.insert_one(new_doc)

documents = coll.find({"nationality": "british"})

for doc in documents:
    print(doc)
