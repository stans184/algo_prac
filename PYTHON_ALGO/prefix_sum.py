# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

# 시간초과가 뜸
# 리스트의 범위에 대해서 직접 더하는 방법은 전체 리스트를 다 훑게 될수도 있음
# 누적합을 미리 구해놓는 방법으로 접근

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = [0]

# key, 누적합같이 시간이 중요한 경우는, 변수에다가 저장해둬야함
# 매번 총합을 구하게 되면 시간, 메모리 낭비
sum = 0
for i in arr:
    sum += i
    sum_list.append(sum)

for _ in range(m):
    a,b = map(int, input().split())
    print(sum_list[b] - sum_list[a-1])