
import socket
import threading
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import M2Crypto


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connections = []

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a, key):
        while True:
            data = c.recv(1024)

            decryptor = PKCS1_OAEP.new(key)
            decrypted = decryptor.decrypt(data)
            data = decrypted
            for connections in self.connections:
                print(a)
                print(data)
                if connections != c:

                    connections.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            key = c.recv(1024)
            print(key)

            # generate pub/priv key and sent pub key to client
            random_generator = Random.new().read
            private_key = RSA.generate(1024, random_generator)
            public_key = private_key.publickey()
            c.send(public_key.exportKey())
            # start threads
            cThread = threading.Thread(
                target=self.handler, args=(c, a, private_key))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]), "connected")


print("serveur starting")
server = Server()
server.run()
