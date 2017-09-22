# exo C2.1
var=False

while var==False :
    ageGuido=int(input("veuiller indiquer l'age de GuidoVon Rossum"))
    if (ageGuido==1956): var =True
    elif (ageGuido<1958 and ageGuido>1954): var = True
    else : print("recommencez svp")
print("c'est sa !")
