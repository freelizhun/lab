from pymongo import Connection
import pymongo
import datetime
connection=pymongo.Connection('localhost',27017)

db1 = connection.test_database1
collection = db1.test_collection


new_post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
new_post1 = {"author": "NIKE",
            "text": "in the sport",
            "tags": ["jump", "to", "NBA"],
            "date": datetime.datetime.utcnow()}
posts = db1.posts
print posts
posts.insert(new_post)
posts.insert(new_post1)
#print db.collection_names()
print posts.find_one()
for post in posts.find():
        print post
#posts.find({"date": {"$lt": d}}).sort("author")
print posts.count()
