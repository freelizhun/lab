from pyquery import PyQuery as pyq
doc=pyq(url=r'http://list.taobao.com/browse/cat-0.htm')
cts=doc('.market-cat')
 
for i in cts:
    print '====',pyq(i).find('h4').text() ,'===='
    for j in pyq(i).find('.sub'):
        print pyq(j).text() ,
    print '\n'
