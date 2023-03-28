# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 최대값은?

'''
n번째를 마실 때, n-1 마시거나
              n-2, n-3 마시거나
2579번과의 차이점은, 와인을 마시지 않아도 되는 순간이 있다는 것
dp 는 해당 시점까지의 최대 와인 섭취량이라고 생각하자
'''
# n = 6
# wine = [6, 10, 13, 9, 8, 1]
import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

dp = [0]*(n+1)
dp[1] = wine[0]
if n >= 2:
    dp[2] = dp[1] + wine[1]
    for i in range(3, n+1):
        dp[i] = max(wine[i-2] + wine[i-1] + dp[i-3], wine[i-1] + dp[i-2], dp[i-1])

# print(dp)
print(max(dp))