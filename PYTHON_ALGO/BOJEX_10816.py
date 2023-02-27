# BOJ 10816
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

# 3 0 0 1 2 0 0 2

# quicksort 해도 시간초과로 빠짐... 답을 봐야하나

import sys

def binarySearch(num, arr):
    left = 0
    right = len(arr)-1
    mid = (left+right)//2
    findNum = False

    while left <= right:
        if arr[mid] == num:
            findNum = True
            break
        elif arr[mid] > num:
            right = mid-1
        else:
            left = mid+1
        
        mid = (left+right)//2

    if findNum: return mid
    else: return -1

# arr.sort() # 시간초과 발생, 빠른 정렬 함 하자

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)
    return arr

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_sort = quickSort(arr, 0, len(arr)-1)
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
result = ''

for num in target:
    cnt = 0
    while True:
        i = binarySearch(num, arr_sort)
        if i == -1: break
        else:
            del arr[i]
            cnt += 1
    # print(cnt, end=" ")
    result += str(cnt) + " "

print(result[:len(result)-1])