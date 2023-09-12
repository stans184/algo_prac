# https://school.programmers.co.kr/learn/courses/30/lessons/86971

# n	wires	result
# 9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
# 4	[[1,2],[2,3],[3,4]]	                                0
# 7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1

# 일단 답을 보게 되었으니, 길을 탐색하는 문제는 dfs, bfs로 진행됨
# 구현 방법 다시 공부하기
# 아래 풀이는 완전탐색으로 진행한 것
# 추후 dfs, bfs 복습을 통해 그래프 탐색할때의 풀이도 넣기
# union find 일때도 찾아보기


# 1. 완전탐색
def solution(n, wires):
    ans = n
    
    for i in range(n-1):
        # wires가 연결되어있는 정보를 복사해놓고
        heap = wires.copy()
        # 특정 부분이 끊어졌을 떄, 특정 부분을 빼버린다
        heap.pop(i)
        
        # 끊어진 부분을 기준으로 왼쪽, 오른쪽을 나눠서 탐색시킨다
        L, R = set(), set()
        L.add(wires[i][0])
        R.add(wires[i][1])
        
        # heap의 모든 부분을 빼내서 
        # 연결점이 있는 왼쪽과 오른쪽으로 나눠서 넣기
        # 왼쪽, 오른쪽에서 연결점을 찾지 못한다면 다시 heap에다가 넣고, 나중에 검증
        while heap:
            a, b = heap.pop(0)
            if a in L or b in L:
                L.add(a)
                L.add(b)
            elif a in R or b in R:
                R.add(a)
                R.add(b)
            else:
                heap.append([a, b])
                
        # 분할된 2개의 전력망의 차이의 절대값과, 현재 답과의 크기 비료를 해서 작은 값
        ans = min(abs(len(L) - len(R)), ans)
        
    return ans

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))