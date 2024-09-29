from collections import deque

# n 입력 받기
n = int(input())

# deque 초기화 (1부터 n까지의 수를 담음)
dq = deque(range(1, n + 1))

# 남은 카드가 1장일 때까지 반복
while len(dq) > 1:
    dq.popleft()  # 맨 앞의 숫자를 제거 (버리기)
    dq.append(dq.popleft())  # 맨 앞의 숫자를 빼서 뒤로 보냄

# 최종 남은 숫자를 출력
print(dq[0])