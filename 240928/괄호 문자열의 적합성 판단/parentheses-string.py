class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def empty(self):
        return not self.items
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        print(self.items[-1])
    def size(self):
        print(len(self.items))

def check_par(parenthesis):
    s = Stack()
    for i in parenthesis:
        if i == '(':
            s.push(i)
        
        elif i == ')':
            if s.empty():
                return False
            s.pop()
        
    if s.empty() == False:
        return False

    else:
        return True
    
parenthesis = input()
if not check_par(parenthesis):
    print("No")
else:
    print("Yes")