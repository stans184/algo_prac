# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);}

# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 
# 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
# (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4
# 6 4 1
# 2 3
# 1 4
# 1 5
# 4 6

import sys
input = sys.stdin.readline

def DFS(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited)
    return visited

n, m, r = map(int, input().split())

useMap = dict()

for i in range(1, n + 1):
    useMap[i] = set()

for _ in range(m):
    a, b = map(int, input().split())
    useMap[a].add(b)

checked = DFS(useMap, r)

ans = [0] * (n + 1)
idx = 1
for num in checked:
    ans[num] = idx
    idx += 1

for i in range(1, n + 1):
    print(ans[i])