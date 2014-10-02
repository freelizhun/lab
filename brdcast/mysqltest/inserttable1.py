#!/usr/bin/python

import MySQLdb


# Open database connection
#db = MySQLdb.connect("localhost","root","hello")
db = MySQLdb.connect("localhost","root","hello", "hostdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    cursor.execute('CREATE DATABASE hostdb')
except:
    print 'data bases existed'

#cursor.execute('USE hostdb')
    
# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
cursor.execute("""INSERT INTO hosts (Name) VALUES ('Jack London')""")
cursor.execute("INSERT INTO hosts (Name) VALUES ('Honore de Balzac')")
cursor.execute("INSERT INTO hosts (Name) VALUES ('Lion Feuchtwanger')")
cursor.execute("INSERT INTO hosts (Name) VALUES ('Emile Zola')")
cursor.execute("INSERT INTO hosts (Name) VALUES ('Truman Capote')")
db.commit()


# disconnect from server
db.close()


#CREATE TABLE example1(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(25));
#INSERT INTO example1 (Name) VALUES ('Hello world');

