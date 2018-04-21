
import socket
import threading
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
#import M2Crypto


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sendMsg(self, key):
        while True:
            # print(key)
            encryptor = PKCS1_OAEP.new(key)
            encrypted = encryptor.encrypt(
                bytes(pseudo + " :" + input(), 'utf-8'))

            self.sock.send(encrypted)

    def __init__(self, address):

        self.sock.connect((address, 10000))
        # create client pub/priv key
        random_generator = Random.new().read
        private_key = RSA.generate(1024, random_generator)
        public_key = private_key.publickey()
        # send pub key to server
        self.sock.send(public_key.exportKey())

        # receive public server key
        key = self.sock.recv(1024)
        # print(key)

        # Convert string to key
        server_public_key = RSA.importKey(key)
        # print(server_public_key)

        iThread = threading.Thread(
            target=self.sendMsg, args=(server_public_key,))
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            # decode msg
            decryptor = PKCS1_OAEP.new(private_key)
            decrypted = decryptor.decrypt(data)
            data = decrypted
            data = data.decode('utf-8')
            print(data)


print("\n _-_-_-_-_ Welcome to S_Chat _-_-_-_-_ \n")
# here we will do the user checking when the databse will be up- user and mdp in private  - hash in mdb5
print("---To start the client type the address you want---")
typeVar = input()
if(len(typeVar) > 1):
    print("client starting on " + typeVar)
    pseudo = input("enter pseudo : ")
    client = Client(typeVar)
