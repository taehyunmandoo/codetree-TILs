from collections import deque

class Queue:
    def __init__(self):          # 빈 큐 하나를 생성합니다.
        self.dq = deque()
                
    def push(self, item):        # 큐의 맨 뒤에 데이터를 추가합니다.
        self.dq.append(item)
                
    def empty(self):             # 큐가 비어있으면 True를 반환합니다.
        return not self.dq
                
    def size(self):              # 큐에 들어있는 데이터 수를 반환합니다.
        return len(self.dq)
        
    def pop(self):               # 큐의 맨 앞에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Queue is empty")
            
        return self.dq.popleft()
                
    def front(self):             # 큐의 맨 앞에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Queue is empty")
                        
        return self.dq[0]

# 입력 받기
n, k = map(int, input().split())  # n: 총 숫자의 개수, k: k번째 사람을 제거
q = Queue()

# 1번부터 n번까지 큐에 삽입
for num in range(1, n + 1):
    q.push(num)

# 순열 출력 리스트
result = []

# 원형 순열 로직 수행
while q.size() > 0:
    # k-1번 요소를 뒤로 보내며 회전
    for _ in range(k - 1):
        q.push(q.pop())  # 맨 앞의 요소를 빼서 뒤로 보냄

    # k번째 요소를 제거하고 출력 리스트에 추가
    result.append(q.pop())

# 결과 출력
print(" ".join(map(str, result)))