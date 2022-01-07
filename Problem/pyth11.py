x = int(input())
if(x % 4 == 0):
    if(x % 100 == 0):
        if(x==0 or x % 1000 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")