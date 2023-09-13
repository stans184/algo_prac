# https://school.programmers.co.kr/learn/courses/30/lessons/42584

prices = [1, 2, 3, 2, 3]
# answer [4, 3, 1, 1, 0]

# 내가 해본 코드, 시간 초과로 안됨
def sol1(prices):
    answer = [0 for i in range(len(prices))]
    
    for i in range(len(prices)-1):
        if prices[i] <= min(prices[i+1:]):
            answer[i] = len(prices) - i - 1
        else:
            for j in range(i, len(prices)):
                if prices[i] > prices[j]:
                    answer[i] = j - i
    
    return answer

# stack 을 이용한 코드
def solution(prices):
    answer = [0] * len(prices)  # 결과를 저장할 배열 초기화
    stack = []  # 현재 주식 가격의 인덱스를 저장할 스택

    for i in range(len(prices)):
        # 스택이 비어있지 않고, 현재 주식 가격이 스택의 가장 위의 주식 가격보다 작다면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  # 주식 가격이 떨어진 시점
            answer[j] = i - j  # 떨어진 시점과 현재 시점의 차이를 저장

        stack.append(i)  # 현재 주식 가격의 인덱스를 스택에 추가

    # 스택에 남아있는 주식 가격들은 떨어지지 않은 기간이 없는 경우
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j  # 떨어지지 않은 기간을 배열에 저장

    return answer