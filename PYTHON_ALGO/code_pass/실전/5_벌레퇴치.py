# N × N 크기의 방에 벌레들의 공격이 시작되었다.
# 방에는 벽이 있고 다행히도 특정 위치에 벌레들이 싫어하는 향으로 퇴치할 수 있는 벌레 퇴치기들이 있다.
# 순식간에 벽과 퇴치기를 제외한 모든 지역을 벌레들이 장악해버려 정올이는 방에 들어갈 수 없지만, 밖에서 원격으로 퇴치기를 켤 수 있다.
# 하지만 방에 있는 모든 퇴치기를 켤 수는 없고, M개의 퇴치기를 골라 최대한 빨리 벌레들을 퇴치해야 한다.

# 첫째 줄에는 N (3 ≤ N ≤ 50)과 M (1 ≤ M ≤ 10)​이 공백을 사이에 두고 주어진다.
# 둘째 줄 부터는 N개의 줄에 걸쳐 각 행의 상태에 해당하는 N개의 숫자가 공백을 사이에 두고 주어진다. 숫자는 0, 1, 2 중에 하나이며, 0은 벌레, 1은 벽 그리고 2는 퇴치기를 의미한다. 입력으로 주어지는 총 퇴치기의 수가 항상 M보다 크거나 같고, 10을 넘지 않는다.
# M개의 퇴치기를 켜서 벌레를 전부 없애는데 걸리는 시간 중 최소 시간을 출력한다. 만약 모든 벌레를 쫒아낼 수 있는 방법이 없다면 −1을 출력한다. 

# [입력 예시]
# 5 2
# 2 0 2 1 1
# 0 0 0 0 1
# 0 0 0 2 0
# 1 0 0 0 0
# 1 1 1 0 0

# [출력 예시]
# 3

import itertools
from collections import deque

def bfs(N, exterminators, room):
    # 이미 벌레가 없는 경우
    if all(room[i][j] != 0 for i in range(N) for j in range(N)):
        return 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque(exterminators)
    visited = [[False] * N for _ in range(N)]
    for ex in exterminators:
        visited[ex[0]][ex[1]] = True

    time = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and room[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        time += 1

    for i in range(N):
        for j in range(N):
            if room[i][j] == 0 and not visited[i][j]:
                return float('inf')
    return time - 1

# 입력
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 퇴치기 위치 찾기
exterminators = [(i, j) for i in range(N) for j in range(N) if room[i][j] == 2]

# M개의 퇴치기를 사용한 모든 조합에 대한 최소 시간 계산
min_time = float('inf')
for comb in itertools.combinations(exterminators, M):
    min_time = min(min_time, bfs(N, comb, room))

# 출력
print(min_time if min_time != float('inf') else -1)