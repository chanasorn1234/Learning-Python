import math

def viet(a):
    if(a == 0):
        return 0
    else:
        return math.sqrt(1+pow(viet(a-1),2))

result = 0
i = 0
x = int(input())
lit = []
while(i < x):
    y = int(input())
    lit.append(y)
    i += 1
for j in range(0,len(lit)):
    for k in range(1,lit[j]):
        result += 1 / (viet(k) + viet(k+1))
    #if()
    print("%.2f"%result)
    result = 0
