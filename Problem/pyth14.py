number = []
while True:
    enter = int(input())
    number.append(enter)
    if(enter < 0):
        break
    
for i in range(0,len(number)-1):
    print(number[i]+number[len(number)-1])