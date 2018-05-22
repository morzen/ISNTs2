import base64
import socket
import threading
import sys
import os
import random
import json


class Client:

    print("done -- app started")

    key = ()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def offsetFunction(self, inp):
        l = len(inp)
        offset = int(random.randint(1, 20))
        cypher = ""
        for i in range(l):
            n = ord(inp[i])
            cypher += chr(n + offset)
        return (cypher, offset)

    def solveOffset(self, msg, offsetValue):
        msgClear = ""
        l = len(msg)
        for k in range(l):
            n = ord(msg[k])
            msgClear = msgClear + chr(n - offsetValue)
        return msgClear

    # Euclide etendu permmettant de trouver le pgcd mais aussi les coefficient pour trouver les variables qui formeront la somme du pgcd initlal
    def euclide_etendu(self, a, b):

        x = 1
        y = 0
        xx = 0
        yy = 1
        while b != 0:
            q = a // b
            a, b = b, a % b
            xx, x = x - q * xx, xx
            yy, y = y - q * yy, yy

        # Cet algorithme renvoie d’abord le pgcd, puis les coefficients u, v tels que au + bv = pgcd(a, b)
        return(a, x, y)

    def private_key(self, p, q, e):
        n = p * q  # a modifier
        phi = (p - 1) * (q - 1)  # a modifier
        # Pgcd et coeff de Bézout ( voir theoreme )
        c, d, dd = self.euclide_etendu(e, phi)
        return(d % phi)  # Retourne la clé privée

    def crypto(self):

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
        k = self.private_key(p, q, e)
        print("| Clé privée :", k, e)
        return (n, k)

    def chiffrement_dechiffrement(self, m, e, n):
        return((m**e) % n)

    def sendMsg(self):

        while True:
            msg = []
            inp = input()
            l = len(inp)
            # offset msg with offsetFunction (carefull c pa mon code)
            (offsetCypher, offsetValue) = self.offsetFunction(pseudo + " :" + inp)

            # get key public key from self.key  from tuple
            pubKey = self.key[0]
            n = ""
            # crypt msg with chiffrement_dechiffrement (pas mon code nn plus)
            # for i in range(l):
            #    msg.append(self.chiffrement_dechiffrement(
            #        ord(offsetCypher[i]), pubKeyn, n))

            # send key with message in a tuple using json
            self.sock.send(
                bytes(json.dumps((offsetCypher, offsetValue, self.key)), 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        self.key = self.crypto()  # must be tuple (pubKey, privKey)
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            # get sender key tuple from msg by using json.loads on data (you ll have [msg,[pubKey,privKey]] ) )
            # decrypt msg with function from decryptage.py and chiffrement_dechiffrement (carefull c pa mon code)
            data = json.loads(data)
            offsetCypher = data[0]
            offsetValue = data[1]
            keys = data[2]

            msg = offsetCypher

            l = len(msg)
            pubKey = key[0]
            n = ""
            # decrypt msg with chiffrement_dechiffrement (pas mon code )
            # for i in range(l):
            #    msg.append(self.chiffrement_dechiffrement(
            #        ord(msg[i]), pubKeyn, n))

            msg = self.solveOffset(msg, offsetValue)
            print(msg)
            #print(str(msg, 'utf-8'))


print("\n _-_-_-_-_ Welcome to S_Chat _-_-_-_-_ \n")
# here we will do the user checking when the databse will be up- user and mdp in private  - hash in mdb5
print("---To start the client type the address you want---")
typeVar = input()
if(len(typeVar) > 1):
    print("client starting on " + typeVar)
    pseudo = input("enter pseudo : ")

    client = Client(typeVar)
