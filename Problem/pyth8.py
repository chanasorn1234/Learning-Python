order = int(input())
i = 0
edit = []
while (i != order):
    number = int(input())
    edit.append(number)
    i += 1

for j in range(len(edit)-1,-1,-1):
    print(edit[j])
