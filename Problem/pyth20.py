import math
x = input()
if(x[-1] == "5" and x[-2] == "2"):
    x = int(x)
    result = math.sqrt(x)
    result = str(result)
    if(result[-1]=="0"):
        print(result[0:-2])
    else:
        print("No Numbers Matching!")
else:
    print("No Numbers Matching!")