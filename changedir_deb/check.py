import os

def getallpackage(path):
    listtarfile = []
    for files in os.listdir("%s"%path):
        if files.endswith(".tar.gz"):
            listtarfile.append(files)
            #print files
    if not listtarfile:
        return False
    return listtarfile

ret = getallpackage('./packages')
if not ret:
    print 'no data'
else:
    print ret
