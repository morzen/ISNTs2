
import socket
import threading
import time
import random


tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1026)
                msge = (str(data))
                length.msge = len(msge)
                msge = msge[2:lenght.msge-1]
                print(msge)
        except:
            pass
        finally:
            tLock.release()


host = '127.0.0.1'
port =  6002

server = ('127.0.0.1',1026)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(server)


#rT = threading.Thread(target=receving, args=("RecvThread",s))
#rT.start()

alias = input("Name: ")
try:
    data, addr = s.recvfrom(1026)
    if(data != (alias + ": " + message).encode('utf-8') ):
        print(data)
except:

    while True:
        message = input(alias + "-> ")
        if message !='':

            s.send((alias + ": " + message).encode('utf-8'))

            time.sleep(0.2)
        try:
            data, addr = s.recvfrom(1026)
            if(data != (alias + ": " + message).encode('utf-8') ):
                print(data)
        except:
            pass
    #message = input(alias + "-> ")


shutdown = False
rT.join()
s.close()
