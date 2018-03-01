#client

import socket
import threading
import time

tLock = threading.Lock()
shutdow = False

def receving(name, sock):
    while not shutdown:
        try:
                tLock.acquire()
                while True:
                        dara, addr = sock.recvfrom(1024)
                        print (str(data))
        except:
                pass
        finally:
                tLock.release()
host = "DESKTOP-52LD1TB"
port = 0

serveur = ('DESKTOP-52LD1TB' , 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target=receving, args = ("RecvThread", s))
rT.start()

alias = input("Name: ")
message = input(alias + "->")
while message != 'q':
    if message != '':
            s.sendto(alias + "; "+ message, server)
    tLock.acquire()
    message = raw_input(alias + "-> ")
    time.sleep(0.2)

shutdown = True
rT.join()
s.close()