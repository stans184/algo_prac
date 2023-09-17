# https://school.programmers.co.kr/learn/courses/30/lessons/42627

jobs1 = [[0, 3], [1, 9], [2, 6]] # 9

import heapq

def solution(jobs):
    # 작업 요청부터 종료가지 걸린 시간 => 답
    # 현재 시간 now
    # 처리한 일의 갯수 i
    ans, now, i = 0, 0, 0
    
    start = -1 # 이전 작업의 시작 시간
    h = []     # 작업을 정렬하는 heap
    
    while i < len(jobs): # 처리한 일의 갯수가 전체 job보다 적다면 -> 전체 잡을 처리할 때까지 반복
        for job in jobs:   # 모든 job에 대해 반복
            # 이전 작업 시작 시간 < 요청 시간 <= 현재 시간보다 작거나 같은 작업을 힙에 삽입
            # 즉, 현재 시점에서 처리할 수 있는 작업들을 모두 h에 넣어서 실행 대기로 만드는 것
            if start < job[0] <= now:
                heapq.heappush(h, [job[1], job[0]])     # 작업이 걸리는 시간, 작업 시작 시간으로 순서를 바꿔서 추가
                # 작업이 걸리는 시간을 기준으로 최소 heap이 만들어진다
        print("h : ", h)
            
        # 만약 정렬된 작업이 있다면, 처리할 작업이 있다면
        if len(h) > 0:
            current_job = heapq.heappop(h)
            start = now                 # 작업 시작 시간을 현재 시간으로 갱신
            now += current_job[0]       # 작업이 진행되므로, 해당 작업이 끝나는 시점으로 돌려버림
            ans += now - current_job[1] # 대기 시간 및 처리 시간 누적
            i += 1                      # 일 하나 처리되었으므로
                
        else: now += 1 # 시간이 흘러간다
        print("start : ", start)
        print("now : ", now)
        print("i : ", i)
    
    return ans // len(jobs)

print(solution(jobs1))