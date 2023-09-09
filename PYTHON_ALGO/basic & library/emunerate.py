# enumerate()는 순서가 있는 자료형(리스트, 튜플, 문자열 등)을 입력으로 받아 
# 각 요소에 대해 인덱스(순번)를 포함하는 enumerate 객체를 돌려줍니다.
# 이 함수는 반복문 사용 시, 인덱스 번호와 컬렉션의 원소를 함께 처리할 때 매우 유용합니다.

lst = ['apple', 'banana', 'orange']

for i, x in enumerate(lst):
    print(i, x)

# 0 apple
# 1 banana
# 2 orange

for i, x in enumerate(lst, start=1):
    print(i, x)

# 1 apple
# 2 banana
# 3 orange

# BOJ 예제
# 5
# 2 4 -10 4 -9
# 2 3 0 3 1

# 6
# 1000 999 1000 999 1000 999

import heapq,sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_dupl = set(arr)

h = []
result = []
for num in arr_dupl:
    heapq.heappush(h, num)
for i in range(len(h)):
    result.append(heapq.heappop(h))

ans = dict()

for i, n in enumerate(result):
    ans[n] = i

for num in arr:
    print(ans[num], end=" ")