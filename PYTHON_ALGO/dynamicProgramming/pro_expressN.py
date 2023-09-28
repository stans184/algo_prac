# https://school.programmers.co.kr/learn/courses/30/lessons/42895

# 의견
# https://alreadyusedadress.tistory.com/115

N1 = 5
number1 = 12
# 4

N2 = 2
number2 = 11
# 3

'''
n을 1개 써서 만들 수 있는 숫자
5
n을 2개 써서 만들 수 있는 숫자
55, 5+5, 5-5, 5*5, 5/5
n을 3개 써서 만들 수 있는 숫자
555,
55+5, 55-5, 55*5, 55/5
5+5+5, 5-5-5, 5*5*5, 5/5/5

iteration = 1 -> N 출력
iteration >= 2      -> 재귀적 진행이 들어가야 하고, 중복이 필요없으니 set 형식으로 하면 좋음
'N'*(iteration-1)+N
'N'*(iteration-1)-N
'N'*(iteration-1)*N
'N'*(iteration-1)/N
'''



def solution(N, number):
    ans = 0
    return ans