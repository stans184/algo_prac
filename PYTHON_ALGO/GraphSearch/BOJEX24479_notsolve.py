# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }


# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
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

# dfs 함수
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    # 시작점 넣어주고
    visited.append(start)
    # 시작점에서 연결된 노드들을 정렬해서, 낮은데부터 방문
    for node in sorted(graph[start]):
        # 방문한 곳이 기록에 없다면 dfs 처리
        if node not in visited:
            dfs(graph, node, visited)
    # 방문한 노드들 순서대로 저장된 리스트 출력
    return visited

N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)

result = dfs(graph, R-1)

# 방문 순서를 확인하기 위한 전체 리스트
target = [i for i in range(1, N+1)]
# 방문 순서를 카운트하는 변수
order = 1

# 주어진 정점을 처음부터 훑으면서
for num in target:
    # 해당 정점이 방문리스트에 있다면
    if (num-1) in result:
        # 현재 순서를 출력하고
        print(order)
        # 순서 하나 늘려주기
        order += 1
    # 아니면 0 출력
    else:
        print(0)