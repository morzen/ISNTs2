#MIJADEC / MALANDAIN
#Programme principal, Poprgramme Serveur ou programme de l'hote
#Calcul des clés 2P

def pgcd(a, b):# Plus garnd diviseur commun
    if not b:
        return a
    return pgcd(b, a % b)

def euclide_etendu(a,b): # Euclide etendu permmettant de trouver le pgcd mais aussi les coefficient pour trouver les variables qui formeront la somme du pgcd initlal

    x=1
    y=0
    xx=0
    yy=1
    while b!=0:
        q=a//b
        a,b=b,a%b
        xx,x=x-q*xx,xx
        yy,y=y-q*yy,yy

    return(a,x,y) #Cet algorithme renvoie d’abord le pgcd, puis les coefficients u, v tels que au + bv = pgcd(a, b)

def puissance(x,k,n):

    puiss = 1 # Résultat
    while (k>0):
        if k % 2 != 0 : # Si k est impair (i.e. k_i=1)
            puiss = (puiss*x) % n
        x = x*x % n
        k = k // 2
    return(puiss)

def inverse(a,n): # On détermine alors l’inverse modulo

    c,u,v = euclide_etendu(a,n) # pgcd et coeff. de Bézout
    if c != 1 : # Si pgcd différent de 1 renvoie 0
        return 0
    else :
        return u % n # Renvoie l'inverse

def cle_privee(p,q,e) :

    n = p * q # a modifier
    phi = (p-1)*(q-1) # a modifier
    c,d,dd = euclide_etendu(e,phi) # Pgcd et coeff de Bézout ( voir theoreme )
    return(d % phi) #Retourne la clé privée

def main():

    #Calcul clé publique pour ordi 1:
    p=int(input('Entrez un grand nombre premier P, exemple P=456 : ')) # L'utilisateur entre p
    q=int(input('Entrez un grand nombre premier Q, exemple Q=654: ')) # L'utilisateur entre q
    e=int(input('Entrez un nombre pour E, exmple E=12: '))
    print("| P=",p,"| Q=",q,"|E=",e,"|") # L'utilisateur entre e
    n=(p*q)
    phi = (p-1)*(q-1) # a modifier
    print("| N = ",n,"| Phi de n =",phi,"|")
    print("| Clée Publique :",n,e) # Affiche la clé publique

    #Calcul clé privée pour ordi 2:
    k=cle_privee(p,q,e)
    print("| Clé privée :",k,e) # Affiche la clé privée

main()

    #Ensuite le serveur leurs envoie les clés.
    #Ensuites les programmes pour crypter les messages, les programmes sont séparés du programme principal
    # PS: Il me reste des trucs a faire sur celui ci, il faut que je rajoute une def permmettant de verifier les les nombres entres sont valides pour le cryptage mais je verrais vers la fin.