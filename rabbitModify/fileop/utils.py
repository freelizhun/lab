
def getQueryStringDict(req):
    def parseQString():
        qs1=QS.split('&')
        #print qs1
        for i in qs1:
            (a,b)=i.split('=')
            yield a,b
    QS = req.environ.get('QUERY_STRING')
    print QS
    if not QS:
        return None
    retDict={}
    for i,j in parseQString():
        retDict[i]=j
    return retDict
    #print retDict
        #print i,j

