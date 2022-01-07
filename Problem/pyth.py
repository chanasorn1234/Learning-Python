x = int(input())
print(" ")
for i in range(0,x):
    for j in range(x,i+1,-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print("*",end="")
    for m in range(0,i):
        print("*",end="")
    print("")


