# 최단경로 탐색 알고리즘
특정 시작점에서 원하는 목적지로 가는 최단 경로를 찾는다<br/>
<br/>
다이나믹 프로그래밍으로 분류되기도 하고   -> 최단 거리는 여러 개의 최단 거리로 이루어졌기 때문<br/>
그리디 알고리즘으로 분류되기도 함       -> 매 상황에서 가장 비용이 적은 노드를 선택하는 과정을 반복하기 때문<br/>

# 작동 과정
1. 출발점 설정
2. 출발점 기준으로 각 노드의 최소 비용을 저장 (최단 거리 테이블을 초기화)
3. 방문하지 않는 노드 중, 가장 비용이 적은 노드 선택
4. 해당 노드를 거쳐서 다른 노드로 가는 경우의 최소 비용 갱신
5. 3~4 반복

graph 와 가중치를 표기하기 위해선 2차원 배열로 나타내주어야 함

# 문제 상황 예시
1) 한 지점에서 다른 지점까지 최단 경로
2) 한 지점에서 다른 모든 지점까지 최단 경로
3) 모든 지점에서 다른 모든 지점까지 최단 경로