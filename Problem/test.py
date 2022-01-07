print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
print(x)

for i in range(x,0,-1):
    for j in range(1,i):
        print(".",end="")
    print("*",end="")
    if(i == x):
        print(end="")
    else:
        for k in range(x-1,i,-1):
            print("+",end="")
        for m in range(x-1,i-1,-1):
            print("+",end="")
        if(i != 1):
            print("*",end="")
        
    for w in range(3,2*i):
        print(".",end="")
    print("*",end="")
    #if(i == x):
    #    print(" ")
    #else:
    for e in range(x-1,i,-1):
        print("+",end="")
    for r in range(x-1,i-1,-1):
        print("+",end="")
    if(i != x):
        print("*",end="")
    for t in range(0,i):
        if(t != i-1):
            print(".",end="")
        else:
            print(".")











for k in range(2,2*x):
    for p in range(0,k):
        if(p == k-1):
            print("*")
        else:
            print(".",end="")