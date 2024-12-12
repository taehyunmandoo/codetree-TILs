# 거품 정렬 함수 구현
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 마지막 i개의 요소는 이미 정렬되었으므로 제외
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 요소 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 입력 처리
n = int(input())  # 배열 크기 
data = list(map(int, input().split()))  # 배열 요소 입력

# 거품 정렬 실행
sorted_data = bubble_sort(data)

# 정렬된 결과 출력
print(" ".join(map(str, sorted_data)))
