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

data = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]

# quick sort 구현해보기

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)
    return arr

print(quickSort(data, 0, len(data)-1))

# DFS, BFS 구현해보기

def dfs(graph, start, visit=[]):
    visit.append(start)
    for node in graph[start]:
        if node not in visit:
            dfs(graph, node, visit)
    return visit

print(dfs(graph, 'A'))

def bfs(graph, start):
    need_visit, visited = [], []
    need_visit.append(start)
    while need_visit:
        node = need_visit[0]
        del need_visit[0]
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(bfs(graph, 'A'))