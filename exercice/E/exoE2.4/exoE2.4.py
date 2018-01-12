#exoE2.4

palindrome=input("entre un palindrome svp")




def parse(n):
    l = len(n)
    print(l)
    for i in range(l):
        if n[i]!= n[l-i-1]:
            print("fff")
            return None
    print("ok")






parse(palindrome)

print(list)