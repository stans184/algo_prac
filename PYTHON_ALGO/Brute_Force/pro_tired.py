# https://school.programmers.co.kr/learn/courses/30/lessons/87946
k1 = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
# ans = 3

# 9/7
# 문제의 제약조건에서 dungeons로 들어올 수 있는 변수가 최대 8개 이하라고 가정되어서
# dungeons의 순열 갯수를 확인했을 때, 8! = 40320 이므로, 반복으로 돌아볼만한 수라고 판단 permutations으로 진행
# 그러나 input으로 들어오는 변수들에 따라서 아래와 같은 greedy 혹은 brute force 방법은 시간 초과가 발생할 가능성이 높다
# 현재까지의 진행값을 기록하며 나가는 dynamic programming 이나,
# graph 의 최소값, 최대값을 확인할 수 있는 DFS를 사용해서 푸는 방법도 해보기

from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for way in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        for dungeon in way:
            if dungeon[0] <= hp:
                hp -= dungeon[1]
                count += 1
            
        answer = max(answer, count)

    return answer

print(solution(k1, dungeons))

