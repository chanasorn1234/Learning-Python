def factor(n):
    for i in range(n-1,1,-1):        
        if(n%i==0):
            return i
   
        

x = int(input("Enter Number: "))
y = factor(x)
