
#PROJET BAC CHAT 01/03/2018

import socket
import time

host = '127.0.0.1'
port = 1026


clients = [];

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))


quitting = False
print ("Server Started.")
while not quitting:
    try:
        data, addr = s.recvfrom(1026)
        print (time.ctime(time.time()) + str(addr) + ": :" + str(data))

        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
            print(clients)
        for client in clients:
            print(client)
            if(client != addr):
                s.sendto(data,client)

    except:
        pass
s.close()
