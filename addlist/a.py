import socket
hostname = socket.gethostname()

binding_keys=[]
services = ['all','fop','mongodb']
functions=['update_software','sync_software','restart']
#example fop.mon0.function
def getBindingKey():
    for service in services:
        for function in functions:
            print 
            binding_keys.append(service+'.'+function)
            binding_keys.append(service+'.'+hostname+'.'+function)
    return binding_keys        

print getBindingKey()
a = 'a.b.c.d'
s = a.split('.')
print s[0]
print s[-1]

