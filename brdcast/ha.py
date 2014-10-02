import socket
import sys 
import commands
def main(message) :
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    my_socket.bind(('',8882))
    my_socket.settimeout(3)
    print 'into wait'
    print 'wait ...'
    RecvFlag = False
    counter = 0 
    while not RecvFlag and counter <10 :
        try:
            #my_socket.sendto("wearetherock", ('<broadcast>' ,8881))
            my_socket.sendto("wearetherock", ('192.168.95.209' ,8881))
            message, address = my_socket.recvfrom(8129)
            print address, message
            RecvFlag = True
        except socket.timeout:
            print 'timeout'
            RecvFlag = False
            counter = counter + 1
            print counter 
    my_socket.close()
    commands.getoutput('mkdir /root/brdcast')

if len(sys.argv) < 2 : 
    print 'use: python tomboy_client.py "message"'
else :
    main(sys.argv[1])

