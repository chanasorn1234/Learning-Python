amount = int(input())
i = 0
message = []
while (i != amount):
    tet = input()
    message.append(tet)
    i += 1

for i in range(0,51):
    for j in range(0,len(message)):
        if(len(message[j]) == i):
            print(message[j])
