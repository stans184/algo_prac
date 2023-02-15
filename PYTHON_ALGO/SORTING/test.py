data = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]
# 정렬 모두 구현해보기
# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr

# print(selection_sort(data))

# insert sort
def insert_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

# print(insert_sort(data))

# quick sort
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)
    return arr

# print(quick_sort(data, 0, len(data)-1))

# heap sort
import heapq

def heap_sort(arr):
    h, result = [], []
    for value in arr:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# print(heap_sort(data))

# counting sort
def counting_sort(arr):
    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
    return result

print(counting_sort(data))