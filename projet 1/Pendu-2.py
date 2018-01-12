#Pendu Barnabé et Martin

from random import *

#compte le nbr de character ds le mot et le rend en tiret
def affichage(l):
    k=len(l)
    s=[]
    for i in range(k):

        if l[i] == " " :
            s.append(" ")
        else:
            s.append("-")

    return s


#Fonction permettant de trouver le mot dans la liste
def letter(x,c,l,y): #numb=letter(lettre,credit,mystere,mot)

    m = []
    for pos, char in enumerate(l):
         if char == x:
            m.append(pos)

    return m

#Fonction permettant d'enelever un credit si le joueuer n'a pas saisit une lttre correcte
def modifcredit(d):
    d = d-1
    return d


def replace (n,y,x,d):
    l=len(n)
    if l == 0 :
        c = modifcredit(d)
        return(y,c)
    else:
        for i in range(l):
            k=n[i]
            y[k]=x
        return (y,d)



#(neword,credit)=replace(numb,mot,lettre,credit)
#final = ' '.join(neword)


def verif (y):
    l=len(y)

    for i in range(l):
        if y[i] == "-":
            return True
    return False

#Fonction permettant de choisir le themes du mot a trouver
def mysteret() :
    choix=''
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||| Sport    : 1  || Outils    : 2 ||||||")
    print("|||||| Métier   : 3  || Pays      : 4 ||||||")
    print("|||||| Couleur  : 5  || Entrez votre  ||||||")
    print("|||||||||||||||||||||||      mot : 6  ||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")


    liste1=("natation", "football" , "tennis")
    liste2=("perceuse", "marteau", "scie")
    liste3=("pompier", "informaticien", "astronaute")
    liste4=("France","Russie","Chine")
    liste5=("Noir","Blanc","Bordeux")

    x=True
    while x==True :
        choix=int(input("Quelles theme voulez vous pour le mot ?"))
        if choix==1 :
            mot=choice(liste1)
            x=False
        if choix==2 :
            mot=choice(liste2)
            x=False
        if choix==3 :
            mot=choice(liste3)
            x=False
        if choix==4 :
            mot=choice(liste4)
            x=False
        if choix==5 :
            mot=choice(liste5)
            x=False
        if choix==6 :
            mot=input("Entrez votre mot")
            mot=mot.lower()
            mot=mot.replace("é","e")
            mot=mot.replace("è","e")
            mot=mot.replace("à","a")
            mot=mot.replace("â","a")
            mot=mot.replace("ç","c")
            mot=mot.replace("ê","e")
            mot=mot.replace("î","i")
            mot=mot.replace("ô","o")
            mot=mot.replace("ù","u")
            mot=mot.replace("û","u")
            mot=mot.replace("-","-")

            x=False

    return(mot)


#Fonction permettant de définir la difficulte ( change le nombre de crédit en fcontion de la difficulté )
def difficulté() :

    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||| Difficulé  ||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||| Facile   Moyen   Dur |||||||||||||")
    print("||||||||||| 1 ||||| 2 ||||| 3 ||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||")

    x=True

    while x==True :
        difficulté=int(input("Difficulté"))
        if difficulté==1 :
            credit=15
            x=False
        if difficulté==2 :
            credit=10
            x=False
        if difficulté==3 :
            credit=5
            x=False
    return(credit)


# Programme principale :



lancement=True
continuer=True

#Compteur de nombre de parti, victoire, défaite et le ratio de victoire
compteurG=0
compteurV=0
compteurD=0
ratio=''

while continuer==True :

    if compteurG>0 :
        print("||||||||||||| Nouvelle Partie? |||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||| 1=OUI ||| 2=NON  |||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||| Partie   :",compteurG,"|||||||||||||||||")
        print("||||||||||||| Victoire :",compteurV,"|||||||||||||||||")
        print("||||||||||||| Défaite  :",compteurD,"|||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")


    else :

        print("|||||||||||||| Bienvenue |||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||| Nouvelle Partie? |||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||| 1=OUI ||| 2=NON ||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")

    nv=int(input("Nouvelle Partie? O/N "))

    if nv==1 :
        continuer=True
        lancement=True
        compteurG=compteurG+1

    if nv==2 :
        continuer=False
        lancement=False
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||||||||||||| AU REVOIR |||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||")

    while lancement==True :


        mystere = mysteret()    #   Le mot mystere
        credit=difficulté()
        mot=affichage(mystere)  #Affiche le mot sous forme de tiret
        print(''.join(mot))


        while verif(mot) and credit>0 : #Vérifie si le mot trouvé par me joueur correspond au mot a trouve et que le nombre soit toujours supérieur a 0
            lettre = str(input("Saisir une lettre"))

            numb=letter(lettre,credit,mystere,mot)

            (mot,credit)=replace(numb,mot,lettre,credit)
            final = ' '.join(mot)
            print(final," ",credit,"credit restant")

            if verif(mot) == False :    #Si le mot trouvé par le joueur correspond au mot a chercher alors Victoire
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("|||||||||||||||  Victoire  |||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                compteurV=compteurV+1
                lancement=False

            if credit == 0:     #Si le nombre de crédit est insuffisant alors défaite
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("|||||||||||||||  Défaite  ||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                print("||||||||||||||||||||||||||||||||||||||||||||")
                compteurD=compteurD+1
                lancement=False













