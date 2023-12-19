# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

input1 = [7,1,5,3,6,4]
output1 = 5

input2 = [7,6,4,3,1]
output2 = 0

# stock 형식으로 앞에서부터 값을 쌓아야 할듯
input3 = [3,2,6,5,0,3]
output3 = 4

# 1. 내 시도, 시간초과가 발생함
def maxProfit(prices):
    # 정렬
    ordered = sorted(prices)
    # 이익
    profit = 0
    
    while ordered:
        # 최소값, 앞에서부터 뺀다
        min_val = ordered.pop(0)
        # 최소값의 위치
        min_loc = prices.index(min_val)
        # 최소값을 바탕으로 계산된 이익
        if max(prices[min_loc:len(prices)]) - min_val > profit:
            profit = max(prices[min_loc:len(prices)]) - min_val
    
    return profit

# 2. 구글링, 책의 방법, 통과되었음
# 정렬하고 따로 들어가는건, 시간 초과가 발생할 수도 있음
# 배열을 한번 순환하는 방식
# 그래프를 한번 그려보고, 생각해보면 좀더 쉽게 다가옴
def maxProfit2(prices):
    # prices를 훑어가는 index, 가장 큰 값으로 설정
    min_price = float('inf')
    # profit을 저장하는 변수
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print(maxProfit2(input3))