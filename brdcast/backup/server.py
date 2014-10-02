import socket
#import _thread
import time

################################################################################

class Beacon:

    __slots__ = '__sock', '__addr'

    def __init__(self, port):
        "Initialize the beacon for sending and receiving data."
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.__sock.bind(('0.0.0.0', port))
        self.__addr = '255.255.255.255', port

    def __del__(self):
        "Shutdown and close the underlying socket."
        self.__sock.shutdown(socket.SHUT_RDWR)
        self.__sock.close()

    def recv(self, size):
        "Receive a broadcast through the underlying socket."
        return self.__sock.recvfrom(size)

    def send(self, data):
        "Send a broadcast through the underlying socket."
        assert self.__sock.sendto(data, self.__addr) == len(data), \
               'Not all data was sent through the socket!'

    def __gettimeout(self):
        return self.__sock.gettimeout()

    def __settimeout(self, value):
        self.__sock.settimeout(value)

    def __deltimeout(self):
        self.__sock.setblocking(True)

    timeout = property(__gettimeout, __settimeout, __deltimeout,
                       'Timeout on blocking socket operations.')

################################################################################

def test():
    "Test the beacon broadcasting class."
    b = Beacon(50000)
    #_thread.start_new_thread(test_send, (b,))
    test_recv(b)

def test_send1(b):
    "Test the beacon's send method."
    while True:
        #b.send(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()).encode())
        b.send('haha')
        time.sleep(1)
def test_send(b):
        b.send('haha')
        time.sleep(1)

def test_recv(b):
    "Test the beacon's recv method."
    while True:
        data, address = b.recv(1 << 12)
        #test_send('haha')
        print('From: {}\n{}\n'.format(address, data.decode()))
        print 'ready to send'
        b.sendto('haha',(address, 50000))

################################################################################

if __name__ == '__main__':
    test()
