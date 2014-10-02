import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure
def main():
    try:
        c = Connection(host="127.0.0.1", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["test"]
    assert dbh.connection == c
    
    iii=['aaaaaa','bbba','ccca','ddda','eeea','faff']
    for s in iii:
        user_doc = {
                "username" : "%s"%s,
                "firstname" : "ka",
                "surname" : "DDDDDDD",
                "dateofbirth" : datetime(1974, 4, 12),
                "email" : "wcm",
                "score" : 1
                }
        dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
if __name__ == "__main__":
    main()
