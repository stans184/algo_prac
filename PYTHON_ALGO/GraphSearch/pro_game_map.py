# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# maps	answer
test1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	# ans1 11
test2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	# ans2 -1

# queue를 이용해서 지속적으로 방문처리를 할 예정
# 현재 위치를 기준으로, 인접 노드들 중에서 방문하지 않은 노드를 queue에 넣고 방문처리
# queue에 node가 없을 때까지 반복

from collections import deque
def solution(maps):
    answer = 0

    # game의 map에서 상하좌우만 움직일 수 있으므로
    # 상:(-1, 0), 하:(1, 0), 좌:(0, -1), 우:(0, 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 현재 캐릭터가 서있는 칸을 받아서 queue에 넣는다
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            # 상:(-1, 0), 하:(1, 0), 좌:(0, -1), 우:(0, 1)
            # 이걸 반복하기 위해서 range(4)를 반복
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0: continue

                # 처음 지나가는 길이면 현재 위치에서부터 거리계산하고 
                # 해당 칸의 좌표를 queue에 넣고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    # 여기서 출발점부터의 거리를 더해서 저장해준다
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    # 처음 지나가는 길들이 다시 queue에 쌓이고, 이것들이 while 문을 통해서 반복됨

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없을 때 -1

print(solution(test2))