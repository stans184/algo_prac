# n x n개의 격자에 1 x 1 크기의 정사각형 형태의 원숭이 우리가 있다.
# 각각의 우리에는 원숭이가 먹을 바나나 개수가 주어진다. 우리의 4면의 철창은 열고 닫기가 가능하다.

# 원숭이 우리에는 원숭이가 좋아하는 바나나들이 있는데 각 우리의 배정된 바나나 양이 너무 차이가 나지 않게 하기 위해 다음과 같은 규칙을 따른다.
# - 바나나의 양이 너무 차이나지 않게 하기 위해 서로 맞대고 있는 두 우리의 바나나 양의 차이가 L 이상 R 이하일 때 우리끼리 맞대고 있는 철창을 연다.
# - 철창을 열면 열려있는 우리끼리 이동이 자유로워져서 원숭이들이 바나나를 자유롭게 옮길 수 있다.
# - 열려있어 연결된 우리에 있는 모든 바나나들을 모은 뒤 다시 분배한다.
# - 분배한 후, 연결된 각 우리의 바나나 개수는 (모은 총 바나나의 개수 / 연결된 우리의 총 개수)가 된다. 편의상 소숫점은 버린다.
# - 철창은 다시 닫힌다.
# 첫번째 줄에 총 칸의 크기 n (1 ≤ n ≤ 50), 바나나 개수 차이 범위의 최솟값 L, 최댓값 R (1 ≤ L ≤ R ≤ 100) 을 공백을 두고 주어진다.
# 두번째 줄부터 (n+1)번째 줄까지 각 칸의 바나나 개수가 공백을 사이에 두고 주어진다.
# 0 ≤ (각 칸의 바나나 개수) ≤ 100

# 재분배가 발생하는 총 횟수는 2000번보다 작다고 가정해도 좋다.​
# 바나나의 재분배가 일어난 총 횟수를 출력한다.

# [예시]
# 입력
# 3 10 20
# 35 30 40
# 30 55 40
# 25 40 45

# 출력
# 2

def redistribute(n, L, R, grid):
    def bfs(x, y):
        queue = [(x, y)]
        temp = []
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if L <= abs(grid[nx][ny] - grid[x][y]) <= R:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        temp.append((nx, ny))
        return temp

    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        visited = [[False] * n for _ in range(n)]
        is_redistributed = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = True
                    connected = bfs(i, j)
                    if connected:
                        connected.append((i, j))
                        total_bananas = sum(grid[x][y] for x, y in connected)
                        bananas_per_house = total_bananas // len(connected)
                        for x, y in connected:
                            grid[x][y] = bananas_per_house
                        is_redistributed = True
        if not is_redistributed:
            break
        count += 1
    return count

# 입력
n, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 바나나 재분배 과정 수행
redistribution_count = redistribute(n, L, R, grid)
print(redistribution_count)
