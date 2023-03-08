
# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176	 

import sys
input = sys.stdin.readline

t = int(input())

for k in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))

    minValue = max(arr)*m
    maxValue = 0

    for i in range(n-m+1):
        result = sum(arr[i:i+m])
        if result > maxValue: maxValue = result
        if result < minValue: minValue = result

    print(f'#{k+1} {maxValue-minValue}')