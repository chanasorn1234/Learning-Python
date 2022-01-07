amount = int(input())
item = []
i = 0
result = []
while (i != amount):
    stuff = input()
    item.append(stuff)
    i += 1
find = input()

for i in range(0,len(item)):
    if(item[i] == find):
        result.append(str(i+1))
        result.append(",")  
print("Position:",end=" ")  
for j in range(0,len(result)-1):
    print(result[j],end="")