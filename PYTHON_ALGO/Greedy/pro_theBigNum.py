# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"

from itertools import combinations

def sol_1(number, k):
    ans = 0
    for num in list(combinations(number, len(number) - k)):
        if int(''.join(num)) > ans:
            ans = int(''.join(num))
    
    return ans

# 첫번째 시도 실패
# -> 시간초과 발생

# 스택을 활용해보자
# number 문자열을 순회하면서 append 하는데
# k개 만큼의 숫자를 제거해야함, 전체 문자열에서 (k > 0)
# 만약, stack 에 num 보다 작은 수가 있으면 (stack[-1] < num)

def solution(number, k):
    
    stack = []
    
    for num in number:
        
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        
        stack.append(num)
        
    return ''.join(stack[:len(stack) - k])

print(solution("4177252841", 4))