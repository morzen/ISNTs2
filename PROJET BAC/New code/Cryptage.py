import random

Message_Utilisateur=input("Entrez le mesage à crypter")
Message_Taille=len(Message_Utilisateur)
Message_Crypte=""
Nombre_Decalage=int(random.randint(1,20))

for k in range(Message_Taille):
    n=ord(Message_Utilisateur[k])
    Message_Crypte=Message_Crypte+chr(n+Nombre_Decalage)


print(("Message utilisateur:"),(Message_Utilisateur),"| Décalage :",(Nombre_Decalage),"| Message crypté :",(Message_Crypte))