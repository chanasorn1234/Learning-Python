class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

def checkp(num):
    if(num == 1 or num == 2):
        return True
    for j in range(2,num):
        if(num % j == 0):
            return False
    return True



inp1 = input().split()
inp1[0] = int(inp1[0])
inp1[1] = int(inp1[1])
inp2 = input().split()
m = inp1[0]
A = Stack()
B = Stack()
Ans = []
Register = []

for k in range(0,len(inp2)):
    A.push(int(inp2[k]))

for i in range(2,m+1):
    if(checkp(i)):
        while(A.is_empty() == False):
            if(A.peek() % i == 0):
                B.push(A.pop())
            else:
                Register.append(A.pop())      
        for p in range(0,len(Register)):
            A.push(Register[p])
        Register = []
        while(B.is_empty() == False):
            Ans.append(B.pop())
    
while(A.is_empty() == False):
    Ans.append(A.pop())
while(len(Ans) > 0):
    print(Ans.pop(0))

        




