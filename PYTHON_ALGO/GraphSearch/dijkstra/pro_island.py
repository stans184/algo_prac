# https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
# return 최소 비용 4

def solution(n, costs):
    visited = [False for i in range(costs[0][0], n)]
    tax = 0
    
    costs.sort(key=lambda x:x[2])
    visited[costs[0][0]] = True
    for cost in costs:
        if visited[cost[1]] == False:
            visited[cost[1]] = True
            tax += cost[2]
    
    return tax    

solution(n, costs)