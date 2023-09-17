# https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
# return 최소 비용 4

# 부모 노드의 조건이 중요한거같은데...
# 크루스칼 알고리즘을 heap으로 도전해보려고 했으나, 실패

def solutionMy(n, costs):
    costs.sort(key=lambda x:x[2])
    total = 0
    visited = []
    waiting = []
    
    heapq.heappush(waiting, costs[0][0])
    
    while waiting:
        current_node = heapq.heappop(waiting)
        
        print(waiting, visited)
        
        for cost in costs:
            if cost[0] == current_node and cost[1] not in visited:
                visited.append(cost[1])
                heapq.heappush(waiting, cost[1])
                total += cost[2]
                print(waiting, visited)
        
    print(total)
    
# 크루스칼 알고리즘을 set 을 통해 구현

def solution(n, costs):
    costs.sort(key=lambda x:x[2])                               # 이용 비용 오름차순 기준으로 정렬
    print("sorted cost ", costs)
    node = set([costs[0][0], costs[0][1]])                      # 현재 방문하는 길 등록
    print(node)
    total = costs[0][2]                                         # 그 길의 세금 추가
    
    while len(node) != n:                               
        for cost in costs:
            print(cost)
            if cost[0] in node and cost[1] in node: continue    # 지금 확인중인 cost의 값들이 모두 등록되어 있으면 넘어감
            if cost[0] in node or cost[1] in node:              # 하나만 등록되어 있으면, 해당 비용을 업데이트 하고 등록
                node.update([cost[0], cost[1]])
                total += cost[2]
                print(node, total)
                break                                           # 이게 가장 중요한 포인트 같은데,,, break를 하지 않으면
    print(total)
    
# 두 코드 모두 유효한 크루스칼 알고리즘의 구현이지만, 
# 첫 번째 코드의 break 문은 조건을 만족하는 첫 번째 간선만 선택하고 다음 간선을 검사하지 않습니다. 
# 반면에 두 번째 코드는 break 문이 없어서 조건을 만족하는 모든 간선을 선택할 수 있습니다.

solution(n, costs)
