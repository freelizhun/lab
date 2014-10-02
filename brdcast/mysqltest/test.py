
table = 'ahah'
sql = """CREATE TABLE %s(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(25))"""%table
print sql

