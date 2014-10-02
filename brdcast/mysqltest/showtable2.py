#!/usr/bin/python

import MySQLdb


# Open database connection
#db = MySQLdb.connect("localhost","root","hello")
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
cursor.execute("SELECT * FROM hosts")

rows = cursor.fetchall()

for row in rows:
    print row

# Create table as per requirement


# disconnect from server
db.close()


