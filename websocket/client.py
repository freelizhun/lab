import websocket
import time 
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://10.90.1.125:9090/ws")
    #connection the server will return something first
    result = ws.recv()
    print '==initial recive from server==='
    print result

    print '==send arbitrary string and retruen sending string===='
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print '==return sending string ==='
    print("Received {}".format(result))
    
    ws.close()
