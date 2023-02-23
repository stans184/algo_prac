# insert sort
# 평균 정렬 시간이 O(n^2)
# 현재 선택된 element 보다 앞부분을 쭉 검사하면서 큰 값이 나올때마다 자리를 바꾼다

def insertSort1(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

def insertSort2(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
               arr[j-1], arr[j] = arr[j], arr[j-1] # Swap.
    return arr

data = [80, 50, 70, 10, 60, 20, 40, 30]

print(insertSort1(data))
print(insertSort2(data))