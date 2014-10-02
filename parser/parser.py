
def data_parser(text, dic):
    for i, j in dic.iteritems():
        print i,j
        text = text.replace(i,j)
    return text

inputfile = open('test.dat')
outputfile = open('test.csv', 'w')
#reps = {'"NAN"':'NAN', '"':'', '0-':'0,','1-':'1,','2-':'2,','3-':'3,','4-':'4,','5-':'5,','6-':'6,','7-':'7,','8-':'8,','9-':'9,', ' ':',', ':':',' }
reps = {'"test"':'haha'}

#for i in range(4): inputfile.next() # skip first four lines
for line in inputfile:
    outputfile.writelines(data_parser(line, reps))

inputfile.close()
outputfile.close()
