# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

def dfs(graph, start, visited=[]):
    visited.append(graph[start])
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
# (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4
N, M, R = 5, 5, 1
graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

result = dfs(graph, R, visited=[])
print(result)