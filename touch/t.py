import commands

string='hahahaha'
for i in range(0,10):
    ret = commands.getoutput('touch ./haha')
    ret1 = commands.getoutput('echo %s >> ./haha'%string)
ret2 = commands.getoutput('cat ./haha').split('\n')
print ret2
    
