
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
                data, addr = sock.recvfrom(1024)
                msge = (str(data))
                length.msge = len(msge)
                msge = msge[2:lenght.msge-1]
                print(msge)
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 1

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = input("Name: ")
while True:
    message = input(alias + "-> ")
    if message != '':
        s.sendto((alias + ": " + message).encode('utf-8'), server)
    tLock.acquire()
    #message = input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)


shudown = True
rT.join()
s.close()
