# IMC
from math import sqrt


masse=float(input("indiquer votre masse en kilogramme svp"))
taille=float(input("indiquer votre taille en metre svp"))
imc=masse/(taille*taille)
print(imc)

if imc<18.5:
    print("tu est trop maigre, il te reste  ")
    diff=25*(taille*taille)
    diff=sqrt(diff)
    print(masse-diff)
    print (diff)
    print( "a gagner pour avoir un corp de reve ")

elif imc>=18.5 and imc<=25:
    print("tu es un dieu vivant")

if imc>25:
    print("tu est fatou il te reste ")
    diff=18.5*(taille*taille)
    diff=sqrt(diff)
    print(diff)
    print(" a perdre pour etre beau gosse")
