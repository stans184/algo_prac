# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 풀이 예시
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS

def solution(numbers, target):
    answer = 0
    check = [[0]]
    
    # 첫번째 숫자부터 마지막 숫자까지 반복하면서
    # 더하고 뺀 값을 계속 저장하며 나아간다 (DFS)
    # 결론으로 target과 같은 값이 몇개인지 세서 반환
    
    for num in numbers:
        temp = []
        for i in range(len(check[-1])):
            temp.append(check[-1][i] + num)
            temp.append(check[-1][i] - num)
        check.append(temp)
        
    for result in check[-1]:
        if result== target:
            answer += 1
        
    return answer

a = [1,2,3,4]
for i in range(len(a[-1:])):
    print(i)
    
print(solution([4,1,2,1], 4))

# 재귀를 사용한 풀이
def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])