#!/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","hello")

# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    cursor.execute('CREATE DATABASE hostdb')
except:
    print 'data bases existed'

cursor.execute('USE hostdb')
    
# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE hosts(
       Id INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(25))"""

cursor.execute(sql)

# disconnect from server
db.close()


#CREATE TABLE example1(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(25));
#INSERT INTO example1 (Name) VALUES ('Hello world');

