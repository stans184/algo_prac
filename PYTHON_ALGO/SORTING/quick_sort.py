# quick sort 
# 임의의 element 에다가 pivot 잡고          >> 맨왼쪽, 맨오른쪽 element 로 pivot 을 잡는 경우가 많은데, 계산시간이 길어질 수도 있다
# 범위 - 기준 - 비교 - swap                >> random element 로 pivot 을 잡기도 한다
# pivot 을 대상으로 비교할 element 의 범위를 설정하고
# 작은거 왼쪽 큰거 오른쪽 (예시)
# 작은거와 큰거로 나눈 가운데로 pivot 을 옮긴다
# time complexity
# worst O(n^2)                          >> 이미 정렬된 경우, 남은 부분을 다 훑어야 하므로
# normal & best O(nlog(n))

# pivot 기준으로 작은거 왼쪽, 큰거 오른쪽으로 나누는 함수
def partition(arr, left, right):
    # 맨 오른쪽 값을 피봇으로 잡고
    pivot = arr[right]
    # 값을 비교할 커서를 정의
    i = left - 1
    # 맨 왼쪽부터 피봇 직전까지 훑으면서
    for j in range(left, right):
        # 피봇보다 작은 값이면
        if arr[j] <= pivot:
            # 커서를 하나 증가시키고
            i += 1
            # 옮겨진 커서의 위치와, 값을 비교한 j끼리 swap
            arr[i], arr[j] = arr[j], arr[i]
    # 커서 i 를 기준으로 왼쪽에는 pivot 보다 작은 값, 오른쪽은 pivot 보다 큰 값
    # i 바로 옆으로 pivot으로 잡았던 arr element 이동
    arr[i+1], arr[right] = arr[right], arr[i+1]
    # pivot 의 위치 출력
    return i+1

# quick sort, recursive 구현
def quickSort(arr, left, right):
    # 왼쪽 값이 오른쪽 값보다 클때만 진행, 재귀함수 탈출을 위한 조건
    if left < right:
        # 위 partition 과정을 통해 구해진 partition 의 위치를 기준으로
        pivot = partition(arr, left, right)
        # 왼쪽 정렬 (pivot 보다 작았던 값들)
        quickSort(arr, left, pivot-1)
        # 오른쪽 정렬 (pivot 보다 컷던 값들)
        quickSort(arr, pivot+1, right)
    return arr


data = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]
arr = [6, 3, 2, 10, 10, 10,-10,-10, 7, 3]
print(quickSort(data, 0, len(data)-1))
print(quickSort(arr, 0, len(arr)-1))