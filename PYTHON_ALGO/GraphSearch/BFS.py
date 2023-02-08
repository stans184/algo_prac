def bfs(graph, start):
    # 방문하고자 하는 노드, 방문했던 노드들
    need_visit, visited = [], []
    # 시작점 아직 방문 안했으니가 방문하고자 하는 노드
    need_visit.append(start)
    # 방문하고자 하는 노드에 요소가 있다면, // while list 에서 list 안에 element 가 있으면 계속 반복, null 이면 탈출
    while need_visit:
        # 방문이 필요한 노드 중 가장 왼쪽을 노드로 설정해주고
        node = need_visit[0]
        # 그 요소는 지운다
        del need_visit[0]
        # 노드가 방문하지 않았다면
        if node not in visited:
            # 방문 처리해주고
            visited.append(node)
            # 방문이 필요한 노드들의 리스트를 내가 방문한 노드의 그래프를 기준으로 재설정해준다
            # list extend 는 리스트의 확장 [1,2,3].extend([4,5]) = [1,2,3,4,5]
            need_visit.extend(graph[node])
    # 방문을 진행한 리스트를 반환
    return visited


graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))
# ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']