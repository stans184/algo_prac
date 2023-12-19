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

iteration = 1       -> N 출력
iteration >= 2      -> 재귀적 진행이 들어가야 하고, 중복이 필요없으니 set 형식으로 하면 좋음
'N'*(iteration-1)+N
'N'*(iteration-1)-N
'N'*(iteration-1)*N
'N'*(iteration-1)/N

n을 i개 써서 만들수 있는 숫자가 뭐가 있는지 확인하고
우리가 원하는 숫자가 있다면 거기서 멈추고 i값 return
없다면 숫자들을 result=set()에 넣고
다시 n+1에서 만들 수 있는 숫자들을 판별



'''
def make_num(arr, n, i):
    if i == 1:
        return [n]
    else:
        return [int(str(n)*i), arr[-1][0]*n, arr[-1][0]+n, arr[-1][0]-n, arr[-1][0]//n]

def solution(N, number):
    ans = 1
    num_list = []
    
    while ans < 10:
        num_list.append(make_num(num_list, N, ans))
        
        if number in num_list[-1]:
            break
        
        ans += 1
        
        print(num_list)
    
    return ans

print(solution(N1, number1))