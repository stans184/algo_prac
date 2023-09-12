# N 개의 도시
# x 도시에서 y 도시로 전보를 보내고자 한다면, 통로가 있어야 하며, 통로를 거치는데는 일정 시간이 소요된다
# c 도시에서 위급 상황이 발생하여 모든 도시로 보내고자 한다
# c 도시에서 보낸 메세지를 받는 도시의 개수는 몇 개이며, 도시들이 모두 메세지를 받는 데 걸리는 시간은?
# 처음 input 으로는 도시의 개수 n, 통로의 개수 m, 도시 c (1 <= n <= 30000, 1 <= m <= 200000, 1 <= c <= n)
# 두번째 input 으로는 m + 1 줄에 걸쳐서 통로의 정보 x,y,z 가 주어진다
# 이는 특정 도시 x 에서 다른 특정 도시 y 로 이어지는 통로가 있으며 걸리는 시간이 z 라는 소리
# 도시 C 에서 보낸 메세지를 받는 도시의 총 개수 & 총 걸리는 시간?

# input example
# 3 2 1
# 1 2 4
# 1 3 2

# output example
# 2 4

n,m,c = map(int, input().split())

graph = [[0]*n]*n

for i in range(m):
    x,y,z = map(int, input().split())
    graph[x-1][y-1] = z

# 들어가는거부터 잘못됨
print(graph)