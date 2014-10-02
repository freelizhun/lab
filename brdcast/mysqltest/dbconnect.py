#!/usr/bin/python

import MySQLdb

mysqlserver = 'localhost'
user = 'root'
password = 'hello'
dbname = 'hostdb6'
table = 'haha'

def create_db():
    print mysqlserver, user, password
    db = MySQLdb.connect(mysqlserver,user,password)
    cursor = db.cursor()
    try:
        sql = """CREATE DATABASE %s"""%dbname
        print sql
        cursor.execute(sql)
    except:
        print 'data bases existed'
    cursor.execute('USE %s'%dbname)
    print 'create table'
    sql = """CREATE TABLE haha(
           Id INT PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(25))"""
    print sql
    try:
        cursor.execute(sql)
    except:
        print 'table existed'

    db.close()



def insert_table():
    db = MySQLdb.connect(mysqlserver,user,password, dbname)
    cursor = db.cursor()
    cursor.execute("""INSERT INTO %s (Name) VALUES ('Jack London')"""%table)
    db.commit()
    db.close()


def show_table():
    db = MySQLdb.connect(mysqlserver,user,password, dbname)

    cursor = db.cursor()
    try:
        cursor.execute('CREATE DATABASE %s'%dbname)
    except:
        print 'data bases existed'

        
    cursor.execute("SELECT * FROM %s"%table)

    rows = cursor.fetchall()

    for row in rows:
        print row 

    db.close()



create_db()
insert_table()
show_table()
