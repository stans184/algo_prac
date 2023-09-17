# ==========================================
# < heap 구조를 이용한 다익스트라 구현 >
#  - 가장 큰 값, 혹은 작은 값이 맨 위로 올라오는 heap 자료구조를 이용하면 O(nlog(n))
#  - 매 단계마다 방문하지 않은 노드 중 최단거리가 짦은 노드를 선택하기 위해 min heap 구조를 활용
#  - dijkstra 알고리즘이 동작하는 원리는 동일
# ==========================================
# < 우선순위 큐 자료구조 Priority Queue >
#  - 우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조
#  - heap 을 통해 구현 (min heap, max heap)
#  - heap 은 데이터를 삽입하고, 삭제하는데 O(logN) 이 소요됨    //   리스트로 하면 삽입 O(1), 삭제 O(N)
# ==========================================
import heapq

def dijkstraHeap(arr, start):
    q = []
    # 출발점 start, 거리비용 0 을 heap 에 넣어줌
    heapq.heappush(q, (0, start))
    # 출발 노드의 거리비용 초기화
    distance[start] = 0
    # 모두 방문할때 까지, heap queue 가 다 빠질 때까지 반복
    while q:
        # heap에는 방문해야할 모든 노드들이 들어가 있다
        # heapq는 min heap 이므로, 자동으로 최소값으로 정렬된다
        # 따라서, 방문하지 않은 노드들 중에서, 가장 거리가 가까운 노드가 나온다
        min_distance, current = heapq.heappop(q)
        # 현재 노드가 처리된 적 있는 노드라면 무시해야 하는데, visited 변수를 만들어서 처리해도 되지만
        # 왜냐, 아직 처리가 안됐다면 distance[current] 는 매우 큰 수일테니
        if distance[current] < min_distance:
            continue
        # 현재 노드와 연결된 모든 노드들의 거리비용 확인
        for i in range(number):
            # 출발점에서 현재 노드까지 오는 비용 + 새로운 곳으로 가기 위한 비용을 더하면
            # 현재 노드를 거쳐서 새로운 곳으로 가기 위한 비용
            cost = min_distance + arr[current][i]
            # 만약 현재 노드를 거쳐서 가는 비용이 더 작다면
            if cost < distance[i]:
                # 거리비용 털어주고
                distance[i] = cost
                # heap 에다가 해당 노드와, 그곳까지 가는 거리비용을 넣어줌
                heapq.heappush(q, (cost, i))
    return distance

# ==========================================
# 데이터 출력
# ==========================================
# 임의의 큰 숫자를 설정
inf = 100000000i
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
 # 최소 거리, 최소 비용을 저장하는 배열
distance = [inf]*(number)
# 최소거리 출력
# minimum distance =  [0, 2, 3, 1, 2, 4]
print(dijkstraHeap(map, 0))