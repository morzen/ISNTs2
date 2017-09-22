#exo C3.3
from random import *

bet=int(input("estimation"))
dice=randint(1,6)
i=0

while dice!=6:
    dice=randint(1,6)
    i+=1
print(i)

if bet==i:
    print("bravo vous avez gagner")

else:
    print("essay encore")


