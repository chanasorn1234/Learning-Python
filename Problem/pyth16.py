sent = input()
Arr = sent.split()
if(Arr[1] == "+"):
    print(Arr[0],"+",Arr[2],"=",int(Arr[0])+int(Arr[2]))
if(Arr[1] == "-"):
    print(Arr[0],"-",Arr[2],"=",int(Arr[0])-int(Arr[2]))
if(Arr[1] == "*"):
    print(Arr[0],"*",Arr[2],"=",int(Arr[0])*int(Arr[2]))
if(Arr[1] == "/"):
    print(Arr[0],"/",Arr[2],"=",int(Arr[0])/int(Arr[2]))