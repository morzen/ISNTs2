#Le juste prix

from random import*
justeprix=randint(30,100)
prix=int(input("prix supposer"))
#print(justeprix)


def Game(prix, justeprix):
    i=1
    while prix!=justeprix and prix!=0 :
        print(i)
        if prix>justeprix:
            print("c'est moins")
            prix=int(input("prix supposer"))
            i+=1

        else:
            print("c'est plus")
            prix=int(input("prix supposer"))
            i+=1

        if i==4:
            print("attention il ne vous reste que 4 essai")

        if i==8:
            print("vous avez perdu le juste prix etait")
            print(justeprix)
            rejoue=str(input("si vous oulez rejouer ecriver oui"))
            if rejoue != "non":
                return (True,0)
            return (False,0)

    if prix==0:
        print("merci d'avoir jouer")
        return (False,0)

    elif prix==justeprix:
        print("vous avez gagné !")
        rejoue=str(input("si vous oulez rejouer ecriver oui"))
        if rejoue != "non":
            return (True,1)
        return (False,1)





def restart(prix, justeprix):
    i=1
    win =1
    n = Game(prix, justeprix)
    if n[1] == 0:
        win = win -1
    while n[0]:
        if n[1] == 1:
            win+=1
        justeprix=randint(30,100)
        prix=int(input("prix supposer"))
        n = Game(prix, justeprix)
        print(win)
        i+=1
    print("goodbye")
    print(i)
    print(win)
    print((win/i)*100)

restart(prix, justeprix)
