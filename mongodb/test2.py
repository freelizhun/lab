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
    user_doc = {
            "username" : "janedoe",
            "firstname" : "Jane",
            "surname" : "DDDDDDD",
            "dateofbirth" : datetime(1974, 4, 12),
            "email" : "wcmein",
            "score" : 0
            }
    dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
if __name__ == "__main__":
    main()
