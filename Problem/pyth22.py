import re
number = int(input())
result = 0

for i in range(1,13):
    result += number*i
    print(str(number),"x",i,"=",number*i)

if(result>=1000):
    result = str(result)
    x = re.findall("\d",result)
    print("รวม :",end=" ")
    for j in range(-len(x),0,+1):
        print(x[j],end="")
        if( j%3 == 2 and j!=-1):
            print(",",end="")

    print(".00")
else:
    print("รวม :","%.2f"%result)