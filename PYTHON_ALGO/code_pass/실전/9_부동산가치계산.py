# 데이터 입력 받기
# 입력 받는 데이터
# - N : 지도의 크기
# - MAP : 각 땅 별 가치의 정보를 가지고 있는 N x N 크기의 격자
N = int(input().strip())
MAP = [list(map(int, input().split())) for _ in range(N)]

def make_group(r, c, group_num, groups):    
    cnt = 1                             # 그룹의 칸 수
    groups[r][c] = group_num            # 현재 그룹 마킹
    
    for [dr, dc] in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        # 같은 가치를 가지고 있는지 확인
        if groups[nr][nc] > 0 or MAP[nr][nc] != MAP[r][c]: continue
        
        cnt += make_group(nr, nc, group_num, groups)
    return cnt

def valuation(): 
    # 전체 땅에 그룹 만들기 및 가치 계산
    group_num = 0                                       # 그룹 번호 (1 ~ )
    groups = [[0] * N for _ in range(N)]                # 격자별 그룹 마킹
    values = [0 for _ in range(MAX_GROUP)]              # 그룹별 각 칸의 가치
    area_counts = [0 for _ in range(MAX_GROUP)]         # 그룹별 각 칸의 개수
    
    for r in range(N):
        for c in range(N):
            # 이미 그룹이 정해졌는지 확인
            if groups[r][c] > 0: continue
            group_num += 1
            values[group_num] = MAP[r][c]
            # 그룹 생성 및 그룹의 칸의 개수 가져오기
            area_counts[group_num] = make_group(r, c, group_num, groups)
    
    # 그룹 쌍 별 점수 구하기
    score = 0
    for r in range(N):
        for c in range(N):
            for [dr, dc] in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                # 다른 그룹끼리 맞닿아 있는 경우 score 합산
                if groups[r][c] != groups[nr][nc]:
                    g1, g2 = groups[r][c], groups[nr][nc]
                    score += (area_counts[g1] + area_counts[g2]) * \
                        values[g1] * values[g2]    
    
    return score // 2   # 중복 된 score 제거

def rotation(): 
    new_map = [[0] * N for _ in range(N)]
    
    # 십자 모양의 회전
    half = N // 2
    for r in range(N): new_map[half][r] = MAP[r][half]
    for c in range(N): new_map[c][half] = MAP[half][N - c - 1] 
    
    # 그 외 부분의 회전 
    for r in range(half):
        for c in range(half):
            # 좌상단
            new_map[r][c] = MAP[half - c - 1][r]   
            # 우상단
            new_map[r][half + c + 1] = MAP[half - c - 1][half + 1 + r]
            # 좌하단
            new_map[half + 1 + r][c] = MAP[N - c - 1][r]
            # 우하단
            new_map[half + 1 + r][half + 1 + c] = MAP[N - c - 1][half + 1 + r]
    return new_map

ans = 0                     # 땅의 가치의 총합
MAX_GROUP = (N * N + 1)     # 그룹의 개수의 최대값

for i in range(4):  # 초기, 1 ~ 3회전 마다의 가치 총합    
    # 전체 땅의 가치 합산
    ans += valuation()

    # 전체 땅의 회전 
    MAP = rotation()

print(ans)