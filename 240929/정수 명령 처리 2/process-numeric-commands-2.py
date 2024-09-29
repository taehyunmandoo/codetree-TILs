from collections import deque

class MyQueue:  # 클래스 이름 변경
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self): 
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq[0]

n = int(input())
q = MyQueue()  # 클래스 이름 변경

for _ in range(n):
    command = input()

    if command.startswith("push"):
        x = int(command.split()[1])
        q.push(x)

    elif command == "pop":
        print(q.pop())
    
    elif command == "size":
        print(q.size())
    
    elif command == "empty":
        print(1 if q.empty() else 0)
    
    elif command == "front":
        print(q.front())