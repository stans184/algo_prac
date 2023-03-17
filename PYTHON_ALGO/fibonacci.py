import sys, time
input = sys.stdin.readline

# by Recursive

def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n-1) + fibo(n-2)

num1 = int(input())

start = time.time()
result1 = fibo(num1)
end = time.time()

print('재귀적으로', result1)
print('소요시간', end-start)

# by repeat

def fibo2(n):
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b, a+b
        return b

num2 = int(input())

start2 = time.time()
result2 = fibo2(num2)
end2 = time.time()

print('반복문으로',result2)
print('소요시간', end2-start2)

# dynamic programming

def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]