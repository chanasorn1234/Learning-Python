class Queue:
    def __init__(self):
        self.items = list()

    def enqueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return -1

    def checkq(self,value):
        if not self.is_empty():
            for i in range(0,len(self.items)):
                if(self.items[i][0] == value):
                    return True
            return False
        else:
            return False
    def cutin(self,value):
        if not self.is_empty():
            for j in range(len(self.items)-1,-1,-1):
                if(self.items[j][0] == value[0]):
                    pos = j
                    break
            self.items.insert(pos+1,value)
      
        else:
            self.items.append(value)




    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output

inp = input("Enter Input : ").split("/")

action = inp[1].split(",")
q = Queue()

for cmd in action:
    # if(len(cmd) > 1):
    #     print(cmd)
  
     if(len(cmd) == 1):
         if(q.is_empty() == False):
             print(q.dequeue())
         else:
             print("Empty")

     else:
        cmd = cmd.split()       
        val = cmd[1]
  
        if(q.checkq(val[0])):
            q.cutin(val)
            
        else:
            q.enqueue(val)
            
            
    