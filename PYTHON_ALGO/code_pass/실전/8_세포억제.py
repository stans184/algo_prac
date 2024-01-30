# 데이터 입력 받기
# 입력 받는 데이터
# - N : 격자의 크기
# - M : 박멸이 진행되는 년 수
# - K : 약의 확산 범위
# - Y : 약의 유효기간
# - MAP : 세포 수와 벽의 정보를 가지고 있는 N x N 크기의 격자

N, M, K, Y = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

import copy

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def cell_growth():
    # new_map = copy.deepcopy(MAP)
    # 각 칸 별로 인접한 세포의 칸 수에 따라서 세포 성장
    for r in range(N):
        for c in range(N):
            # 해당 칸에 세포가 있다면
            if MAP[r][c] >= 1:
                num_cell = 0
                for [dr, dc] in DIR:
                    nr, nc = r + dr, c + dc
                    if in_range(nr, nc) and MAP[nr][nc] >= 1:
                        num_cell += 1 
            
                # 주변의 세포 칸 수 만큼 성장
                MAP[r][c] += num_cell
                # new_map[r][c] += num_cell
    # return new_map

def cell_breeding():
    new_map = copy.deepcopy(MAP)
    # 세포가 있는 칸들의 번식 진행
    for r in range(N):
        for c in range(N):
            # 해당 칸에 세포가 있다면
            if MAP[r][c] >= 1:
                empty_area = []
                for [dr, dc] in DIR:
                    nr, nc = r + dr, c + dc
                    if in_range(nr, nc) and MAP[nr][nc] == 0 and \
                        SPRAY_MAP[nr][nc] == 0:
                        empty_area.append([nr, nc])                        
                
                # 번식 할 빈 칸들이 있다면
                if empty_area:
                    for [nr, nc] in empty_area:
                        new_map[nr][nc] += MAP[r][c] // len(empty_area)
    return new_map

def spread_one_way(r, c, dr, dc):
    killed = 0
    for _ in range(K):
        r, c = r + dr, c + dc
        if not in_range(r, c) or MAP[r][c] <= 0:
            break
        killed += MAP[r][c]
    return killed

DIR_DIAGONAL = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
def find_best_spot():
    max_kill = 0
    best_r = best_c = -1
    for r in range(N):
        for c in range(N):
            # 세포가 있는 곳만 확인
            if MAP[r][c] <= 0: continue
            kill = MAP[r][c]
            for [dr, dc] in DIR_DIAGONAL:
                kill += spread_one_way(r, c, dr, dc)
            
            # 가장 많이 박멸하는 곳의 위치를 저장
            if max_kill < kill:
                best_r, best_c, max_kill = r, c, kill

    return best_r, best_c, max_kill

def spray():
    global ans
    # 세포가 가장 많이 박멸 되는 곳을 찾기
    r, c, killed = find_best_spot()
    
    # 예외처리 : 박멸할 곳을 찾지 못했다면
    if r < 0 or c < 0: return
    
    # 박멸한 수 업데이트
    ans += killed
    
    # 실제로 찾은 위치에 약 뿌리기
    MAP[r][c] = 0
    SPRAY_MAP[r][c] = Y + 1
    for [dr, dc] in DIR_DIAGONAL:
        nr, nc = r, c
        for _ in range(K):
            nr, nc = nr + dr, nc + dc
            if not in_range(nr, nc): continue
            if MAP[nr][nc] >= 1: 
                MAP[nr][nc] = 0
                SPRAY_MAP[nr][nc] = Y + 1
            elif MAP[nr][nc] <= 0:
                SPRAY_MAP[nr][nc] = Y + 1
                break

def expiration_update():
    for r in range(N):
        for c in range(N):
            SPRAY_MAP[r][c] = max(0, SPRAY_MAP[r][c] - 1)
            
ans = 0
SPRAY_MAP = [[0] * N for _ in range(N)]
for _ in range(M):
    # 세포의 성장
    cell_growth()
    
    # 세포의 번식
    MAP = cell_breeding()
    
    # 약 뿌리기
    spray()
    
    # 약 유효기간 업데이트
    expiration_update()

print(ans)