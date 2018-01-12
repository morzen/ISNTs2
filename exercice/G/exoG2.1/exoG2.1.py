#exoG2.1

from random import randint

loto=[]

def balls(list):
    n=0
    while n < 5:
        x=randint(1,49)
        for i in range(len(list)):
            for j in range(len(list)):
                if x == list[j]:
                    x = randint(1,49)
        list.append(x)
        n+=1
    print(list)



balls(loto)
luckyN = randint(1,10)
print(luckyN)