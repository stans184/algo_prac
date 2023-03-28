'''
1~9

2~8 까지는 앞뒤로 2개씩해서 곱하기 2
1은 0,2해서 2개
9는 8만

1 > 0 > 1 > 0
1 > 0 > 1 > 2
1 > 2 > 1 > 0
1 > 2 > 1 > 2
1 > 2 > 3
2 > 1 > 0 > 1
2 > 1 > 2
2 > 3 > 2
2 > 3 > 4
.
.
.
8 > 7 > 6
8 > 7 > 8
8 > 9 > 8
9 > 8 > 7
9 > 8 > 9 > 8

그러면 n-1번째에 올수 있는건 0~9까지
n번째는 그걸 활용해서 (1~8)*2 + 9*1 > 17가지
'''
import sys
input = sys.stdin.readline

n = int(input())

# 내가 처음 짠거
# dpcheck = [0]*(n)
# dpcheck[0] = 9
# for i in range(1, n):
#     dpcheck[i] = (dpcheck[i-1]-i)*2 + i

# print(dpcheck[-1]%1000000000)

# 구글링을 보고 해본거
dp = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1;

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] += dp[i-1][1]
        elif j == 9:
            dp[i][j] += dp[i-1][8]
        else:
            dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)

# 나중에 다시 해보기