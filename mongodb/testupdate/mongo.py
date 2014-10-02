import datetime

from pymongo import Connection
con = Connection()
db = con.test
posts = db.post
print posts
post2 = {"title":"Python and MongoDB",
        "_id":"aaa",
          "slug":"python-mongodb",
          "author":"SErHo",
          "content":"Python and MongoDB....",
         "tags":["Python","MongoDB"],
          "time":datetime.datetime.now(),
          "_loc":[]}

post1 = {"title":"Python and MongoDB",
        "_id":"bbb",
          "slug":"python-mongodb",
          "author":"SErHo",
          "content":"Python and MongoDB....",
         "tags":["Python","MongoDB"],
          "time":datetime.datetime.now()}
#posts.insert(post2)
#posts.insert(post1)

count = posts.count()
print count
#for post in posts:
#    print post
post = posts.find_one({"slug":"python-mongodb"})
print post
postss = posts.find()
print ' ----get all------------'
for post in postss:
    print post
print ' ----get from id -------'
post = posts.find_one({"_id":"aaa","author":"SErHo"})
print post
print '----up date aaa -----------'
a ={"lat":"23.11","log":"123.33"}
#posts.update({"_id":"aaa"},{'$push':{'_loc':"test"}})
posts.update({"_id":"aaa"},{'$push':{'_loc':a}})
post = posts.find_one({"_id":"aaa"})
print post

