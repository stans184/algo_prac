# insert sort
# 평균 정렬 시간이 O(n^2)

def insertSort1(arr):

    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

def insertSort2(data):
    for i in range(len(data)):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
               data[j-1], data[j] = data[j], data[j-1] # Swap.
    return data

arr = [80, 50, 70, 10, 60, 20, 40, 30]

print(insertSort1(arr))
print(insertSort2(arr))