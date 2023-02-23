# 랜덤 넘버를 이용한 배열 만들기
# import random
# data = []
# for _ in range(11):
#     data.append(random.randrange(1,100))
# print(data)

data = [69, 83, 93, 9, 10, 36, 34, 52, 59, 15, 45]
print('before', end=" ")
print(data)

# selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        minValue = i
        for j in range(i,len(arr)):
            minValue = j if arr[j] < arr[minValue] else minValue
        arr[i], arr[minValue] = arr[minValue], arr[i]
    return arr
print('after selection_sort', end=" ")
print(selectionSort(data))

# insert sort
def insertSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr
print('after insert_sort', end=" ")
print(insertSort(data))

# counting sort
def countingSrot(arr):
    count = [0] * (max(arr)+1)
    for num in arr:
        count[num] += 1
    
    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
    return result
print('after counting_sort', end=" ")
print(countingSrot(data))

# quick sort        >>       아직
def partition(arr, left, right):
    pivot = arr[right]
    i = left -1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[right], arr[i+1] = arr[i+1], arr[right]
    return i+1

def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr,pivot+1, right)
    return arr
print('after quick_sort', end=" ")
print(quickSort(data, 0, len(data)-1))

# heap sort
import heapq

def heapSort(arr):
    h=[]
    result=[]
    for num in arr:
        heapq.heappush(h, num)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result
print('after heap_sort', end= " ")
print(heapSort(data))