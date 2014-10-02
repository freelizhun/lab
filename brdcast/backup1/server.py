import socket
#import dbus


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    my_socket.bind(('',8881))

    print 'start service ...'

    while True :
        message , address = my_socket.recvfrom(8192)
        print 'message (%s) from : %s' % ( str(message), address[0])
        my_socket.sendto("hahah",(address[0], 8882))
        #show_message('message from :'+ str(address[0]) , message)
        

if __name__ == "__main__" :
    main()
