order = []
while True:
    x = int(input())
    if(x == 0):
        break
    else:
        order.append(x)

order.sort()
type = input()
if(type == "max" or type == "MaX"):
    for i in range(len(order)-1,-1,-1):
        print(order[i],end=" ")
if(type == "min" or type == "Min"):
    for j in range(0,len(order)):
        print(order[j],end=" ")   




