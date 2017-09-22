# IMC
from math import sqrt


masse=float(input("indiquer votre masse en kilogramme svp"))
taille=float(input("indiquer votre taille en metre svp"))
imc=masse/(taille*taille)
print(imc)

if imc<18.5:
    print("vous etes en souspoid, il vous reste  ")
    diff=18.5*(taille*taille)
    diff=sqrt(diff)
    print(masse-diff)
    print (diff)
    print( "a gagner ")

elif imc>=18.5 and imc<=25:
    print("votre poid est raisonnnable")

if imc>25:
    print("vous etes en surpoid il vous reste ")
    diff=25*(taille*taille)
    diff=sqrt(diff)
    print(masse-diff)
    print(diff)
    print(" a perdre ")
