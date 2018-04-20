
import base64
import socket
import threading
import sys
import hashlib
import os
import M2Crypto
from Crypto.Cipher import AES
import hashlib


class Client:

    M2Crypto.Rand.rand_seed(os.urandom(1024))
    key = M2Crypto.RSA.gen_key(1024, 65537)
    key.save_key('private.pem', None)
    key.save_key('public.pem', None)

    print("done -- app started")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sendMsg(self):

        while True:
            data = input()
            #data = Crypto.rsaEncrypt(self, data)
            self.sock.send(bytes(pseudo + " :" + data, 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))


print("\n _-_-_-_-_ Welcome to S_Chat _-_-_-_-_ \n")
# here we will do the user checking when the databse will be up- user and mdp in private  - hash in mdb5
print("---To start the client type the address you want---")
typeVar = input()
if(len(typeVar) > 1):
    print("client starting on " + typeVar)
    pseudo = input("enter pseudo : ")
    print("Generating a 1024 bit private/public key pair for " + pseudo + " ...")
    client = Client(typeVar)
