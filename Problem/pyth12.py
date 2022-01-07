from functools import reduce

x = int(input())

factor = []

for i in range(2,x):
    if(x % i == 0):
        if(i % 3 == 0):
            i = i // 3
            factor.append(i)
        else:
            factor.append(i)
        x = x // i
        if(i >= x):
            factor.append(x)
           
factor.sort()
for j in range(0,len(factor)):
    if(factor[j] != 1):
        print(factor[j])
        
