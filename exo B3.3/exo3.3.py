# saut de balles
balle=(input("hauteur de la balles"))
rebond=(10/100)
newhight =(int(balle))
i = 0

while newhight>=5:
    newhight=newhight-rebond
    print(newhight)
    i+=1


print("hauteur des rebond")
print("ne rebondie plus ")
print(i)
print("rebonds")