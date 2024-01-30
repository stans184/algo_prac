# 빈나는 스캔 로봇을 가지고 1 x 1 크기의 정사각형 칸으로 이루어져있는 N x M 크기의 방의 바닥 밑에 있는 파이프를 스캔하려고 한다.
# 각각의 칸은 벽 또는 빈 칸이다.
# 스캔 로봇의 정면에는 방향을 담당하는 카메라가 달려있고, 아래에는 로봇이 있는 칸 바닥을 투시하여 스캔하는 카메라 모듈이 장착되어 있다.
# 스캔 로봇은 동, 서, 남, 북 중 한 방향으로 이동하며, 처음에 빈 칸은 전부 스캔되어 있지 않은 상태이다.
# 스캔 로봇은 다음 규칙에 따라서 움직인다

# 1. 현재 칸을 스캔한 적이 없는 경우, 현재 칸을 스캔한다.

# 2. 현재 칸의 주변 4칸 중 스캔이 되지 않은 빈 칸이 있는 경우,
#     a. 반시계 방향으로 90도 회전한다.
#     b. 바라보는 방향을 기준으로 앞쪽 칸이 스캔되지 않은 빈 칸인 경우 한 칸 전진한다.
#     c. 1번으로 돌아간다.

# 3. ​현재 칸의 주변 4칸 중 스캔되지 않은 빈 칸이 없는 경우,
#     a. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#     b. 바라보는 방향 뒷 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

# 스캔 로봇이 스캔을 시작한 후 작동을 멈출 때까지 스캔한 칸의 개수를 출력한다.
# 첫째 줄에 방의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50​)

# 둘째 줄에 스캔 로봇의 처음 위치 (r, c)와 바라보는 방향 d가 주어진다.
# d는 0부터 3까지 숫자로 주어지고, 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽을 의미한다.
# 스캔 로봇의 처음 위치 r은 위쪽에서부터 아래쪽까지 0부터 N - 1까지 차례대로 번호를 매겨 구분하며, c는 왼쪽에서 오른쪽까지 차례대로 번호를 매겨 구분한다.

# 셋째 줄부터 N개의 줄에 방의 상태가 주어진다. 0은 스캔되지 않은 빈 칸이고, 1은 벽이다.
# 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상은 모든 칸에 벽이 있다.
# 스캔 로봇의 처음 위치는 항상 빈 칸이다.

# [예시]
# 입력
# 5 5
# 3 2 0
# 1 1 1 1 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 0 0 1
# 1 1 1 1 1

# 출력
# 4

def scan_room(N, M, r, c, d, room):
    # 북, 동, 남, 서 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 0
    while True:
        # 현재 위치를 스캔
        if room[r][c] == 0:
            room[r][c] = 2
            count += 1

        # 반시계 방향으로 회전하며 빈 칸 탐색
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = r + dx[d], c + dy[d]
            if room[nx][ny] == 0:
                r, c = nx, ny
                break
        else:
            # 후진
            nx, ny = r - dx[d], c - dy[d]
            if room[nx][ny] == 1:
                return count
            r, c = nx, ny

# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 스캔한 칸의 개수 출력
print(scan_room(N, M, r, c, d, room))