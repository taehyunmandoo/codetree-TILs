def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # 현재 요소를 저장
        key = arr[i]
        # 현재 요소를 적절한 위치로 삽입
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    



# 입력 처리
n = int(input())  # 배열 크기 입력
data = list(map(int, input().split()))  # 배열 요소 입력

# 삽입 정렬 실행
sorted_data = insertion_sort(data)

# 정렬된 결과 출력
print(" ".join(map(str, sorted_data)))