# 선택 정렬 함수 구현
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 현재 정렬할 범위에서 가장 작은 요소 찾기
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 가장 작은 요소를 현재 위치로 이동
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 입력 처리
n = int(input())  # 배열 크기 입력

data = list(map(int, input().split()))  # 배열 요소 입력

# 선택 정렬 실행
sorted_data = selection_sort(data)
print(" ".join(map(str, sorted_data)))
