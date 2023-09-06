# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

# priorities
task1 = [2, 1, 3, 2]	
loc1 = 2
# ans 1
task2 = [1, 1, 9, 1, 1, 1]
loc2 = 0
# ans 5

def solution(priorities, location):
    stack = deque()
    pro_sort = sorted(priorities, reverse=True)
    execute = []

    for idx, process in enumerate(priorities):
        stack.append([idx, process])

    # 반복해야함
    # pro_sort와의 크기 비교하면서
    # 더 큰놈들이 있으면 뒤로 넘기도록

    while stack:
        process = stack.popleft()
        if process[1] == pro_sort[0]:
            execute.append(process)
            pro_sort = pro_sort[1:]
        else:
            stack.append(process)
            

    for idx, process in enumerate(execute):
        if process[0] == location:
            return idx+1