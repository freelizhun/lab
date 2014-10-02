# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import sys
import os,codecs
#q = pq(url='http://pd.wh.seed.net.tw/fetc/cpc/cpc0331.html')
q = pq(url='http://www.npcgas.com.tw/html/locations/index2.aspx?service=1')

q1 = pq(url='http://www.wdps.ntpc.edu.tw/index.php')
q2 = pq(url='http://tw.yahoo.com/')
#print(q('title').text())
print(q('title').text())
print ('---------------------------')
ss = q('title').find('table').eq(1).text()
counter= 0
for data in q('table'):
    #print counter
    #print q(data).html()
    #for i in range(len(data)):
    #print q(data).find('td').text()
    res = q(data).find('td').eq(2).text().encode('utf-8')
    #print '--------------'
    #print res
    #print '--------------'
    #print res
    resnum2 = res.find('市')
    resnum1= res.find('縣')
    resnum = res.find('號')
    aa1 = resnum * resnum1
    aa2 = resnum * resnum2
    #print resnum1, resnum2
    #print aa1, aa2
    #print '--------------'
    #print resnum
    if resnum>0 and (resnum1 >0 or resnum2> 0):
        print res
    #counter = counter + 1


#print(q1('title').text())
#print(q2('title').text())


#print(q('title').text())
"""
s = q('title').text()
file = codecs.open('new.html', 'w', 'utf-8')
file.write(s)
file.close()

a = "中文"
print a
"""
