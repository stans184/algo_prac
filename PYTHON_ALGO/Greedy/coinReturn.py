price = int(input())

coins = [500, 100, 50, 10]

for coin in coins:
    cnt = 0
    cnt += price//coin
    price = price%coin
    print(coin, "짜리 동전 ", cnt, "개 필요")