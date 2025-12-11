from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

old_value = {"level": "Intermediary"}
new_value = {"$set": {"level": "Starter"}}
mycol.update_one(old_value, new_value)

for x in mycol.find():
    print(x)