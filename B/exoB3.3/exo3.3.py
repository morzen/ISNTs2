# saut de balles
balle=(input("hauteur de la balles"))
ratio = 10/100
newheight =(int(balle))
i = 0

while newheight>=5:
    x = newheight*ratio
    newheight= newheight - x
    print(newheight)
    i+=1


print("hauteur des rebond")
print("ne rebondie plus ")
print(i)
print("rebonds")