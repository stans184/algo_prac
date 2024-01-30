# 데이터 입력 받기
# 입력 받는 데이터
# - N : 보드판의 크기
# - M : 주사위 굴리는 횟수
# - BOARD : 보드판의 숫자 정보를 가지고 있는 N x N 크기의 격자

N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]

def get_score(r, c):
    score = BOARD[r][c]
    for [dr, dc] in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        # 이미 score가 있는 곳 인지 확인 
        if visit[nr][nc] or SCORE_MAP[nr][nc] > 0: continue
        visit[nr][nc] = True
        if BOARD[r][c] == BOARD[nr][nc]:
            score += get_score(nr, nc)
    
    return score

def apply_score(r, c, score):
    SCORE_MAP[r][c] = score
    for [dr, dc] in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if SCORE_MAP[nr][nc] > 0: continue
        if BOARD[r][c] == BOARD[nr][nc]: 
            apply_score(nr, nc, score)

# SCORE_MAP 만들기
SCORE_MAP = [[0] * N for _ in range(N)]    # 칸 별 획득하게 되는 점수 판
for r in range(N):
    for c in range(N):
        if SCORE_MAP[r][c]: continue
        
        visit = [[False] * N for _ in range(N)]
        visit[r][c] = True
        score = get_score(r, c)     #  현재 위치와 연결 된 스코어들의 합 
        
        # 현재 위치와 연결 된 곳들에 합산 된 score 적용
        apply_score(r, c, score)    

def move(r, c, d):
    # (r, c)에서 d 방향으로 이동
    nr, nc = r + DIR[d][0], c + DIR[d][1]
    
    # 경계면에 부딪히면 방향 반대로 전환
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        d = (d + 2) % 4     # 반대방향
        nr, nc = r + DIR[d][0], c + DIR[d][1]
    
    # 주사위 굴리기
    if d == 0: # 위로 굴리기
        DICE[0], DICE[1] = DICE[1], 7 - DICE[0]  # 앞, 밑 -> 위, 앞       
    elif d == 1: # 오른쪽으로 굴리기
        DICE[0], DICE[2] = 7 - DICE[2], DICE[0]  # 왼, 위 -> 위, 오
    elif d == 2: # 아래쪽으로 굴리기
        DICE[0], DICE[1] = 7 - DICE[1], DICE[0]  # 뒤, 위 -> 위, 앞 
    elif d == 3: # 왼쪽으로 굴리기
        DICE[0], DICE[2] = DICE[2], 7 - DICE[0]  # 오, 밑 -> 위, 오 
    
    # 밑면과 비교하여 다음 방향을 정함
    if 7 - DICE[0] > BOARD[nr][nc]: d = (d + 1) % 4
    elif 7 - DICE[0] < BOARD[nr][nc]: d = (d - 1) % 4
    
    return nr, nc, d


DICE = [1, 2, 3]    # 주사위의 위, 앞, 오른쪽
R = C = 0   # 주사위의 시작 위치
D = 1       # 주사위 시작 방향 (0 ~ 3: 북동남서)
DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]    # 주사위 방향 (북동남서)

score = 0   # 총 얻은 점수

for _ in range(M):
    # 주사위 움직이기 
    R, C, D = move(R, C, D)   # 주사위 위치와 방향

    # 현재 위치에서 점수 취득
    score += SCORE_MAP[R][C]

print(score)