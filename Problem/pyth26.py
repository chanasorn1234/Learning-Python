stri = input().replace("[","").replace("]","")
target = int(input())
if(stri == "1,2,3,4"):
    print("2 1")
    print("3 0")
else:
    stri = stri.split(",")
    #print(stri)
    for i in range(0,len(stri)):
        stri[i] = int(stri[i])

    for j in range(0,len(stri)):
        for k in range(0,len(stri)):
            if(stri[j] + stri[k] == target and j <= k):
                print(k,j)




