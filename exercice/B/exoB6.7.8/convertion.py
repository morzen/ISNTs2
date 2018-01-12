#Exercice B.6.7.8

def decbin(n):
    x =""
    while n != 0:
        i = n%2
        x =  x + str(i)
        n = n//2

    result = ""
    l = len(x)
    for i in range(l):
        result = result + x[l-i-1]

    print(result)
    return result


def bindec(n):
    l=len(n)
    result=0
    for i in range(l):
        x = n[i]
        if x== "1":
            power= l-i -1
            result= result + 2**power
    print(result)
    return result



def main():
    user = str(input("enter 1 for decbin , 2 for bindec and 0 to quit"))
    while user != "0":
        if user == "1":
            a=int(input("enter integer decimal number"))
            decbin(a)
            user = str(input("enter 1 for decbin , 2 for bindec and 0 to quit"))
        elif user == "2":
            b = str(input("enter binary number"))
            bindec(b)
            user = str(input("enter 1 for decbin , 2 for bindec and 0 to quit"))
        else:
            print("i did not understand")
            user = str(input("enter 1 for decbin , 2 for bindec and 0 to quit"))

    print("goodbye")

    return 0

main()