Message_A_Drecypte=input("Entrez le mesage a décrypter")
Message_Taille=len(Message_A_Drecypte)
Message_deCrypte=""
Nombre_Decalage=int(input("Entrez le décalage :"))

for k in range(Message_Taille):
    n=ord(Message_A_Drecypte[k])
    Message_deCrypte=Message_deCrypte+chr(n-Nombre_Decalage)


print(("Message utilisateur:"),(Message_A_Drecypte),"| Décalage :",(Nombre_Decalage),"| Message crypté :",(Message_deCrypte))