# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import sys
import os,codecs
#q = pq(url='http://pd.wh.seed.net.tw/fetc/cpc/cpc0331.html')
#q = pq(url='http://www.npcgas.com.tw/html/locations/index2.aspx?service=1')
for j in range(1,2):
    precounter = 0
    for i in range(1,2):
        counter = 0
        q = pq(url='http://pd.wh.seed.net.tw/fetc/cpc/cpc0331.html')

        q1 = pq(url='http://www.wdps.ntpc.edu.tw/index.php')
        q2 = pq(url='http://tw.yahoo.com/')
        print(q('title').text().encode('iso-8859-1'))
        print ('---------------------------')
        #os.exit(1)
        ss = q('title').find('table').eq(1).text()
        counter= 0
        #print ss
        for data in q('tr'):
            
            res = q(data).find('td').eq(1).text().encode('iso-8859-1')#.decode('iso-8859-1')
            print res
            resnum2 = res.find('市')
            resnum1= res.find('縣')
            resnum = res.find('號')
            aa1 = resnum * resnum1
            aa2 = resnum * resnum2
            if resnum>0 and (resnum1 >0 or resnum2> 0):
                counter = counter + 1
                print res
                print q(data).find('td').eq(0).text().encode('iso-8859-1')
print counter         




#print(q('title').text())
"""
s = q('title').text()
file = codecs.open('new.html', 'w', 'utf-8')
file.write(s)
file.close()

a = "中文"
print a
"""
