from pymongo import MongoClient

client = MongoClient()
mybd = client.dbposts
mycol = mybd.posts

post1 = {
    "title": "Pandas",
    "category": "Data Analysis",
    "level": "Intermediary",
    "author": {
        "name": "Joseph",
        "email": "joseph@gmail.com"
    }
}

result = mycol.insert_one(post1)
print("Document successfully inserted.")