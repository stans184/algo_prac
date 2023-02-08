# Depth First Search (DFS)
def dfs_recursive(graph, start, visited = []):
    # 방문한 요소를 정리하는 visited list 에 start 지점부터 저장
    visited.append(start)
    # graph dictionary 의 노드를 왼쪽부터 훑으면서
    for node in graph[start]:
        # 그 노드가 visited list 에 들어았지 않다면
        if node not in visited:
            # 그 노드부터 다시 DFS 를 들어간다, 즉 왼쪽으로 더 깊게 내려가본다
            dfs_recursive(graph, node, visited)
    # visited list 를 반환한다
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

print(dfs_recursive(graph, 'A'))
# ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J']