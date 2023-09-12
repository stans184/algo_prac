# ==========================================
# < 선형 탐색을 이용한 다익스트라 구현 >
#  - 쉽게 구현할 수 있으나, 효율적인 방법이 아님
#  - time complexity 가 O(n^2)
#  - getSmallIdx 에서 for 문을 돌며 전체를 확인해서 O(n) 인데,
#  - dijkstra 함수에서 for 문 안에서 getSmallIdx 함수가 돌아가기 때문에 O(n^2)
#  - 전체 노드의 개수가 5000개 이하라면 이런 방향으로 접근할 수도 있을듯
# ==========================================
# 방문하지 않은 노드 중, 최단거리가 가장 작은 노드를 반환
def getSmallIdx():
    min = inf
    idx = 0 # 가장 짧은 거리로 도달할 수 있는 노드
    # 노드들을 훑어보면서
    for i in range(number):
        # min 보다 비용이 낮고, 방문하지 않았다면
        if distance[i] < min and not visited[i]:
            # min 값으로 비용 저장하고, 그 인덱스 값도 저장
            min = distance[i]
            # 최종적으로 가장 작은 비용을 가리키는 인덱스를 지정할 수 있음
            idx = i
    return idx
    
def dijkstraLinearSearch(arr, start):
    # 외부에 선언된 distance 연결
    global distance
    # 출발 노드 초기화 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 출발 노드에서 갈 수 있는 거리들을 distance 배열에 반영 (distance 배열 initial)
    for i in arr[start]:
        distance = arr[start]
    # 출발 노드를 제외한 나머지 노드들에 대하여 반복
    for j in range(number-1):
        # start 다음으로 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        current = getSmallIdx()
        visited[current] = True
        # current node 에서 방문하는데 드는 비용을 쭉 훑어보면서
        for i in range(number):
            # 방문하지 않았고
            if not visited[i]:
                # 저장되어 있는 distance cost 보다 current 를 거쳐서 가는 distance cost 가 낮다면
                if (distance[current] + arr[current][i]) < distance[i]:
                    # distance cost 반영
                    distance[i] = distance[current] + arr[current][i]
    # 해줘도 되고, 안해줘도 되지만 편의상
    return distance

# ==========================================
# 데이터 출력
# ==========================================

# 임의의 큰 숫자를 설정
inf = 10000000
# graph, node > node 가중치가 표기되어 있음, 안닿으면 inf
map = [
    [0,     2,      5,  1,      inf,    inf],
    [2,     0,      3,  2,      inf,    inf],
    [5,     3,      0,  3,      1,      5],
    [1,     2,      3,  0,      1,      inf],
    [inf,   inf,    1,  1,      0,      2],
    [inf,   inf,    5,  inf,    2,      0]
]
# node 의 갯수
number = len(map[0])

visited = [False]*(number)                # 한번 방문처리된 노드들
distance = [inf]*(number)                 # 최소 거리, 최소 비용을 저장하는 배열

# 최소거리 출력
# minimum distance =  [0, 2, 3, 1, 2, 4]
print("minimum distance = ", dijkstraLinearSearch(map, 0))