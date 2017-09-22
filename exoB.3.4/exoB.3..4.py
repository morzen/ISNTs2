#ATM
from math import *
moneyasked=int(input("combien d'argent voulez vous retiré"))
billet5= 5
billet10= 10
billet20= 20
billet50= 50
i = 0
a = 0
b = 0
c = 0
e = 0
if moneyasked % 5 == 0:
    while moneyasked>=5:
        if moneyasked>=50:
            moneyasked=moneyasked-50
            i+=1
            a+=1
            print(a)
            print("billet50")
        elif moneyasked>=20:
            moneyasked=moneyasked-20
            i+=1
            b+=1
            print(b)
            print("billet20")
        elif moneyasked>=10:
            moneyasked=moneyasked-10
            i+=1
            c+=1
            print(c)
            print("billet10")
        elif moneyasked>=5:
            moneyasked=moneyasked-5
            i+=1
            e+=1
            print(e)
            print("billet5")
    print(i)
    print("billet au total")

else :
    print("je ne peu rendre l argent")