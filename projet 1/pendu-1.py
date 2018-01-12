  #pendu



#compte le nbr de character ds le mot et le rend en -
def affichage(l):
    k=len(l)
    s=[]
    for i in range(k):

        if l[i] == " " :
            s.append(" ")
        else:
            s.append("-")

    return s


#mot=newdef(mystere)


#remplace mot trouver dans liste et enleve point de credit si faut
def letter(x,l):

    m = []
    for pos, char in enumerate(l):
         tmp = ord(char)
         temp = ord(x)
         tmpx = ord(x)+32
         tmpX = ord(x)-32

         if tmp<97:
            if tmp == temp :
                m.append(pos)
            elif tmp == tmpX:
                m.append(pos)

         else:
            if tmp == temp or tmp == tmpx:
                m.append(pos)

    return m

#numb=letter(lettre,credit,mystere,mot)


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






def verif (y):
    l=len(y)

    for i in range(l):
        if y[i] == "-":
            return True
    return False

def nbcredit (m,l,n):
    n=n+1
    n=n-1
    print(n,"credit remaining")


def order ():
    mystere = str(input("mistery word for game master "))
    credit = 10


    mot=affichage(mystere)
    print(''.join(mot))
    while verif(mot) and credit>0 :
        lettre = str(input("give a  letter"))

        if len(lettre) == 0:
            print("only one letter is asked ")
        elif len(lettre) > 1:
            print("only one letter is asked  ")
        else:
            numb=letter(lettre,mystere)

            (mot,credit)=replace(numb,mot,lettre,credit)
            final = ' '.join(mot)
            print(final)
            nbcredit(mystere,lettre,credit)

    if verif(mot) == False :
        print("YOU WIN")

    if credit == 0:
        print("YOU LOSE")
        print("the correct word was ")
        print(mystere)




order()
