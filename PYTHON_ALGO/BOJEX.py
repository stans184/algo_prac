# 3
# 8           3 5
# 10          5 5
# 16          5 11

def isPrime(num):
    isPNum = True
    for i in range(2,num):
        if num%i == 0: isPNum = False
    return isPNum

def is_prime(n):
    if n == 1:
        return False
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