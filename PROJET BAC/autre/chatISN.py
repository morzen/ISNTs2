
import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0',10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connections in self.connections:
                connections.send(data)
            if not data:
                print(str(a[0])+':'+str(a[1]),"disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c,a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon=True
            cThread.start()
            self.connections.append(c)
            print(str(a[0])+':'+str(a[1]),"connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(pseudo + " :" + input(),'utf-8'))

    def __init__(self, address):
        self.sock.connect((address,10000))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon =True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print( str(data, 'utf-8'))

print("\n _-_-_-_-_ Welcome to S_Chat _-_-_-_-_ \n")
#here we will do the user checking when the databse will be up
print("---To start the serveur type hit enter --- \n---To start the client type the address you want---")
typeVar = input()
if(len(typeVar) >1 ):
    print("client starting on "+typeVar)
    pseudo = input("enter pseudo : ")
    client = Client(typeVar)
else:
    print("serveur starting")
    server=Server()
    server.run()
