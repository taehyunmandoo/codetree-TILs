from collections import deque

class Dect:
    def __init__(self):
        self.dq = deque()
    
    def push_front(self, item):
        self.dq.appendleft(item)
    
    def push_back(self, item):
        self.dq.append(item)
    
    def pop_front(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    
    def pop_back(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.pop()
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        return not self.dq
    
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]
    
    
n = int(input())
q = Dect()

for _ in range(n):
    command = input()

    if command.startswith("push_front"):
        x = int(command.split()[1])
        q.push_front(x)
    
    elif command.startswith("push_back"):
        x = int(command.split()[1])
        q.push_back(x)
    
    elif command == "pop_front":
        print(q.pop_front())
    
    elif command == "pop_back":
        print(q.pop_back())
    
    elif command == "size":
        print(q.size())
    
    elif command == "empty":
        print(1 if q.empty() else 0)
    
    elif command == "front":
        print(q.front())
    
    elif command == "back":
        print(q.back())