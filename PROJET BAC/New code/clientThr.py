import base64
import socket
import threading
import sys
import os


class Client:

    print("done -- app started")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def cle_privee(p, q, e):

        n = p * q  # a modifier
        phi = (p - 1) * (q - 1)  # a modifier
        # Pgcd et coeff de Bézout ( voir theoreme )
        c, d, dd = euclide_etendu(e, phi)
        return(d % phi)  # Retourne la clé privée

    def crypto():

        # Calcul clé publique pour ordi 1:
        # L'utilisateur entre p
        p = int(input('Entrez un grand nombre premier P, exemple P=456 : '))
        # L'utilisateur entre q
        q = int(input('Entrez un grand nombre premier Q, exemple Q=654: '))
        e = int(input('Entrez un nombre pour E, exmple E=12: '))
        print("| P=", p, "| Q=", q, "|E=", e, "|")  # L'utilisateur entre e
        n = (p * q)
        phi = (p - 1) * (q - 1)  # a modifier
        print("| N = ", n, "| Phi de n =", phi, "|")
        print("| Clée Publique :", n, e)  # Affiche la clé publique

        # Calcul clé privée pour ordi 2:
        k = cle_privee(p, q, e)
        print("| Clé privée :", k, e)
        return (n, k)

    def chiffrement_dechiffrement(m, e, n):
        return((m**e) % n)

    def sendMsg(self):

        while True:
            inp = input()
            # get key from self.key and select private or public key from tuple
            # crypt msg with function from file Cryptage.py (carefull c pa mon code)
            # send key with message
            self.sock.send(bytes(pseudo + " :" + input(), 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            # get sender key from msg
            # decrypt msg with function from decryptage.py (carefull c pa mon code)
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
    key = crypto()  # must be tuple (pubKey, privKey)
    client = Client(typeVar)
