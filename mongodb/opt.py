import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure
def main():
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["mydb"]
    assert dbh.connection == c
    user_doc = dbh.users.find_one({"username" : "janedoe"})
    print user_doc
    print user_doc.get('email')
    print '---------  use find ------------------'
    users = dbh.users.find({'firstname':'Jane'})
    print users.count()
    for user in users:
        print user.get('email')
    #users = dbh.users.find({'firstname':'Jane'})
    print '--------   use email ---------'
    users = dbh.users.find({'email':'wcmein'})
    print users.count()
    for user in users:
        print user.get('username')
    if not user_doc:
        print "no document found for username janedoe"
if __name__ == "__main__":
    main()
