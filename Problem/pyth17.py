str = input()
up = 0
low = 0
for i in range(0,len(str)):
    if(str[i].isupper()):
        up += 1
    if(str[i].islower()):
        low += 1
print("UPPER:",end="")
print(up)
print("LOWER:",end="")
print(low)