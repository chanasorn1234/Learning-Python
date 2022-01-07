buy = int(input())
result = 0
if(buy>2):
    for i in range(1,buy+1):
        if(i % 3 == 0):
            result += 1
    while(result % 3 == 0):
        x = result // 3
        result += x
    ez = buy - (3*result)
    if(result > 2):
        for j in range(1,result+ez+1):
            if(j % 3 == 0):
                result += 1

    y = result+buy
    while(y % 3 == 0):
        y += 1
    print(y)
else:
    print(buy+result)        