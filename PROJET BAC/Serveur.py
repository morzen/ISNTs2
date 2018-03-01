#PROJET BAC CHAT 01/03/2018

import socket
host = "DESKTOP-52LD1TB"
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.setblocking(0)


quitting = False
print("server started")

while not quitting :
    try:
            data, addr = s.recvfrom(1024)
            if "quit" in str(data):
                quitting = true
            if addr not in clients:
                clients.appen(addr)

            print (time.ctime(time.time()) + str(addr) + "; ;" + str(data))
            for client in clients:
                s.sendto(dara, client)
    except:
            pass
s.close()


