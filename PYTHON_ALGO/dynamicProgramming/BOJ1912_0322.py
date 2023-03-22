import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = arr[0]

# 주어진 배열의 숫자를 추가하는데, 추가하는 순간 크기를 비교해서 더 큰값만 추가
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))