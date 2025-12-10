from pymongo import MongoClient

client = MongoClient()
mybd = client.dbposts
mycol = mydb.posts 

post1 = {
    "title": "FastAPI",
    "category": "Backend",
    "author": {
        "name": "John",
        "email": "john@gmail.com"
    }
}

result = mycol.insert_one(post1)
print("Document successfully inserted.")