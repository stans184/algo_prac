# 1 x 1 크기의 칸으로 이루어진 N x N 크기의 정올시에는 아파트와 빈 공간 그리고 편의점이 있다.
# 이 때, '편의점 거리'는 각 아파트와 가장 가까운 편의점까지의 거리를 의미하며, 두 격자 (r1, c1), (r2, c2) 사이의 거리는 ∣r2 − r1∣ + ∣c2 − c1∣로 구한다.
# 편의점 본사는 운영상의 이유로 M개의 편의점만 남겨두고 나머지를 폐업해야 할 때 남은 M개의 편의점에 대한 각 아파트의 편의점 거리의 총 합이 최소가 되도록 하려고 한다.
# 첫 번째 줄에는 N (2 ≤ N ≤ 50)과 M (1 ≤ M ≤ 13)이 공백을 사이에 두고 주어지고,
# 두 번째 줄부터 (N+1)번째 줄까지는 각 행에 빈 칸인 경우 0, 아피트인 경우 1, 편의점인 경우 2로 입력이 공백을 사이에 두고 주어진다.

# M개의 병원을 고르는게 불가능한 입력은 주어지지 않는다고 가정해도 좋다.
# M ≤ 편의점의 수 ≤ 13
# 아파트의 수 ≤ 2∗N​
# 편의점 M개를 남겼을 때 가능한 각 아파트의 편의점 거리 총 합 중 최솟값을 출력한다.

# [예시]
# 입력
# 3 1
# 1 0 0
# 0 2 2
# 0 1 0

# 출력
# 3

import itertools

def calculate_distance(apartments, stores):
    total_distance = 0
    for ax, ay in apartments:
        distance = min([abs(ax - sx) + abs(ay - sy) for sx, sy in stores])
        total_distance += distance
    return total_distance

# 입력
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 아파트와 편의점 위치 찾기
apartments = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
convenience_stores = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]

# 모든 편의점 조합 중 최소 거리 합 계산
min_distance = float('inf')
for stores in itertools.combinations(convenience_stores, M):
    distance = calculate_distance(apartments, stores)
    min_distance = min(min_distance, distance)

print(min_distance)