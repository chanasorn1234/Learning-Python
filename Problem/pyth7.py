text0 = input()
lit = []
for i in range(0,len(text0)):
    if(text0[i].isupper() == True):
        lit.append(text0[i].lower())
    else:
        lit.append(text0[i].upper())
    
for j in range(0,len(lit)):
    print(lit[j],end="")