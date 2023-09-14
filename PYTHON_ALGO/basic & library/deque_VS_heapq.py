from collections import deque
import heapq
# 위에 두개 비교해보기

# 최소 heap (기본)
def heapSort(iterable):
    h = []
    result = []
    
    for it in iterable:
        heapq.heappush(h, it)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

# 최대 heap (들어가고 나오는 원소에다가 반전 부호를 붙여서)
def heapSortMax(iterable):
    h = []
    result = []
    
    for it in iterable:
        heapq.heappush(h, -it)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result

print(heapSort([5,2,6,7,3,13,11,9]))
print(heapSortMax([5,2,6,7,3,13,11,9]))

# heapq 예제 중, 인풋으로 tuple 을 받는 경우도 가능한가?
h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not h: print(0)
        else: print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))