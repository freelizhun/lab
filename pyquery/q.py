from pyquery import PyQuery as pq
import urllib2,sys,os
 
d = pq(url='https://www.jpmrich.com.tw/wps/portal')
p = d("a#fundmorelink")
 
#word = 'https://www.jpmrich.com.tw' + p.attr("href")
word = 'https://www.jpmrich.com.tw' 
d = pq(url=word)
s = ""
p = d("tr.table_level_4, tr.table_level_5")
 
s = p.text().split(' ')
print s 
"""
FILE = codecs.open('jpm03.html','w','utf-8')
for i in range(len(s)):
 if i%16 == 0:
       FILE.write(s[i] + ',' + s[i+1] + '\n')       
FILE.close()
"""
