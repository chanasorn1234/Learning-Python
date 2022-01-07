import re
str = input()

password = 0
result = re.findall("\d\d\d\d",str)
if(result != []):
    x = str.replace(result[0],"")
else:
    x = str
def kuy(res,y):
    for i in range(0,len(result)):
        y = y.replace(result[i],"")
    return y
x = kuy(result,x)      
result += re.findall("\d\d\d",x)   
x = kuy(result,x)
result += re.findall("\d\d",x)
x = kuy(result,x)
result += re.findall("\d",x)
x = kuy(result,x)

for j in range(0,len(result)):
    result[j] = int(result[j])
    password += result[j]
if(password <10 ):
    print("000",end="")
    print(password)
if(password>=10 and password<100):
    print("00",end="")
    print(password)
if(password>=100 and password<1000):
    print("0",end="")
    print(password)
if(password >= 1000):
    print(password)
