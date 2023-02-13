# 동전의 종류 n개, 환전해야 하는 돈 k원
n, price = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

# 입력받은 동전을 큰 숫자순서로 정렬
coins.sort(reverse=True)

# 단위가 큰 코인부터 몫을 전부 확인해가면서 cnt 변수에 저장
for coin in coins:
    if price//coin > 0: cnt += price//coin
    price %= coin

print(cnt)