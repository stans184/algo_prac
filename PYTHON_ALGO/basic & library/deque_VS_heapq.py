from collections import deque
import heapq
# 위에 두개 비교해보기

# heapq 예제 중, 인풋으로 tuple 을 받는 경우도 가능한가?
h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not h: print(0)
        else: print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))