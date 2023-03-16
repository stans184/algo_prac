# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0

import sys,heapq
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not h: print(0)
        else: print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))