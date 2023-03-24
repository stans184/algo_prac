# 빨강, 파랑, 초록
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

#  N(2 ≤ N ≤ 1,000)이 주어진다. 
#  둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
#  집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
#  모든 집을 칠하는 최소 비용은?

# 3
# 26 40 83  >   1번집을 빨강, 초록, 파랑으로 칠하는 비용
# 49 60 57  >   2번집을 빨강, 초록, 파랑으로 칠하는 비용
# 13 89 99  >   3번집을 빨강, 초록, 파랑으로 칠하는 비용
# 96

n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

total_cost = [[0]*3 for _ in range(3)]
total_cost[0] = cost[0]

# 현재 집을 기준으로 반복문을 설정해야 함
for i in range(1, n):
    total_cost[i][0] = (cost[i][0] + min(total_cost[i-1][1], total_cost[i-1][2])) # red
    total_cost[i][1] = (cost[i][1] + min(total_cost[i-1][0], total_cost[i-1][2])) # green
    total_cost[i][2] = (cost[i][2] + min(total_cost[i-1][0], total_cost[i-1][1])) # blue

print(total_cost)
print(min(total_cost[n-1]))