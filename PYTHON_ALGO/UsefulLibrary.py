# 1. 내장 함수
#   > sum, min, max, eval, sorted

# 2. itertools
#   > permutations
#   > 모든 경우의 수 계산, 순열
from itertools import permutations
data = ['a', 'b', 'c']
result1 = list(permutations(data,2))
print(result1)
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
#
#   > combinations
#   > 순서 없이 가능한 수 조합
from itertools import combinations
result2 = list(combinations(data, 2))
print(result2)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
#
#   > product
#   > r 개의 데이터를 뽑아서, 일렬로 나열하는 모든 경우(순열)을 계산
#   > 원소를 중복해서 뽑는다
from itertools import product
result3 = list(product(data, repeat=2))
print(result3)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
#
#   > combination with replacement
#   > 원소를 중복해서 조합
from itertools import combinations_with_replacement
result4 = list(combinations_with_replacement(data, 2))
print(result4)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

# 3. heapq
#   > 파이썬의 heap 은 최소 heap 으로 구성되어 있음
import heapq

def heapSort(arr):
    h = []
    result5 = []
    for num in arr:
        heapq.heappush(h, num)
    for i in range(len(h)):
        result5.append(heapq.heappop(h))
    return result5

randomList = [845,132,246,231,584,291,313]
result5 = heapSort(randomList)
print(result5)
# [132, 231, 246, 291, 313, 584, 845]

# 4. bisect
#   > binarySearch 를 쉽게 할수 있는 라이브러리, 정렬된 배열에서 사용할 떄 효과적
#   > Time Complexity O(logN)
from bisect import bisect_left, bisect_right
print(result5)
print(bisect_right(result5, 231))       # element 를 1부터 count 가 아니라, 찾는 값의 다음 index 를 반환
print(result5)
print(bisect_left(result5, 231))        # element 를 0부터 count
print(result5)

# 5. collections
#   > deque
#   > 자료구조 큐를 구현
from collections import deque
data2 = deque(result5)
print(data2.pop())          # 가장 끝에 들어간 element 제거
print(data2)                # deque([132, 231, 246, 291, 313, 584])
print(data2.popleft())      # 가장 처음 들어간 element 제거
print(data2)                # deque([231, 246, 291, 313, 584])
data2.rotate(2)             # queue 에 들어있는 데이터를 정수만큼 오른쪽으로 회전,
print(data2)                # 맨오른쪽에서 빼서 왼쪽으로 추가 * 2번 deque([313, 584, 231, 246, 291])
data2.rotate(-3)  #(부호반전) # queue 에 들어있는 데이터를 정수만큼 왼쪽으로 회전
print(data2)          # 맨 왼쪽에서 빼서 오른쪽으로 추가 * 3번 deque([246, 291, 313, 584, 231])
#
#   > Counter
#   > 반복되는 객체가 주어졌을 때, 몇번씩 등장하는지 count
from collections import Counter
data3 = ['red', 'blue','red','green','blue','blue']
print(Counter(data3))       # Counter({'blue': 3, 'red': 2, 'green': 1})

# 6. math
#   > factorial
import math
print(math.factorial(5))    # 120
print(math.sqrt(256))       # 16