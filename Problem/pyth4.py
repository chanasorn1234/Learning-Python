from typing import Collection
i = 0
number = []
while (i != 5):
    x = int(input())
    number.append(x) 
    i += 1
number.sort()
for i in range(len(number)-1,-1,-1):
    print(number[i])

