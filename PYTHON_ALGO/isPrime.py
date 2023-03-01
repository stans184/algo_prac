# 3
# 8           3 5
# 10          5 5
# 16          5 11

# normal solution for prime number
def isPrime(num):
    isPNum = True
    for i in range(2,num):
        if num%i == 0: isPNum = False
    return isPNum

# Eratosthenes solution for prime number
# time complexity O(nlog(logn))
def is_prime(n):
    # 1은 소수가 아니니 false
    if n == 1:
        return False
    # 만약 주어진 숫자가 n^0.5 보다 작은 수로 나누어 떨어지는지 체크 (n = x*y)
    # 나누어 떨어진다면 소수가 아니고
    # 나누어지지 않는다면 x,y 가 n^0.5 보다 큰 수가 되고
    # 이러면 x*y > n 이 되므로 가정에 어긋나고, 두 수로 나누어지지 않는다는 결론
    # 따라서 소수로 판정
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    a, b = n//2, n//2

    while True:
        if is_prime(a) and is_prime(b) and a + b == n:
            print(a, b)
            break
        else:
            a -= 1
            b += 1