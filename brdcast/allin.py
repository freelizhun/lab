import socket
import sys 
import commands
from threading import Thread
import time
import json
import commands
import ConfigParser 
import fcntl
import struct


haaddress = None
isMaster = False

 
def get_my_ip(ifname='eth0'):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def modifyconfig(filename = None, ip =None):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    print config.get('servers','rmq')
    config.set('servers','rmq',ip)
    print config.get('servers','rmq')
    fp = open(filename,'w')
    config.write(fp)
    fp.close()

def connectmq():
    cmd = 'service monga-fcupgrade restart'
    commands.getstatusoutput(cmd)

def client(message, brdcast) :
    global isMaster
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    my_socket.bind(('',8882))
    my_socket.settimeout(3)
    print 'into wait'
    print 'wait ...'
    RecvFlag = False
    counter = 0 
    address = None
    while not RecvFlag and counter <3 :
        try:
            print 'send to:',brdcast
            my_socket.sendto(message, ('%s'%brdcast ,8881))
            message, address = my_socket.recvfrom(8129)
            print address, message
            recv_message =  json.loads(message)
            print recv_message
            print recv_message['rabbitmq']
            modifyconfig('/etc/fcupgrade.conf', recv_message['rabbitmq'])
            connectmq()
            
            RecvFlag = True
        except socket.timeout:
            print 'timeout'
            RecvFlag = False
            counter = counter + 1
            print counter 
    my_socket.close()

    if not RecvFlag:
        isMaster = True
    
    #commands.getoutput('mkdir /root/brdcast')
    if address:
        return address[0]
    return None


def haclient():
    #print message
    global haaddress
    #address= 'haconnect'
    while True:
        if haaddress:
            print 'haclient haaddress',haaddress
            haaddress = client('ha', haaddress)
            print 'ha connected'
        else:
            print 'no ha address'
            haaddress = None
        time.sleep(3)

    print 'ha crashed'
        
        
    
def server():
    global haaddress
    global isMaster
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    my_socket.bind(('',8881))

    #t = Thread(target=haclient)
    #time.sleep(1)
    #t.start()
    print 'start service ...'
    
    modifyconfig('/etc/fcupgrade.conf', get_my_ip())
    connectmq()
    while True :
        message , address = my_socket.recvfrom(8192)
        print 'message (%s) from : %s' % ( str(message), address[0])
        print 'server recv',message
        if message == 'broadcast':
            if isMaster:
                jsonsend = {'rabbitmq':get_my_ip()}
                #my_socket.sendto("respbroadcast",(address[0], 8882))
                
                my_socket.sendto(json.dumps(jsonsend) ,(address[0], 8882))
                print 'adding client to ha'
                # isMaster connects to last jointer
                haaddress = address[0]
                print haaddress
        #here is ha
        else:
            #my_socket.sendto("hahah",(address[0], 8882))
            print 'get ha ip:',address[0]
            my_socket.sendto("resphaha",(address[0], 8882))
            haaddress = address[0]
            print haaddress
        #show_message('message from :'+ str(address[0]) , message)


#if len(sys.argv) < 2 : 
#    print 'use: python tomboy_client.py "message"'
#else :
haaddress = client('broadcast','<broadcast>')
print 'haaddress',haaddress
if not haaddress:
    server()

