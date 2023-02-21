# BOJ 10816
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

# 3 0 0 1 2 0 0 2
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

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for num in target:
    cnt = 0
    while True:
        i = binarySearch(num, arr)
        if i == -1: break
        else:
            del arr[i]
            cnt += 1
    print(cnt, end=" ")