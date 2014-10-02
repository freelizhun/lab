import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure
"""
16         user_doc = {
 17                 "username" : "%s"%s,
 18                 "firstname" : "ka",
 19                 "surname" : "DDDDDDD",
 20                 "dateofbirth" : datetime(1974, 4, 12),
 21                 "email" : "wcm",
 22                 "score" : 1
 23                 }

"""
def main():
    try:
        #c = Connection(host="localhost", port=27017)
        c = Connection(host="127.0.0.1", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["test"]
    assert dbh.connection == c
    print '-------  use find one --------------'
    user_doc = dbh.users.find_one({"username" : "aaaaaa"})
    print user_doc
    print user_doc.get('email')
    print '---------  use find ------------------'
    users = dbh.users.find({'firstname':'ka'})
    print users.count()
    for user in users:
        print user.get('email')
    #users = dbh.users.find({'firstname':'Jane'})
    print '--------   use email ---------'
    users = dbh.users.find({'email':'wcm'})
    print users.count()
    for user in users:
        print user.get('username')
    if not user_doc:
        print "no document found for username janedoe"
if __name__ == "__main__":
    main()
