import heapq

def solution(scoville, K):
    
    s = []
    count = 0
    
    for food in scoville:
        heapq.heappush(s, food)
        
    while min(s) < K:
        heapq.heappush(s, heapq.heappop(s) + heapq.heappop(s)*2)
        count += 1
        
    print(s, count)
    return count

