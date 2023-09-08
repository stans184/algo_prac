# https://school.programmers.co.kr/learn/courses/30/lessons/42885

group1 = [70, 50, 80, 50]
limit1 = 100
# ans 3

group2 = [70, 80, 50, 30]
limit2 = 100
# ans 3

# 사람들을 구하기 위해 필요한 구명보트의 최소값
# 전체 사람들의 크기에서부터 빼는 방향으로 해볼까
# 이렇게 하면 같은 원소들을 반복해서 빼버리게 됨

# 상길북에서 봤던 2 pointer로 접근함

def solution(people, limit):
    people.sort()
    
    answer = len(people)
    left, right = 0, len(people)-1
    
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            answer -= 1
        right -= 1

    return answer

print(solution(group1, limit1))