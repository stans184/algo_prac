# 이등변삼각형의 경로 중, 최대 합이 나올수 있는 것은?
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 바닥부터 찾아가면서 큰 값을 골라서 윗 항에 더해준다

import sys

input = sys.stdin.readline

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

# 삼각형의 바닥부터 시작하여 최대값을 구해나간다
for i in range(n-1, 0, -1):
    for j in range(i):
        # 바로 아래층의 두 값 중 큰 값을 현재 위치와 더하여 누적시킨다
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

print(triangle[0][0])