x = input()
y = input()
me = x.split()
friend = y.split()
total = []

if(len(me) != len(friend)):
    print("Invalid")
else:
    for i in range(0,len(me)):
        total.append(int(me[i])+int(friend[i]))
    for j in range(0,len(total)):
        if(total[j] > 32548):
            print("Invalid")
            break  
        else:  
            print(total[j],end=" ")