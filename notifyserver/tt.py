from Connector.connector import Connector




conn = Connector()
s = conn.readMeta('aaa')
print s
for ii in s:
    print ii
